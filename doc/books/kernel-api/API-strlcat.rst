
.. _API-strlcat:

=======
strlcat
=======

*man strlcat(9)*

*4.6.0-rc1*

Append a length-limited, C-string to another


Synopsis
========

.. c:function:: size_t strlcat( char * dest, const char * src, size_t count )

Arguments
=========

``dest``
    The string to be appended to

``src``
    The string to append to it

``count``
    The size of the destination buffer.
