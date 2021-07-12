# Prueba técnica 0907

### Version: 0.2.0

Principal punto de entrada desde el frontal hacia todo el backend. API será el encargado de persistir la información recogida a través de un cron de GCP y la entrega de dicha información

## Instalación

### Instalar y configurar dependencias externas

TODO

#### Instalación en Linux
```bash
sudo apt update && sudo apt install postgresql postgresql-contrib 
```
Comprobar que postgresql están funcionando:
```bash
sudo systemctl status postgresql
```
Si están funcionando, debería salir "active" o algo en verde.

#### Configuración
Crea la base de datos de postgresql:
```bash
createdb mydbname
```
Instalar las dependencias:
```bash
pip install -r requirements.txt
```

Copia el archivo `.env.example` y renómbralo como `.env`, actualizando las credenciales de la base de datos:
```bash
cp .env.example .env
```
Migra la base de datos y crea un superusuario, que servirá para acceder luego al admin de django:
```bash
python manage.py migrate
python manage.py createsuperuser
```
Finalmente, ejecuta el servidor:
```bash
python manage.py runserver
```
