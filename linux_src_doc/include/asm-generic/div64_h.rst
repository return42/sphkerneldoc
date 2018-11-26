.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/div64.h

.. _`do_div`:

do_div
======

.. c:function::  do_div( n,  base)

    returns 2 values: calculate remainder and update new dividend

    :param n:
        pointer to uint64_t dividend (will be updated)
    :type n: 

    :param base:
        uint32_t divisor
    :type base: 

.. _`do_div.summary`:

Summary
-------

``uint32_t remainder = *n % base;``
``*n = *n / base;``

.. _`do_div.return`:

Return
------

(uint32_t)remainder

.. _`do_div.note`:

NOTE
----

macro parameter \ ``n``\  is evaluated multiple times,
beware of side effects!

.. This file was automatic generated / don't edit.

