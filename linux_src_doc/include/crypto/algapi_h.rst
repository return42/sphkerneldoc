.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/algapi.h

.. _`crypto_memneq`:

crypto_memneq
=============

.. c:function:: int crypto_memneq(const void *a, const void *b, size_t size)

    Compare two areas of memory without leaking timing information.

    :param a:
        One area of memory
    :type a: const void \*

    :param b:
        Another area of memory
    :type b: const void \*

    :param size:
        The size of the area.
    :type size: size_t

.. _`crypto_memneq.description`:

Description
-----------

Returns 0 when data is equal, 1 otherwise.

.. This file was automatic generated / don't edit.

