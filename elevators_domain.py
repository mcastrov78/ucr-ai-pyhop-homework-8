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
    for item in state.origin.items():
        origins.append([item[1], state.destin[item[0]]])
    origins.sort(key=lambda x: x[0])
    return origins


def board_people(state, goal):
    print("Arrivals: %s:" % get_possible_arrivals(state))
    for arrival in get_possible_arrivals(state):
        return [('board', arrival, state.lift_at)]


def unboard_people(state, goal):
    print("Departures: %s:" % get_possible_departures(state))
    for departure in get_possible_departures(state):
        return [('depart', departure, state.lift_at)]


def move_to(state, destiny):
    if state.lift_at < destiny:
        return [('up', state.lift_at, destiny)]
    elif state.lift_at > destiny:
        return [('down', state.lift_at, destiny)]
    return []


def serve(state, goal, ordered_origin_list):
    if len(ordered_origin_list) > 0:
        origin = ordered_origin_list.pop(0)
        return[('move_to', origin[0]),
               ('board_people', goal),
               ('move_to', origin[1]),
               ('unboard_people', goal),
               ('serve', goal, ordered_origin_list)]
    else: return[]


def serve_people(state, goal):
    return [('serve', goal, get_ordered_origin_list(state))]


pyhop.declare_methods('serve_people', serve_people)
pyhop.declare_methods('serve', serve)
pyhop.declare_methods('move_to', move_to)
pyhop.declare_methods('board_people', board_people)
pyhop.declare_methods('unboard_people', unboard_people)
