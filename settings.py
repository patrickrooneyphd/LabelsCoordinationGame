from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0,
    'doc': "",
    'points_decimal_places': 0,
    'real_world_currency_decimal_places': 0
}

SESSION_CONFIGS = [
    {
        'name': 'turnaround_labels',
        'display_name': "Labels and Turnarounds",
        'num_demo_participants': 16,
        'app_sequence': ['turnaround_labels'],
        'use_browser_bots': False
    },
    {
        'name': 'turnaround_labels_comm',
        'display_name': "Labels and Turnarounds_comm",
        'num_demo_participants': 16,
        'app_sequence': ['turnaround_labels_comm'],
        'use_browser_bots': False
    },
    {
        'name': 'turnaround_labels_pun_bonus',
        'display_name': "Labels and Turnarounds_pun_bonus",
        'num_demo_participants': 16,
        'app_sequence': ['turnaround_labels_pun_bonus'],
        'use_browser_bots': False
    },
    {
        'name': 'turnaround_labels_punish_unan_atleast1',
        'display_name': "Labels and Turnarounds_punish_unan_atleast1",
        'num_demo_participants': 16,
        'app_sequence': ['turnaround_labels_punish_unan_atleast1'],
        'use_browser_bots': False
    },
    {
        'name': 'turnaround_labels_punish_costly',
        'display_name': "Labels and Turnarounds_punish_costly",
        'num_demo_participants': 16,
        'app_sequence': ['turnaround_labels_punish_costly'],
        'use_browser_bots': False
    },
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 0
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2


ROOMS = [
    dict(
        name='BRL_EconomicGameExperiment',
        display_name='BRL_EconomicGameExperiment',
    ),
    dict(
        name='TEEL_EconomicGameExperiment',
        display_name='TEEL_EconomicGameExperiment',
    ),
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = ')9l4$syir$d@$&ukdtcs6xnzwn3sfraf1fv6c^$*yiyw4%f&!j'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree',
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  ]
INSTALLED_OTREE_APPS = []

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )