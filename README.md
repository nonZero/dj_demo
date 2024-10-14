Requirements:

- python 3.12
- uv
- postgres w/your user is a postgres superuser

To run:

    - git clone https://github.com/nonZero/dj_demo.git
    - cd dj_demo
    - createdb dj_demo
    - uv run python manage.py migrate
    - uv run python manage.py create_fake_data
    - uv run python manage.py show_best
