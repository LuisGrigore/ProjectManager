from project_manager.errors.base_error import Error

class NetworkError(Error):
    def __init__(self, message: str = '', status_code: int = 200):
        super().__init__(message)
        self.status_code = status_code


