from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import psycopg2
import uvicorn
import time

conn = None
reconnect_attempt_number = 10

async def connection_cursor():
    global conn

    for i in range(reconnect_attempt_number):
        try:
            if conn is None:
                print("DB CONNECTION IS NOT INITIALIZED")
                raise Exception("DB CONNECTION IS NONE")
            return conn.cursor()
        except (psycopg2.DatabaseError, Exception) as error:
            try:
                print("TRYING TO INITIALIZE DB CONNECTION")
                conn = psycopg2.connect(database="gigachad",
                                        host="gigachad-db",
                                        user="admin",
                                        password="admin",
                                        port="5432")
                print("DB IS CONNECTED")

                return conn.cursor()
            except (psycopg2.DatabaseError, Exception) as error:
                print("DB IS NOT CONNECTED YET (ATTEMPT {}):".format(i))
                print(error)
                if reconnect_attempt_number > i + 1:
                    print("GONNA TRY TO RECONNECT")
                else:
                    print("THAT WAS LAST ONE")
                time.sleep(5)


security = HTTPBasic()
app = FastAPI(dependencies=[Depends(security)])


@app.get("/users")
async def get_users():
    cur = await connection_cursor()
    cur.execute("select * from users")
    return cur.fetchall()


uvicorn.run(app, host="0.0.0.0", port=8000)