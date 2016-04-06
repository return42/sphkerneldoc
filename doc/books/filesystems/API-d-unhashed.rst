
.. _API-d-unhashed:

==========
d_unhashed
==========

*man d_unhashed(9)*

*4.6.0-rc1*

is dentry hashed


Synopsis
========

.. c:function:: int d_unhashed( const struct dentry * dentry )

Arguments
=========

``dentry``
    entry to check


Description
===========

Returns true if the dentry passed is not currently hashed.
