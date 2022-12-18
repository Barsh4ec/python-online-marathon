FROM python:3
RUN mkdir /sprint18
WORKDIR /sprint18
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py"]
CMD [ "runserver", "0.0.0.0:8000"]