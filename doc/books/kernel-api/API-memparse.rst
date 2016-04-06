
.. _API-memparse:

========
memparse
========

*man memparse(9)*

*4.6.0-rc1*

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

Parses a string into a number. The number stored at ``ptr`` is potentially suffixed with K, M, G, T, P, E.
