.. -*- coding: utf-8; mode: rst -*-

.. _API---release-region:

================
__release_region
================

*man __release_region(9)*

*4.6.0-rc5*

release a previously reserved resource region


Synopsis
========

.. c:function:: void __release_region( struct resource * parent, resource_size_t start, resource_size_t n )

Arguments
=========

``parent``
    parent resource descriptor

``start``
    resource start address

``n``
    resource region size


Description
===========

The described resource region must match a currently busy region.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
