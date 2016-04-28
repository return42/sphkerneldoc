.. -*- coding: utf-8; mode: rst -*-

.. _API-sparse-memory-present-with-active-regions:

=========================================
sparse_memory_present_with_active_regions
=========================================

*man sparse_memory_present_with_active_regions(9)*

*4.6.0-rc5*

Call memory_present for each active range


Synopsis
========

.. c:function:: void sparse_memory_present_with_active_regions( int nid )

Arguments
=========

``nid``
    The node to call memory_present for. If MAX_NUMNODES, all nodes
    will be used.


Description
===========

If an architecture guarantees that all ranges registered contain no
holes and may be freed, this function may be used instead of calling
``memory_present`` manually.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
