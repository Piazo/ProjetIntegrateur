FROM python:2.7

# Create app directory
WORKDIR /app
EXPOSE 5000

COPY . /app
RUN pip install flask
RUN pip install flask-restful
RUN pip install requests

ENV FLASK_APP "resultProcessing.py"

ENTRYPOINT [ "flask" ]
CMD ["run", "-h", "0.0.0.0"]

# docker build -t name . 
# sudo docker run -it -p 51001:5000 -d name