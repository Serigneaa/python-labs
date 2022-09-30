import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/mydatabase')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

print(actor.columns.keys())
print(repr(metadata.tables['actor']))