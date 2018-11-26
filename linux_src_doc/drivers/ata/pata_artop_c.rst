.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_artop.c

.. _`artop62x0_pre_reset`:

artop62x0_pre_reset
===================

.. c:function:: int artop62x0_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param link:
        link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`artop62x0_pre_reset.description`:

Description
-----------

Nothing complicated needed here.

.. _`artop6260_cable_detect`:

artop6260_cable_detect
======================

.. c:function:: int artop6260_cable_detect(struct ata_port *ap)

    identify cable type

    :param ap:
        Port
    :type ap: struct ata_port \*

.. _`artop6260_cable_detect.description`:

Description
-----------

Identify the cable type for the ARTOP interface in question

.. _`artop6210_load_piomode`:

artop6210_load_piomode
======================

.. c:function:: void artop6210_load_piomode(struct ata_port *ap, struct ata_device *adev, unsigned int pio)

    Load a set of PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device
    :type adev: struct ata_device \*

    :param pio:
        PIO mode
    :type pio: unsigned int

.. _`artop6210_load_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. This
is used both to set PIO timings in PIO mode and also to set the
matching PIO clocking for UDMA, as well as the MWDMA timings.

.. _`artop6210_load_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6210_set_piomode`:

artop6210_set_piomode
=====================

.. c:function:: void artop6210_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device we are configuring
    :type adev: struct ata_device \*

.. _`artop6210_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. For
ARTOP we must also clear the UDMA bits if we are not doing UDMA. In
the event UDMA is used the later call to set_dmamode will set the
bits as required.

.. _`artop6210_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6260_load_piomode`:

artop6260_load_piomode
======================

.. c:function:: void artop6260_load_piomode(struct ata_port *ap, struct ata_device *adev, unsigned int pio)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device we are configuring
    :type adev: struct ata_device \*

    :param pio:
        PIO mode
    :type pio: unsigned int

.. _`artop6260_load_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. The
ARTOP6260 and relatives store the timing data differently.

.. _`artop6260_load_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6260_set_piomode`:

artop6260_set_piomode
=====================

.. c:function:: void artop6260_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device we are configuring
    :type adev: struct ata_device \*

.. _`artop6260_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. For
ARTOP we must also clear the UDMA bits if we are not doing UDMA. In
the event UDMA is used the later call to set_dmamode will set the
bits as required.

.. _`artop6260_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6210_set_dmamode`:

artop6210_set_dmamode
=====================

.. c:function:: void artop6210_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device whose timings we are configuring
    :type adev: struct ata_device \*

.. _`artop6210_set_dmamode.description`:

Description
-----------

Set DMA mode for device, in host controller PCI config space.

.. _`artop6210_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6260_set_dmamode`:

artop6260_set_dmamode
=====================

.. c:function:: void artop6260_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device we are configuring
    :type adev: struct ata_device \*

.. _`artop6260_set_dmamode.description`:

Description
-----------

Set DMA mode for device, in host controller PCI config space. The
ARTOP6260 and relatives store the timing data differently.

.. _`artop6260_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`artop6210_qc_defer`:

artop6210_qc_defer
==================

.. c:function:: int artop6210_qc_defer(struct ata_queued_cmd *qc)

    implement serialization

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`artop6210_qc_defer.description`:

Description
-----------

Issue commands per host on this chip.

.. _`artop_init_one`:

artop_init_one
==============

.. c:function:: int artop_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Register ARTOP ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`artop_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`artop_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`artop_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

