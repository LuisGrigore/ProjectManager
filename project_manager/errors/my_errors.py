from project_manager.errors.https_errors import NotFoundError, NotPersistedError


class UserNotFoundError(NotFoundError):
    def __init__(self):
        super().__init__('User not found.')

class UserNotPersistedError(NotPersistedError):
    def __init__(self):
        super().__init__('User could not be saved.')