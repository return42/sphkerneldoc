.. -*- coding: utf-8; mode: rst -*-

.. _API-skip-spaces:

===========
skip_spaces
===========

*man skip_spaces(9)*

*4.6.0-rc5*

Removes leading whitespace from ``str``.


Synopsis
========

.. c:function:: char * skip_spaces( const char * str )

Arguments
=========

``str``
    The string to be stripped.


Description
===========

Returns a pointer to the first non-whitespace character in ``str``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
