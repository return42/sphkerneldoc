
.. _API-strnstr:

=======
strnstr
=======

*man strnstr(9)*

*4.6.0-rc1*

Find the first substring in a length-limited string


Synopsis
========

.. c:function:: char ⋆ strnstr( const char * s1, const char * s2, size_t len )

Arguments
=========

``s1``
    The string to be searched

``s2``
    The string to search for

``len``
    the maximum number of characters to search
