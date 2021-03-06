# log-book-backend

The backend for a log book app for teachers to use (using Django)

## Note

The secret key used in this project is just for testing purposes; it will be changed later.

## Setup - api (backend)

1. Create a virtual environment

   - On Mac and Linux - `python3 -m venv venv`
   - On Windows - `py -m venv venv`

2. Activate the virtual environment

   - On Mac and Linux - `source venv/bin/activate`
   - On Windows - `.\venv\Scripts\activate`

3. To confirm if you are in the virtual environment:

   - On Mac and Linux, `which python`

      Should return `.../venv/bin/python`

   - On Windows, `where python`

      Should return `.../venv/bin/python.exe`

4. Run `pip install -r requirements.txt`

## Contributing

1. Before committing, run `pytest`
2. Only if the `pre-commit` hook passes, the commit successfully runs
