# Clean Code Architecture

Here I try to give an overview of clean code architecture. And try to create an
example project. This is simple blogsite project inspired by Clean Code Architecture.

### Features:

- Can signup
- Can see user list
- Can create blog post
- Can see post list
- Can retrieve a post
- Implementation of a simple permission management pipeline

### Installation:

- Create a virtual env.
```shell
python -m venv venv

# You can use any approach to create virtual env
```
- Activate the virtualenv.
- Install the requirements.
```shell
pip install -r requirements.txt
```
- Apply the migration
```commandline
alembic upgrade head
```
- Navigate to the `src/infrastructure/web/`.
- Run the app using below command.
```commandline
flask run
```
> If you need to generate migration file. Then run `alembic revision --autogenerate`

The app should run up and run now.
The API's are given bellow
- `GET /users/`
  - This will list down all users.
- `POST /signup/`
  - This will be used for registration. The sample data given bellow.
  ```json
  {
    "name": "your_name",
    "email": "your_email",
    "password": "password"
  }
  ```
- `POST /login/`
  - To login into the system. Sample request body:
  ```json
    {
        "email": "your_email",
        "password": "your_password"
    }
  ```
- `GET /posts/`
  - Get the list all posts.
- `GET /posts/<identifier>/`
  - Retrieve a single post.
- `POST /posts/`
  - For creating a new post. Example of request body:
  ```json
  {
    "title": "post_title",
    "content": "post_content"
  }
  ```

> JWT token should be pass as `Bearer` token.