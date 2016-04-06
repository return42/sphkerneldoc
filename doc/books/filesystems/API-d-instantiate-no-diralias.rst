
.. _API-d-instantiate-no-diralias:

=========================
d_instantiate_no_diralias
=========================

*man d_instantiate_no_diralias(9)*

*4.6.0-rc1*

instantiate a non-aliased dentry


Synopsis
========

.. c:function:: int d_instantiate_no_diralias( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to complete

``inode``
    inode to attach to this dentry


Description
===========

Fill in inode information in the entry. If a directory alias is found, then return an error (and drop inode). Together with ``d_materialise_unique`` this guarantees that a
directory inode may never have more than one alias.
