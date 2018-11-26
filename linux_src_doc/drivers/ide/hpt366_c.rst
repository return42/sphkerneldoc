.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/hpt366.c

.. _`hpt3xxn_set_clock`:

hpt3xxn_set_clock
=================

.. c:function:: void hpt3xxn_set_clock(ide_hwif_t *hwif, u8 mode)

    perform clock switching dance

    :param hwif:
        hwif to switch
    :type hwif: ide_hwif_t \*

    :param mode:
        clocking mode (0x21 for write, 0x23 otherwise)
    :type mode: u8

.. _`hpt3xxn_set_clock.description`:

Description
-----------

Switch the DPLL clock on the HPT3xxN devices. This is a right mess.

.. _`hpt3xxn_rw_disk`:

hpt3xxn_rw_disk
===============

.. c:function:: void hpt3xxn_rw_disk(ide_drive_t *drive, struct request *rq)

    prepare for I/O

    :param drive:
        drive for command
    :type drive: ide_drive_t \*

    :param rq:
        block request structure
    :type rq: struct request \*

.. _`hpt3xxn_rw_disk.description`:

Description
-----------

This is called when a disk I/O is issued to HPT3xxN.
We need it because of the clock switching.

.. _`hpt37x_calibrate_dpll`:

hpt37x_calibrate_dpll
=====================

.. c:function:: int hpt37x_calibrate_dpll(struct pci_dev *dev, u16 f_low, u16 f_high)

    calibrate the DPLL

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param f_low:
        *undescribed*
    :type f_low: u16

    :param f_high:
        *undescribed*
    :type f_high: u16

.. _`hpt37x_calibrate_dpll.description`:

Description
-----------

Perform a calibration cycle on the DPLL.
Returns 1 if this succeeds

.. _`hpt366_init_one`:

hpt366_init_one
===============

.. c:function:: int hpt366_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when an HPT366 is found

    :param dev:
        the hpt366 device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`hpt366_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. This file was automatic generated / don't edit.

