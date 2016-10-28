.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ehci-omap.c

.. _`ehci_hcd_omap_probe`:

ehci_hcd_omap_probe
===================

.. c:function:: int ehci_hcd_omap_probe(struct platform_device *pdev)

    initialize TI-based HCDs

    :param struct platform_device \*pdev:
        *undescribed*

.. _`ehci_hcd_omap_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. _`ehci_hcd_omap_remove`:

ehci_hcd_omap_remove
====================

.. c:function:: int ehci_hcd_omap_remove(struct platform_device *pdev)

    shutdown processing for EHCI HCDs

    :param struct platform_device \*pdev:
        USB Host Controller being removed

.. _`ehci_hcd_omap_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_ehci_hcd_omap_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.  It is always called from a thread
context, normally "rmmod", "apmd", or something similar.

.. This file was automatic generated / don't edit.

