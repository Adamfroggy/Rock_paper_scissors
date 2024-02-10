from flask_sqlalchemy import SQLAlchemy

# create a DB objec from the SQLAlchemy class

DB = SQLAlchemy()


class User(DB.Model):
    # ID column
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # username column
    username = DB.Column(DB.String, nullable=False)
    # most recent tweet id
    newest_tweet_id = DB.Column(DB.BigInteger)
    # backref is as-if we had added a tweet list to the user class
    # tweets = []

    def __repr__(self):
        return f"User: {self.username}"


class Tweet(DB.Model):
    # ID column
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # text column
    text = DB.Column(DB.Unicode(300))
    # store our word embeddings "vectorization"
    vect = DB.Column(DB.PickleType, nullable=False)
    # user_id column (foreign / secondary key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    # user column creates a two-way link between a user object and  a tweet
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"Tweet: {self.text}"
