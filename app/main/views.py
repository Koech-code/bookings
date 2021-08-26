from datetime import date
from flask import render_template, url_for, redirect, abort
from flask.globals import session
from flask.helpers import flash
from ..models import Cancel, Session
from . import main
from .forms import BookForm
from .. import db


@main.route('/')
def index():
    title='Home'
    sessions=Session.query.filter_by(status="Booked").all()
    available=Session.query.filter_by(status="Freed").all()

    session=Cancel.query.all()
    print(sessions)
    return render_template('index.html',title=title, session=sessions, sessions=session, available=available)

@main.route('/book',methods=['POST','GET'])
def book():
    title='Book'
    form= BookForm()
    if form.validate_on_submit():
        tarehe=form.tarehe.data
        service=form.service.data
        email=form.email.data
        booking=Session(tarehe=tarehe, service=service, email=email, status='Booked')  
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('book.html',title=title,form=form)

@main.route('/delete_post/<int:id>',methods=['POST','GET'])
def del_posts(id):
   com_to_del=Session.query.filter_by(id=id).first()
   com_to=Cancel(tarehe=com_to_del.tarehe, service=com_to_del.service, email=com_to_del.email, status='Freed')
   db.session.add(com_to)
   db.session.commit()

   db.session.delete(com_to_del)
   db.session.commit()
   flash('You have successfully cancelled a booked service', 'success')
   return redirect(url_for('main.index'))

@main.route('/edit_post/<int:id>',methods=['POST','GET'])
# @login_required
# @permission_required(Permission.MODERATE_COMMENTS)
def edit_session(id):
    art=Session.query.filter_by(id=id).first()
    print(art)
    if art is None:
        abort(404)
            
    if art.status=='Booked':
        art.status='Freed'
        db.session.add(art)
        db.session.commit()
        return redirect(url_for('main.index') )
    else:
        art.status='Booked'
        db.session.add(art)
        db.session.commit()

    return render_template('index.html')
    