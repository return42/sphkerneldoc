
.. _API-drm-dev-register:

================
drm_dev_register
================

*man drm_dev_register(9)*

*4.6.0-rc1*

Register DRM device


Synopsis
========

.. c:function:: int drm_dev_register( struct drm_device * dev, unsigned long flags )

Arguments
=========

``dev``
    Device to register

``flags``
    Flags passed to the driver's .\ ``load`` function


Description
===========

Register the DRM device ``dev`` with the system, advertise device to user-space and start normal device operation. ``dev`` must be allocated via ``drm_dev_alloc`` previously.

Never call this twice on any device!


NOTE
====

To ensure backward compatibility with existing drivers method this function calls the ->``load`` method after registering the device nodes, creating race conditions. Usage of the
->``load`` methods is therefore deprecated, drivers must perform all initialization before calling ``drm_dev_register``.


RETURNS
=======

0 on success, negative error code on failure.
