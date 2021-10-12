## StudentPostgresql_Alembic_with FastAPI
>Create a Database connection with Postgresql

>Create model class with table name and column,
perform CRUD operation using POST and GET methods

>Initialize Alembic in command line by using **alembic init alembic**

>It will create a Folder called Alembic with alembic.ini file

>Go to alembic.ini file to change the db url to Postgresql url

>Then create a table using **alembic revision -m "create user table"**

>Which creates the user.py file under Alembic folder > Version

>You can go to that file, there will be two option upgrade() and degrade() where you can give table columns,
**alembic upgrade head**

>Run python file under **uvicorn sql_app.main:app --reload**

>Code samples from https://www.youtube.com/c/MKFastt/videos
