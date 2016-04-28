.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-display-power-get:

=======================
intel_display_power_get
=======================

*man intel_display_power_get(9)*

*4.6.0-rc5*

grab a power domain reference


Synopsis
========

.. c:function:: void intel_display_power_get( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to reference


Description
===========

This function grabs a power domain reference for ``domain`` and ensures
that the power domain and all its parents are powered up. Therefore
users should only grab a reference to the innermost power domain they
need.

Any power domain reference obtained by this function must have a
symmetric call to ``intel_display_power_put`` to release the reference
again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
