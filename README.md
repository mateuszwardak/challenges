# Challenges app

To run the project:
1) Make sure you have Docker installed on your PC
2) Go to the project's directory in your terminal
3) Build and start Docker containers using docker-compose:
    ```
    docker-compose up
    ```
4) Open a browser and go to **127.0.0.1:8000** to view the app.

To run tests:
1) Run manage.py command using docker-compose:
    ```
   docker-compose run web python manage.py test
   ```