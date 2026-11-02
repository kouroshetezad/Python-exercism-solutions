"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons_id):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons_id)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_wagon , second_wagon , *rest = each_wagons_id
    each_wagons_id = rest + [first_wagon, second_wagon]
    one_pos = each_wagons_id.index(1)
    each_wagons_id.pop(one_pos)
    each_wagons_id.insert(0, 1)
    one , *rest = each_wagons_id
    final_list = [one] + missing_wagons + rest

    return final_list

def add_missing_stops(route , **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stop_stations = []
    for stop in stops.values():
        stop_stations.append(stop)
    route['stops'] = stop_stations
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route = {**route , **more_route_information}
    return extended_route

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    first_row = []
    second_row = []
    third_row = []
    for row in wagons_rows: 
        
        first_row.append(row[0])
        second_row.append(row[1])
        third_row.append(row[2])
    wagons_rows = first_row , second_row , third_row
    return list(wagons_rows)