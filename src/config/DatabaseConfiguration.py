
def init_db(app,env):
    #implement later
    host=env['datasource']['host']
    driver=env['datasource']['driver']
    username=env['datasource']['username']
    password=env['datasource']['password']
    port=env['datasource']['port']
    database=env['datasource']['database']
    cnxString = 'mssql+pyodbc://{}:{}@{}/{}?driver={}'.format(username,password,host,database,driver)
    app.config['SQLALCHEMY_DATABASE_URI'] = cnxString
    # engine = sa.create_engine(cnxString)
    print("-"*40)
    print("Initialized the database")
    print("-"*40)
    return app
