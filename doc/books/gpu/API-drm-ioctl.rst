.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-ioctl:

=========
drm_ioctl
=========

*man drm_ioctl(9)*

*4.6.0-rc5*

ioctl callback implementation for DRM drivers


Synopsis
========

.. c:function:: long drm_ioctl( struct file * filp, unsigned int cmd, unsigned long arg )

Arguments
=========

``filp``
    file this ioctl is called on

``cmd``
    ioctl cmd number

``arg``
    user argument


Looks up the ioctl function in the
==================================

:ioctls table, checking for root previleges if so required, and
dispatches to the respective function.


Returns
=======

Zero on success, negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
