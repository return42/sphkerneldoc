.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-power-domains-fini:

========================
intel_power_domains_fini
========================

*man intel_power_domains_fini(9)*

*4.6.0-rc5*

finalizes the power domain structures


Synopsis
========

.. c:function:: void intel_power_domains_fini( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Finalizes the power domain structures for ``dev_priv`` depending upon
the supported platform. This function also disables runtime pm and
ensures that the device stays powered up so that the driver can be
reloaded.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
