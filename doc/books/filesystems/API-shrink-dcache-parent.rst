.. -*- coding: utf-8; mode: rst -*-

.. _API-shrink-dcache-parent:

====================
shrink_dcache_parent
====================

*man shrink_dcache_parent(9)*

*4.6.0-rc5*

prune dcache


Synopsis
========

.. c:function:: void shrink_dcache_parent( struct dentry * parent )

Arguments
=========

``parent``
    parent of entries to prune


Description
===========

Prune the dcache to remove unused children of the parent dentry.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
