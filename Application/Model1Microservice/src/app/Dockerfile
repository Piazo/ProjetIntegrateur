FROM python:3.8

RUN pip3 install pipenv

ENV PROJECT_DIR /usr/src/applicationapi

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
# COPY Pipfile.lock .
COPY . .

# --ignore-pipfile
RUN pipenv install --deploy 
RUN pipenv install flask
RUN pipenv install flask-restful

EXPOSE 5000

CMD ["pipenv", "run", "python", "main.py"]