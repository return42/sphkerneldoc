.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-framebuffer-reference:

=========================
drm_framebuffer_reference
=========================

*man drm_framebuffer_reference(9)*

*4.6.0-rc5*

incr the fb refcnt


Synopsis
========

.. c:function:: void drm_framebuffer_reference( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer


Description
===========

This functions increments the fb's refcount.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
