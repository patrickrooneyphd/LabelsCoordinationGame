Traceback (most recent call last):
  File "/anaconda3/lib/python3.6/site-packages/otree_startup/__init__.py", line 217, in do_django_setup
    django.setup()
  File "/anaconda3/lib/python3.6/site-packages/django/__init__.py", line 27, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/anaconda3/lib/python3.6/site-packages/django/apps/registry.py", line 108, in populate
    app_config.import_models()
  File "/anaconda3/lib/python3.6/site-packages/django/apps/config.py", line 202, in import_models
    self.models_module = import_module(models_module_name)
  File "/anaconda3/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/pjrooney/oTree/my_wlg/models.py", line 6, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
