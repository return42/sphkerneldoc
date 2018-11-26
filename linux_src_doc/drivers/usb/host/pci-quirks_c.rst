.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/pci-quirks.c

.. _`quirk_usb_handoff_xhci`:

quirk_usb_handoff_xhci
======================

.. c:function:: void quirk_usb_handoff_xhci(struct pci_dev *pdev)

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`quirk_usb_handoff_xhci.description`:

Description
-----------

Takes care of the handoff between the Pre-OS (i.e. BIOS) and the OS.
It signals to the BIOS that the OS wants control of the host controller,
and then waits 1 second for the BIOS to hand over control.
If we timeout, assume the BIOS is broken and take control anyway.

.. This file was automatic generated / don't edit.

