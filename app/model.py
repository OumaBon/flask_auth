from app import db, bcrypt, login_manager


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"{self.username,\
            self.email
    }"

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def get_user_email(cls, email):
        return cls.query.filter_by(email= email).first()




@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user
