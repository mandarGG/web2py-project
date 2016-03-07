db.define_table('post',
		Field('Name',requires=IS_NOT_EMPTY()),
		Field('Comments','text',requires=IS_NOT_EMPTY()),
		auth.signature)

db.define_table('appointment',
        Field('Your_Name',requires=IS_NOT_EMPTY()),
        Field('Doctors_Name',requires=IS_NOT_EMPTY()),
        Field('Reason','text',requires=IS_NOT_EMPTY()),
        Field('Date_of_appointment','date',requires=IS_NOT_EMPTY()),
        auth.signature)

db.define_table('equip',
        Field('Name_of_equipment',requires=IS_NOT_EMPTY()),
        Field('No_of_working_equip',requires=IS_NOT_EMPTY()),
        Field('Brought_on','date'),
        Field('Photo_equip','upload'),
        )

db.define_table('med',
        Field('Name_of_medicine',requires=IS_NOT_EMPTY()),
        Field('No_of_units_available',requires=IS_NOT_EMPTY()),
        Field('medimage','upload'),
        Field('sp_use','text'),
        )

db.define_table('profile',
        Field('Name_of_staffmember',requires=IS_NOT_EMPTY()),
        Field('Date_of_birth','date',requires=IS_DATE()),
        Field('Qualification','text',requires=IS_NOT_EMPTY()),
        Field('Photo','upload'),
        Field('Speciality','text'),
        Field('Start_time','text'),
        Field('End_time','text'),
        )
list=[]
