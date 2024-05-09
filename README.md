# Hall Management System API with flas

Clone the app and cd in the dir
```bash
source .venv/bin/activate
```

Install all requirements through:
```bash
pip install -r requirements.txt
```

Make a copy of the .env file
```bash
mv .env.example .env
```
You can now update your `.env` file as you wish

### Setting up your Database
Run the following commands one afte the other

1. Init your database
```bash
flask db init
```

2. Run the migrations in the migrations dir
```bash
flask db upgrade
```
