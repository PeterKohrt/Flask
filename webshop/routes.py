from flask import render_template, url_for, flash, redirect #, request, Flask 
from webshop import app, db
from webshop.models import Article
from webshop.forms import RegistrationForm, LoginForm, ArticleForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/allarticle")
def allarticle():
    article_list = Article.query.all()
    return render_template('all_article.html', posts=article_list)

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

@app.route("/article", methods=['GET', 'POST'])
def article():
    form = ArticleForm()
    if form.validate_on_submit():
        article_x = Article(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(article_x)
        db.session.commit()
        flash(f'Article {form.name.data} added!', 'success')
        return redirect(url_for('article'))
    return render_template('article.html', title='Article', form=form)