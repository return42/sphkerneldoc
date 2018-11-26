.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_sc1200.c

.. _`sc1200_clock`:

sc1200_clock
============

.. c:function:: int sc1200_clock( void)

    PCI clock

    :param void:
        no arguments
    :type void: 

.. _`sc1200_clock.description`:

Description
-----------

Return the PCI bus clocking for the SC1200 chipset configuration
in use. We return 0 for 33MHz 1 for 48MHz and 2 for 66Mhz

.. _`sc1200_set_piomode`:

sc1200_set_piomode
==================

.. c:function:: void sc1200_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        device on the interface
    :type adev: struct ata_device \*

.. _`sc1200_set_piomode.description`:

Description
-----------

Set our PIO requirements. This is fairly simple on the SC1200

.. _`sc1200_set_dmamode`:

sc1200_set_dmamode
==================

.. c:function:: void sc1200_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        Device being configured
    :type adev: struct ata_device \*

.. _`sc1200_set_dmamode.description`:

Description
-----------

We cannot mix MWDMA and UDMA without reloading timings each switch
master to slave.

.. _`sc1200_qc_issue`:

sc1200_qc_issue
===============

.. c:function:: unsigned int sc1200_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param qc:
        command pending
    :type qc: struct ata_queued_cmd \*

.. _`sc1200_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary.  Specifically we have a problem that there is only
one MWDMA/UDMA bit.

.. _`sc1200_qc_defer`:

sc1200_qc_defer
===============

.. c:function:: int sc1200_qc_defer(struct ata_queued_cmd *qc)

    implement serialization

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`sc1200_qc_defer.description`:

Description
-----------

Serialize command issue on this controller.

.. _`sc1200_init_one`:

sc1200_init_one
===============

.. c:function:: int sc1200_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise an SC1200

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        Entry in match table
    :type id: const struct pci_device_id \*

.. _`sc1200_init_one.description`:

Description
-----------

Just throw the needed data at the libata helper and it does all
our work.

.. This file was automatic generated / don't edit.

