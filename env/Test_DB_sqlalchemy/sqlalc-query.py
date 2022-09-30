import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:3695@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'PENELOPE')
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)