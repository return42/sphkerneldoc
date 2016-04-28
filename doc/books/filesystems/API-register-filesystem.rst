.. -*- coding: utf-8; mode: rst -*-

.. _API-register-filesystem:

===================
register_filesystem
===================

*man register_filesystem(9)*

*4.6.0-rc5*

register a new filesystem


Synopsis
========

.. c:function:: int register_filesystem( struct file_system_type * fs )

Arguments
=========

``fs``
    the file system structure


Description
===========

Adds the file system passed to the list of file systems the kernel is
aware of for mount and other syscalls. Returns 0 on success, or a
negative errno code on an error.

The ``struct file_system_type`` that is passed is linked into the kernel
structures and must not be freed until the file system has been
unregistered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
