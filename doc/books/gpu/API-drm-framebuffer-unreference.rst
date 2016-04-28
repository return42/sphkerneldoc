.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-framebuffer-unreference:

===========================
drm_framebuffer_unreference
===========================

*man drm_framebuffer_unreference(9)*

*4.6.0-rc5*

unref a framebuffer


Synopsis
========

.. c:function:: void drm_framebuffer_unreference( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer to unref


Description
===========

This functions decrements the fb's refcount and frees it if it drops to
zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
