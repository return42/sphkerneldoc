.. -*- coding: utf-8; mode: rst -*-

.. _API-cdev-init:

=========
cdev_init
=========

*man cdev_init(9)*

*4.6.0-rc5*

initialize a cdev structure


Synopsis
========

.. c:function:: void cdev_init( struct cdev * cdev, const struct file_operations * fops )

Arguments
=========

``cdev``
    the structure to initialize

``fops``
    the file_operations for this device


Description
===========

Initializes ``cdev``, remembering ``fops``, making it ready to add to
the system with ``cdev_add``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
