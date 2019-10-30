from pyhop import *
import elevators_domain

print('')
print_operators()

print('')
print_methods()

print("""
****************************************
Exercise 2
****************************************
""")

print("- Define state1: a on b, b on c, c on d, d on e, e on table")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state1 = State('state1')
state1.pos = {'a':'b',  'b':'c', 'c':'d', 'd':'e', 'e':'table'}
state1.clear = {'a':True, 'b':False, 'c':False, 'd':False, 'e':False}
state1.holding = False
print_state(state1)

print("- Define goal1:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal1 = Goal('goal1')
goal1.pos = {'d':'table'}
goal1.clear = {'d':True}
goal1.holding = False
print_goal(goal1)

pyhop(state1, [('move_blocks', goal1)], verbose=1)


print("""
****************************************
Exercise 3
****************************************
""")

print("- Define state1")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state1 = State('state1')
state1.lift_at = 0
state1.origin = {'p0':3, 'p1':2, 'p2':0}
state1.destin = {'p0':0, 'p1':0, 'p2':4}
state1.boarded = {'p0':False, 'p1':False, 'p2':False}
state1.served = {'p0':False, 'p1':False, 'p2':False}
print_state(state1)

print("- Define goal1:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal1 = Goal('goal1')
goal1.served = {'p0':True, 'p1':True, 'p2':True}
print_goal(goal1)

print("- Simple state change 1 ...")
print("\tMust return False: %s" % elevators_domain.up(state1, 2, 0))
print("\tMust return False: %s" % elevators_domain.board(state1, 'p1', 2))
elevators_domain.up(state1, 0, 2)
elevators_domain.board(state1, 'p1', 2)
print_state(state1)
print("- Simple state change 2 ...")
print("\tMust return False: %s" % elevators_domain.down(state1, 0, 2))
print("\tMust return False: %s" % elevators_domain.depart(state1, 'p1', 2))
elevators_domain.down(state1, 2, 0)
elevators_domain.depart(state1, 'p1', 0)
print_state(state1)

# Planning Tests
state1 = State('state1')
state1.lift_at = 0
state1.origin = {'p0':3, 'p1':2, 'p2':0}
state1.destin = {'p0':0, 'p1':0, 'p2':4}
state1.boarded = {'p0':False, 'p1':False, 'p2':False}
state1.served = {'p0':False, 'p1':False, 'p2':False}
print_state(state1)

pyhop(state1, [('serve_people', goal1)], verbose=1)