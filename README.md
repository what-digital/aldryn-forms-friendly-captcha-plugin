# Aldryn Forms FriendlyCaptcha Plugin

This python module is open-source, available here: https://gitlab.com/what-digital/aldryn-forms-friendlycaptcha-plugin/


## Setup

`pip install aldryn-forms-friendlycaptcha-plugin`

Add the following to your `settings.py`: 

```
INSTALLED_APPS = [
    'friendly_captcha'
    'aldryn_forms_friendlycaptcha_plugin',
]

FRC_CAPTCHA_SECRET = env('FRC_CAPTCHA_SECRET', '123')
FRC_CAPTCHA_SITE_KEY = env('FRC_CAPTCHA_SITE_KEY', '123')

FRC_CAPTCHA_VERIFICATION_URL = env('FRC_CAPTCHA_VERIFICATION_URL', 'https://api.friendlycaptcha.com/api/v1/siteverify')
```

If you're using bootstrap4, beware that django renders the form errors with class `invalid-feedback`, which is invisible in bs4.


## Versioning and Packages

- versioning is done in versioning in `aldryn_forms_friendlycaptcha_plugin/__init__.py`
- for each version a tag is added to the gitlab repository in the form of `^(\d+\.)?(\d+\.)?(\*|\d+)$`, example: 0.0.10

- There is a PyPI version which relies on the gitlab tags (the download_url relies on correct gitlab tags being set): https://pypi.org/project/aldryn-forms-friendlycaptcha-plugin/

In order to release a new version of the Divio add-on:

- Increment version number in `addons-dev/aldryn-forms-friendlycaptcha-plugin/aldryn_forms_friendlycaptcha_plugin/__init__.py`
- Then git add, commit and tag with the version number and push to the repo

```
git add .
git commit -m "<message>"
git tag 0.0.XX
git push origin 0.0.19
```

Then, in order to release a new pypi version:

- python3 setup.py sdist bdist_wheel
- twine upload --repository-url https://test.pypi.org/legacy/ dist/*
- twine upload dist/*

### Development

- Run `pip install -e ../aldryn-forms-friendlycaptcha-plugin/` in your demo project
- You can open aldryn_forms_recaptcha_plugin in pycharm and set the python interpreter of the demo project to get proper django support and code completion.


## Dependencies

- aldryn_forms
