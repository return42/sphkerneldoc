
.. _API-d-rehash:

========
d_rehash
========

*man d_rehash(9)*

*4.6.0-rc1*

add an entry back to the hash


Synopsis
========

.. c:function:: void d_rehash( struct dentry * entry )

Arguments
=========

``entry``
    dentry to add to the hash


Description
===========

Adds a dentry to the hash according to its name.
