
.. _API-z8530-read-port:

===============
z8530_read_port
===============

*man z8530_read_port(9)*

*4.6.0-rc1*

Architecture specific interface function


Synopsis
========

.. c:function:: int z8530_read_port( unsigned long p )

Arguments
=========

``p``
    port to read


Description
===========

Provided port access methods. The Comtrol SV11 requires no delays between accesses and uses PC I/O. Some drivers may need a 5uS delay

In the longer term this should become an architecture specific section so that this can become a generic driver interface for all platforms. For now we only handle PC I/O ports
with or without the dread 5uS sanity delay.

The caller must hold sufficient locks to avoid violating the horrible 5uS delay rule.
