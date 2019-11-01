import pyhop


# Operators
def up(state, f1, f2):
    """taken from:
        (:action up
        :parameters (?f1 - floor ?f2 - floor)
        :precondition (and (lift-at ?f1) (above ?f1 ?f2))
        :effect (and (lift-at ?f2) (not (lift-at ?f1))))"""
    if state.lift_at == f1 and f2 > f1:
        state.lift_at = f2
        return state
    else:
        return False


def down(state, f1, f2):
    """taken from:
        (:action down
        :parameters (?f1 - floor ?f2 - floor)
        :precondition (and (lift-at ?f1) (above ?f2 ?f1))
        :effect (and (lift-at ?f2) (not (lift-at ?f1))))"""
    if state.lift_at == f1 and f2 < f1:
        state.lift_at = f2
        return state
    else:
        return False


def board(state, p, f):
    """taken from:
        (:action board
        :parameters (?f - floor ?p - passenger)
        :precondition (and (lift-at ?f) (origin ?p ?f))
        :effect (boarded ?p))"""
    if state.lift_at == f and state.origin[p] == f:
        state.boarded[p] = True
        return state
    else:
        return False


def depart(state, p, f):
    """taken from:
        (:action depart
        :parameters (?f - floor ?p - passenger)
        :precondition (and (lift-at ?f) (destin ?p ?f)
            (boarded ?p))
        :effect (and (not (boarded ?p))
            (served ?p)))"""
    if state.lift_at == f and state.destin[p] == f and state.boarded[p]:
        state.boarded[p] = False
        state.served[p] = True
        return state
    else:
        return False


pyhop.declare_operators(up, down, board, depart)


# Methods
def get_ordered_origin_list(state, goal):
    """Returns an ordered list of origins for passengers in goal"""
    origins = []
    for origin in state.origin.items():
        passenger = origin[0]
        if passenger in goal.served and goal.served[passenger]:
            origins.append([origin[1], state.destin[origin[0]]])
    origins.sort(key=lambda o: o[0])
    return origins


def move_to(state, target):
    """Moves lift from current flor to target floor"""
    if state.lift_at < target:
        return [('up', state.lift_at, target)]
    elif state.lift_at > target:
        return [('down', state.lift_at, target)]
    return []


def board_people(state, goal):
    """Boards all passengers that can and should be boarded on this floor"""
    arrivals = []
    for origin in state.origin.items():
        passenger = origin[0]
        if passenger in goal.served and goal.served[passenger]:
            floor = origin[1]
            if state.lift_at == floor and not state.boarded[passenger] and not state.served[passenger]:
                arrivals.append(('board', passenger, state.lift_at))
    return arrivals

def depart_people(state, goal):
    """Departs all passengers that can depart on this floor"""
    departures = []
    for departure in state.destin.items():
        passenger = departure[0]
        if passenger in goal.served and goal.served[passenger]:
            floor = departure[1]
            if state.lift_at == floor and state.boarded[passenger] and not state.served[passenger]:
                departures.append(('depart', passenger, state.lift_at))
    return departures


def all_served(state, goal):
    """Checks whether all passengers in goal have been served"""
    for thisPassenger in state.served:
        if not state.served[thisPassenger] and thisPassenger in goal.served and goal.served[thisPassenger]:
            return False
    return True


def serve_people(state, goal, ordered_origin_list=None):
    """Takes each passenger in goal to their target floor"""
    if ordered_origin_list is None:
        ordered_origin_list = get_ordered_origin_list(state, goal)
    while not all_served(state, goal):
        origin = ordered_origin_list.pop(0)
        return[('move_to', origin[0]),
               ('board_people', goal),
               ('move_to', origin[1]),
               ('depart_people', goal),
               ('serve_people', goal, ordered_origin_list)]
    return[]


pyhop.declare_methods('serve_people', serve_people)
pyhop.declare_methods('move_to', move_to)
pyhop.declare_methods('board_people', board_people)
pyhop.declare_methods('depart_people', depart_people)
