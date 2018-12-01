from flask import render_template
from app import app

class routes:
    """
    Routes class takes care of all webpages being created, in the MVC it acts as the view.
    """

    @app.route('/')
    @app.route('/index')
    def index():
        """
        Index page
        """
        user = {'username': 'MrDemnoc'}
        posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            }
        ]
        return render_template('index.html', title='Home', user=user, posts=posts)
