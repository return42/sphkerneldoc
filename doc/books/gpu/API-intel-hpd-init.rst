.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-hpd-init:

==============
intel_hpd_init
==============

*man intel_hpd_init(9)*

*4.6.0-rc5*

initializes and enables hpd support


Synopsis
========

.. c:function:: void intel_hpd_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function enables the hotplug support. It requires that interrupts
have already been enabled with ``intel_irq_init_hw``. From this point on
hotplug and poll request can run concurrently to other code, so locking
rules must be obeyed.

This is a separate step from interrupt enabling to simplify the locking
rules in the driver load and resume code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
