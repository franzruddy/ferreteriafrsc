import web

db_host = 'localhost'
db_name = 'ferreteriafrsc'
db_user = 'ferreteriafrsc'
db_pw = 'ferreteriafrsc.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )