.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/alpha/include/asm/local.h

.. _`local_add_unless`:

local_add_unless
================

.. c:function::  local_add_unless( l,  a,  u)

    add unless the number is a given value

    :param l:
        pointer of type local_t
    :type l: 

    :param a:
        the amount to add to l...
    :type a: 

    :param u:
        ...unless l is equal to u.
    :type u: 

.. _`local_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``l``\ , so long as it was not \ ``u``\ .
Returns non-zero if \ ``l``\  was not \ ``u``\ , and zero otherwise.

.. This file was automatic generated / don't edit.

