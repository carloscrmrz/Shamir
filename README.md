# Shamir

**Integrantes:**
- Cabrera Ramirez Carlos
- Medina Guzman Sergio

**Proyecto 03** para la clase de **Modelado y Programacion** con el profesor Jose Galaviz, Ximena Lezama, Luis Soto y Karla Esquivel en la Facultad de Ciencias, UNAM.

**Shamir** es una aplicacion que permite esconder un mensaje de texto en una imagen, y a su vez obtener mensajes escondidos en imagenes previamente creadas con la aplicacion.

# 🔎 Uso Shamir

1. **Sistema Operativo:** Linux · Mac OS / OS X · Windows 10
2. **Version de Python:** Python 3.6+

### Prerrequisitos
Antes de instalar los modulos, asegurate que `pip3` este actualizado.

```
$ pip3 install -r requirements.txt
```

Para ejecutarse, ya situados en el directorio Shamir tendremos dos opciones:

- Para codificar un archivo:
```
$ python3 shamir.py -c /path/to/file [-m/-s <MINIMUM> <SHARES>] 
```

Hay que tener en cuenta que dependiendo la opcion que elijamos (-m o -s) tendremos que poner PRIMERO la cantidad que indicamos (-m para MINIMUM, -s para SHARES) y luego la cantidad que nos falta. Por ejemplo para seleccionar un minimo de 3 shares y que se creen 5 en total seria `$ python3 shamir.py -c /path/to/file -m 3 5`.

Al ejecutar este comando nos pedira una contrasena, despues se crearan dos archivos, uno con terminacion `.aes` y el otro con terminacion `.frg`, el primero sera nuestro archivo codificado, el cual es seguro pasar o si es necesario guardar, el segundo archivo contiene los fragmentos con los cuales podemos decodificar nuestro archivo `.aes`.

- Para decodificar un archivo:
```
$ python3 shamir.py -d /path/to/aes_file /path/to/shares_file [-m/-s <MINIMUM> <SHARES>]
```

Seguiremos las mismas reglas para la opcion -m/-s que al encriptar, esto es para indicarle a nuestro programa cuantos fragmentos son los minimos para obtener de nuevo el hash de la contrasena.

