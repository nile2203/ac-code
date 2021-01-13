from app_jwt import db


class CustomUser(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    password = db.Column(db.String(100), nullable=True)
    token = db.Column(db.Integer, db.ForeignKey('tokens.id'))

    def __repr__(self):
        return '<CustomUser: {} {}>'.format(self.id, self.email)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(100), nullable=True)
    user = db.relationship('CustomUser', backref='user', uselist=False)

    def __repr__(self):
        return '<Role: {} {}>'.format(self.id, self.name)


class AuthToken(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(500))
    refresh_token = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)
    user = db.relationship('CustomUser', backref='user_token', uselist=False)

    def __repr__(self):
        return '<Role: {} {}>'.format(self.id, self.name)