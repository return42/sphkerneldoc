.. -*- coding: utf-8; mode: rst -*-

.. _API-dget-dlock:

==========
dget_dlock
==========

*man dget_dlock(9)*

*4.6.0-rc5*

get a reference to a dentry


Synopsis
========

.. c:function:: struct dentry * dget_dlock( struct dentry * dentry )

Arguments
=========

``dentry``
    dentry to get a reference to


Description
===========

Given a dentry or ``NULL`` pointer increment the reference count if
appropriate and return the dentry. A dentry will not be destroyed when
it has references.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
