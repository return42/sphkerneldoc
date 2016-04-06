
.. _API-strspn:

======
strspn
======

*man strspn(9)*

*4.6.0-rc1*

Calculate the length of the initial substring of ``s`` which only contain letters in ``accept``


Synopsis
========

.. c:function:: size_t strspn( const char * s, const char * accept )

Arguments
=========

``s``
    The string to be searched

``accept``
    The string to search for
