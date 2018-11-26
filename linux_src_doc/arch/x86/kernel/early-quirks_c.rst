.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/early-quirks.c

.. _`check_dev_quirk`:

check_dev_quirk
===============

.. c:function:: int check_dev_quirk(int num, int slot, int func)

    apply early quirks to a given PCI device

    :param num:
        bus number
    :type num: int

    :param slot:
        slot number
    :type slot: int

    :param func:
        PCI function
    :type func: int

.. _`check_dev_quirk.description`:

Description
-----------

Check the vendor & device ID against the early quirks table.

If the device is single function, let \ :c:func:`early_pci_scan_bus`\  know so we don't
poke at this device again.

.. This file was automatic generated / don't edit.

