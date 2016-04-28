.. -*- coding: utf-8; mode: rst -*-

.. _API-securityfs-remove:

=================
securityfs_remove
=================

*man securityfs_remove(9)*

*4.6.0-rc5*

removes a file or directory from the securityfs filesystem


Synopsis
========

.. c:function:: void securityfs_remove( struct dentry * dentry )

Arguments
=========

``dentry``
    a pointer to a the dentry of the file or directory to be removed.


Description
===========

This function removes a file or directory in securityfs that was
previously created with a call to another securityfs function (like
``securityfs_create_file`` or variants thereof.)

This function is required to be called in order for the file to be
removed. No automatic cleanup of files will happen when a module is
removed; you are responsible here.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
