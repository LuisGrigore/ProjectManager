from project_manager.errors.network_base_error import NetworkError


class NotPersistedError(NetworkError):
    def __init__(self, message: str = 'Object not persisted'):
        super().__init__(message, 500)

class NotFoundError(NetworkError):
    def __init__(self, message: str = 'Object not found'):
        super().__init__(message, 404)
