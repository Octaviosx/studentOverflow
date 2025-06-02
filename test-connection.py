
import reflex as rx

@rx.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(next_page or url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@rx.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'