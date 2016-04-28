.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-csr-ucode-fini:

====================
intel_csr_ucode_fini
====================

*man intel_csr_ucode_fini(9)*

*4.6.0-rc5*

unload the CSR firmware.


Synopsis
========

.. c:function:: void intel_csr_ucode_fini( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 drm device.


Description
===========

Firmmware unloading includes freeing the internal momory and reset the
firmware loading status.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
