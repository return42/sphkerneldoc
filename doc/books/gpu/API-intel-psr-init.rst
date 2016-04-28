.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-psr-init:

==============
intel_psr_init
==============

*man intel_psr_init(9)*

*4.6.0-rc5*

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

This function is called only once at driver load to initialize basic PSR
stuff.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
