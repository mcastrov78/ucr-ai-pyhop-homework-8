from pyhop import *
import blocks_world_operators
import blocks_world_methods

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
