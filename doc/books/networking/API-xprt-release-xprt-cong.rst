.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-release-xprt-cong:

======================
xprt_release_xprt_cong
======================

*man xprt_release_xprt_cong(9)*

*4.6.0-rc5*

allow other requests to use a transport


Synopsis
========

.. c:function:: void xprt_release_xprt_cong( struct rpc_xprt * xprt, struct rpc_task * task )

Arguments
=========

``xprt``
    transport with other tasks potentially waiting

``task``
    task that is releasing access to the transport


Description
===========

Note that “task” can be NULL. Another task is awoken to use the
transport if the transport's congestion window allows it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
