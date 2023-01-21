FROM python:3.8

# Create app directory
WORKDIR /app
EXPOSE 5000

COPY . /app
RUN pip install flask
RUN pip install flask-restful

ENV FLASK_APP "globalOrchestrator.py"

ENTRYPOINT [ "flask" ]
CMD ["run", "-h", "0.0.0.0"]