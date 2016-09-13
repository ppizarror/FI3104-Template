# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ERRORS
Tratamiento de errores.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: MiT
"""

# Importación de librerías
from accents import del_accent_by_os
from colors import Colors

# Constantes
COLOR = Colors()

# Códigos de errores
BAD_ERROR_CODE = 'BAD_ERROR_CODE'
ERROR_BADCONFIG = 'La linea \'{0}\' del archivo de configuraciones \'{1}\' ' \
                  'no es válida. '
ERROR_BADINDEXCONFIG = 'El índice seleccionado <{0}> no pertenece a las ' \
                       'configuraciones cargadas. '
ERROR_BADPARAMETERTYPE = 'Error en el tipo de un parámetro. '
ERROR_BADPARAMETERTYPE_MSG = 'El parámetro {0} debe ser del tipo {1}. '
ERROR_CONFIGBADEXPORT = 'No se pudo guardar el archivo de configuraciones. '
ERROR_CONFIGCORRUPT = 'El archivo de configuraciones \'{0}\' está corrupto. '
ERROR_CONFIGNOTEXISTENT = 'El parámetro {0} no existe en las configuraciones. '
ERROR_DIFFERENT_LIST_SIZES = 'Las listas pasadas por argumento difieren en ' \
                             'cantidad de elementos.'
ERROR_HEADER = '{0}[ERROR] {1}'.format(COLOR.red(), COLOR.end())
ERROR_NOCONFIGFILE = 'No existe archivo de configuraciones \'{0}\'. '
ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE = 'Valor parámetro incorrecto. '
NO_ERROR = 'OK'
PLOT_ERROR_ON_SAVE = 'Ocurrió un error al generar el gráfico. '
PLOT_ERROR_DVI_NOT_INSTALLED = 'Intente instalar el programa dvipng, pruebe ' \
                               'el comando \'sudo apt install dvipng\'. '
ST_ERROR = '[ERR]'
ST_INFO = '[INF]'
ST_WARNING = '[WRN]'
ST_WARNING_ID = '[ERR][{0}]'
WARNING_HEADER = '{0}[WARNING] {1}'.format(COLOR.blue(), COLOR.end())
WARNING_NOCONFIGFOUND = 'No se han encontrado configuraciones en el archivo ' \
                        '\'{0}\'. '
WRAP_ERROR_MSG = 70


def _create_msg(message, *args):
    """
    Función que crea un mensaje de error dado argumentos iniciales.

    :param message: Código de error
    :type message: str
    :param args: Argumentos adicionales
    :type args: list

    :return: Mensaje de error
    :rtype: str
    """
    return message.format(*args)


def st_error(msg, call_exit=False, module=None, exception=None):
    """
    Muestra un mensaje de error en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param exception: Excepción
    :type exception: Exception

    :return: void
    :type: None
    """
    if module is None:
        print del_accent_by_os(
            COLOR.red() + ST_ERROR + COLOR.end() + " {0}".format(msg))
    else:
        print del_accent_by_os(
            COLOR.red() + ST_ERROR + COLOR.end() + " {0} ".format(
                msg) + "[" + COLOR.underline() + module + COLOR.end() + "]")
    if exception is not None:
        print del_accent_by_os("      {0}".format(str(exception)))
    if call_exit:
        exit()


def st_info(msg, call_exit=False):
    """
    Muestra un mensaje de información en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool

    :return: void
    :rtype: None
    """
    print del_accent_by_os(
        COLOR.dark_cyan() + ST_INFO + COLOR.end() + " {0}".format(msg))
    if call_exit:
        exit()


def throw(errcode, *args):
    """
    Lanza un error terminal.

    :param errcode: Código de error
    :type errcode: str
    :param args: Argumentos
    :type args: list

    :return: void
    :rtype: None
    """
    st_error(_create_msg(errcode, *args), True)


def st_warning(msg, call_exit=False, module=None, errname=None):
    """
    Muestra un mensaje de precaución en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param errname: Excepción
    :type errname: Exception

    :return: void
    :rtype: None
    """
    if module is None:
        print del_accent_by_os(
            COLOR.blue() + ST_WARNING + COLOR.end() + " {0}".format(msg))
    else:
        print del_accent_by_os(
            COLOR.blue() + ST_ERROR + COLOR.end() + " {0} ".format(
                msg) + "[" + COLOR.underline() + module + COLOR.end() + "]")
    if errname is not None:
        print del_accent_by_os("      {0}".format(str(errname)))
    if call_exit:
        exit()


def warning(warcode, *args):
    """
    Lanza una advertencia

    :param warcode: Código de la advertencia
    :type warcode: str
    :param args: Argumentos
    :type args: list

    :return: void
    :rtype: None
    """
    warcode = _create_msg(warcode, args)
    st_warning(warcode)


def _parse_lang_error(msg):
    """
    Formatea un código de error.

    :param msg: Mensaje de error
    :type msg: str

    :return: String con mensaje de error
    :rtype: str
    """

    def insert_each(string, each, every):
        """
        Inserta el string -each- cada -every- caracteres en el string -string-.

        :param string: String a formatear
        :type string: str
        :param each: String a insertar
        :type each: str
        :param every: Cantidad de caracteres
        :type every: int

        :return: string formateado
        :rtype: str
        """
        return each.join(
            string[i:i + every] for i in xrange(0, len(string), every))

    data = msg.split("::")
    code = data[0].strip().split("[")[1]
    code = code.replace("]", "")
    msg = data[1].strip()
    msg = insert_each(msg, "-\n\t    ", WRAP_ERROR_MSG)
    return COLOR.red() + ST_WARNING_ID.format(code) + COLOR.end() + " " + msg


class ExceptionBehaviour(object):
    """
    Clase que permite manejar clases de error
    """

    def __init__(self):
        """
        Constructor de la clase.

        :return: void
        :rtype: None
        """

        # Variables de clase
        self._exceptionMsgCode = False
        self._exceptionsDisabled = False
        self._exceptionStrBehaviour = False
        self._isEnabledExceptionThrowable = False

    def disable_exception_as_string(self):
        """
        Desactiva el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = False

    def disable_exception_code(self):
        """
        Desactiva el retornar el mensaje de cada excepción como un código de
        error.

        :return: void
        :rtype: None
        """
        self._exceptionMsgCode = False

    def disable_exceptions(self):
        """
        Desactiva todas las excepciones.

        :return: void
        :rtype: None
        """
        self.disable_exception_as_string()
        self.disable_exception_throw()
        self._exceptionsDisabled = True

    def disable_exception_throw(self):
        """
        Desactiva el lanzamiento de excepciones en python en vez de la función
        throw que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = False

    def enable_exception_as_string(self):
        """
        Activa el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = True
        self.disable_exception_throw()
        self.enable_exceptions()

    def enable_exception_code(self):
        """
        Activa el retornar el mensaje de cada excepción como un código.

        :return: void
        :rtype: None
        """
        self._exceptionMsgCode = True

    def enable_exceptions(self):
        """
        Activa las excepciones.

        :return: void
        :rtype: None
        """
        self._exceptionsDisabled = False

    def enable_exception_throw(self):
        """
        Activa el lanzamiento de excepciones en python en vez de la función
        throw que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = True
        self.disable_exception_as_string()
        self.enable_exceptions()

    # noinspection PyUnusedLocal
    def _throw_exception(self, e, *format_args):
        """
        Función que lanza una excepción según comportamiento.

        :param e: Error string
        :type e: str
        :param format_args: Argumentos opcionales de los errores
        :type format_args: list

        :return: String o void
        :rtype: object
        """
        # Si no se han deshabilitado las excepciones
        if not self._exceptionsDisabled:

            # Se obtiene el mensaje a retornar (string o código de error)
            err = ""
            if self._exceptionMsgCode:  # Como código
                try:  # Se comprueba que el código exista
                    eval(e)
                    err = e
                except:
                    err = "BAD_ERROR_CODE"
            else:  # Como string (mensaje)
                try:  # Se comprueba que el código exista
                    err = del_accent_by_os(eval(e))
                except:
                    err = BAD_ERROR_CODE

            # Si la excepción se retorna como un string
            if self._exceptionStrBehaviour:
                return err

            # Si la excepción lanza error o Exception
            else:

                # Lanzar excepción
                if self._isEnabledExceptionThrowable:
                    raise Exception(err)

                # Lanzar error
                else:
                    throw(err)
