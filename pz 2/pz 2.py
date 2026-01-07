import hashlib
from datetime import datetime


class User:

    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = True

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)

    def __str__(self):
        return f"User: {self.username}, Role: {self.__class__.__name__}"


class Administrator(User):

    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else ["admin_panel", "manage_users"]

    def grant_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)


class RegularUser(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_login_time(self):
        self.last_login = datetime.now()


class GuestUser(User):

    def __init__(self, username, password=""):
        super().__init__(username, password)
        self.read_only = True

    def verify_password(self, password):
        return super().verify_password(password)


class AccessControl:

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username in self.users:
            raise ValueError(f"Користувач {user.username} вже існує.")
        self.users[user.username] = user
        print(f"Користувача {user.username} ({type(user).__name__}) додано.")

    def authenticate_user(self, username, password):

        user = self.users.get(username)

        if not user:
            print(f"Помилка входу: користувача {username} не знайдено.")
            return None

        if not user.is_active:
            print(f"Помилка входу: акаунт {username} деактивовано.")
            return None

        if user.verify_password(password):
            print(f"Вхід успішний: {username}")

            if isinstance(user, RegularUser):
                user.update_login_time()

            return user
        else:
            print(f"Помилка входу: невірний пароль для {username}.")
            return None


if __name__ == "__main__":
    ac = AccessControl()

    admin = Administrator("admin_max", "secureAdminPass123")
    user_bob = RegularUser("bob_builder", "pizza123")
    guest = GuestUser("guest_01")  # Пароль за замовчуванням пустий або можна задати
    ac.add_user(admin)
    ac.add_user(user_bob)
    ac.add_user(guest)

    print("-" * 30)

    current_user = ac.authenticate_user("admin_max", "secureAdminPass123")
    if current_user:
        print(f"Права доступу: {current_user.permissions}")

    print("-" * 30)

    ac.authenticate_user("bob_builder", "wrong_password")

    print("-" * 30)

    reg_user = ac.authenticate_user("bob_builder", "pizza123")
    if reg_user:
        print(f"Останній вхід: {reg_user.last_login}")