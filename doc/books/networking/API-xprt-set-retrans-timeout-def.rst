.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-set-retrans-timeout-def:

============================
xprt_set_retrans_timeout_def
============================

*man xprt_set_retrans_timeout_def(9)*

*4.6.0-rc5*

set a request's retransmit timeout


Synopsis
========

.. c:function:: void xprt_set_retrans_timeout_def( struct rpc_task * task )

Arguments
=========

``task``
    task whose timeout is to be set


Description
===========

Set a request's retransmit timeout based on the transport's default
timeout parameters. Used by transports that don't adjust the retransmit
timeout based on round-trip time estimation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
