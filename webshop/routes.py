from flask import render_template, url_for, flash, redirect #, request, Flask 
from webshop import app, db
from webshop.models import Article
from webshop.forms import RegistrationForm, LoginForm, ArticleForm

"""from flask_restplus import Resource, Api

todos = {}
api = Api(app)

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
"""

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/article_add", methods=['GET', 'POST'])
def article_add():
    form = ArticleForm()
    if form.validate_on_submit():
        article_x = Article(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(article_x)
        db.session.commit()
        flash(f'Article {form.name.data} added!', 'success')
        return redirect(url_for('article_add'))
    return render_template('article_add.html', title='Add Article', form=form)