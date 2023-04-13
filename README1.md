# Proyecto_Coder
IDEA: tienda web para comprar articulos varios.


Dentro de la App1 encontramos:

Tres modelos en models.py: Usuario, Articulo y Opiniones.

Un forms.py donde encontramos un formulario para insertar datos en cada uno de los modelos.

Las urls, en urls.py, correspondientes para la creacion de cada modelo, ademas de la url para buscar articulos creados y una url para visualizar opiniones de usuarios.

Un views.py en donde encontramos todas las funciones para hacer funcionar nuestra pagina.

Existe una carpeta de plantillas, en donde se encuentran todas las plantillas de la web. Todas heredan de base.html.


La página web cuenta con una barra superior que nos direcciona hacia: INICIO, CREAR USUARIO, CREAR ARTICULO, BUSCAR ARTICULO U OPINIONES.

En inicio, por ahora, no contamos con nada. Solo con un mensaje de bienvenida.

Al clickear en "Crear Usuario" nos dirige a un formulario para crear un usuario ingresando nombre, edad, email y celular. Para enviar los datos existe un botón de aceptar. Luego somos dirigidos a una plantilla que nos dice que el usuario se creó correctamente.

Al clickear en "Crear articulo" nos dirige a un formulario para crear un articulo ingresando nombre, categoria y precio. También cuenta con un botón de aceptar para enviar los datos.

Al clickear en "Buscar articulo" nos conduce hacia un formulario que nos permite buscar un articulo dentro de la base de datos y que dependiendo de lo ingresado podemos visualizar: 1)los elementos relacionados a la busqueda 2)que no existen productos relacionados a su busqueda 2)o que no ingresó nada para buscar

Al clickear en "Opiniones" se nos dirige hacia una plantilla que nos muestra los datos del modelo Opiniones, que son las opiniones brindadas por los usuarios. Para escribir una nueva Opinion existe un boton que redirige hacia el formulario para ingresar nuevos datos al modelo.
