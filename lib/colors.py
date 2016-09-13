#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
COLORS
Maneja los colores en la consola.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2015 - 2016
Licencia: GPLv2
"""

# Importación de librerías
from ostype import is_windows


# noinspection PyClassHasNoInit
class Colors(object):
    """
    Permite manejar colores en la terminal.
    """

    @staticmethod
    def bold():
        """
        Texto en negrita.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[1m'

    @staticmethod
    def blue():
        """
        Colors azul.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[94m'

    @staticmethod
    def cyan():
        """
        Colors púrpura.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[96m'

    @staticmethod
    def dark_cyan():
        """
        Colors cian oscuro.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[36m'

    @staticmethod
    def end():
        """
        Terminación del formato.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[0m'

    @staticmethod
    def green():
        """
        Colors verde.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[92m'

    @staticmethod
    def purple():
        """
        Colors púrpura.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[95m'

    @staticmethod
    def red():
        """
        Colors rojo.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[91m'

    @staticmethod
    def underline():
        """
        Texto subrayado.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[4m'

    @staticmethod
    def yellow():
        """
        Colors verde.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[93m'
