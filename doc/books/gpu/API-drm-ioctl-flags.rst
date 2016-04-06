
.. _API-drm-ioctl-flags:

===============
drm_ioctl_flags
===============

*man drm_ioctl_flags(9)*

*4.6.0-rc1*

Check for core ioctl and return ioctl permission flags


Synopsis
========

.. c:function:: bool drm_ioctl_flags( unsigned int nr, unsigned int * flags )

Arguments
=========

``nr``
    ioctl number

``flags``
    where to return the ioctl permission flags


Description
===========

This ioctl is only used by the vmwgfx driver to augment the access checks done by the drm core and insofar a pretty decent layering violation. This shouldn't be used by any
drivers.


Returns
=======

True if the ``nr`` corresponds to a DRM core ioctl numer, false otherwise.
