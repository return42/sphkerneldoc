
.. _API-path-get:

========
path_get
========

*man path_get(9)*

*4.6.0-rc1*

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

Given a path increment the reference count to the dentry and the vfsmount.
