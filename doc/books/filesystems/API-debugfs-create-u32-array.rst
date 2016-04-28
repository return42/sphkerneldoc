.. -*- coding: utf-8; mode: rst -*-

.. _API-debugfs-create-u32-array:

========================
debugfs_create_u32_array
========================

*man debugfs_create_u32_array(9)*

*4.6.0-rc5*

create a debugfs file that is used to read u32 array.


Synopsis
========

.. c:function:: struct dentry * debugfs_create_u32_array( const char * name, umode_t mode, struct dentry * parent, u32 * array, u32 elements )

Arguments
=========

``name``
    a pointer to a string containing the name of the file to create.

``mode``
    the permission that the file should have.

``parent``
    a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is ``NULL``, then the
    file will be created in the root of the debugfs filesystem.

``array``
    u32 array that provides data.

``elements``
    total number of elements in the array.


Description
===========

This function creates a file in debugfs with the given name that exports
``array`` as data. If the ``mode`` variable is so set it can be read
from. Writing is not supported. Seek within the file is also not
supported. Once array is created its size can not be changed.

The function returns a pointer to dentry on success. If debugfs is not
enabled in the kernel, the value -``ENODEV`` will be returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
