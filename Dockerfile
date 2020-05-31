# 1 
FROM python:3.8.3

# 2
COPY . /app
WORKDIR /app

# 3
RUN pip install -r requirements.txt

# 4
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]