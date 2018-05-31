from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

def run():

    db=create_engine('mysql://One_example:1234567@localhost/project_one',echo=False)

    metadata = MetaData(db)
    application_table = Table('job_application_job_1',metadata,
                  Column('id',Integer,primary_key=True),
                  Column('firstQuestion',String),
                  Column('secondQuestion',Float),
                  Column('thirdQuestion',Float),
                  Column('fourthQuestion',String),
                  Column('fifthQuestion',String),
                  Column('user',Integer),
                  )

    applications = application_table.select().execute()

    for x in applications:
        a = open(str(x.user+"_application.txt"),'w')
        a.write("Tell us about yourself.\n"+str(x.firstQuestion)+"\n\nHow much experience do you have in a similar position?\n"+
        str(x.secondQuestion)+"\n\nWhat are your salary expectations?\n"+str(x.thirdQuestion)+"\n"+
        "\nWhat are your strengths and weaknesses?\n\n"+str(x.fourthQuestion)+"\n\n"+"When can you start?\n"+str(x.fifthQuestion)        
          )
        a.close()
