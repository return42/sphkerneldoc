
.. _API-intel-psr-init:

==============
intel_psr_init
==============

*man intel_psr_init(9)*

*4.6.0-rc1*

Init basic PSR work and mutex.


Synopsis
========

.. c:function:: void intel_psr_init( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function is called only once at driver load to initialize basic PSR stuff.
