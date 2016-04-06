
.. _API-memcpy:

======
memcpy
======

*man memcpy(9)*

*4.6.0-rc1*

Copy one area of memory to another


Synopsis
========

.. c:function:: void ⋆ memcpy( void * dest, const void * src, size_t count )

Arguments
=========

``dest``
    Where to copy to

``src``
    Where to copy from

``count``
    The size of the area.


Description
===========

You should not use this function to access IO space, use ``memcpy_toio`` or ``memcpy_fromio`` instead.
