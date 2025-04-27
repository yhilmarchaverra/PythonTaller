FROM python:3.8.10
WORKDIR /app
COPY ./static .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 2005
CMD [ "python", "app.py"]
