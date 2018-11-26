.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/fotg210-hcd.c

.. _`fotg210_hcd_probe`:

fotg210_hcd_probe
=================

.. c:function:: int fotg210_hcd_probe(struct platform_device *pdev)

    initialize faraday FOTG210 HCDs

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`fotg210_hcd_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. _`fotg210_hcd_remove`:

fotg210_hcd_remove
==================

.. c:function:: int fotg210_hcd_remove(struct platform_device *pdev)

    shutdown processing for EHCI HCDs

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. This file was automatic generated / don't edit.

