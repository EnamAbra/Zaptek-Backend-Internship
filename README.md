# Zaptek Backend Internship

Python backend projects and assignments completed during my backend development internship.

## Projects

### Innovation API

A FastAPI backend API for managing student innovation-club applications.

The API uses mock/sample data instead of a database, as required by the assignment.

#### Features

- Create applications
- Retrieve all applications
- Retrieve a single application
- Update applications
- Delete applications
- Pydantic data validation
- Email validation
- URL validation
- Application status validation
- 404 error handling
- Interactive Swagger API documentation

#### Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

#### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/applications` | Get all applications |
| GET | `/applications/{id}` | Get a single application |
| POST | `/applications` | Create an application |
| PUT | `/applications/{id}` | Update an application |
| DELETE | `/applications/{id}` | Delete an application |

#### Run Locally

```bash
uvicorn main:app --reload