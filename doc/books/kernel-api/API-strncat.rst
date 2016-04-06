
.. _API-strncat:

=======
strncat
=======

*man strncat(9)*

*4.6.0-rc1*

Append a length-limited, C-string to another


Synopsis
========

.. c:function:: char ⋆ strncat( char * dest, const char * src, size_t count )

Arguments
=========

``dest``
    The string to be appended to

``src``
    The string to append to it

``count``
    The maximum numbers of bytes to copy


Description
===========

Note that in contrast to ``strncpy``, ``strncat`` ensures the result is terminated.
