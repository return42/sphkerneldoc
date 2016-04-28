.. -*- coding: utf-8; mode: rst -*-

.. _API-d-unhashed:

==========
d_unhashed
==========

*man d_unhashed(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
