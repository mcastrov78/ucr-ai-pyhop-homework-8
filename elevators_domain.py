import pyhop


# Operators
def up(state, f1, f2):
    if state.lift_at == f1 and f2 > f1:
        state.lift_at = f2
        return state
    else: return False


def down(state, f1, f2):
    if state.lift_at == f1 and f2 < f1:
        state.lift_at = f2
        return state
    else: return False


def board(state, p, f):
    if state.lift_at == f and state.origin[p] == f:
        state.boarded[p] = True
        return state
    else: return False


def depart(state, p, f):
    if state.lift_at == f and state.destin[p] == f and state.boarded[p]:
        state.boarded[p] = False
        state.served[p] = True
        return state
    else: return False


pyhop.declare_operators(up, down, board, depart)


# Methods
def get_possible_arrivals(state):
    arrivals = []
    for origin in state.origin.items():
        passenger = origin[0]
        floor = origin[1]
        if state.lift_at == floor and not state.boarded[passenger] and not state.served[passenger]:
            arrivals.append(passenger)
    return arrivals


def get_possible_departures(state):
    departures = []
    for departure in state.destin.items():
        passenger = departure[0]
        floor = departure[1]
        if state.lift_at == floor and state.boarded[passenger] and not state.served[passenger]:
            departures.append(departure[0])
    return departures


def get_ordered_origin_list(state):
    origins = []
    for origin in state.origin.values():
        origins.append(origin)
    origins.sort()
    return origins


def get_ordered_destin_list(state):
    destins = []
    for destin in state.destin.values():
        destins.append(destin)
    destins.sort()
    return destins


def serve_people(state, goal):
    ordered_origin_list = get_ordered_origin_list(state)
    ordered_destin_list = get_ordered_destin_list(state)
    print("Origins: %s:" % ordered_origin_list)
    print("Destins: %s:" % ordered_destin_list)

    board_next(state, ordered_destin_list)

    '''
    print("Arrivals: %s:" % get_possible_arrivals(state))
    for arrival in get_possible_arrivals(state):
        board(state, arrival, state.lift_at)
    pyhop.print_state(state)

    print("Departures: %s:" % get_possible_departures(state))
    for departure in get_possible_departures(state):
        depart(state, arrival, state.lift_at)
    pyhop.print_state(state)
    '''
    return False


def board_next(state, ordered_origin_list):
    if state.lift_at == ordered_origin_list[0]:
        for arrival in get_possible_arrivals(state):
            board(state, arrival, state.lift_at)
            pyhop.print_state(state)
        ordered_origin_list.pop(0)
        return [('board_next', state, ordered_origin_list)]

    elif state.lift_at < ordered_origin_list[0]:
        #for next_origin in ordered_origin_list:
        up(state, state.lift_at, ordered_origin_list[0])
        for arrival in get_possible_arrivals(state):
            board(state, arrival, state.lift_at)
            pyhop.print_state(state)
        ordered_origin_list.pop(0)
        return [('board_next', state, ordered_origin_list)]
    return False

pyhop.declare_methods('serve_people', serve_people, board_next)