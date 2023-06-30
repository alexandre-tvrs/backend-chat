FROM python:3.11.4
ENV PYTHONBUFFERED=1
ENV PORT 8080
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m pip install Pillow
COPY . /app/
# --- start: For this app ---
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', '@Admin123')" | python manage.py shell
# --- end ---
CMD gunicorn -b :8080 chattcc.wsgi:application
EXPOSE ${PORT}