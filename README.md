# VCart - E-Commerce Website  

## Overview  
**VCart** is a fully functional **e-commerce website** built using Django and MySQL. This project provides basic CRUD (Create, Read, Update, Delete) operations and a structured template-based UI. It features multiple product categories, including **Clothing, Electronics, and Groceries**, with all data stored in a MySQL database.  

The application consists of **three Django apps**, each handling different sections of the e-commerce platform.  

---

## Features  
- **Category-Based Navigation** (Clothing, Electronics, Groceries)  
- **CRUD Operations** (Add, Edit, Delete Products)  
- **Admin Panel for Management**  
- **Django Template-Based UI**  

---

## Screens and Navigation  

### **1. Electronics Page**  
📍 URL: [http://127.0.0.1:8000/electronics/](http://127.0.0.1:8000/electronics/)  

![image](https://github.com/user-attachments/assets/6b792da1-e62f-494f-b570-ddcb0892ccd9)

### **2. Groceries Page**  
📍 URL: [http://127.0.0.1:8000/groceries/](http://127.0.0.1:8000/groceries/)  

![image](https://github.com/user-attachments/assets/b09d0085-fe8b-4377-a380-23238bb98616)

### **3. Clothing Page**  
📍 URL: [http://127.0.0.1:8000/cloths/](http://127.0.0.1:8000/cloths/)  

![image](https://github.com/user-attachments/assets/1178d464-dc2d-4552-b43a-8397c52a036f)

### **4. Add New Clothing Item**  
📍 URL: [http://127.0.0.1:8000/cloths/add/](http://127.0.0.1:8000/cloths/add/)  

![image](https://github.com/user-attachments/assets/af9a807f-1226-468f-a1a4-643ec10a39a5)

### **5. Edit Clothing Item**  
📍 URL: [http://127.0.0.1:8000/cloths/edit/<int:cloth_id>/](http://127.0.0.1:8000/cloths/edit/)  
📌 **Route Name:** `cloth-edit`  

### **6. Delete Clothing Item**  
📍 URL: [http://127.0.0.1:8000/cloths/delete/<int:cloth_id>/](http://127.0.0.1:8000/cloths/delete/)  
📌 **Route Name:** `cloth-delete`  

### **7. Admin Panel**  
📍 URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
👤 **To access the admin panel, create a superuser:**  
```sh
python manage.py createsuperuser
```

---

## Database Configuration  

To configure the **VCart** project with MySQL, follow these steps:  

### **1. Create MySQL Database**  
Ensure MySQL is installed and running, then create a database:  
```sql
CREATE DATABASE vcart;
```

### **2. Update Django `settings.py`**  
Modify the database settings in the `settings.py` file of the **VCart** project directory.  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vcart',  # Database name
        'USER': 'your_mysql_username',  # Replace with MySQL username
        'PASSWORD': 'your_mysql_password',  # Replace with MySQL password
        'HOST': 'localhost',  # Default host
        'PORT': '3306',  # Default MySQL port
    }
}
```

### **3. Install MySQL Client for Django**  
Run the following command to install MySQL client:  
```sh
pip install mysqlclient
```
or  
```sh
pip install pymysql
```
(If using `pymysql`, add this in `__init__.py` inside your Django project folder:)  
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### **4. Apply Migrations**  
Run the following commands to apply database migrations:  
```sh
python manage.py makemigrations
python manage.py migrate
```

---

## Running the Project  

1. **Clone the Repository**  
```sh
git clone https://github.com/your-username/vcart.git
cd vcart
```

2. **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3. **Run the Django Server**  
```sh
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

---

## Contributing  
Feel free to contribute to this project by submitting issues or pull requests.  

---

## License  
This project is licensed under the **MIT License**.  

---
🚀 **VCart - Your Custom E-Commerce Solution!**
