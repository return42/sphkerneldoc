.. -*- coding: utf-8; mode: rst -*-

.. _API-media-devnode-create:

====================
media_devnode_create
====================

*man media_devnode_create(9)*

*4.6.0-rc5*

creates and initializes a device node interface


Synopsis
========

.. c:function:: struct media_intf_devnode * media_devnode_create( struct media_device * mdev, u32 type, u32 flags, u32 major, u32 minor )

Arguments
=========

``mdev``
    pointer to struct ``media_device``

``type``
    type of the interface, as given by MEDIA_INTF_T_* macros as
    defined in the uapi/media/media.h header.

``flags``
    Interface flags as defined in uapi/media/media.h.

``major``
    Device node major number.

``minor``
    Device node minor number.


Return
======

if succeeded, returns a pointer to the newly allocated
``media_intf_devnode`` pointer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
