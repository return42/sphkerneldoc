.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/boot/string.c

.. _`simple_strtoull`:

simple_strtoull
===============

.. c:function:: unsigned long long simple_strtoull(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long long

    :param cp:
        The start of the string
    :type cp: const char \*

    :param endp:
        A pointer to the end of the parsed string will be placed here
    :type endp: char \*\*

    :param base:
        The number base to use
    :type base: unsigned int

.. _`strlen`:

strlen
======

.. c:function:: size_t strlen(const char *s)

    Find the length of a string

    :param s:
        The string to be sized
    :type s: const char \*

.. _`strstr`:

strstr
======

.. c:function:: char *strstr(const char *s1, const char *s2)

    Find the first substring in a \ ``NUL``\  terminated string

    :param s1:
        The string to be searched
    :type s1: const char \*

    :param s2:
        The string to search for
    :type s2: const char \*

.. _`strchr`:

strchr
======

.. c:function:: char *strchr(const char *s, int c)

    Find the first occurrence of the character c in the string s.

    :param s:
        the string to be searched
    :type s: const char \*

    :param c:
        the character to search for
    :type c: int

.. This file was automatic generated / don't edit.

