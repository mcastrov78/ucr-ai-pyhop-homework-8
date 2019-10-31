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

print("- Define state: a on b, b on c, c on d, d on e, e on table")
"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""
state = State('state')
state.pos = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'table'}
state.clear = {'a':True, 'b':False, 'c':False, 'd':False, 'e':False}
state.holding = False
print_state(state)

print("- Define goal:")
"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values.
"""
goal = Goal('goal')
goal.pos = {'d': 'table'}
goal.clear = {'d':True}
goal.holding = False
print_goal(goal)

pyhop(state, [('move_blocks', goal)], verbose=1)
