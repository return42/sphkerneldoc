.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dev-unregister:

==================
drm_dev_unregister
==================

*man drm_dev_unregister(9)*

*4.6.0-rc5*

Unregister DRM device


Synopsis
========

.. c:function:: void drm_dev_unregister( struct drm_device * dev )

Arguments
=========

``dev``
    Device to unregister


Description
===========

Unregister the DRM device from the system. This does the reverse of
``drm_dev_register`` but does not deallocate the device. The caller must
call ``drm_dev_unref`` to drop their final reference.

This should be called first in the device teardown code to make sure
userspace can't access the device instance any more.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
