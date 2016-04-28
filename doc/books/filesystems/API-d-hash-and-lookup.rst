.. -*- coding: utf-8; mode: rst -*-

.. _API-d-hash-and-lookup:

=================
d_hash_and_lookup
=================

*man d_hash_and_lookup(9)*

*4.6.0-rc5*

hash the qstr then search for a dentry


Synopsis
========

.. c:function:: struct dentry * d_hash_and_lookup( struct dentry * dir, struct qstr * name )

Arguments
=========

``dir``
    Directory to search in

``name``
    qstr of name we wish to find


Description
===========

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
