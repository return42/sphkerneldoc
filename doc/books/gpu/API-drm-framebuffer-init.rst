.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-framebuffer-init:

====================
drm_framebuffer_init
====================

*man drm_framebuffer_init(9)*

*4.6.0-rc5*

initialize a framebuffer


Synopsis
========

.. c:function:: int drm_framebuffer_init( struct drm_device * dev, struct drm_framebuffer * fb, const struct drm_framebuffer_funcs * funcs )

Arguments
=========

``dev``
    DRM device

``fb``
    framebuffer to be initialized

``funcs``
    ... with these functions


Description
===========

Allocates an ID for the framebuffer's parent mode object, sets its mode
functions & device file and adds it to the master fd list.


IMPORTANT
=========

This functions publishes the fb and makes it available for concurrent
access by other users. Which means by this point the fb _must_ be
fully set up - since all the fb attributes are invariant over its
lifetime, no further locking but only correct reference counting is
required.


Returns
=======

Zero on success, error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
