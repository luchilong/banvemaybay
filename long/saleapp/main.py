from flask import render_template, request, redirect
from saleapp import app, utils, login
from saleapp.models import User
from flask_login import login_user
from saleapp.admin import *
import hashlib, os


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)


@app.route("/products")
def product_list():
    kw = request.args.get("kw")
    cate_id = request.args.get("category_id")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    products = utils.read_products(cate_id=cate_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template('products.html',
                           products=products)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product-detail.html',
                           product=product)


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if password == confirm_password:
            avatar = request.files["avatar"]
            avatar_path = 'images/upload/%s' % avatar.filename
            avatar.save(os.path.join(app.config['ROOT_PROJECT_PATH'],
                                     'static/', avatar_path))

            if utils.add_user(name=name, email=email, username=username,
                              password=password, avatar=avatar_path):
                return redirect('/admin')
        else:
            err_msg = "Mật khẩu KHÔNG khớp!"

    return render_template('register.html', err_msg=err_msg)


@app.route("/login", methods=['post'])
def login_usr():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = User.query.filter(username==username,
                                 password==password).first()

        if user:
            login_user(user=user)

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return User.query.get(user_id)



if __name__ == "__main__":
    app.run(debug=True)
