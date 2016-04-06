
.. _API-initChainBuffers:

================
initChainBuffers
================

*man initChainBuffers(9)*

*4.6.0-rc1*

Allocate memory for and initialize chain buffers


Synopsis
========

.. c:function:: int initChainBuffers( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Description
===========

Allocates memory for and initializes chain buffers, chain buffer control arrays and spinlock.
