import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.insert(newTable)
new_records = [{'Id':'2', 'name':'Software Ninjaneer', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'Data Scientist', 'salary':70000, 'active':True}]
result_proxy = connection.execute(query, new_records)