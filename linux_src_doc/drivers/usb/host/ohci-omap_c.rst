.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ohci-omap.c

.. _`ohci_hcd_omap_probe`:

ohci_hcd_omap_probe
===================

.. c:function:: int ohci_hcd_omap_probe(struct platform_device *pdev)

    initialize OMAP-based HCDs

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`ohci_hcd_omap_probe.context`:

Context
-------

!in_interrupt()

.. _`ohci_hcd_omap_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. _`ohci_hcd_omap_remove`:

ohci_hcd_omap_remove
====================

.. c:function:: int ohci_hcd_omap_remove(struct platform_device *pdev)

    shutdown processing for OMAP-based HCDs

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`ohci_hcd_omap_remove.context`:

Context
-------

!in_interrupt()

.. _`ohci_hcd_omap_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`ohci_hcd_omap_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.  It is always called from a thread
context, normally "rmmod", "apmd", or something similar.

.. This file was automatic generated / don't edit.

