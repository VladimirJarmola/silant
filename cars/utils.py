from django.db.models import Q
from cars.models import Cars


def q_search(query):

    number_list = []
    for number in query.split():
        if number.isdigit():
            number_list.append(number)

    q_objects = Q()

    if number_list:
        for token in number_list:
            if token.isdigit():
                token_mod = token.zfill(4)
                q_objects |= Q(serial_number_vehicle=token_mod)
        return Cars.objects.filter(q_objects)
    else:
        return None
