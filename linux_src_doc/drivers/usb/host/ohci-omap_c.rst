.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ohci-omap.c

.. _`usb_hcd_omap_probe`:

usb_hcd_omap_probe
==================

.. c:function:: int usb_hcd_omap_probe(const struct hc_driver *driver, struct platform_device *pdev)

    initialize OMAP-based HCDs

    :param const struct hc_driver \*driver:
        *undescribed*

    :param struct platform_device \*pdev:
        *undescribed*

.. _`usb_hcd_omap_probe.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_omap_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. _`usb_hcd_omap_remove`:

usb_hcd_omap_remove
===================

.. c:function:: void usb_hcd_omap_remove(struct usb_hcd *hcd, struct platform_device *pdev)

    shutdown processing for OMAP-based HCDs

    :param struct usb_hcd \*hcd:
        *undescribed*

    :param struct platform_device \*pdev:
        *undescribed*

.. _`usb_hcd_omap_remove.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_omap_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_hcd_omap_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.  It is always called from a thread
context, normally "rmmod", "apmd", or something similar.

.. This file was automatic generated / don't edit.

