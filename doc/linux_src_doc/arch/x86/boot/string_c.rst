.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/boot/string.c

.. _`simple_strtoull`:

simple_strtoull
===============

.. c:function:: unsigned long long simple_strtoull(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long long

    :param const char \*cp:
        The start of the string

    :param char \*\*endp:
        A pointer to the end of the parsed string will be placed here

    :param unsigned int base:
        The number base to use

.. _`strlen`:

strlen
======

.. c:function:: size_t strlen(const char *s)

    Find the length of a string

    :param const char \*s:
        The string to be sized

.. _`strstr`:

strstr
======

.. c:function:: char *strstr(const char *s1, const char *s2)

    Find the first substring in a \ ``NUL``\  terminated string

    :param const char \*s1:
        The string to be searched

    :param const char \*s2:
        The string to search for

.. This file was automatic generated / don't edit.

