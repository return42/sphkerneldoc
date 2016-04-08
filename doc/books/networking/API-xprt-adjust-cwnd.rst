
.. _API-xprt-adjust-cwnd:

================
xprt_adjust_cwnd
================

*man xprt_adjust_cwnd(9)*

*4.6.0-rc1*

adjust transport congestion window


Synopsis
========

.. c:function:: void xprt_adjust_cwnd( struct rpc_xprt * xprt, struct rpc_task * task, int result )

Arguments
=========

``xprt``
    pointer to xprt

``task``
    recently completed RPC request used to adjust window

``result``
    result code of completed RPC request


Description
===========

The transport code maintains an estimate on the maximum number of out- standing RPC requests, using a smoothed version of the congestion avoidance implemented in 44BSD. This is
basically the Van Jacobson


congestion algorithm
====================

If a retransmit occurs, the congestion window is halved; otherwise, it is incremented by 1/cwnd when

- a reply is received and - a full number of requests are outstanding and - the congestion window hasn't been updated recently.
