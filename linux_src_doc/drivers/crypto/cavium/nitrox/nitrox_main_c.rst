.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_main.c

.. _`ucode`:

struct ucode
============

.. c:type:: struct ucode

    Firmware Header

.. _`ucode.definition`:

Definition
----------

.. code-block:: c

    struct ucode {
        u8 id;
        char version[VERSION_LEN - 1];
        __be32 code_size;
        u8 raz[12];
        u64 code[0];
    }

.. _`ucode.members`:

Members
-------

id
    microcode ID

version
    firmware version

code_size
    code section size

raz
    alignment

code
    code section

.. _`write_to_ucd_unit`:

write_to_ucd_unit
=================

.. c:function:: void write_to_ucd_unit(struct nitrox_device *ndev, struct ucode *ucode)

    Write Firmware to NITROX UCD unit

    :param ndev:
        *undescribed*
    :type ndev: struct nitrox_device \*

    :param ucode:
        *undescribed*
    :type ucode: struct ucode \*

.. _`nitrox_add_to_devlist`:

nitrox_add_to_devlist
=====================

.. c:function:: int nitrox_add_to_devlist(struct nitrox_device *ndev)

    add NITROX device to global device list

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

.. _`nitrox_remove_from_devlist`:

nitrox_remove_from_devlist
==========================

.. c:function:: void nitrox_remove_from_devlist(struct nitrox_device *ndev)

    remove NITROX device from global device list

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

.. _`nitrox_bist_check`:

nitrox_bist_check
=================

.. c:function:: int nitrox_bist_check(struct nitrox_device *ndev)

    Check NITORX BIST registers status

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

.. _`nitrox_probe`:

nitrox_probe
============

.. c:function:: int nitrox_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    NITROX Initialization function.

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param id:
        entry in nitrox_pci_tbl
    :type id: const struct pci_device_id \*

.. _`nitrox_probe.return`:

Return
------

0, if the driver is bound to the device, or
a negative error if there is failure.

.. _`nitrox_remove`:

nitrox_remove
=============

.. c:function:: void nitrox_remove(struct pci_dev *pdev)

    Unbind the driver from the device.

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. This file was automatic generated / don't edit.

