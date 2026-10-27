from django.templatetags.static import static
from unfold_farsi.settings import apply_unfold_farsi_defaults



LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"


UNFOLD = apply_unfold_farsi_defaults(
    {
        "SITE_TITLE": "Managment",
        "SITE_HEADER": "Managment",
        "SITE_SUBHEADER": "داشبورد  مدیریت",
        "SHOW_LANGUAGES": False,
    },
    static=static,
)


# Application definition

INSTALLED_APPS = [
    "unfold_farsi",
    "unfold",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

STATIC_URL = 'static/'
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

