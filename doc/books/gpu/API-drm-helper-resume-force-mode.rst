
.. _API-drm-helper-resume-force-mode:

============================
drm_helper_resume_force_mode
============================

*man drm_helper_resume_force_mode(9)*

*4.6.0-rc1*

force-restore mode setting configuration


Synopsis
========

.. c:function:: void drm_helper_resume_force_mode( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device which should be restored


Description
===========

Drivers which use the mode setting helpers can use this function to force-restore the mode setting configuration e.g. on resume or when something else might have trampled over the
hw state (like some overzealous old BIOSen tended to do).

This helper doesn't provide a error return value since restoring the old config should never fail due to resource allocation issues since the driver has successfully set the
restored configuration already. Hence this should boil down to the equivalent of a few dpms on calls, which also don't provide an error code.

Drivers where simply restoring an old configuration again might fail (e.g. due to slight differences in allocating shared resources when the configuration is restored in a
different order than when userspace set it up) need to use their own restore logic.

This function is deprecated. New drivers should implement atomic mode- setting and use the atomic suspend/resume helpers.


See also
========

``drm_atomic_helper_suspend``, ``drm_atomic_helper_resume``
