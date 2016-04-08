
.. _API-xprt-release-rqst-cong:

======================
xprt_release_rqst_cong
======================

*man xprt_release_rqst_cong(9)*

*4.6.0-rc1*

housekeeping when request is complete


Synopsis
========

.. c:function:: void xprt_release_rqst_cong( struct rpc_task * task )

Arguments
=========

``task``
    RPC request that recently completed


Description
===========

Useful for transports that require congestion control.
