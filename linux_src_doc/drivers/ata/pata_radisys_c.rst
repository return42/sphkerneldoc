.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_radisys.c

.. _`radisys_set_piomode`:

radisys_set_piomode
===================

.. c:function:: void radisys_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device whose timings we are configuring
    :type adev: struct ata_device \*

.. _`radisys_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`radisys_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`radisys_set_dmamode`:

radisys_set_dmamode
===================

.. c:function:: void radisys_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device to program
    :type adev: struct ata_device \*

.. _`radisys_set_dmamode.description`:

Description
-----------

Set MWDMA mode for device, in host controller PCI config space.

.. _`radisys_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`radisys_qc_issue`:

radisys_qc_issue
================

.. c:function:: unsigned int radisys_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param qc:
        command pending
    :type qc: struct ata_queued_cmd \*

.. _`radisys_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary. Our logic also clears TIME0/TIME1 for the other device so
that, even if we get this wrong, cycles to the other device will
be made PIO0.

.. _`radisys_init_one`:

radisys_init_one
================

.. c:function:: int radisys_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register PIIX ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in radisys_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

.. _`radisys_init_one.description`:

Description
-----------

Called from kernel PCI layer.  We probe for combined mode (sigh),
and then hand over control to libata, for it to do the rest.

.. _`radisys_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`radisys_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

