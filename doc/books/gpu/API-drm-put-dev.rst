.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-put-dev:

===========
drm_put_dev
===========

*man drm_put_dev(9)*

*4.6.0-rc5*

Unregister and release a DRM device


Synopsis
========

.. c:function:: void drm_put_dev( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Called at module unload time or when a PCI device is unplugged.

Cleans up all DRM device, calling ``drm_lastclose``.


Note
====

Use of this function is deprecated. It will eventually go away
completely. Please use ``drm_dev_unregister`` and ``drm_dev_unref``
explicitly instead to make sure that the device isn't userspace
accessible any more while teardown is in progress, ensuring that
userspace can't access an inconsistent state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
