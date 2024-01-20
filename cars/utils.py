from django.db.models import Q
from cars.models import Cars


def q_search(query):

    # if query.isdigit() and len(query) <= 4:
    #     str_query = str(query).zfill(4)
    #     return Cars.objects.all().filter(serial_number_vehicle=str_query)
    
    number_list = [number for number in query.split()]
    
    q_objects = Q()

    for token in number_list:
        token_mod = token.zfill(4)
        q_objects |= Q(serial_number_vehicle=token_mod)

    return Cars.objects.filter(q_objects)
