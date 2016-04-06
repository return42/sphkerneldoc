
.. _API-sscanf:

======
sscanf
======

*man sscanf(9)*

*4.6.0-rc1*

Unformat a buffer into a list of arguments


Synopsis
========

.. c:function:: int sscanf( const char * buf, const char * fmt, ... )

Arguments
=========

``buf``
    input buffer

``fmt``
    formatting of buffer @...: resulting arguments

``...``
    variable arguments
