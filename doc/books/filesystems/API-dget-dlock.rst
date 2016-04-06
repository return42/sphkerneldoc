
.. _API-dget-dlock:

==========
dget_dlock
==========

*man dget_dlock(9)*

*4.6.0-rc1*

get a reference to a dentry


Synopsis
========

.. c:function:: struct dentry ⋆ dget_dlock( struct dentry * dentry )

Arguments
=========

``dentry``
    dentry to get a reference to


Description
===========

Given a dentry or ``NULL`` pointer increment the reference count if appropriate and return the dentry. A dentry will not be destroyed when it has references.
