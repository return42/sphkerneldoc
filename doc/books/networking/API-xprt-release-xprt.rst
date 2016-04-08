
.. _API-xprt-release-xprt:

=================
xprt_release_xprt
=================

*man xprt_release_xprt(9)*

*4.6.0-rc1*

allow other requests to use a transport


Synopsis
========

.. c:function:: void xprt_release_xprt( struct rpc_xprt * xprt, struct rpc_task * task )

Arguments
=========

``xprt``
    transport with other tasks potentially waiting

``task``
    task that is releasing access to the transport


Description
===========

Note that “task” can be NULL. No congestion control is provided.
