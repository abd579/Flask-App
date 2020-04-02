from flask import Flask, render_template and request , url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Abdullah Mahmud',
        'title': 'Science',
        'content': 'CSE',
        'date_posted': 'April 2, 2020'
    }
    {
        'author': 'Sajjel hossain',
        'title': 'Science',
        'content': 'CSE',
        'date_posted': 'April 2, 2020'
    }
]
@app.route("/")
def main():
    return render_template('app.html')
@app.route('/send , methods=['POST']')
def send():
    if request.method =='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html',sum=sum)
        elif operation == 'subtraction':
            sum = float(num1) - float(num2)
            return render_template('app.html',sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * (num2)
            return render_template('app.html',sum=sum)
        elif operation == 'divide':
            sum = float(num1) / (num2)
            return render_template('app.html',sum=sum)
        else:
            return render_template('app.html')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


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


if __name__ == '__main__':
    app.run(debug=True)
