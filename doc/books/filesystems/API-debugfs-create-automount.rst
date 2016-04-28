.. -*- coding: utf-8; mode: rst -*-

.. _API-debugfs-create-automount:

========================
debugfs_create_automount
========================

*man debugfs_create_automount(9)*

*4.6.0-rc5*

create automount point in the debugfs filesystem


Synopsis
========

.. c:function:: struct dentry * debugfs_create_automount( const char * name, struct dentry * parent, struct vfsmount *(*f) void *, void * data )

Arguments
=========

``name``
    a pointer to a string containing the name of the file to create.

``parent``
    a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the file
    will be created in the root of the debugfs filesystem.

``f``
    function to be called when pathname resolution steps on that one.

``data``
    opaque argument to pass to ``f``.


Description
===========

``f`` should return what ->``d_automount`` would.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
