.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/via82cxxx.c

.. _`via_set_speed`:

via_set_speed
=============

.. c:function:: void via_set_speed(ide_hwif_t *hwif, u8 dn, struct ide_timing *timing)

    write timing registers

    :param hwif:
        *undescribed*
    :type hwif: ide_hwif_t \*

    :param dn:
        device
    :type dn: u8

    :param timing:
        IDE timing data to use
    :type timing: struct ide_timing \*

.. _`via_set_speed.description`:

Description
-----------

via_set_speed writes timing values to the chipset registers

.. _`via_set_drive`:

via_set_drive
=============

.. c:function:: void via_set_drive(ide_hwif_t *hwif, ide_drive_t *drive)

    configure transfer mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        Drive to set up
    :type drive: ide_drive_t \*

.. _`via_set_drive.description`:

Description
-----------

\ :c:func:`via_set_drive`\  computes timing values configures the chipset to
a desired transfer mode.  It also can be called by upper layers.

.. _`via_set_pio_mode`:

via_set_pio_mode
================

.. c:function:: void via_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`via_set_pio_mode.description`:

Description
-----------

A callback from the upper layers for PIO-only tuning.

.. _`init_chipset_via82cxxx`:

init_chipset_via82cxxx
======================

.. c:function:: int init_chipset_via82cxxx(struct pci_dev *dev)

    initialization handler

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`init_chipset_via82cxxx.description`:

Description
-----------

The initialization callback. Here we determine the IDE chip type
and initialize its drive independent registers.

.. This file was automatic generated / don't edit.

