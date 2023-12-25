from sqlalchemy import create_engine
from werkzeug.security import (
        check_password_hash,
        generate_password_hash
    )

from accounts import UPLOAD_FOLDER, DataBaseDeclare
from accounts.extensions import database as db
from accounts.utils import (
        get_unique_filename,
        remove_existing_file,
        unique_security_token,
        unique_uid,
    )

from datetime import datetime, timedelta
import os


DATABASE_URL = os.getenv('DATABASE_URI', None)

engine = create_engine(DATABASE_URL, echo=True)
class User(autoload_with=engine):
    """
    A Base User model class.
    """

    __tablename__ = 'user'

    id = db.Column(db.String(38), primary_key=True, default=unique_uid, unique=True, nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    active = db.Column(db.Boolean, default=True, nullable=True)
    security_token = db.Column(db.String(200), default=unique_security_token)
    is_send = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    profile = db.Relationship('Profile', backref='user', cascade='save-update, merge, delete')

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save_profile(self):
        profile = Profile(user_id=self.id)
        profile.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        self.save_profile()
    
    def is_active(self):
        return self.active
    
    def is_token_expire(self):
        expiry_time = (
            self.is_send
            + timedelta(minutes=15)
        )
        current_time = datetime.now()
        return expiry_time <= current_time
        
    def __repr__(self):
        return '<User> {}'.format(self.email)


class Profile(DataBaseDeclare):
    """
    A User profile model class.
    """

    __tablename__ = 'profile'

    id = db.Column(db.String(38), primary_key=True, default=unique_uid, unique=True, nullable=False)
    bio = db.Column(db.String(200), default='')
    phone_number = db.Column(db.String(200), default='')
    city = db.Column(db.String(200), default='')
    avator = db.Column(db.String(250), default='')

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    user_id = db.Column(db.String(38), db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return '<Profile> {}'.format(self.user.username)

    def set_avator(self, profile_image):
        if self.avator:
            path = os.path.join(UPLOAD_FOLDER, self.avator)
            remove_existing_file(path=path)
            
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(os.path.join(UPLOAD_FOLDER), exist_ok=True)
            
        self.avator = get_unique_filename(profile_image.filename)
        profile_image.save(os.path.join(UPLOAD_FOLDER, self.avator))

    def save(self):
        db.session.add(self)
        db.session.commit()