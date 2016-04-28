.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-check-pch-fifo-underruns:

==============================
intel_check_pch_fifo_underruns
==============================

*man intel_check_pch_fifo_underruns(9)*

*4.6.0-rc5*

check for PCH fifo underruns immediately


Synopsis
========

.. c:function:: void intel_check_pch_fifo_underruns( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Check for PCH fifo underruns immediately. Useful on CPT/PPT where the
shared error interrupt may have been disabled, and so PCH fifo underruns
won't necessarily raise an interrupt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
