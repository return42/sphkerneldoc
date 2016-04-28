.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-count-iostats:

=================
rpc_count_iostats
=================

*man rpc_count_iostats(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
