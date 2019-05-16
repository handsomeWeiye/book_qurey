from flask import redirect,url_for,render_template,flash
from qurey_systerm import db,app
from qurey_systerm.forms import Updata
from qurey_systerm.models import Data
from qurey_systerm import bootstrap

@app.route('/',methods=['GET','POST'])
def index():


    datas = Data.query.order_by(Data.timestamp.desc()).all()
    form = Updata()

    if form.validate_on_submit():
        author = form.author.data
        book = form.book.data
        updata = Data(author=author,book=book)
        db.session.add(updata)
        db.session.commit()
        flash('query success')
        return redirect(url_for('index'))

    return render_template('index.html', datas=datas, form=form)



