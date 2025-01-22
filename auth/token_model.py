from datetime import datetime, timedelta


class Token:
    def __init__(self, username: str, ttl: int, creation_time: datetime):
        self._username = username
        self._expiration = creation_time + timedelta(minutes= ttl)
        self._creation_time = creation_time

    def __hash__(self):
        return hash((self._username, self._creation_time.strftime("%Y-%m-%d %H:%M:%S.%f")))

    def belongs_to(self, username: str) -> bool:
        if self._username == username:
            return True
        return False

    def is_alive(self, current_date: datetime) -> bool:
        return self._expiration > current_date