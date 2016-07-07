.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_acpi.c

.. _`pacpi_pre_reset`:

pacpi_pre_reset
===============

.. c:function:: int pacpi_pre_reset(struct ata_link *link, unsigned long deadline)

    check for 40/80 pin

    :param struct ata_link \*link:
        *undescribed*

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`pacpi_pre_reset.description`:

Description
-----------

Perform the PATA port setup we need.

.. _`pacpi_cable_detect`:

pacpi_cable_detect
==================

.. c:function:: int pacpi_cable_detect(struct ata_port *ap)

    cable type detection

    :param struct ata_port \*ap:
        port to detect

.. _`pacpi_cable_detect.description`:

Description
-----------

Perform device specific cable detection

.. _`pacpi_discover_modes`:

pacpi_discover_modes
====================

.. c:function:: unsigned long pacpi_discover_modes(struct ata_port *ap, struct ata_device *adev)

    filter non ACPI modes

    :param struct ata_port \*ap:
        *undescribed*

    :param struct ata_device \*adev:
        ATA device

.. _`pacpi_discover_modes.description`:

Description
-----------

Try the modes available and see which ones the ACPI method will
set up sensibly. From this we get a mask of ACPI modes we can use

.. _`pacpi_mode_filter`:

pacpi_mode_filter
=================

.. c:function:: unsigned long pacpi_mode_filter(struct ata_device *adev, unsigned long mask)

    mode filter for ACPI

    :param struct ata_device \*adev:
        device

    :param unsigned long mask:
        mask of valid modes

.. _`pacpi_mode_filter.description`:

Description
-----------

Filter the valid mode list according to our own specific rules, in
this case the list of discovered valid modes obtained by ACPI probing

.. _`pacpi_set_piomode`:

pacpi_set_piomode
=================

.. c:function:: void pacpi_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`pacpi_set_dmamode`:

pacpi_set_dmamode
=================

.. c:function:: void pacpi_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`pacpi_qc_issue`:

pacpi_qc_issue
==============

.. c:function:: unsigned int pacpi_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`pacpi_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary.

.. _`pacpi_port_start`:

pacpi_port_start
================

.. c:function:: int pacpi_port_start(struct ata_port *ap)

    port setup

    :param struct ata_port \*ap:
        ATA port being set up

.. _`pacpi_port_start.description`:

Description
-----------

Use the port_start hook to maintain private control structures

.. _`pacpi_init_one`:

pacpi_init_one
==============

.. c:function:: int pacpi_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Register ACPI ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*id:
        *undescribed*

.. _`pacpi_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`pacpi_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`pacpi_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

