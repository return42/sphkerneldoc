
.. _API-intel-sanitize-enable-execlists:

===============================
intel_sanitize_enable_execlists
===============================

*man intel_sanitize_enable_execlists(9)*

*4.6.0-rc1*

sanitize i915.enable_execlists


Synopsis
========

.. c:function:: int intel_sanitize_enable_execlists( struct drm_device * dev, int enable_execlists )

Arguments
=========

``dev``
    DRM device.

``enable_execlists``
    value of i915.enable_execlists module parameter.


Description
===========

Only certain platforms support Execlists (the prerequisites being support for Logical Ring Contexts and Aliasing PPGTT or better).


Return
======

1 if Execlists is supported and has to be enabled.
