<div align="center">

# 🇮🇷 Django Unfold Farsi

### A beautiful Persian Admin Panel for Django

**Bring Persian language and RTL support to Django Unfold.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![Language](https://img.shields.io/badge/Language-Persian-239B56?style=for-the-badge)
![RTL](https://img.shields.io/badge/Layout-RTL-8E44AD?style=for-the-badge)

<br>

**پنل راست چین چنگو**

</div>

---

## ✨ Features

| Feature | Description |
|:---:|---|
| 🇮🇷 | پشتیبانی از زبان فارسی |
| ↔️ | رابط کاربری راست‌چین (RTL) |
| 🎨 | قالب مدیریتی Django Unfold |
| 🕒 | تنظیم منطقه زمانی تهران |
| ⚡ | نصب و راه‌اندازی سریع |

---

## 🚀 Installation

### `01` — Install Django Unfold

```bash
pip install django-unfold
```

### `02` — Install Unfold Farsi

```bash
pip install django-unfold-farsi
```

### `03` — Configure `settings.py`

فایل تنظیمات پروژه Django خود را باز کنید و کد زیر را در آن قرار دهید.

```python
from django.templatetags.static import static
from unfold_farsi.settings import apply_unfold_farsi_defaults


LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"

USE_I18N = True
USE_TZ = True


UNFOLD = apply_unfold_farsi_defaults(
    {
        "SITE_TITLE": "Management",
        "SITE_HEADER": "Management",
        "SITE_SUBHEADER": "داشبورد مدیریت",
        "SHOW_LANGUAGES": False,
    },
    static=static,
)


INSTALLED_APPS = [
    "unfold_farsi",
    "unfold",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "unfold_farsi.middleware.PersianDefaultLanguageMiddleware",
    "django.middleware.locale.LocaleMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

> **⚠️ Important:** این کد را با تنظیمات فعلی پروژه ادغام کنید. مواردی مثل `INSTALLED_APPS` و `MIDDLEWARE` را دوباره تعریف نکنید؛ فقط تنظیمات موردنیاز را به فهرست‌های موجود اضافه کنید.

---

## 🎬 Run the Project

پس از ذخیره تنظیمات، دستورات زیر را به‌ترتیب اجرا کنید:

**Apply migrations**

```bash
python manage.py migrate
```

**Create an admin user**

```bash
python manage.py createsuperuser
```

**Run the development server**

```bash
python manage.py runserver
```

---

## 🌐 Admin Panel

<div align="center">

### Your Persian Admin Panel Is Ready! 🎉

[**Open Django Admin →**](http://127.0.0.1:8000/admin/)

`http://127.0.0.1:8000/admin/`

</div>

---

## 💡 Quick Setup

```bash
# Install dependencies
python -m pip install django-unfold django-unfold-farsi

# Apply database migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

<div align="center">

### 💚 Built for Django Developers

**Django + Unfold + Persian = ❤️**

*Made with Python 🐍*

</div>
