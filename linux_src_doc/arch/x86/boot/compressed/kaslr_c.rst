.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/boot/compressed/kaslr.c

.. _`_memparse`:

_memparse
=========

.. c:function:: unsigned long long _memparse(const char *ptr, char **retptr)

    Parse a string with mem suffixes into a number

    :param const char \*ptr:
        Where parse begins

    :param char \*\*retptr:
        (output) Optional pointer to next char after parse completes

.. _`_memparse.description`:

Description
-----------

Parses a string into a number.  The number stored at \ ``ptr``\  is
potentially suffixed with K, M, G, T, P, E.

.. This file was automatic generated / don't edit.

