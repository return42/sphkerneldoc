.. -*- coding: utf-8; mode: rst -*-

.. _API-memparse:

========
memparse
========

*man memparse(9)*

*4.6.0-rc5*

parse a string with mem suffixes into a number


Synopsis
========

.. c:function:: unsigned long long memparse( const char * ptr, char ** retptr )

Arguments
=========

``ptr``
    Where parse begins

``retptr``
    (output) Optional pointer to next char after parse completes


Description
===========

Parses a string into a number. The number stored at ``ptr`` is
potentially suffixed with K, M, G, T, P, E.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
