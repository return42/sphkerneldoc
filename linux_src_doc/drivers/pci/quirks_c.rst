.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/quirks.c

.. _`quirk_via_vlink`:

quirk_via_vlink
===============

.. c:function:: void quirk_via_vlink(struct pci_dev *dev)

    VIA VLink IRQ number update

    :param struct pci_dev \*dev:
        PCI device

.. _`quirk_via_vlink.description`:

Description
-----------

If the device we are dealing with is on a PIC IRQ we need to
ensure that the IRQ line register which usually is not relevant
for PCI cards, is actually written so that interrupts get sent
to the right place.
We only do this on systems where a VIA south bridge was detected,
and only for VIA devices on the motherboard (see quirk_via_bridge
above).

.. This file was automatic generated / don't edit.

