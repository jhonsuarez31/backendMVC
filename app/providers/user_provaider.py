from flask import jsonify
from core.db.session import db_session
from models.user import User
from flask import abort as flask_abort


#Get user by id
def get_by_id (id, abort=False):
    user = db_session.query(User).filter_by(id=id).first()
    if user is None and abort:
        flask_abort(404, f'El usuario  no existe en el sistema.')
    return user

#Get user by email
def get_by_id(email, abort=False):
    user = db_session.query(User).filter_by(email=email).first()
    if user is None and abort:
        flask_abort(404, f'El usuario  no existe en el sistema.')
    return user

#Get all user

def get_all_users():
    users = db_session.query(User).all()
    return users

# Delete user
def delete_user(id):
    user = get_by_id(id=id)
    db_session.delete(user)
    db_session.commit()

# Register user

