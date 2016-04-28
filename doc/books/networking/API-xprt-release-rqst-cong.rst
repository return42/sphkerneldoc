.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-release-rqst-cong:

======================
xprt_release_rqst_cong
======================

*man xprt_release_rqst_cong(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
