DESAFIO 4: IMPLEMENTACION DE MAP, FILTER Y REDUCE PROPIAS
 
DESCRIPCION DEL DESAFIO
Crear mis propias versiones de las funciones map, filter y reduce de Python.
Cada una recibe una funcion y una lista (y un valor inicial en el caso de
reduce) y devuelve el resultado como lista o como un solo valor.
 
 
SOLUCION
El archivo desafio_4.py contiene tres funciones:
 
1. mi_map(funcion, lista)
   Aplica "funcion" a cada elemento de la lista.
   Devuelve: una lista con los resultados.
 
2. mi_filter(funcion, lista)
   Conserva los elementos para los que "funcion" devuelve True.
   Devuelve: una lista filtrada.
 
3. mi_reduce(funcion, lista, inicial)
   Acumula los elementos de la lista en un solo valor.
   Devuelve: el valor acumulado final.
 
 
COMO FUNCIONA CADA UNA
- mi_map: recorre la lista con un ciclo for y agrega a una lista nueva el
  resultado de funcion(elemento).
 
- mi_filter: recorre la lista y, con un if, agrega el elemento original
  solo si funcion(elemento) es verdadero.
 
- mi_reduce: empieza con un acumulador igual a "inicial" y, en cada vuelta,
  lo reemplaza por funcion(acumulado, elemento).
 
 
EJEMPLOS
mi_map(cuadrado, [1, 2, 3])               ->  [1, 4, 9]
mi_filter(es_par, [1, 2, 3, 4])           ->  [2, 4]
mi_reduce(sumar, [1, 2, 3, 4], 0)         ->  10
mi_reduce(multiplicar, [1, 2, 3, 4], 1)   ->  24
 
 
CASOS DE PRUEBA CONSIDERADOS
- Listas vacias: mi_map y mi_filter devuelven []; mi_reduce devuelve el
  valor inicial.
- Funciones lambda como argumento.
- Filtros donde ningun elemento cumple la condicion.
 
 
COMO EJECUTARLO
python desafio_4.py
 
 
CONCEPTOS DE PYTHON UTILIZADOS
Funciones como argumentos, ciclos for, condicionales if, listas y .append(),
docstrings y funciones lambda.