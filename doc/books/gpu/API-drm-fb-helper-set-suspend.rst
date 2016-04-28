.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-set-suspend:

=========================
drm_fb_helper_set_suspend
=========================

*man drm_fb_helper_set_suspend(9)*

*4.6.0-rc5*

wrapper around fb_set_suspend


Synopsis
========

.. c:function:: void drm_fb_helper_set_suspend( struct drm_fb_helper * fb_helper, int state )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper

``state``
    desired state, zero to resume, non-zero to suspend


Description
===========

A wrapper around fb_set_suspend implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
