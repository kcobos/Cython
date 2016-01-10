#Cython

##¿Qué es Cython?
Es un compilador basado en Pyrex.

Permite crear funciones en Python y compilarlas en lenguaje objeto.

También permite hacer llamadas a funciones de C/C++.

##¿Qué ventajas tiene?
Al compilar en lenguaje objeto funciones, éstas no se tienen que interpretar para ejecutarse por lo que ganamos velocidad en la ejecución de un programa.

También podemos encapsular una aplicación hecha en C/C++ para, por ejemplo, desde Python hacerle una interfaz o pasarle datos obtenidos desde internet.

##Instalación
###Linux:
	sudo apt-get install cython libpython2.7-dev # Para Python2
	sudo apt-get install cython3 libpython3.4-dev # Para Python3
###Windows:
	Existen múltiples opciones 
		https://github.com/cython/cython/wiki/InstallingOnWindows

##Un ejemplo simple
Para empezar vamos a hacer un ejemplo simple como puede ser la sucesión de Fibonacci de forma recursiva.
Vamos a crear una función de Fibonacci de tres maneras diferentes:
* En Python normal
* En Cython (Python compilado)
* En C/C++
Por último vamos a hacer una comparación de tiempos entre las distintas funciones.

###Creación de ficheros
####fibonacciPython.py (Python normal)
    def fibonacciRec(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacciRec(n-2) + fibonacciRec(n-1)

####fibonacciCython.pyx (Cython)
    def fibonacciRec(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacciRec(n-2) + fibonacciRec(n-1)

####fibonacci.cpp (C/C++)
    int fibonacciRec(int n){
        if (n==0)
            return 0;
        else if (n==1)
            return 1;
        else
            return fibonacciRec(n-2) + fibonacciRec(n-1);
    }

    extern "C" {
        int fibonacciRecC(int n){return fibonacciRec(n);}
    }


##Aclaraciones
Cython tiene la misma sintaxis que Python aunque cosas nuevas. 

Cuidado con la extensión de los archivos!!

En C/C++, hay que especificar las funciones o las variables que tiene una vinculación externa, es decir, aquellas que queramos llamar desde Python.

Para ello usamos el bloque “extern” donde dentro declaramos variables y funciones que se van a poder usar desde Python.

##Compilación de Cython 
Una vez que tenemos los ficheros pyx (Cython) tenemos que generar su código objeto.

Para ello necesitamos hacer uso de un script de configuración que lo que va a hacer es buscar todos los archivos con extensión pyx y va a generar su código objeto, un archivo con extensión so.

####Lo único que tenemos que hacer es llamar a dicho script de la siguiente manera:
	python setup.py build_ext --inplace #Python2
	python3 setup.py build_ext --inplace #Python3

###Script de configuración
    from distutils.core import setup
    from Cython.Build import cythonize
    import glob, os
    files = []
    os.chdir(".")

    for file in glob.glob("*.pyx"):
        files.append(file)
    
    setup(
        ext_modules = cythonize(files)
    )

##Uso de Cython
Una vez generado el código objeto, hacer uso de las funciones que haya en el fichero .pyx
####Para ello necesitamos importar el módulo y ya podemos usarlas:
	import fibonacciCython #importa el archivo “fibonacciCython.so”
	print(fibonacciCython.fibonacciRec(5)) #se hace uso de la función fibonacciRec

###Compilación de C/C++ para el uso con Python 
####Una vez creado el archivo C/C++ con las funciones que se quieran usar en Python especificadas para que se vinculen externamente, podemos proceder a compilarlo:
	g++ -c -fPIC fibonacci.cpp -o fibonacci.o
	g++ -shared -Wl,-soname,libfibonacci.so -o libfibonacci.so  fibonacci.o
Con esto hemos creado el archivo .so necesario para trabajar en Python.

###Uso de C/C++ en Python
####Una vez generado el archivo .so, en nuestro caso libfibonacci.so, podemos usar las funciones externalizadas de la siguiente manera:
    from ctypes import cdll #importamos cdll para cargar bibliotecas de C/C++
    libfi = cdll.LoadLibrary('./libfibonacci.so') #cargamos la biblioteca en libfi
    print(libfi.fibonacciRecC(5)) #usamos las funciones de dicha biblioteca

##Comparativa de funciones
####Para saber si Cython realmente merece la pena, hemos comparado los tiempos de ejecución para distintos tamaños de n:
    | N  | Python   | Cython   | C/C++   |
    |----|----------|----------|---------|
    | 39 | 29.1104  | 18.1274  | 0.8510  |
    | 40 | 47.2322  | 29.4395  | 1.4826  |
    | 41 | 76.4090  | 47.3236  | 2.4527  |
    | 42 | 123.7818 | 75.5095  | 3.8937  |
    | 43 | 202.2534 | 123.7621 | 6.1991  |
    | 44 | 327.2314 | 199.7456 | 9.9453  |
    | 45 | 529.8116 | 364.6818 | 15.9019 |

##Para terminar
Desde Cython se puede hacer llamadas a funciones de C/C++:
####cythonC.pyx
	from libc.stdlib cimport atoi
	cdef parse_charptr_to_py_int(char* s):
		assert s is not NULL, "string is NULL"
		return atoi(s)
	def string_to_int(n):
		return parse_charptr_to_py_int(n)

Usándose de igual manera que un .pyx normal.

##Enlaces de interés
* http://docs.cython.org/src/tutorial/cython_tutorial.html
* http://docs.cython.org/src/userguide/language_basics.html
* http://docs.cython.org/src/userguide/wrapping_CPlusPlus.html
