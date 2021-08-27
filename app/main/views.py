from datetime import date
from flask import render_template, url_for, redirect, abort
from flask.globals import session
from flask.helpers import flash
from ..models import Cancel, Contact, Session
from . import main
from .forms import BookForm,FeedbackForm
from .. import db
from flask_login import login_required,current_user


@main.route('/')
def index():
    items= [
        {'id': 1,  'service': 'Black hair', 'price': 'Ksh.500'},
        {'id': 2,  'service': 'Box', 'price': 'Ksh.950'},
        {'id': 3,  'service': 'Beards', 'price': 'Ksh. 700'},
        {'id': 4,  'service': 'Dreadlocks', 'price': 'Ksh. 550'},
        {'id': 5,  'service': 'Obama', 'price': 'Ksh. 650'},
        {'id': 6,  'service': 'Facial hair', 'price': 'Ksh. 750'},
        {'id': 7,  'service': 'Buzzcut', 'price': 'Ksh. 800'},
        {'id': 8,  'service': 'Fade', 'price': 'Ksh. 1200'}
    ]
    return render_template('homepage.html', items=items)

@main.route('/book',methods=['POST','GET'])
@login_required
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
        return redirect(url_for('main.homepage'))
    return render_template('book.html',title=title,form=form)

@main.route('/delete_post/<int:id>',methods=['POST','GET'])
@login_required
def del_posts(id):
   com_to_del=Session.query.filter_by(id=id).first()
   com_to=Cancel(tarehe=com_to_del.tarehe, service=com_to_del.service, email=com_to_del.email, status='Freed')
   db.session.add(com_to)
   db.session.commit()

   db.session.delete(com_to_del)
   db.session.commit()
   flash('You have successfully cancelled a booked service', 'success')
   return redirect(url_for('main.homepage'))

@main.route('/edit_post/<int:id>',methods=['POST','GET'])
@login_required
def edit_session(id):
    art=Cancel.query.filter_by(id=id).first()
    print(art)
    if art is None:
        abort(404)
    if art.status=='Booked':
        art=Cancel.query.filter_by(id=id).first()
        com_to=Session(tarehe=art.tarehe, service=art.service, email=art.email, status='Freed')
        db.session.add(com_to)
        db.session.commit()
        db.session.delete(art)
        db.session.commit()
        return redirect(url_for('main.homepage') )
    else:
        art=Cancel.query.filter_by(id=id).first()
        com_to=Session(tarehe=art.tarehe, service=art.service, email=current_user.email, status='Booked')
        db.session.add(com_to)
        db.session.commit()
        db.session.delete(art)
        db.session.commit()
        return redirect(url_for('main.homepage') )
    return redirect(url_for('main.index'))


@main.route('/homepage')
@login_required
def homepage():
    title='Home'
    sessions=Session.query.filter_by(status="Booked").all()
    available=Session.query.filter_by(status="Freed").all()

    session=Cancel.query.all()
    print(sessions)
    return render_template('index.html',title=title, session=sessions, sessions=session, available=available)

@main.route('/contact', methods=['GET','POST'])
def contact():
    form= FeedbackForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        message=form.message.data
        feedback=Contact(name=name, message=message, email=email)  
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('contact.html',form=form)