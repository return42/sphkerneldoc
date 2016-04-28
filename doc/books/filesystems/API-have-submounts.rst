.. -*- coding: utf-8; mode: rst -*-

.. _API-have-submounts:

==============
have_submounts
==============

*man have_submounts(9)*

*4.6.0-rc5*

check for mounts over a dentry


Synopsis
========

.. c:function:: int have_submounts( struct dentry * parent )

Arguments
=========

``parent``
    dentry to check.


Description
===========

Return true if the parent or its subdirectories contain a mount point


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
