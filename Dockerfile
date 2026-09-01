FROM python:3.14
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD gunicorn -b 0.0.0.0:5000 "app:create_app()" --capture-output --enable-stdio-inheritance