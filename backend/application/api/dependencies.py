
from backend.infrastructure.uow.unit_of_work import UnitOfWork


def get_uow():
    uow = UnitOfWork()
    try:
        yield uow
    finally:
        uow.close()