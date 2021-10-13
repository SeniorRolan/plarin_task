from mongoengine import Document, StringField, IntField, ListField


class Employee(Document):
    employee_id=IntField()
    name = StringField()
    email = StringField()
    age = IntField()
    company = StringField()
    join_date = StringField()
    job_title = StringField()
    gender = StringField()
    salary = IntField()
