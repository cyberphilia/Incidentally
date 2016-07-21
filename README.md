# incidentally

## Assumptions

You have virtualbox and vagrant installed.

## Getting Started

open terminal in the incidentally directory

```shell
vagrant up
```

```shell
vagrant ssh
```

```shell
cd /vagrant
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```
