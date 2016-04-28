.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-guc-ucode-init:

====================
intel_guc_ucode_init
====================

*man intel_guc_ucode_init(9)*

*4.6.0-rc5*

define parameters and fetch firmware


Synopsis
========

.. c:function:: void intel_guc_ucode_init( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

Called early during driver load, but after GEM is initialised.

The firmware will be transferred to the GuC's memory later, when
``intel_guc_ucode_load`` is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
