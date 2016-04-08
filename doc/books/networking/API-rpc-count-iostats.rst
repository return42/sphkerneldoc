
.. _API-rpc-count-iostats:

=================
rpc_count_iostats
=================

*man rpc_count_iostats(9)*

*4.6.0-rc1*

tally up per-task stats


Synopsis
========

.. c:function:: void rpc_count_iostats( const struct rpc_task * task, struct rpc_iostats * stats )

Arguments
=========

``task``
    completed rpc_task

``stats``
    array of stat structures


Description
===========

Uses the statidx from ``task``
