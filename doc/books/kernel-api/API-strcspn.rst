
.. _API-strcspn:

=======
strcspn
=======

*man strcspn(9)*

*4.6.0-rc1*

Calculate the length of the initial substring of ``s`` which does not contain letters in ``reject``


Synopsis
========

.. c:function:: size_t strcspn( const char * s, const char * reject )

Arguments
=========

``s``
    The string to be searched

``reject``
    The string to avoid
