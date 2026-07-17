from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, User)

    def get_by_email(self, email):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_username(self, username):
        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )