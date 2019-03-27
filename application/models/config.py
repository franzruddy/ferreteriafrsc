import web


#db_host = 'localhost'
#db_name = 'ferreteriafrsc'
#db_user = 'ferreteriafrsc'
#db_pw = 'ferreteriafrsc.2019'



db_host = 'ffn96u87j5ogvehy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'z1rrqah4pevhxp8b'
db_user = 'oghxt0d6syslw8fv'
db_pw = 'gg2kpeb9a6bp8m52'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )