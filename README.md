# TFG-Servicio_Web
TFG basado en un Servicio Web que mostrará información relevante sobre la ETSIIT como fechas de exámenes junto con la hora, guías docentes de cada una de las asignaturas...Todo esto irá también acompañado de un Bot de Telegram para aumentar su accesibilidad.

## Fuentes de datos de la cuales obtener infomación sobre GII

* Horarios = https://etsiit.ugr.es/pages/calendario_academico/horarios-curso-20172018/horariosgii1718/!

* Guías docentes = https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/guiasdocentes_curso_actual

* Fecha y hora de exámenes = https://etsiit.ugr.es/pages/calendario_academico/examenes-curso-1819/calendarioexamenes1819gii/!

## Despliegue en un PaaS

Para mi proyecto he empleado el PaaS [Heroku](https://www.heroku.com/).

Los pasos a seguir para su despliegue son los siguientes:

-Instalamos el cliente de heroku desde su propia página o mediante el siguiente comando:

<code>sudo snap install --classic heroku</code>

-Una vez instalado, procedemos a autenticarnos en heroku.

<code>heroku login</code>

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/login_heroku.png)

-Creamos la aplicación la cual vamos a desplegar.

<code>heroku apps:create --region eu subjectsgii</code>

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/config_app.png)

-Añadimos los siguientes ficheros:

* [Procfile](https://github.com/franfermi/TFG-Servicio_Web/blob/master/Procfile), fichero de ejecución de Heroku. Worker para el servicio bot de Telegram y Web para el servicio web desplegado.
* [runtime.txt](https://github.com/franfermi/TFG-Servicio_Web/blob/master/runtime.txt), especificamos la versión de python utilizada.
* [requirements.txt](https://github.com/franfermi/TFG-Servicio_Web/blob/master/requirements.txt), añadimos las dependencias de nuestro proyecto.

-Desplegamos Github desde Heroku para un despliegue automático:

En la opción de despliegue de Heroku, en métodos de despliegue seleccionamos la opción Github y conectamos el repositorio de nuestro proyecto.

Por último, activamos el despliegue automático para cada vez que realicemos un push de nuestro proyecto se actualice también en Heroku.

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/despliegueAutHeroku.png)

-Para configurar el token de Telegram para su uso desde Heroku:

<code>heroku config:set TOKEN=$$$$ --app informaticaugrbot</code>

-Por último, lanzamos tanto el bot como el servicio web.

<code>heroku ps:scale worker=1 --app informaticaugrbot</code>

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/botConfigurado.png)

<code>heroku ps:scale web=1 --app informaticaugrbot</code>

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/despliegueWebCorrecto.png)

-Comprobamos que están activos y funcionando en heroku.

![curl](https://github.com/franfermi/TFG-Servicio_Web/blob/master/img/dynosHeroku.png)