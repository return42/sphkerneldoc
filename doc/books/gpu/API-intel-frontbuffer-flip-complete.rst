
.. _API-intel-frontbuffer-flip-complete:

===============================
intel_frontbuffer_flip_complete
===============================

*man intel_frontbuffer_flip_complete(9)*

*4.6.0-rc1*

complete asynchronous frontbuffer flip


Synopsis
========

.. c:function:: void intel_frontbuffer_flip_complete( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

This function gets called after the flip has been latched and will complete on the next vblank. It will execute the flush if it hasn't been cancelled yet.

Can be called without any locks held.
