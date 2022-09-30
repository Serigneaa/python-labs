import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.delete(newTable).where(newTable.columns.salary == 80000)
results = connection.execute(query)