.. -*- coding: utf-8; mode: rst -*-

.. _API-region-intersects:

=================
region_intersects
=================

*man region_intersects(9)*

*4.6.0-rc5*

determine intersection of region with known resources


Synopsis
========

.. c:function:: int region_intersects( resource_size_t start, size_t size, unsigned long flags, unsigned long desc )

Arguments
=========

``start``
    region start address

``size``
    size of region

``flags``
    flags of resource (in iomem_resource)

``desc``
    descriptor of resource (in iomem_resource) or IORES_DESC_NONE


Description
===========

Check if the specified region partially overlaps or fully eclipses a
resource identified by ``flags`` and ``desc`` (optional with
IORES_DESC_NONE). Return REGION_DISJOINT if the region does not
overlap ``flags``/``desc``, return REGION_MIXED if the region overlaps
``flags``/``desc`` and another resource, and return REGION_INTERSECTS
if the region overlaps ``flags``/``desc`` and no other defined resource.
Note that REGION_INTERSECTS is also returned in the case when the
specified region overlaps RAM and undefined memory holes.

``region_intersect`` is used by memory remapping functions to ensure the
user is not remapping RAM and is a vast speed up over walking through
the resource table page by page.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
