
.. _API-intel-irq-init:

==============
intel_irq_init
==============

*man intel_irq_init(9)*

*4.6.0-rc1*

initializes irq support


Synopsis
========

.. c:function:: void intel_irq_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function initializes all the irq support including work items, timers and all the vtables. It does not setup the interrupt itself though.
