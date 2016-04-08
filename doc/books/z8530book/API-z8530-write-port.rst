
.. _API-z8530-write-port:

================
z8530_write_port
================

*man z8530_write_port(9)*

*4.6.0-rc1*

Architecture specific interface function


Synopsis
========

.. c:function:: void z8530_write_port( unsigned long p, u8 d )

Arguments
=========

``p``
    port to write

``d``
    value to write


Description
===========

Write a value to a port with delays if need be. Note that the caller must hold locks to avoid read/writes from other contexts violating the 5uS rule

In the longer term this should become an architecture specific section so that this can become a generic driver interface for all platforms. For now we only handle PC I/O ports
with or without the dread 5uS sanity delay.
