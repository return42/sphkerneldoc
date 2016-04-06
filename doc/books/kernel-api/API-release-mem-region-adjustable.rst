
.. _API-release-mem-region-adjustable:

=============================
release_mem_region_adjustable
=============================

*man release_mem_region_adjustable(9)*

*4.6.0-rc1*

release a previously reserved memory region


Synopsis
========

.. c:function:: int release_mem_region_adjustable( struct resource * parent, resource_size_t start, resource_size_t size )

Arguments
=========

``parent``
    parent resource descriptor

``start``
    resource start address

``size``
    resource region size


Description
===========

This interface is intended for memory hot-delete. The requested region is released from a currently busy memory resource. The requested region must either match exactly or fit into
a single busy resource entry. In the latter case, the remaining resource is adjusted accordingly. Existing children of the busy memory resource must be immutable in the request.


Note
====

- Additional release conditions, such as overlapping region, can be supported after they are confirmed as valid cases. - When a busy memory resource gets split into two entries,
the code assumes that all children remain in the lower address entry for simplicity. Enhance this logic when necessary.
