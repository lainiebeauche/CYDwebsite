from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

ENGINE = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(ENGINE)
DBSession = sessionmaker(bind=ENGINE)
SESSION = DBSession()


def get_user_from_database(username):
    """Gets a :obj:`User` object by username.

    Args:
        username (str): the username of the user to retrieve.

    Returns:
        :obj:`User`: the :obj:`User` object for the given username.

    """
    return SESSION.query(User).filter_by(username=username).first()


def is_username_taken(username):
    """Test whether a username is already taken.

    Args:
        username (str): the username to check.

    Returns:
        bool: `True` if the username is already taken. `False` otherwise.

    """
    user = get_user_from_database(username)
    if user is None:
        # This user wasn't found, so the username isn't taken
        return False
    else:
        # We found a user with this username
        return True

    # Note that the above if-else statement is equivalent to just one line:
    # `return user is not None`


def add_user(name, username, password):
    """Add a user to the database.

    Args:
        name (str): the name of the user.
        username (str): the username of the user.
        password (str): the password for login.

    """
    user = User(
        name=name,
        username=username,
        password=password
    )
    SESSION.add(user)
    SESSION.commit()


def authenticate(username, password):
    """Test the given username and password combination.

    Args:
        username (str): the username to authenticate.
        password (str): the password to try.

    Returns:
        bool: `True` if the username exists and the password are correct;
            `False` otherwise.

    """
    user = get_user_from_database(username)
    if user is not None:
        correct_password = user.password
        return correct_password == password
    return False