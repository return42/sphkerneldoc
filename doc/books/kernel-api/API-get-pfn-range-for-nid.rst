
.. _API-get-pfn-range-for-nid:

=====================
get_pfn_range_for_nid
=====================

*man get_pfn_range_for_nid(9)*

*4.6.0-rc1*

Return the start and end page frames for a node


Synopsis
========

.. c:function:: void get_pfn_range_for_nid( unsigned int nid, unsigned long * start_pfn, unsigned long * end_pfn )

Arguments
=========

``nid``
    The nid to return the range for. If MAX_NUMNODES, the min and max PFN are returned.

``start_pfn``
    Passed by reference. On return, it will have the node start_pfn.

``end_pfn``
    Passed by reference. On return, it will have the node end_pfn.


Description
===========

It returns the start and end page frame of a node based on information provided by ``memblock_set_node``. If called for a node with no available memory, a warning is printed and
the start and end PFNs will be 0.
