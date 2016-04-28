.. -*- coding: utf-8; mode: rst -*-

.. _API-path-put:

========
path_put
========

*man path_put(9)*

*4.6.0-rc5*

put a reference to a path


Synopsis
========

.. c:function:: void path_put( const struct path * path )

Arguments
=========

``path``
    path to put the reference to


Description
===========

Given a path decrement the reference count to the dentry and the
vfsmount.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
