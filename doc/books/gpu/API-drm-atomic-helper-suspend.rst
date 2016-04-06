
.. _API-drm-atomic-helper-suspend:

=========================
drm_atomic_helper_suspend
=========================

*man drm_atomic_helper_suspend(9)*

*4.6.0-rc1*

subsystem-level suspend helper


Synopsis
========

.. c:function:: struct drm_atomic_state ⋆ drm_atomic_helper_suspend( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Duplicates the current atomic state, disables all active outputs and then returns a pointer to the original atomic state to the caller. Drivers can pass this pointer to the
``drm_atomic_helper_resume`` helper upon resume to restore the output configuration that was active at the time the system entered suspend.

Note that it is potentially unsafe to use this. The atomic state object returned by this function is assumed to be persistent. Drivers must ensure that this holds true. Before
calling this function, drivers must make sure to suspend fbdev emulation so that nothing can be using the device.


Returns
=======

A pointer to a copy of the state before suspend on success or an ``ERR_PTR``- encoded error code on failure. Drivers should store the returned atomic state object and pass it to
the ``drm_atomic_helper_resume`` helper upon resume.


See also
========

``drm_atomic_helper_duplicate_state``, ``drm_atomic_helper_disable_all``, ``drm_atomic_helper_resume``
