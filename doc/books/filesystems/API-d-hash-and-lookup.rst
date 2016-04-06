
.. _API-d-hash-and-lookup:

=================
d_hash_and_lookup
=================

*man d_hash_and_lookup(9)*

*4.6.0-rc1*

hash the qstr then search for a dentry


Synopsis
========

.. c:function:: struct dentry ⋆ d_hash_and_lookup( struct dentry * dir, struct qstr * name )

Arguments
=========

``dir``
    Directory to search in

``name``
    qstr of name we wish to find


Description
===========

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)
