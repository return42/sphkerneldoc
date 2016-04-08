
.. _API-xprt-set-retrans-timeout-rtt:

============================
xprt_set_retrans_timeout_rtt
============================

*man xprt_set_retrans_timeout_rtt(9)*

*4.6.0-rc1*

set a request's retransmit timeout


Synopsis
========

.. c:function:: void xprt_set_retrans_timeout_rtt( struct rpc_task * task )

Arguments
=========

``task``
    task whose timeout is to be set


Description
===========

Set a request's retransmit timeout using the RTT estimator.
