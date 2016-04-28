.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-devnode:

====================
struct media_devnode
====================

*man struct media_devnode(9)*

*4.6.0-rc5*

Media device node


Synopsis
========

.. code-block:: c

    struct media_devnode {
      const struct media_file_operations * fops;
      struct device dev;
      struct cdev cdev;
      struct device * parent;
      int minor;
      unsigned long flags;
      void (* release) (struct media_devnode *mdev);
    };


Members
=======

fops
    pointer to struct ``media_file_operations`` with media device ops

dev
    struct device pointer for the media controller device

cdev
    struct cdev pointer character device

parent
    parent device

minor
    device node minor number

flags
    flags, combination of the MEDIA_FLAG_* constants

release
    release callback called at the end of ``media_devnode_release``


Description
===========

This structure represents a media-related device node.

The ``parent`` is a physical device. It must be set by core or device
drivers before registering the node.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
