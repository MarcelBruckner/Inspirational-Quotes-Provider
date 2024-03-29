# 
FROM python:3.10

# 
WORKDIR /app

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /app
COPY ./data /app/data

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]