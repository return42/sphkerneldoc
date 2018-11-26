.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/compiler.h

.. _`offset_to_ptr`:

offset_to_ptr
=============

.. c:function:: void *offset_to_ptr(const int *off)

    convert a relative memory offset to an absolute pointer

    :param off:
        the address of the 32-bit offset value
    :type off: const int \*

.. _`compiletime_assert`:

compiletime_assert
==================

.. c:function::  compiletime_assert( condition,  msg)

    break build and emit msg if condition is false

    :param condition:
        a compile-time constant condition to check
    :type condition: 

    :param msg:
        a message to emit if condition is false
    :type msg: 

.. _`compiletime_assert.description`:

Description
-----------

In tradition of POSIX assert, this macro will break the build if the
supplied condition is \*false\*, emitting the supplied error message if the
compiler has support to do so.

.. This file was automatic generated / don't edit.

