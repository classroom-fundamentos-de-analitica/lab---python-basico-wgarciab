"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open("data.csv", "r") as file:
    data = file.readlines()
data = [row.replace("\n", "") for row in data]
data = [row.split("\t") for row in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    column2 = [int(row[1]) for row in data]
    result = sum(column2)
    
    return result


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    column1 = [row[0] for row in data]
    uniqueLetters = list(set(column1))
    result = [(letter, column1.count(letter)) for letter in uniqueLetters]
    result.sort()
    
    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    column1 = [row[0] for row in data]
    uniqueLetters = list(set(column1))
    result = [(letter, sum([int(row[1]) for row in data if row[0] == letter])) for letter in uniqueLetters]
    result.sort()

    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    months = [row[2].split("-")[1] for row in data]
    uniqueMonths = list(set(months))
    result = [(month, months.count(month)) for month in uniqueMonths]
    result.sort()

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    column1 = [row[0] for row in data]
    uniqueLetters = list(set(column1))
    result = [
        (letter, 
        max([int(row[1]) for row in data if row[0] == letter]), 
        min([int(row[1]) for row in data if row[0] == letter])) 
        for letter in uniqueLetters
        ]
    result.sort()

    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    column5Splitted = [row[4].split(",") for row in data]
    flatList = [item for sublist in column5Splitted for item in sublist]
    listDict = [row.split(":") for row in flatList]
    keys = [row[0] for row in listDict]
    uniqueKeys = list(set(keys))

    result = [
        (key, 
        min([int(row[1]) for row in listDict if row[0] == key]), 
        max([int(row[1]) for row in listDict if row[0] == key])) 
        for key in uniqueKeys
        ]
    result.sort()

    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    column2 = [int(row[1]) for row in data]
    uniqueNumbers = list(set(column2))
    result = [(number, [row[0] for row in data if int(row[1]) == number]) for number in uniqueNumbers]
    result.sort()

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    column2 = [int(row[1]) for row in data]
    uniqueNumbers = list(set(column2))
    result = [(number, sorted(list(set([row[0] for row in data if int(row[1]) == number])))) for number in uniqueNumbers]
    result.sort()

    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    column5Splitted = [row[4].split(",") for row in data]
    flatList = [item for sublist in column5Splitted for item in sublist]
    listDict = [row.split(":") for row in flatList]
    keys = [row[0] for row in listDict]
    uniqueKeys = list(set(keys))

    result = {key : keys.count(key) for key in sorted(uniqueKeys)}

    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    result = [
        (row[0], 
        len(row[3].split(",")), 
        len(row[4].split(","))) 
        for row in data
    ]

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    column4Splitted = [row[3].split(",") for row in data]
    listDict = [[letter, data[i_row][1]] for i_row, row in enumerate(column4Splitted) for letter in row]
    column1 = [row[0] for row in listDict]
    uniqueLetters = list(set(column1))
    
    result = {
        letter : sum([int(row[1]) for row in listDict if row[0] == letter]) 
        for letter in sorted(uniqueLetters)
    }

    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    column5Splitted = [row[4].split(",") for row in data]
    column5Values = [[item.split(":")[1] for item in row] for row in column5Splitted]
    listDict = [[data[i_row][0], number] for i_row, row in enumerate(column5Values) for number in row]
    column1 = [row[0] for row in listDict]
    uniqueLetters = list(set(column1))

    result = {
        letter : sum([int(row[1]) for row in listDict if row[0] == letter]) 
        for letter in sorted(uniqueLetters)
    }

    return result