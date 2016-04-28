.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-display-set-init-power:

============================
intel_display_set_init_power
============================

*man intel_display_set_init_power(9)*

*4.6.0-rc5*

set the initial power domain state


Synopsis
========

.. c:function:: void intel_display_set_init_power( struct drm_i915_private * dev_priv, bool enable )

Arguments
=========

``dev_priv``
    i915 device instance

``enable``
    whether to enable or disable the initial power domain state


Description
===========

For simplicity our driver load/unload and system suspend/resume code
assumes that all power domains are always enabled. This functions
controls the state of this little hack. While the initial power domain
state is enabled runtime pm is effectively disabled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
