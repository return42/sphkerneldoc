.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_ns87415.c

.. _`ns87415_set_mode`:

ns87415_set_mode
================

.. c:function:: void ns87415_set_mode(struct ata_port *ap, struct ata_device *adev, u8 mode)

    Initialize host controller mode timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device whose timings we are configuring
    :type adev: struct ata_device \*

    :param mode:
        Mode to set
    :type mode: u8

.. _`ns87415_set_mode.description`:

Description
-----------

Program the mode registers for this controller, channel and
device. Because the chip is quite an old design we have to do this
for PIO/DMA switches.

.. _`ns87415_set_mode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`ns87415_set_piomode`:

ns87415_set_piomode
===================

.. c:function:: void ns87415_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Device to program
    :type adev: struct ata_device \*

.. _`ns87415_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`ns87415_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`ns87415_bmdma_setup`:

ns87415_bmdma_setup
===================

.. c:function:: void ns87415_bmdma_setup(struct ata_queued_cmd *qc)

    Set up DMA

    :param qc:
        Command block
    :type qc: struct ata_queued_cmd \*

.. _`ns87415_bmdma_setup.description`:

Description
-----------

Set up for bus masterng DMA. We have to do this ourselves
rather than use the helper due to a chip erratum

.. _`ns87415_bmdma_start`:

ns87415_bmdma_start
===================

.. c:function:: void ns87415_bmdma_start(struct ata_queued_cmd *qc)

    Begin DMA transfer

    :param qc:
        Command block
    :type qc: struct ata_queued_cmd \*

.. _`ns87415_bmdma_start.description`:

Description
-----------

Switch the timings for the chip and set up for a DMA transfer
before the DMA burst begins.

.. _`ns87415_bmdma_start.fixme`:

FIXME
-----

We should do lazy switching on bmdma_start versus
ata_pio_data_xfer for better performance.

.. _`ns87415_bmdma_stop`:

ns87415_bmdma_stop
==================

.. c:function:: void ns87415_bmdma_stop(struct ata_queued_cmd *qc)

    End DMA transfer

    :param qc:
        Command block
    :type qc: struct ata_queued_cmd \*

.. _`ns87415_bmdma_stop.description`:

Description
-----------

End DMA mode and switch the controller back into PIO mode

.. _`ns87415_irq_clear`:

ns87415_irq_clear
=================

.. c:function:: void ns87415_irq_clear(struct ata_port *ap)

    Clear interrupt

    :param ap:
        Channel to clear
    :type ap: struct ata_port \*

.. _`ns87415_irq_clear.erratum`:

Erratum
-------

Due to a chip bug regisers 02 and 0A bit 1 and 2 (the
error bits) are reset by writing to register 00 or 08.

.. _`ns87415_check_atapi_dma`:

ns87415_check_atapi_dma
=======================

.. c:function:: int ns87415_check_atapi_dma(struct ata_queued_cmd *qc)

    ATAPI DMA filter

    :param qc:
        Command block
    :type qc: struct ata_queued_cmd \*

.. _`ns87415_check_atapi_dma.description`:

Description
-----------

Disable ATAPI DMA (for now). We may be able to do DMA if we
kill the prefetching. This isn't clear.

.. _`ns87560_read_buggy`:

ns87560_read_buggy
==================

.. c:function:: u8 ns87560_read_buggy(void __iomem *port)

    workaround buggy Super I/O chip

    :param port:
        Port to read
    :type port: void __iomem \*

.. _`ns87560_read_buggy.description`:

Description
-----------

Work around chipset problems in the 87560 SuperIO chip

.. _`ns87560_check_status`:

ns87560_check_status
====================

.. c:function:: u8 ns87560_check_status(struct ata_port *ap)

    :param ap:
        channel to check
    :type ap: struct ata_port \*

.. _`ns87560_check_status.description`:

Description
-----------

Return the status of the channel working around the
87560 flaws.

.. _`ns87560_tf_read`:

ns87560_tf_read
===============

.. c:function:: void ns87560_tf_read(struct ata_port *ap, struct ata_taskfile *tf)

    input device's ATA taskfile shadow registers

    :param ap:
        Port from which input is read
    :type ap: struct ata_port \*

    :param tf:
        ATA taskfile register set for storing input
    :type tf: struct ata_taskfile \*

.. _`ns87560_tf_read.description`:

Description
-----------

Reads ATA taskfile registers for currently-selected device
into \ ``tf``\ . Work around the 87560 bugs.

.. _`ns87560_tf_read.locking`:

LOCKING
-------

Inherited from caller.

.. _`ns87560_bmdma_status`:

ns87560_bmdma_status
====================

.. c:function:: u8 ns87560_bmdma_status(struct ata_port *ap)

    :param ap:
        channel to check
    :type ap: struct ata_port \*

.. _`ns87560_bmdma_status.description`:

Description
-----------

Return the DMA status of the channel working around the
87560 flaws.

.. _`ns87415_init_one`:

ns87415_init_one
================

.. c:function:: int ns87415_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register 87415 ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in ns87415_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

.. _`ns87415_init_one.description`:

Description
-----------

Called from kernel PCI layer.  We probe for combined mode (sigh),
and then hand over control to libata, for it to do the rest.

.. _`ns87415_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`ns87415_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

