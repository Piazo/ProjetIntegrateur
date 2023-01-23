FROM python:3.8

# Create app directory
WORKDIR /app
EXPOSE 5000

COPY . /app
RUN pip --timeout=100 install flask
RUN pip --timeout=100 install flask-restful
RUN pip --timeout=100 install requests

ENV FLASK_APP "modelMicroserviceControler.py"

ENTRYPOINT [ "flask" ]
CMD ["run", "-h", "0.0.0.0"]

# docker build -t name . 
# sudo docker run -it -p 51001:5000 -d name