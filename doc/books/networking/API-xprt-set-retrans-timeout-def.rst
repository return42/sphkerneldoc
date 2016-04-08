
.. _API-xprt-set-retrans-timeout-def:

============================
xprt_set_retrans_timeout_def
============================

*man xprt_set_retrans_timeout_def(9)*

*4.6.0-rc1*

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

Set a request's retransmit timeout based on the transport's default timeout parameters. Used by transports that don't adjust the retransmit timeout based on round-trip time
estimation.
