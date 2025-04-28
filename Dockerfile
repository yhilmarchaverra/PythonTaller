FROM python:3.10
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 2005
#CMD [ "uvicorn", "api:app", "--reload", "--host","0.0.0.0", "--port", "2005"]
CMD [ "uvicorn", "api:app", "--host","0.0.0.0", "--port", "2005"]