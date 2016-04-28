.. -*- coding: utf-8; mode: rst -*-

.. _API-sprintf:

=======
sprintf
=======

*man sprintf(9)*

*4.6.0-rc5*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int sprintf( char * buf, const char * fmt, ... )

Arguments
=========

``buf``
    The buffer to place the result into

``fmt``
    The format string to use @...: Arguments for the format string

``...``
    variable arguments


Description
===========

The function returns the number of characters written into ``buf``. Use
``snprintf`` or ``scnprintf`` in order to avoid buffer overflows.

See the ``vsnprintf`` documentation for format string extensions over
C99.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
