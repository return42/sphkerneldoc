
.. _API-d-alloc-pseudo:

==============
d_alloc_pseudo
==============

*man d_alloc_pseudo(9)*

*4.6.0-rc1*

allocate a dentry (for lookup-less filesystems)


Synopsis
========

.. c:function:: struct dentry ⋆ d_alloc_pseudo( struct super_block * sb, const struct qstr * name )

Arguments
=========

``sb``
    the superblock

``name``
    qstr of the name


Description
===========

For a filesystem that just pins its dentries in memory and never performs lookups at all, return an unhashed IS_ROOT dentry.
