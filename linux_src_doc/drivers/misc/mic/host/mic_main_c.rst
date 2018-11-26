.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_main.c

.. _`mic_ops_init`:

mic_ops_init
============

.. c:function:: void mic_ops_init(struct mic_device *mdev)

    Initialize HW specific operation tables.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_ops_init.description`:

Description
-----------

returns none.

.. _`mic_get_family`:

mic_get_family
==============

.. c:function:: enum mic_hw_family mic_get_family(struct pci_dev *pdev)

    Determine hardware family to which this MIC belongs.

    :param pdev:
        The pci device structure
    :type pdev: struct pci_dev \*

.. _`mic_get_family.description`:

Description
-----------

returns family.

.. _`mic_device_init`:

mic_device_init
===============

.. c:function:: void mic_device_init(struct mic_device *mdev, struct pci_dev *pdev)

    Allocates and initializes the MIC device structure

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        The pci device structure
    :type pdev: struct pci_dev \*

.. _`mic_device_init.description`:

Description
-----------

returns none.

.. _`mic_probe`:

mic_probe
=========

.. c:function:: int mic_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

    :param ent:
        entry in mic_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`mic_probe.description`:

Description
-----------

returns 0 on success, < 0 on failure.

.. _`mic_remove`:

mic_remove
==========

.. c:function:: void mic_remove(struct pci_dev *pdev)

    Device Removal Routine mic_remove is called by the PCI subsystem to alert the driver that it should release a PCI device.

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. This file was automatic generated / don't edit.

