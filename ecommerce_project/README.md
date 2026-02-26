# Proyecto E-commerce Django - Sistema de Autenticación

## 1. Propósito
Este proyecto implementa un sistema de gestión de usuarios para un e-commerce, incluyendo registro, inicio de sesión, cierre de sesión y protección de rutas mediante decoradores de Django.

## 2. Requisitos Técnicos
- Python 3.12+
- Django 5.x
- Base de datos: SQLite3 (por defecto)

## 3. Instrucciones de Ejecución
1. Activar entorno virtual: `source venv/Scripts/activate` (Windows) o `source venv/bin/activate` (Mac/Linux).
2. Instalar dependencias: `pip install django`.
3. Aplicar migraciones: `python manage.py migrate`.
4. Iniciar servidor: `python manage.py runserver`.
5. Acceder a: `http://127.0.0.1:8000/`.

## 4. Rutas Principales
- **Registro:** `/auth/register/`
- **Login:** `/auth/login/`
- **Panel Protegido:** `/auth/profile/` (Solo accesible si estás autenticado)
- **Logout:** `/auth/logout/`

## 5. Usuario de Prueba
 Crear uno nuevo en la pestaña de Registro