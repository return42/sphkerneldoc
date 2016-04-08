
.. _API-xprt-write-space:

================
xprt_write_space
================

*man xprt_write_space(9)*

*4.6.0-rc1*

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
