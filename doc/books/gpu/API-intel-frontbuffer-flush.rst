
.. _API-intel-frontbuffer-flush:

=======================
intel_frontbuffer_flush
=======================

*man intel_frontbuffer_flush(9)*

*4.6.0-rc1*

flush frontbuffer


Synopsis
========

.. c:function:: void intel_frontbuffer_flush( struct drm_device * dev, unsigned frontbuffer_bits, enum fb_op_origin origin )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits

``origin``
    which operation caused the flush


Description
===========

This function gets called every time rendering on the given planes has completed and frontbuffer caching can be started again. Flushes will get delayed if they're blocked by some
outstanding asynchronous rendering.

Can be called without any locks held.
