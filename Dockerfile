# 
FROM python:3.9

# 
WORKDIR /app/app

# 
COPY . /app

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
CMD ["python3", "main.py"]
