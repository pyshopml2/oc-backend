FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project

COPY . /project
RUN pip install -r crm/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]