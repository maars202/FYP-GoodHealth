import os
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#            'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    # Mac user -------------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                            '@localhost:3306/Posts'
    # --------------------------------------------------------------------------------

    # # Windows user -------------------------------------------------------------------
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
    #                                         '@localhost:3306/SingHealth'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
    #                                         'pool_recycle': 280}
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        print(f"columns: {columns}")
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        print(f"columns: {columns}")
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result




@app.route('/')
def index():
    posts = Post.query.all()
    # return render_template('index.html', posts=posts)
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in posts]
        }
    ), 200


@app.route('/id')
def index2():
    post_id = 2
    post = Post.query.get_or_404(post_id)
    postcomments = post.comments
    # return render_template('index.html', posts=posts)
    return jsonify(
        {
            "data": [i.to_dict() for i in postcomments]
        }
    ), 200

@app.route('/joinTable')
def index3():
    result = db.engine.execute("""SELECT 
    post.id, post.title, post.content, COMMENT.content, COMMENT.post_id
FROM 
    post
INNER JOIN 
    COMMENT
ON
    post.id=COMMENT.post_id;""")
    print(f"result: {result}")
    for i in result:
        print(i)
    return jsonify(
        {
            "data": []
        }
    ), 200

db.create_all()

# @app.route('/<int:post_id>/')
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', post=post)

# db.drop_all()
# db.create_all()

# post1 = Post(title='Post The First', content='Content for the first post')
# post2 = Post(title='Post The Second', content='Content for the Second post')
# post3 = Post(title='Post The Third', content='Content for the third post')

# comment1 = Comment(content='Comment for the first post', post=post1)
# comment2 = Comment(content='Comment for the second post', post=post2)
# comment3 = Comment(content='Another comment for the second post', post_id=2)
# comment4 = Comment(content='Another comment for the first post', post_id=1)


# db.session.add_all([post1, post2, post3])
# db.session.add_all([comment1, comment2, comment3, comment4])

# db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)