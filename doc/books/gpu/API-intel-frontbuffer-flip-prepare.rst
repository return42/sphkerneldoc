
.. _API-intel-frontbuffer-flip-prepare:

==============================
intel_frontbuffer_flip_prepare
==============================

*man intel_frontbuffer_flip_prepare(9)*

*4.6.0-rc1*

prepare asynchronous frontbuffer flip


Synopsis
========

.. c:function:: void intel_frontbuffer_flip_prepare( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

This function gets called after scheduling a flip on ``obj``. The actual frontbuffer flushing will be delayed until completion is signalled with intel_frontbuffer_flip_complete.
If an invalidate happens in between this flush will be cancelled.

Can be called without any locks held.
