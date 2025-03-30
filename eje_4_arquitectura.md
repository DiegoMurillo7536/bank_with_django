# Sistema Bancario Django

## Descripción General
Este proyecto es una aplicación web bancaria desarrollada con Django que permite a los usuarios gestionar sus cuentas bancarias y realizar transacciones. El sistema incluye funcionalidades de autenticación, gestión de cuentas y operaciones bancarias básicas.

## Arquitectura del Proyecto

### Estructura de Directorios
```
bank_django/
├── bank/
│ ├── forms/
│ │ ├── make_transaction_form.py
│ │ └── top_account_form.py
│ ├── models/
│ │ ├── account.py
│ │ └── transaction.py
│ ├── templates/
│ │ ├── bank/
│ │ │ ├── account/
│ │ │ │ └── top_account.html
│ │ │ └── bank.html
│ │ └── transaction/
│ │ └── make_transaction.html
│ ├── templatetags/
│ │ └── form_tags.py
│ ├── views.py
│ └── urls.py
└── manage.py
```

## Componentes Principales

### Modelos
1. **Account (Cuenta)**
   - Gestiona la información de las cuentas bancarias
   - Campos principales: usuario, saldo, número de cuenta
   - Relaciones con transacciones

2. **Transaction (Transacción)**
   - Registra todas las operaciones bancarias
   - Campos: monto, descripción, cuentas origen/destino
   - Tipos de transacción soportados

### Formularios
1. **MakeTransactionForm**
   - Maneja la creación de nuevas transacciones
   - Validación de montos y cuentas
   - Filtrado de cuentas por usuario

2. **TopAccountForm**
   - Gestiona las recargas de cuenta
   - Validación de montos mínimos
   - Campo de cuenta no editable

### Vistas
1. **bank**
   - Vista principal del dashboard
   - Muestra listado de cuentas del usuario
   - Integra formulario de transacciones

2. **make_transaction**
   - Procesa nuevas transacciones
   - Validación de fondos y permisos
   - Mensajes de confirmación

3. **top_account**
   - Maneja recargas de cuenta
   - Validación de montos
   - Actualización de saldos

### Templates
1. **bank.html**
   - Dashboard principal
   - Listado de cuentas
   - Integración de formularios

2. **make_transaction.html**
   - Formulario de transacciones
   - Selección de cuentas
   - Mensajes de error/éxito

3. **top_account.html**
   - Formulario de recarga
   - Campo de cuenta bloqueado
   - Diseño responsivo con Bootstrap

## Características Principales

### Autenticación y Seguridad
- Login requerido para acceso
- Filtrado de cuentas por usuario
- Validación de permisos en transacciones

### Gestión de Transacciones
- Transferencias entre cuentas
- Recargas de saldo
- Validación de fondos suficientes
- Registro histórico de operaciones

### Interfaz de Usuario
- Diseño responsivo con Bootstrap
- Mensajes de feedback al usuario
- Formularios con validación
- Campos auto-generados y protegidos

### Utilidades
- Template tags personalizados
- Manejo de formularios dinámicos
- Sistema de mensajes temporales

## Flujos de Trabajo

### Realizar una Transacción
1. Usuario accede al dashboard
2. Selecciona cuentas origen y destino
3. Ingresa monto y descripción
4. Sistema valida la operación
5. Actualiza saldos y registra transacción
6. Muestra mensaje de confirmación

### Recargar Cuenta
1. Usuario selecciona cuenta a recargar
2. Sistema muestra formulario con cuenta bloqueada
3. Usuario ingresa monto
4. Sistema valida monto mínimo
5. Actualiza saldo
6. Confirma operación

## Tecnologías Utilizadas
- Django
- Bootstrap
- PostgreSQL
- JavaScript (mensajes temporales)