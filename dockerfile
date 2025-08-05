FROM python:3.11

WORKDIR /app

# کپی کردن requirements.txt اول
COPY requirements.txt .

# نصب پکیج‌ها
RUN pip install --upgrade pip && pip install -r requirements.txt

# کپی کردن بقیه فایل‌ها
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]