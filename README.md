# Tests para las prácticas de Administración de Sistemas

Este repositorio contiene tests para realizar pruebas en los scripts realizados
en las sesiones de prácticas de la asignatura de Administración de Sistemas del
grado de Ingeniería en Informática de la Universidad de Zaragoza.

## Requerimientos

Los tests requieren de un interprete de python versión 2.7 y de la biblioteca
[pexpect](https://pexpect.readthedocs.io/en/stable/).

Python 2.7 se puede instalar ejecutando el comando:

    as@as0:~/sudo apt install python

Pexpect se puede instalar con [pip](https://pypi.org/project/pip/) ejecutando el comando:

    as@as0:~/pip install pexpect

## Descarga y actualización de los tests

Los tests se encuentran dentro de un repositorio git y se pueden
descargar/clonar utilizando el comando:

    as@as0:~/git clone https://github.com/gvalles-unizar/tests_practicas_AS

Al terminar la operación se crearán múltiples directorio con todos los tests y
una carpeta para las prácticas 2, 3 y 4 con los ficheros vacíos que hay que
completar tal y como se muestra a continuación.

    as@as0:~/as_tests_practicas/tree
    .
    ├── practica_2
    │   ├── practica2_1.sh
    │   ├── practica2_2.sh
    │   ├── practica2_3.sh
    │   ├── practica2_4.sh
    │   ├── practica2_5.sh
    │   └── practica2_6.sh
    ├── practica_3
    │   └── practica_3.sh
    ├── practica_4
    │   └── practica_4.sh
    ├── README.md
    ├── tests
    │   ├── correct_user_list.txt
    │   ├── incorrect_user_list_add_3_fields.txt
    │   ├── incorrect_user_list_add_multiple_no_passwd.txt
    │   ├── incorrect_user_list_add_no_passwd.txt
    │   ├── incorrect_user_list_existing_root.txt
    │   ├── incorrect_user_list_remove_non_existing_user.txt
    │   ├── test_practica2_1.py
    │   ├── test_practica2_2.py
    │   ├── test_practica2_3.py
    │   ├── test_practica2_4.py
    │   ├── test_practica2_5.py
    │   ├── test_practica2_6.py
    │   ├── test_practica3.py
    │   └── test_practica4.py
    └── utils
        └── remove_possible_users.sh


Si quieres asegurarte que tienes la última versión de los tests puedes utilizar
[git pull](https://git-scm.com/docs/git-pull) o [git
reset](https://git-scm.com/docs/git-reset) si los has modificado y no quieres
preservar las modificaciones.

    as@as0:~/as_tests_practicas/git pull origin/master

o
    as@as0:~/as_tests_practicas/git fetch --all && git reset --hard origin/master

**IMPORTANTE**: Antes de hacer un git reset recuerda haber copiado tus scripts
en otra carpeta ya que git los borrara. Una alternativa sería trabajar con un
_fork_ propio tal y como se describe en la documentación de [fork de
gitlab](https://docs.gitlab.com/ee/gitlab-basics/fork-project.html)

## Utilización

El nombre de cada test es homónimo al de los scripts de los guiones de
prácticas con el prefijo test\_. Para realizar las pruebas, hay que asegurar
que el fichero a comprobar se encuentra en su localización inicial. Por ejemplo:

    as@as0:~/as_tests_practicas/tests/test_practica2_1.py

Espera que exista el fichero `as_tests_practicas/practica2/practica2_1.sh`.

Cada script comprende varios tests unitarios que pueden ser ejecutados de
manera individual ya que están basados en el módulo
[unittest](https://docs.python.org/2/library/unittest.html) de python.

Cada test incluye varios tests unitarios. Cuando un test unitario se ejecuta
correctamente aparece un punto en la pantalla y si falla aparecerá un mensaje
del tipo:

    as@as0:~/as_tests_practicas/tests/test_practica2_1.py
    ......F
    ======================================================================
    FAIL: test_shebang (__main__.TestPractica2_1)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "./test_practica2_1.py", line 34, in test_shebang
          (pattern.match(first_line) != None), msg='Invalid shebang')
          AssertionError: Invalid shebang

          ----------------------------------------------------------------------
          Ran 7 tests in 0.477s

Después de `FAIL` se indica el nombre del test unitario que ha fallado, en este
caso `test_shebang` lo que nos indicará que debemos revisar la primera línea de
nuestro script. Es importante leer el nombre ya que siempre nos informara de la
parte donde ha ocurrido el error.

## Contacto

Para cualquier sugerencia por favor contactar con gvalles@unizar.es
