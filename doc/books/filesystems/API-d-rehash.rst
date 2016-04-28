.. -*- coding: utf-8; mode: rst -*-

.. _API-d-rehash:

========
d_rehash
========

*man d_rehash(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
