FROM python:3.7-alpine
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /app
COPY ./app.py /app/
COPY ./templates /app/templates
COPY ./static /app/static
EXPOSE 8000
#RUN python3 app.py
#CMD ["python", "/app/app.py"]
#ENV FLASK_ENV development
#VOLUME ./ /app/
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "app:app"]