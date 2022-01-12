from enum import Enum


def enum_to_string(cls) -> str:
    return ', '.join([f'{e.name}' for e in cls])


class department(Enum):
    IT = 'it-services.com'
    SALES = 'sales-dep.com'
    PRESALES = 'pre-sales.com'
    FULFILLMENT = 'fulfillment.com'
    SUPPORT = 'customer-support.com'
