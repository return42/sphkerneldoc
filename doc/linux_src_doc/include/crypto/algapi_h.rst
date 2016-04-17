.. -*- coding: utf-8; mode: rst -*-

========
algapi.h
========


.. _`crypto_memneq`:

crypto_memneq
=============

.. c:function:: int crypto_memneq (const void *a, const void *b, size_t size)

    Compare two areas of memory without leaking timing information.

    :param const void \*a:
        One area of memory

    :param const void \*b:
        Another area of memory

    :param size_t size:
        The size of the area.



.. _`crypto_memneq.description`:

Description
-----------

Returns 0 when data is equal, 1 otherwise.

