
.. _API-intel-hpd-irq-handler:

=====================
intel_hpd_irq_handler
=====================

*man intel_hpd_irq_handler(9)*

*4.6.0-rc1*

main hotplug irq handler


Synopsis
========

.. c:function:: void intel_hpd_irq_handler( struct drm_device * dev, u32 pin_mask, u32 long_mask )

Arguments
=========

``dev``
    drm device

``pin_mask``
    a mask of hpd pins that have triggered the irq

``long_mask``
    a mask of hpd pins that may be long hpd pulses


Description
===========

This is the main hotplug irq handler for all platforms. The platform specific irq handlers call the platform specific hotplug irq handlers, which read and decode the appropriate
registers into bitmasks about hpd pins that have triggered (``pin_mask``), and which of those pins may be long pulses (``long_mask``). The ``long_mask`` is ignored if the port
corresponding to the pin is not a digital port.

Here, we do hotplug irq storm detection and mitigation, and pass further processing to appropriate bottom halves.
