.. -*- coding: utf-8; mode: rst -*-

=====
err.h
=====


.. _`err_cast`:

ERR_CAST
========

.. c:function:: void *ERR_CAST (__force const void *ptr)

    Explicitly cast an error-valued pointer to another pointer type

    :param __force const void \*ptr:
        The pointer to cast.



.. _`err_cast.description`:

Description
-----------

Explicitly cast an error-valued pointer to another pointer type in such a
way as to make it clear that's what's going on.

