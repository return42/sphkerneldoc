
.. _API-have-submounts:

==============
have_submounts
==============

*man have_submounts(9)*

*4.6.0-rc1*

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
