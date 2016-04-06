
.. _API-memmove:

=======
memmove
=======

*man memmove(9)*

*4.6.0-rc1*

Copy one area of memory to another


Synopsis
========

.. c:function:: void ⋆ memmove( void * dest, const void * src, size_t count )

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

Unlike ``memcpy``, ``memmove`` copes with overlapping areas.
