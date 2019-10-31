from pyhop import *
import elevators_domain

print('')
print_operators()

print('')
print_methods()

print("""
****************************************
Exercise 3
****************************************
""")

print("- Define state1")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state2 = State('state1')
state2.lift_at = 0
state2.origin = {'p0':3, 'p1':2, 'p2':0}
state2.destin = {'p0':0, 'p1':0, 'p2':4}
state2.boarded = {'p0':False, 'p1':False, 'p2':False}
state2.served = {'p0':False, 'p1':False, 'p2':False}
print_state(state2)

print("- Define goal1:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal1 = Goal('goal1')
goal1.served = {'p0':True, 'p1':True, 'p2':True}
print_goal(goal1)

# Simple TESTS for OPERATORS
print("- Simple state change 1 ...")
print("\tMust return False: %s" % elevators_domain.up(state2, 2, 0))
print("\tMust return False: %s" % elevators_domain.board(state2, 'p1', 2))
elevators_domain.up(state2, 0, 2)
elevators_domain.board(state2, 'p1', 2)
print_state(state2)
print("- Simple state change 2 ...")
print("\tMust return False: %s" % elevators_domain.down(state2, 0, 2))
print("\tMust return False: %s" % elevators_domain.depart(state2, 'p1', 2))
elevators_domain.down(state2, 2, 0)
elevators_domain.depart(state2, 'p1', 0)
print_state(state2)


print("""
****************************************
Exercise 4 TEST
****************************************
""")

print("- Define state2")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state2 = State('state2')
state2.lift_at = 0
state2.origin = {'p0':3, 'p1':2, 'p2':0}
state2.destin = {'p0':0, 'p1':0, 'p2':4}
state2.boarded = {'p0':False, 'p1':False, 'p2':False}
state2.served = {'p0':False, 'p1':False, 'p2':False}
print_state(state2)

print("- Define goal2:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal2 = Goal('goal2')
goal2.served = {'p0':True, 'p1':True, 'p2':True}
print_goal(goal2)

pyhop(state2, [('serve_people', goal2)], verbose=3)


print("""
****************************************
Exercise 4 REAL
****************************************
""")

print("- Define state3")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state3 = State('state3')
state2.lift_at = 0
state2.origin = {'p1':1, 'p2':4, 'p3':2}
state2.destin = {'p1':4, 'p2':0, 'p3':5}
state2.boarded = {'p1':False, 'p2':False, 'p3':False}
state2.served = {'p1':False, 'p2':False, 'p3':False}
print_state(state2)

print("- Define goal3:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal2 = Goal('goal3')
goal2.served = {'p1':True, 'p2':True, 'p3':True}
print_goal(goal2)

pyhop(state2, [('serve_people', goal2)], verbose=3)
