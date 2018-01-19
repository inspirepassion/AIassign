from classify import *
import math

##
# CSP portion of lab 4.
##
from csp import BinaryConstraint, CSP, CSPState, Variable,\
    basic_constraint_checker, solve_csp_problem

# Implement basic forward checking on the CSPState see csp.py


def forward_checking(state, verbose=False):
    # Before running Forward checking we must ensure
    # that constraints are okay for this state.
    basic = basic_constraint_checker(state, verbose)
    if not basic:
        return False

    # return True if it's initial state
    if state.variable_index < 0:    return True

    cur_var = state.get_current_variable()

    # current variable is carried over when csp.solve() creates children
    cur_var_name = state.get_current_variable_name()
    cur_var_value = cur_var.get_assigned_value()
    constraints = state.get_all_constraints()

    # print "state current name: {}".format(state.get_current_variable_name())

    # if cur_var_name == "5":
    #     for i in constraints:
    #         if cur_var_name == i.get_variable_i_name():
    #             if i.get_variable_j_name() == "4":
    #                 print i#, "\t", i.get_variable_i_name(), i.get_variable_j_name()
    #                 print i.check(state, "B", "O")

    for constraint in constraints:
        i_name = constraint.get_variable_i_name()
        j_name = constraint.get_variable_j_name()

        # !!! I assume as long as there is a constraint for two variables, they are connected to each other
        if cur_var_name == i_name:
            connected_name = j_name
        elif cur_var_name == j_name:
            connected_name = i_name
        else:
            continue

        connected_var = state.get_variable_by_name(connected_name)
        # print "connected_var: {}\n".format(connected_var)
        # if not connected_var.is_assigned(): # comment this line, and unindent the next command and for loop
        connected_domains = connected_var.get_domain()

        for domain in connected_domains:
            # in instruction, he says that constraints are symmetrical, so I assume I just need to check one direction
            if not constraint.check(state, cur_var_value, domain):
                # print "before reduce_domain: {}, __len__(): {}".format(connected_var, connected_var.domain_size())
                connected_var.reduce_domain(domain)
                # print "\nremove domain: {} from variable: {} at state: {} \n".format(domain, connected_var.get_name() ,state.variable_index)
                # print "after reduce_domain: {}, __len__(): {}\n".format(connected_var, connected_var.domain_size())

            if connected_var.domain_size() == 0:
                # print "return False implemented\n"
                return False
    return True

    # Add your forward checking logic here.

    raise NotImplementedError

# Now Implement forward checking + (constraint) propagation through
# singleton domains.


def forward_checking_prop_singleton(state, verbose=False):
    # Run forward checking first.
    fc_checker = forward_checking(state, verbose)
    if not fc_checker:
        return False

    # Add your propagate singleton logic here.
    raise NotImplementedError


# The code here are for the tester
# Do not change.
from moose_csp import moose_csp_problem
from map_coloring_csp import map_coloring_csp_problem


def csp_solver_tree(problem, checker):
    problem_func = globals()[problem]
    checker_func = globals()[checker]
    answer, search_tree = problem_func().solve(checker_func)
    return search_tree.tree_to_string(search_tree)

##
# CODE for the learning portion of lab 4.
##


# Data sets for the lab
# You will be classifying data from these sets.
senate_people = read_congress_data('S110.ord')
senate_votes = read_vote_data('S110desc.csv')

house_people = read_congress_data('H110.ord')
house_votes = read_vote_data('H110desc.csv')

last_senate_people = read_congress_data('S109.ord')
last_senate_votes = read_vote_data('S109desc.csv')


# Part 1: Nearest Neighbors
# An example of evaluating a nearest-neighbors classifier.
senate_group1, senate_group2 = crosscheck_groups(senate_people)
#evaluate(nearest_neighbors(hamming_distance, 1), senate_group1, senate_group2, verbose=1)

# Write the euclidean_distance function.
# This function should take two lists of integers and
# find the Euclidean distance between them.
# See 'hamming_distance()' in classify.py for an example that
# computes Hamming distances.


def euclidean_distance(list1, list2):
    # this is not the right solution!
    return hamming_distance(list1, list2)

# Once you have implemented euclidean_distance, you can check the results:
#evaluate(nearest_neighbors(euclidean_distance, 1), senate_group1, senate_group2)

# By changing the parameters you used, you can get a classifier factory that
# deals better with independents. Make a classifier that makes at most 3
# errors on the Senate.


my_classifier = nearest_neighbors(hamming_distance, 1)
#evaluate(my_classifier, senate_group1, senate_group2, verbose=1)

# Part 2: ID Trees
# print CongressIDTree(senate_people, senate_votes, homogeneous_disorder)

# Now write an information_disorder function to replace homogeneous_disorder,
# which should lead to simpler trees.


def information_disorder(yes, no):
    return homogeneous_disorder(yes, no)

# print CongressIDTree(senate_people, senate_votes, information_disorder)
#evaluate(idtree_maker(senate_votes, homogeneous_disorder), senate_group1, senate_group2)

# Now try it on the House of Representatives. However, do it over a data set
# that only includes the most recent n votes, to show that it is possible to
# classify politicians without ludicrous amounts of information.


def limited_house_classifier(house_people, house_votes, n, verbose=False):
    house_limited, house_limited_votes = limit_votes(house_people,
                                                     house_votes, n)
    house_limited_group1, house_limited_group2 = crosscheck_groups(house_limited)

    if verbose:
        print "ID tree for first group:"
        print CongressIDTree(house_limited_group1, house_limited_votes,
                             information_disorder)
        print
        print "ID tree for second group:"
        print CongressIDTree(house_limited_group2, house_limited_votes,
                             information_disorder)
        print

    return evaluate(idtree_maker(house_limited_votes, information_disorder),
                    house_limited_group1, house_limited_group2)


# Find a value of n that classifies at least 430 representatives correctly.
# Hint: It's not 10.
N_1 = 10
rep_classified = limited_house_classifier(house_people, house_votes, N_1)

# Find a value of n that classifies at least 90 senators correctly.
N_2 = 10
senator_classified = limited_house_classifier(senate_people, senate_votes, N_2)

# Now, find a value of n that classifies at least 95 of last year's senators correctly.
N_3 = 10
old_senator_classified = limited_house_classifier(last_senate_people, last_senate_votes, N_3)


# The standard survey questions.
HOW_MANY_HOURS_THIS_PSET_TOOK = ""
WHAT_I_FOUND_INTERESTING = ""
WHAT_I_FOUND_BORING = ""


# This function is used by the tester, please don't modify it!
def eval_test(eval_fn, group1, group2, verbose=0):
    """ Find eval_fn in globals(), then execute evaluate() on it """
    # Only allow known-safe eval_fn's
    if eval_fn in ['my_classifier']:
        return evaluate(globals()[eval_fn], group1, group2, verbose)
    else:
        raise Exception, "Error: Tester tried to use an invalid evaluation function: '%s'" % eval_fn
