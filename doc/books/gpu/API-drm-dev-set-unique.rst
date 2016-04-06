
.. _API-drm-dev-set-unique:

==================
drm_dev_set_unique
==================

*man drm_dev_set_unique(9)*

*4.6.0-rc1*

Set the unique name of a DRM device


Synopsis
========

.. c:function:: int drm_dev_set_unique( struct drm_device * dev, const char * name )

Arguments
=========

``dev``
    device of which to set the unique name

``name``
    unique name


Description
===========

Sets the unique name of a DRM device using the specified string. Drivers can use this at driver probe time if the unique name of the devices they drive is static.


Return
======

0 on success or a negative error code on failure.
