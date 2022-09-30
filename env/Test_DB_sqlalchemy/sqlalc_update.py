import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(newTable).values(salary=100000).where(newTable.columns.Id == 1)

result = connection.execute(query)