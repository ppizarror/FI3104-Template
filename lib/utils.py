#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UTILS
Este archivo provee de funciones básicas que son globalmente usadas.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: SEPTIEMBRE-OCTUBRE 2015 - 2016
Licencia: GPLv2
"""


def append_list_to_list(origin, l):
    """
    Añade los elementos de la lista l a la lista origin.

    :param origin: Lista a añadir elementos
    :type origin: list
    :param l: Lista con elementos a ser agregados
    :type l: list

    :return: void
    :type: None
    """
    for i in l:
        origin.append(i)


def convert_to_number(s):
    """
    Función que convierte un objeto a diversos tipos de números.

    :param s: String a convertir
    :type s: object

    :return: Número convertido
    :rtype: object
    """
    try:
        s = str(s)
    except:
        return s
    if s.isdigit():  # Es un entero
        return int(s)
    else:
        if "." in s and s.replace(".", "").isdigit():  # Es un flotante
            return float(s)
        else:
            try:  # Es un hexadecimal
                return int(s, 16)
            except ValueError:
                pass
    return s


def del_matrix(matrix):
    """
    Borrar una matriz.

    :param matrix: Matriz
    :type matrix: list

    :return: void
    :rtype: None
    """
    a = len(matrix)
    if a > 0:
        for k in range(a):  # @UnusedVariable
            matrix.pop(0)


def equal_lists(list1, list2):
    """
    Comprueba si dos listas son idénticas en elementos.

    :param list1: Lista 1
    :type list1: list
    :param list2: Lista 2
    :type list2: list

    :return: Booleano indicando comparación
    :rtype: bool
    """
    if len(list1) != len(list2):
        return False
    else:
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                return False
        return True


def number_of_sublists(l):
    """
    Retorna el numero de sublistas que contiene una lista.

    :param l: Lista a calcular
    :type l: list

    :return: Número de sublistas
    :rtype: int
    """
    count = 0
    for i in l:
        if isinstance(i, list):
            count = count + 1 + number_of_sublists(i)
    return count


def print_matrix(matrix):
    """
    Función que imprime una matriz en pantalla.

    :param matrix: Matriz
    :type matrix: list

    :return: void
    :rtype: None
    """
    for j in matrix:
        for k in j:
            print k,
        print "\n"


def sort_and_uniq(linput):  # @ReservedAssignment
    """
    Función que elimina datos repetidos.

    :param linput: Lista
    :type linput: list

    :return: Lista modificada
    :rtype: list
    """
    output = []
    for x in linput:
        if x not in output:
            output.append(x)
    output.sort()
    return output


def string2list(string, separator):
    """
    Función que divide un string en una lista usando un separador.

    :param string: String inicial
    :type string: str
    :param separator: Separador
    :type separator: str

    :return: Lista proveniente de la separación del string
    :rtype: list
    """
    return string.strip().split(separator)


def sum_matrix(matrix):
    """
    Función que suma lista de listas.

    :param matrix: Matrices
    :type matrix: list

    :return: Valor de la suma
    :rtype: float
    """
    suma = 0.0
    try:
        for j in matrix:
            for k in j:
                suma += k
        return suma
    except:
        return -1
