
.. _API-drm-atomic-helper-resume:

========================
drm_atomic_helper_resume
========================

*man drm_atomic_helper_resume(9)*

*4.6.0-rc1*

subsystem-level resume helper


Synopsis
========

.. c:function:: int drm_atomic_helper_resume( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    atomic state to resume to


Description
===========

Calls ``drm_mode_config_reset`` to synchronize hardware and software states, grabs all modeset locks and commits the atomic state object. This can be used in conjunction with the
``drm_atomic_helper_suspend`` helper to implement suspend/resume for drivers that support atomic mode-setting.


Returns
=======

0 on success or a negative error code on failure.


See also
========

``drm_atomic_helper_suspend``
