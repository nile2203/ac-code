from app_jwt.models import CustomUser, db, AuthToken, Role
from app_jwt.utils.hashing import Hashing
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity


class CustomUserEntity:
    def __init__(self, user):
        self.user = user

    @staticmethod
    def get_by_username(username):
        user = CustomUser.query.filter_by(username=username).first()
        return CustomUserEntity(user=user) if user else None

    @staticmethod
    def does_exists(username):
        if CustomUser.query.filter_by(username=username).first():
            return 1

        return 0

    @staticmethod
    def create(username, password, role):
        if CustomUserEntity.does_exists(username) == 1:
            return 0, 'User already exists', None

        user = CustomUser(username=username, password=Hashing(value=password).get_hash(), role=role)
        CustomUserEntity.__save(user)
        return 1, 'User created successfully!', CustomUserEntity(user=user)

    def get_serialized(self):
        return {
            'id': self.user.id,
            'username': self.user.username,
            'role': self.user.role
        }

    def create_token(self):
        access_token = create_access_token(identity=self.user.username)
        refresh_token = create_refresh_token(identity=self.user.username)

        token = AuthToken(user=self.user, access_token=access_token, refresh_token=refresh_token)
        CustomUserEntity.__save(token)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    @staticmethod
    def refresh_token(refresh_token):
        access_token = create_access_token(identity=get_jwt_identity())
        auth_token = AuthToken.query.filter_by(refresh_token=refresh_token).first()
        auth_token.access_token = access_token
        CustomUserEntity.__save(auth_token)

        return {
            'access_token': access_token
        }

    @staticmethod
    def __save(db_object):
        db.session.add(db_object)
        db.session.commit()

    def verify_password(self, password):
        if Hashing(value=password).verify_hash(hashed_value=self.user.password):
            return 1

        return 0

    @staticmethod
    def is_user_admin(access_token):
        role_id = AuthToken.query.filter_by(access_token=access_token, is_active=True).first().user.role
        if Role.query.filter_by(id=role_id, name='admin').first():
            return 1

        return 0

    @staticmethod
    def get_header_token(headers):
        auth_header = headers.get('Authorization')
        auth_headers = auth_header.split(' ')
        if auth_headers:
            return auth_headers[1]

        return None

    def update(self, new_username):
        self.user.username = new_username
        CustomUserEntity.__save(self.user)
        return 1, 'Object updated successfully'

