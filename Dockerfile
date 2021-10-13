FROM python:3.7

RUN mkdir -p /usr/src/app/

RUN pip install fastapi

RUN pip install mongoengine

RUN pip install uvicorn

RUN pip install pydantic

WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]