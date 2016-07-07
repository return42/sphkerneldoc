.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/sata_mv.c

.. _`mv_save_cached_regs`:

mv_save_cached_regs
===================

.. c:function:: void mv_save_cached_regs(struct ata_port *ap)

    (re-)initialize cached port registers

    :param struct ata_port \*ap:
        the port whose registers we are caching

.. _`mv_save_cached_regs.description`:

Description
-----------

Initialize the local cache of port registers,
so that reading them over and over again can
be avoided on the hotter paths of this driver.
This saves a few microseconds each time we switch
to/from EDMA mode to perform (eg.) a drive cache flush.

.. _`mv_write_cached_reg`:

mv_write_cached_reg
===================

.. c:function:: void mv_write_cached_reg(void __iomem *addr, u32 *old, u32 new)

    write to a cached port register

    :param void __iomem \*addr:
        hardware address of the register

    :param u32 \*old:
        pointer to cached value of the register

    :param u32 new:
        new value for the register

.. _`mv_write_cached_reg.description`:

Description
-----------

Write a new value to a cached register,
but only if the value is different from before.

.. _`mv_start_edma`:

mv_start_edma
=============

.. c:function:: void mv_start_edma(struct ata_port *ap, void __iomem *port_mmio, struct mv_port_priv *pp, u8 protocol)

    Enable eDMA engine

    :param struct ata_port \*ap:
        *undescribed*

    :param void __iomem \*port_mmio:
        *undescribed*

    :param struct mv_port_priv \*pp:
        port private data

    :param u8 protocol:
        *undescribed*

.. _`mv_start_edma.description`:

Description
-----------

Verify the local cache of the eDMA state is accurate with a
WARN_ON.

.. _`mv_start_edma.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_stop_edma_engine`:

mv_stop_edma_engine
===================

.. c:function:: int mv_stop_edma_engine(void __iomem *port_mmio)

    Disable eDMA engine

    :param void __iomem \*port_mmio:
        io base address

.. _`mv_stop_edma_engine.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_bmdma_enable_iie`:

mv_bmdma_enable_iie
===================

.. c:function:: void mv_bmdma_enable_iie(struct ata_port *ap, int enable_bmdma)

    set a magic bit on GEN_IIE to allow bmdma

    :param struct ata_port \*ap:
        Port being initialized

    :param int enable_bmdma:
        *undescribed*

.. _`mv_bmdma_enable_iie.there-are-two-dma-modes-on-these-chips`:

There are two DMA modes on these chips
--------------------------------------

basic DMA, and EDMA.

Bit-0 of the "EDMA RESERVED" register enables/disables use
of basic DMA on the GEN_IIE versions of the chips.

This bit survives EDMA resets, and must be set for basic DMA
to function, and should be cleared when EDMA is active.

.. _`mv_port_start`:

mv_port_start
=============

.. c:function:: int mv_port_start(struct ata_port *ap)

    Port specific init/start routine.

    :param struct ata_port \*ap:
        ATA channel to manipulate

.. _`mv_port_start.description`:

Description
-----------

Allocate and point to DMA memory, init port private memory,
zero indices.

.. _`mv_port_start.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_port_stop`:

mv_port_stop
============

.. c:function:: void mv_port_stop(struct ata_port *ap)

    Port specific cleanup/stop routine.

    :param struct ata_port \*ap:
        ATA channel to manipulate

.. _`mv_port_stop.description`:

Description
-----------

Stop DMA, cleanup port memory.

.. _`mv_port_stop.locking`:

LOCKING
-------

This routine uses the host lock to protect the DMA stop.

.. _`mv_fill_sg`:

mv_fill_sg
==========

.. c:function:: void mv_fill_sg(struct ata_queued_cmd *qc)

    Fill out the Marvell ePRD (scatter gather) entries

    :param struct ata_queued_cmd \*qc:
        queued command whose SG list to source from

.. _`mv_fill_sg.description`:

Description
-----------

Populate the SG list and mark the last entry.

.. _`mv_fill_sg.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_sff_irq_clear`:

mv_sff_irq_clear
================

.. c:function:: void mv_sff_irq_clear(struct ata_port *ap)

    Clear hardware interrupt after DMA.

    :param struct ata_port \*ap:
        Port associated with this ATA transaction.

.. _`mv_sff_irq_clear.description`:

Description
-----------

We need this only for ATAPI bmdma transactions,
as otherwise we experience spurious interrupts
after libata-sff handles the bmdma interrupts.

.. _`mv_check_atapi_dma`:

mv_check_atapi_dma
==================

.. c:function:: int mv_check_atapi_dma(struct ata_queued_cmd *qc)

    Filter ATAPI cmds which are unsuitable for DMA.

    :param struct ata_queued_cmd \*qc:
        queued command to check for chipset/DMA compatibility.

.. _`mv_check_atapi_dma.description`:

Description
-----------

The bmdma engines cannot handle speculative data sizes
(bytecount under/over flow).  So only allow DMA for
data transfer commands with known data sizes.

.. _`mv_check_atapi_dma.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_bmdma_setup`:

mv_bmdma_setup
==============

.. c:function:: void mv_bmdma_setup(struct ata_queued_cmd *qc)

    Set up BMDMA transaction

    :param struct ata_queued_cmd \*qc:
        queued command to prepare DMA for.

.. _`mv_bmdma_setup.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_bmdma_start`:

mv_bmdma_start
==============

.. c:function:: void mv_bmdma_start(struct ata_queued_cmd *qc)

    Start a BMDMA transaction

    :param struct ata_queued_cmd \*qc:
        queued command to start DMA on.

.. _`mv_bmdma_start.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_bmdma_stop_ap`:

mv_bmdma_stop_ap
================

.. c:function:: void mv_bmdma_stop_ap(struct ata_port *ap)

    Stop BMDMA transfer

    :param struct ata_port \*ap:
        *undescribed*

.. _`mv_bmdma_stop_ap.description`:

Description
-----------

Clears the ATA_DMA_START flag in the bmdma control register

.. _`mv_bmdma_stop_ap.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_bmdma_status`:

mv_bmdma_status
===============

.. c:function:: u8 mv_bmdma_status(struct ata_port *ap)

    Read BMDMA status

    :param struct ata_port \*ap:
        port for which to retrieve DMA status.

.. _`mv_bmdma_status.description`:

Description
-----------

Read and return equivalent of the sff BMDMA status register.

.. _`mv_bmdma_status.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_qc_prep`:

mv_qc_prep
==========

.. c:function:: void mv_qc_prep(struct ata_queued_cmd *qc)

    Host specific command preparation.

    :param struct ata_queued_cmd \*qc:
        queued command to prepare

.. _`mv_qc_prep.description`:

Description
-----------

This routine simply redirects to the general purpose routine
if command is not DMA.  Else, it handles prep of the CRQB
(command request block), does some sanity checking, and calls
the SG load routine.

.. _`mv_qc_prep.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_qc_prep_iie`:

mv_qc_prep_iie
==============

.. c:function:: void mv_qc_prep_iie(struct ata_queued_cmd *qc)

    Host specific command preparation.

    :param struct ata_queued_cmd \*qc:
        queued command to prepare

.. _`mv_qc_prep_iie.description`:

Description
-----------

This routine simply redirects to the general purpose routine
if command is not DMA.  Else, it handles prep of the CRQB
(command request block), does some sanity checking, and calls
the SG load routine.

.. _`mv_qc_prep_iie.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_sff_check_status`:

mv_sff_check_status
===================

.. c:function:: u8 mv_sff_check_status(struct ata_port *ap)

    fetch device status, if valid

    :param struct ata_port \*ap:
        ATA port to fetch status from

.. _`mv_sff_check_status.description`:

Description
-----------

When using command issue via \ :c:func:`mv_qc_issue_fis`\ ,
the initial ATA_BUSY state does not show up in the
ATA status (shadow) register.  This can confuse libata!

So we have a hook here to fake ATA_BUSY for that situation,
until the first time a BUSY, DRQ, or ERR bit is seen.

The rest of the time, it simply returns the ATA status register.

.. _`mv_send_fis`:

mv_send_fis
===========

.. c:function:: unsigned int mv_send_fis(struct ata_port *ap, u32 *fis, int nwords)

    Send a FIS, using the "Vendor-Unique FIS" register

    :param struct ata_port \*ap:
        *undescribed*

    :param u32 \*fis:
        fis to be sent

    :param int nwords:
        number of 32-bit words in the fis

.. _`mv_qc_issue_fis`:

mv_qc_issue_fis
===============

.. c:function:: unsigned int mv_qc_issue_fis(struct ata_queued_cmd *qc)

    Issue a command directly as a FIS

    :param struct ata_queued_cmd \*qc:
        queued command to start

.. _`mv_qc_issue_fis.description`:

Description
-----------

Note that the ATA shadow registers are not updated
after command issue, so the device will appear "READY"
if polled, even while it is BUSY processing the command.

So we use a status hook to fake ATA_BUSY until the drive changes state.

.. _`mv_qc_issue_fis.note`:

Note
----

we don't get updated shadow regs on \*completion\*
of non-data commands. So avoid sending them via this function,
as they will appear to have completed immediately.

GEN_IIE has special registers that we could get the result tf from,
but earlier chipsets do not.  For now, we ignore those registers.

.. _`mv_qc_issue`:

mv_qc_issue
===========

.. c:function:: unsigned int mv_qc_issue(struct ata_queued_cmd *qc)

    Initiate a command to the host

    :param struct ata_queued_cmd \*qc:
        queued command to start

.. _`mv_qc_issue.description`:

Description
-----------

This routine simply redirects to the general purpose routine
if command is not DMA.  Else, it sanity checks our local
caches of the request producer/consumer indices then enables
DMA and bumps the request producer index.

.. _`mv_qc_issue.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_err_intr`:

mv_err_intr
===========

.. c:function:: void mv_err_intr(struct ata_port *ap)

    Handle error interrupts on the port

    :param struct ata_port \*ap:
        ATA channel to manipulate

.. _`mv_err_intr.description`:

Description
-----------

Most cases require a full reset of the chip's state machine,
which also performs a COMRESET.
Also, if the port disabled DMA, update our cached copy to match.

.. _`mv_err_intr.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_host_intr`:

mv_host_intr
============

.. c:function:: int mv_host_intr(struct ata_host *host, u32 main_irq_cause)

    Handle all interrupts on the given host controller

    :param struct ata_host \*host:
        host specific structure

    :param u32 main_irq_cause:
        Main interrupt cause register for the chip.

.. _`mv_host_intr.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_interrupt`:

mv_interrupt
============

.. c:function:: irqreturn_t mv_interrupt(int irq, void *dev_instance)

    Main interrupt event handler

    :param int irq:
        unused

    :param void \*dev_instance:
        private data; in this case the host structure

.. _`mv_interrupt.description`:

Description
-----------

Read the read only register to determine if any host
controllers have pending interrupts.  If so, call lower level
routine to handle.  Also check for PCI errors which are only
reported here.

.. _`mv_interrupt.locking`:

LOCKING
-------

This routine holds the host lock while processing pending
interrupts.

.. _`mv6_reset_hc`:

mv6_reset_hc
============

.. c:function:: int mv6_reset_hc(struct mv_host_priv *hpriv, void __iomem *mmio, unsigned int n_hc)

    Perform the 6xxx global soft reset

    :param struct mv_host_priv \*hpriv:
        *undescribed*

    :param void __iomem \*mmio:
        base address of the HBA

    :param unsigned int n_hc:
        *undescribed*

.. _`mv6_reset_hc.description`:

Description
-----------

This routine only applies to 6xxx parts.

.. _`mv6_reset_hc.locking`:

LOCKING
-------

Inherited from caller.

.. _`soc_is_65n`:

soc_is_65n
==========

.. c:function:: bool soc_is_65n(struct mv_host_priv *hpriv)

    check if the soc is 65 nano device

    :param struct mv_host_priv \*hpriv:
        *undescribed*

.. _`soc_is_65n.description`:

Description
-----------

Detect the type of the SoC, this is done by reading the PHYCFG_OFS
register, this register should contain non-zero value and it exists only
in the 65 nano devices, when reading it from older devices we get 0.

.. _`mv_port_init`:

mv_port_init
============

.. c:function:: void mv_port_init(struct ata_ioports *port, void __iomem *port_mmio)

    Perform some early initialization on a single port.

    :param struct ata_ioports \*port:
        libata data structure storing shadow register addresses

    :param void __iomem \*port_mmio:
        base address of the port

.. _`mv_port_init.description`:

Description
-----------

Initialize shadow register mmio addresses, clear outstanding
interrupts on the port, and unmask interrupts for the future
start of the port.

.. _`mv_port_init.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_init_host`:

mv_init_host
============

.. c:function:: int mv_init_host(struct ata_host *host)

    Perform some early initialization of the host.

    :param struct ata_host \*host:
        ATA host to initialize

.. _`mv_init_host.description`:

Description
-----------

If possible, do an early global reset of the host.  Then do
our port init and clear/unmask all/relevant host interrupts.

.. _`mv_init_host.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_platform_probe`:

mv_platform_probe
=================

.. c:function:: int mv_platform_probe(struct platform_device *pdev)

    handle a positive probe of an soc Marvell host

    :param struct platform_device \*pdev:
        platform device found

.. _`mv_platform_probe.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_print_info`:

mv_print_info
=============

.. c:function:: void mv_print_info(struct ata_host *host)

    Dump key info to kernel log for perusal.

    :param struct ata_host \*host:
        ATA host to print info about

.. _`mv_print_info.fixme`:

FIXME
-----

complete this.

.. _`mv_print_info.locking`:

LOCKING
-------

Inherited from caller.

.. _`mv_pci_init_one`:

mv_pci_init_one
===============

.. c:function:: int mv_pci_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    handle a positive probe of a PCI Marvell host

    :param struct pci_dev \*pdev:
        PCI device found

    :param const struct pci_device_id \*ent:
        PCI device ID entry for the matched host

.. _`mv_pci_init_one.locking`:

LOCKING
-------

Inherited from caller.

.. This file was automatic generated / don't edit.

