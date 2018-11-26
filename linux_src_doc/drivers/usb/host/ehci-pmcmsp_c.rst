.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ehci-pmcmsp.c

.. _`usb_hcd_msp_probe`:

usb_hcd_msp_probe
=================

.. c:function:: int usb_hcd_msp_probe(const struct hc_driver *driver, struct platform_device *dev)

    initialize PMC MSP-based HCDs

    :param driver:
        *undescribed*
    :type driver: const struct hc_driver \*

    :param dev:
        *undescribed*
    :type dev: struct platform_device \*

.. _`usb_hcd_msp_probe.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_msp_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. _`usb_hcd_msp_remove`:

usb_hcd_msp_remove
==================

.. c:function:: void usb_hcd_msp_remove(struct usb_hcd *hcd, struct platform_device *dev)

    shutdown processing for PMC MSP-based HCDs

    :param hcd:
        *undescribed*
    :type hcd: struct usb_hcd \*

    :param dev:
        USB Host Controller being removed
    :type dev: struct platform_device \*

.. _`usb_hcd_msp_remove.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_msp_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_hcd_msp_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.  It is always called from a thread
context, normally "rmmod", "apmd", or something similar.

may be called without controller electrically present
may be called with controller, bus, and devices active

.. This file was automatic generated / don't edit.

