.. -*- coding: utf-8; mode: rst -*-

.. _API-initChainBuffers:

================
initChainBuffers
================

*man initChainBuffers(9)*

*4.6.0-rc5*

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

Allocates memory for and initializes chain buffers, chain buffer control
arrays and spinlock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
