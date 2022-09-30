import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
              )

metadata.create_all(engine)