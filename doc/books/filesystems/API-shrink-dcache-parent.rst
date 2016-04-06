
.. _API-shrink-dcache-parent:

====================
shrink_dcache_parent
====================

*man shrink_dcache_parent(9)*

*4.6.0-rc1*

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
