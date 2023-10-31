
# Django Transaction Task Api

user currency exchange rate



## Documentation

[Postman Documentation](https://documenter.getpostman.com/view/19588926/2s9YXb8Qw9)

[Swagger Documentation](http://localhost:8000/api/v1/swagger/schema)


## Run Locally

Clone the project

```bash
  git clone https://github.com/mostafamahmoud8/DjangoSampleTask.git
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
  celery -A DjangoSampleTask.celery worker --pool=solo -l info
 
```

to fire up a celery beat worker

```bash
  celery -A DjangoSampleTask.celery beat -l INFO
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