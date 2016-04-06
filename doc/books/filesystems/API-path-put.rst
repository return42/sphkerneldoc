
.. _API-path-put:

========
path_put
========

*man path_put(9)*

*4.6.0-rc1*

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

Given a path decrement the reference count to the dentry and the vfsmount.
