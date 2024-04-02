FROM bitnami/python

COPY main.py main.py

RUN pip3 install psycopg2-binary
RUN pip3 install fastapi
RUN pip3 install uvicorn

CMD [ "python3", "./main.py"]