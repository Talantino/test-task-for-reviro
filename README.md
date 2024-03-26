
# 📦 Inventory Management System

The Inventory Management System, built using Django REST Framework and Docker, is designed to simplify the processes of adding, updating, deleting, and listing products and companies.

## 📋 Features

- CRUD operations for managing products and companies.
- Pagination for efficient listing of products and companies.
- Docker containerization for simplified setup and deployment.
- Swagger integration for API documentation.

## 🛠️ Technologies and Libraries
![Alt text for Logo1](https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)
![Alt text for Logo2](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![Alt text for Logo3](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Alt text for Logo3](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) 
![Alt text for Logo4](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Alt text for Logo5](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)
## 🏁 Installation and Running

### Ensure Docker and Docker Compose are installed :

1. **Clone the repository and navigate to the project directory:**

    ```bash
    git clone git@github.com:Talantino/test-task-for-reviro.git
    cd test_task-for-reviro
    
    ```

2. **Run the application using Docker Compose::**
      ```bash
      docker-compose up --build
      ```

After starting the application, the API will be available at http://localhost:8000/, and the Swagger documentation can be accessed at http://localhost:8000/swagger/.


## 🕹️ Using the API

You can use any HTTP client to work with the API. Below are examples of requests using curl:

Adding a new product:
```bash
curl -X POST http://localhost:8000/products/ -H 'Content-Type: application/json' -d '{"name": "New Product", "description": "Description of the new product", "price": 100, "stock": 50}'
```
Getting the list of products:
```bash
curl -X GET http://localhost:8000/products/
```
## 🔎 Exploring and Testing API with Swagger

The Swagger UI provides an interactive documentation where you can explore all available API endpoints and execute requests directly through the browser.

To use Swagger:

 - Navigate to http://localhost:8000/api/docs/ in your web browser after starting the application.
 - You'll see a list of all available endpoints grouped by resource (e.g., products, companies).
 - Click on any endpoint to expand it and see detailed information, including the HTTP method, parameters, request body schema, and responses.
 - To try out an endpoint, click the "Try it out" button, fill in any required parameters or request body, and hit "Execute". Swagger will make the request to your API and display the response directly in the UI.
 - This makes it easy to test your API's functionality without the need for additional tools like Postman or curl.

## ✅ Running Tests
To run the tests, execute the following command:
```bash
docker-compose run web python manage.py test
```

## 🤝 Contributing
Contributions to improve the project are welcome. Please feel free to fork the repository and submit pull requests.
