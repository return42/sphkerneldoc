.. -*- coding: utf-8; mode: rst -*-

.. _API-path-get:

========
path_get
========

*man path_get(9)*

*4.6.0-rc5*

get a reference to a path


Synopsis
========

.. c:function:: void path_get( const struct path * path )

Arguments
=========

``path``
    path to get the reference to


Description
===========

Given a path increment the reference count to the dentry and the
vfsmount.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
