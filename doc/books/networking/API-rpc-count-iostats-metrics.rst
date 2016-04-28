.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-count-iostats-metrics:

=========================
rpc_count_iostats_metrics
=========================

*man rpc_count_iostats_metrics(9)*

*4.6.0-rc5*

tally up per-task stats


Synopsis
========

.. c:function:: void rpc_count_iostats_metrics( const struct rpc_task * task, struct rpc_iostats * op_metrics )

Arguments
=========

``task``
    completed rpc_task

``op_metrics``
    stat structure for OP that will accumulate stats from ``task``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
