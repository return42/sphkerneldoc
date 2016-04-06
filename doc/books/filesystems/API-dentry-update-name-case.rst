
.. _API-dentry-update-name-case:

=======================
dentry_update_name_case
=======================

*man dentry_update_name_case(9)*

*4.6.0-rc1*

update case insensitive dentry with a new name


Synopsis
========

.. c:function:: void dentry_update_name_case( struct dentry * dentry, struct qstr * name )

Arguments
=========

``dentry``
    dentry to be updated

``name``
    new name


Description
===========

Update a case insensitive dentry with new case of name.

dentry must have been returned by d_lookup with name ``name``. Old and new name lengths must match (ie. no d_compare which allows mismatched name lengths).

Parent inode i_mutex must be held over d_lookup and into this call (to keep renames and concurrent inserts, and readdir(2) away).
