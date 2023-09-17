from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == GET:
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='failure')
            pass
        elif len(firstName) < 2:
            flash("First name must be more than 1 character", category='failure')
            pass
        elif password1 != password2:
            flash("Passwords must match", category='failure')
            pass
        elif len(password1) < 7:
            flash("Password must have 7 or more characterrs", category='failure')
            pass
        else:
            flash("Account created", category='success')
            #Add user to database
    return render_template("sign_up.html", methods=['GET', 'POST'])