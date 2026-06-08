class DomainError(Exception):
    pass


class NotFoundError(DomainError):
    pass


class DuplicatedError(DomainError):
    pass


class DatabaseError(DomainError):
    pass