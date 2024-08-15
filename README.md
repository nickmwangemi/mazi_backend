# Mazi Backend

### Prerequisites

To run this app, you will need to have the Python 3.8 or higher installed on your machine. You can download it from
the [official website](https://www.python.org/downloads/).

### Local Setup

1. Clone the repository.

```bash
  git@github.com:nickmwangemi/mazi_backend.git
```

2. Change into the directory.

```bash
  cd mazi_backend
```

3. Set up a virtual environment and activate it.

```bash
  python3 -m venv .venv && source .venv/bin/activate
```

4. Install the dependencies.

```bash
  pip install -r requirements.txt
```

5. Run the following command to install pre-commit hooks, which will format and
   fix linting issues before you commit your code.

```bash
  pre-commit install
```

6. Ensure you have PostgreSQL installed and running. Create a postgresql user with username and password `mazi`, and
   create a corresponding database called `mazi`.

```bash
  sudo su - postgres -c 'createuser -d -P mazi'
  sudo su - postgres -c 'createdb mazi'
```

- You also have the option of exporting a custom database connection string as an environment variable named
  `DATABASE_URL` which will take precedence over the default.

```bash
  export DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>
```

7. Run migrations to create database tables.

```bash
  python manage.py migrate
```

8. Create a superuser for the admin.

```bash
  python manage.py createsuperuser
```

9. You can now run the server

```bash
  python manage.py runserver
```

### Usage
The app uses celery to asychronously. To start the celery worker, run the following command:
```bash
  celery -A mazi_backend worker --loglevel=info
```


### Monitoring Celery with Flower
[Flower](https://flower.readthedocs.io/en/latest/) is a real-time web application monitoring and administration tool for Celery.

On a separate terminal, run the following command to start Flower:
```bash
celery -A mazi_backend flower --port=5555
```
Navigate to `http://localhost:5555` to view the Flower dashboard. Click "Tasks" to view the tasks that have been executed.
