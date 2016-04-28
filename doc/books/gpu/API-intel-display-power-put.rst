.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-display-power-put:

=======================
intel_display_power_put
=======================

*man intel_display_power_put(9)*

*4.6.0-rc5*

release a power domain reference


Synopsis
========

.. c:function:: void intel_display_power_put( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to reference


Description
===========

This function drops the power domain reference obtained by
``intel_display_power_get`` and might power down the corresponding
hardware block right away if this is the last reference.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
