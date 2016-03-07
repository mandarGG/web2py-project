# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

#response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  #_class="brand",_href="http://www.web2py.com/")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Sign in'),False,URL('user/login'), []),
    (T('About us'), False, URL('default','aboutus'), []),
    (T('Contact Us'), False, URL('default', 'contact'), []),
    (T('FAQ'), False, URL('default', 'faq'), []),
    (T('Key medical Advices'), False, URL('default', 'kma'), [])
  



]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources

    response.menu += [
        (SPAN('Staff Section', _class='highlighted'), False,URL('default', 'view_s') , [
        (T('A quick look'), False,URL('default', 'view_s')),
        (T('New Staff member? Add here'),False,URL('default','add_staff')),
        (T('Manage'),False,URL('default','manage_s')),

                ]
        )]
   
    response.menu += [
        (SPAN('Appointments Section', _class='highlighted'), False,URL('default', 'prev_appoint') , [
        (T('View Appointments '), False,URL('default', 'prev_appoint')),
        (T('Take an Appointment'),False,URL('default','appoint')),
        (T('Manage Appointments '),False,URL('default','manage_appoint')),


                ]
        )]

    response.menu += [
        (SPAN('Medicine and equipment Section', _class='highlighted'), False,URL('default', 'viewm') , [
        (T('A quick look'), False,URL('default', 'viewm')),
        (T('Add equipments/medicines'),False,URL('default','add_m')),
        (T('Manage'),False,URL('default','manage_med')),

                ]
        )]

    response.menu += [
        (SPAN('Comments Section', _class='highlighted'), False,URL('default', 'comment') , [
        (T('View Comments'), False,URL('default', 'comment')),
        (T('Post a Comment'),False,URL('default','create')),
        (T('Manage Comments'),False,URL('default','manage')),


                ]
        )]
    response.menu += [
        (SPAN('More IIIT Sites', _class='highlighted'), False, 'http://iiit.ac.in', [
        (T('Student Mail'), False,'http://students.iiit.ac.in'),
        (T('Research Mail'),False,'http://research.iiit.ac.in'),
        (T('Course Portal'),False,'http://courses.iiit.ac.in'),
        (T('Mess Portal'),False,'http://mess.iiit.ac.in'),
        (T('Felicity 2k15'),False,'http://felicity.iiit.ac.in'),


                ]
         )]
    

if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
