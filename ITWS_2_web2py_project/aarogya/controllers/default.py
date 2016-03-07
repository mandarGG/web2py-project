# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
   # auth.user.settings_register=URL('default','confirm')
    response.flash=T("Welcome!")
    return locals()

def confirm():
    response.flash = T("Congratulations!")
    return dict(message=T('Verification successful.Login normally Now!'))

def aboutus():
    response.flash=T("Great!")
    return locals()

def kma():
    response.flash=T("Read it!")
    return locals()

@auth.requires_login()
def show():
    if request.args:
        posts=db.post(request.args(0,cast=int))
	return locals()

@auth.requires_login()
def show_a():
    if request.args:
        posts_a=db.appointment(request.args(0,cast=int))
    return locals()

def show_m():
    if request.args:
        med_m=db.med(request.args(0,cast=int))
    return locals()

def show_s():
    if request.args:
        posts_s=db.profile(request.args(0,cast=int))
    return locals()

@auth.requires_login()
def comment():
	rows=db(db.post).select()
	return locals()

@auth.requires_login()
def prev_appoint():
    rows_a=db(db.appointment).select()
    return locals()

def viewm():
    rows_m=db(db.med).select()
    return locals()

def view_s():
    rows_s=db(db.profile).select()
    return locals()

def faq():
    response.flash="Ask it!"
    return locals()

@auth.requires_login()
def create():
    myform=SQLFORM(db.post).process()
    if myform.accepted:
        response.flash = "Posted!"
        redirect(URL('index'))
    return locals()


@auth.requires_login()
def cappoint():
    profile=db(db.profile).select()[0]
    x=int(profile.Start_time)
    y=int(profile.End_time)
    time=x
    i=0
    if not len(list):
        while time!=y:
            list.append(time)
            time=time+1
    return locals()

@auth.requires_login()
def see():
    count=0
    while(count<y-x):
        if request.args:
            start=request.args[0]
        if start in list:
            list.remove(start)
            count=count+1


@auth.requires_membership('managers')
def manage_s():
    grid_s=SQLFORM.grid(db.profile)
    return locals()

def contact():
    response.flash=T("Be in touch!")
    return locals()

@auth.requires_membership('managers')
def manage():
    grid=SQLFORM.grid(db.post)
    return locals()

@auth.requires_membership('assistant')
def manage_appoint():
    grid_appoint=SQLFORM.grid(db.appointment)
    return locals()

@auth.requires_membership('managers')
def manage_med():
    grid_m=SQLFORM.grid(db.med)
    return locals()


@auth.requires_login()
def appoint():
    aform=SQLFORM(db.appointment).process()
    if aform.accepted:
        response.flash = "Appointment confirmed!"#now send a email automatically
        redirect(URL('cappoint'))
    return locals()

@auth.requires_membership('assistant')
def equipm():
    eqform=SQLFORM(db.equip).process()
    if eqform.accepted:
        session.flash = "Equipment added!"
        redirect(URL('index'))
    return locals()

@auth.requires_membership('assistant')
def add_m():
    mform=SQLFORM(db.med).process()
    if mform.accepted:
        response.flash = "Medicine details added!"
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def add_staff():
    staff=SQLFORM(db.profile).process()
    if staff.accepted:
        response.flash = "Welcome to IIIT's Aarogya center!"
        redirect(URL('index'))
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login()
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
