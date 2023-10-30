
# Django Transaction Task Api

user currency echange rate



## Documentation

[Postman Documentation](https://documenter.getpostman.com/view/19588926/2s9YXb8Qw9)

[Swaager Documentation](http://localhost:8000/api/v1/swagger/schema)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd DjangoSampleTask
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Open a Ubuntu terminal and add the following

```bash
  redis-server
```

Now open another and write the following

```bash
  redis-cli
```

to fire up a celery worker

```bash
  celery -A did_django_schedule_jobs_v2.celery worker --pool=solo -l info
 
```

to fire up a celery beat worker

```bash
  celery -A didcoding.celery beat -l INFO
```

start server

```bash
  python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```


## External exchange api

[Currency Api](https://currencyapi.com/)