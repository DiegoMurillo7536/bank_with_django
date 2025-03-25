# Bank Django

## Setup

### 1. Creación y activación de un virtual environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
### 2. Instalación de requirements

**Importante**: Si están usando windows, deben irse a requirements.txt y cambiar
```bash
    psycopg2-binary==2.9.10
```
por: 
```bash
    psycopg2==2.9.10
```

y luego ejecutar:

```bash
$ pip install -r requirements.txt
```
### 3. Crear la base de datos y credenciales de conexión para usar PSQL
Deben irse hacia pgadmin o psql y crear la base de datos.
 - ¿Cómo se crea?:
    - En primera instancia, deben irse a pgadmin y crear la base de datos con el
    nombre que ustedes hayan elegido para el proyecto. usando 
    ```SQL
    CREATE DATABASE bank_django;
    ```
    - Luego, dentro del archivo .env, deben irse a las diferentes variables de entorno que se utilizan en el proyecto y crear las variables que se necesiten para la conexión a la base de datos.
    ```bash
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=su_contraseña
    POSTGRES_DB=bank_django
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```
### 4. Modelos
Para crear los modelos, deben irse a la carpeta models y crear un archivo con el mismo nombre que el modelo que se quiere crear.

Ejemplo:
```python
from django.db import models

# Create your models here.
class AccountType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'bank_account_type'
      
```

### 5. Migraciones
Para crear las migraciones, deben irse a la terminal y ejecutar:
```bash
$ python manage.py makemigrations
```
Y luego ejecutar:
```bash
$ python manage.py migrate
```


### 6. Admin
Luego, deben irse a la carpeta admin y crear un archivo con el mismo nombre que el modelo que se quiere crear.

Ejemplo:
```python
from django.contrib import admin

from bank.models.account_type import AccountType

# Register your models here.
@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
```

Luego, deben irse a la terminal y ejecutar:
```bash
$ python manage.py createsuperuser # Aquí deben crear un usuario administrador
$ python manage.py runserver

```
Este comando iniciará un servidor web en el puerto 8000 que se puede acceder a http://localhost:8000/admin/ con el usuario y contraseña que se hayan creado.

### 7. CRUD
Ya en la web de administración ya se pueden crear, leer, actualizar y eliminar los modelos que se hayan creado.




