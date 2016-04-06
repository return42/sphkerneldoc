
.. _API-strsep:

======
strsep
======

*man strsep(9)*

*4.6.0-rc1*

Split a string into tokens


Synopsis
========

.. c:function:: char ⋆ strsep( char ** s, const char * ct )

Arguments
=========

``s``
    The string to be searched

``ct``
    The characters to search for


Description
===========

``strsep`` updates ``s`` to point after the token, ready for the next call.

It returns empty tokens, too, behaving exactly like the libc function of that name. In fact, it was stolen from glibc2 and de-fancy-fied. Same semantics, slimmer shape. ;)
