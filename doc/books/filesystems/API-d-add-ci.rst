
.. _API-d-add-ci:

========
d_add_ci
========

*man d_add_ci(9)*

*4.6.0-rc1*

lookup or allocate new dentry with case-exact name


Synopsis
========

.. c:function:: struct dentry ⋆ d_add_ci( struct dentry * dentry, struct inode * inode, struct qstr * name )

Arguments
=========

``dentry``
    the negative dentry that was passed to the parent's lookup func

``inode``
    the inode case-insensitive lookup has found

``name``
    the case-exact name to be associated with the returned dentry


Description
===========

This is to avoid filling the dcache with case-insensitive names to the same inode, only the actual correct case is stored in the dcache for case-insensitive filesystems.

For a case-insensitive lookup match and if the the case-exact dentry already exists in in the dcache, use it and return it.

If no entry exists with the exact case name, allocate new dentry with the exact case, and return the spliced entry.
