.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-write-space:

================
xprt_write_space
================

*man xprt_write_space(9)*

*4.6.0-rc5*

wake the task waiting for transport output buffer space


Synopsis
========

.. c:function:: void xprt_write_space( struct rpc_xprt * xprt )

Arguments
=========

``xprt``
    transport with waiting tasks


Description
===========

Can be called in a soft IRQ context, so xprt_write_space never sleeps.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
