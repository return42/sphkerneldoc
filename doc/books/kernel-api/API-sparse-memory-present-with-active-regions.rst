
.. _API-sparse-memory-present-with-active-regions:

=========================================
sparse_memory_present_with_active_regions
=========================================

*man sparse_memory_present_with_active_regions(9)*

*4.6.0-rc1*

Call memory_present for each active range


Synopsis
========

.. c:function:: void sparse_memory_present_with_active_regions( int nid )

Arguments
=========

``nid``
    The node to call memory_present for. If MAX_NUMNODES, all nodes will be used.


Description
===========

If an architecture guarantees that all ranges registered contain no holes and may be freed, this function may be used instead of calling ``memory_present`` manually.
