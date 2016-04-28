.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-wait-one-vblank:

===================
drm_wait_one_vblank
===================

*man drm_wait_one_vblank(9)*

*4.6.0-rc5*

wait for one vblank


Synopsis
========

.. c:function:: void drm_wait_one_vblank( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index


Description
===========

This waits for one vblank to pass on ``pipe``, using the irq driver
interfaces. It is a failure to call this when the vblank irq for
``pipe`` is disabled, e.g. due to lack of driver support or because the
crtc is off.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
