FROM python:3.6

# Create app directory
WORKDIR /app
EXPOSE 5000

COPY . /app
RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install requests
RUN python3 -m pip install pymongo

ENV FLASK_APP "dataBase.py"

ENTRYPOINT [ "flask" ]
CMD ["run", "-h", "0.0.0.0"]

# docker build -t name . 
# sudo docker run -it -p 51001:5000 -d name