.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_oldpiix.c

.. _`oldpiix_pre_reset`:

oldpiix_pre_reset
=================

.. c:function:: int oldpiix_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`oldpiix_pre_reset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`oldpiix_set_piomode`:

oldpiix_set_piomode
===================

.. c:function:: void oldpiix_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device whose timings we are configuring

.. _`oldpiix_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`oldpiix_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`oldpiix_set_dmamode`:

oldpiix_set_dmamode
===================

.. c:function:: void oldpiix_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`oldpiix_set_dmamode.description`:

Description
-----------

Set MWDMA mode for device, in host controller PCI config space.

.. _`oldpiix_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`oldpiix_qc_issue`:

oldpiix_qc_issue
================

.. c:function:: unsigned int oldpiix_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`oldpiix_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary. Our logic also clears TIME0/TIME1 for the other device so
that, even if we get this wrong, cycles to the other device will
be made PIO0.

.. _`oldpiix_init_one`:

oldpiix_init_one
================

.. c:function:: int oldpiix_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register PIIX ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in oldpiix_pci_tbl matching with \ ``pdev``\ 

.. _`oldpiix_init_one.description`:

Description
-----------

Called from kernel PCI layer.  We probe for combined mode (sigh),
and then hand over control to libata, for it to do the rest.

.. _`oldpiix_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`oldpiix_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

