.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/ahci_xgene.c

.. _`xgene_ahci_poll_reg_val`:

xgene_ahci_poll_reg_val
=======================

.. c:function:: int xgene_ahci_poll_reg_val(struct ata_port *ap, void __iomem *reg, unsigned int val, unsigned long interval, unsigned long timeout)

    Poll a register on a specific value.

    :param ap:
        ATA port of interest.
    :type ap: struct ata_port \*

    :param reg:
        Register of interest.
    :type reg: void __iomem \*

    :param val:
        Value to be attained.
    :type val: unsigned int

    :param interval:
        waiting interval for polling.
    :type interval: unsigned long

    :param timeout:
        timeout for achieving the value.
    :type timeout: unsigned long

.. _`xgene_ahci_restart_engine`:

xgene_ahci_restart_engine
=========================

.. c:function:: int xgene_ahci_restart_engine(struct ata_port *ap)

    Restart the dma engine.

    :param ap:
        ATA port of interest
    :type ap: struct ata_port \*

.. _`xgene_ahci_restart_engine.description`:

Description
-----------

Waits for completion of multiple commands and restarts
the DMA engine inside the controller.

.. _`xgene_ahci_qc_issue`:

xgene_ahci_qc_issue
===================

.. c:function:: unsigned int xgene_ahci_qc_issue(struct ata_queued_cmd *qc)

    Issue commands to the device

    :param qc:
        Command to issue
    :type qc: struct ata_queued_cmd \*

.. _`xgene_ahci_qc_issue.description`:

Description
-----------

Due to Hardware errata for IDENTIFY DEVICE command, the controller cannot
clear the BSY bit after receiving the PIO setup FIS. This results in the dma
state machine goes into the CMFatalErrorUpdate state and locks up. By
restarting the dma engine, it removes the controller out of lock up state.

Due to H/W errata, the controller is unable to save the PMP
field fetched from command header before sending the H2D FIS.
When the device returns the PMP port field in the D2H FIS, there is
a mismatch and results in command completion failure. The
workaround is to write the pmp value to PxFBS.DEV field before issuing
any command to PMP.

.. _`xgene_ahci_read_id`:

xgene_ahci_read_id
==================

.. c:function:: unsigned int xgene_ahci_read_id(struct ata_device *dev, struct ata_taskfile *tf, u16 *id)

    Read ID data from the specified device

    :param dev:
        device
    :type dev: struct ata_device \*

    :param tf:
        proposed taskfile
    :type tf: struct ata_taskfile \*

    :param id:
        data buffer
    :type id: u16 \*

.. _`xgene_ahci_read_id.description`:

Description
-----------

This custom read ID function is required due to the fact that the HW
does not support DEVSLP.

.. _`xgene_ahci_do_hardreset`:

xgene_ahci_do_hardreset
=======================

.. c:function:: int xgene_ahci_do_hardreset(struct ata_link *link, unsigned long deadline, bool *online)

    Issue the actual COMRESET

    :param link:
        link to reset
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

    :param online:
        Return value to indicate if device online
    :type online: bool \*

.. _`xgene_ahci_do_hardreset.description`:

Description
-----------

Due to the limitation of the hardware PHY, a difference set of setting is
required for each supported disk speed - Gen3 (6.0Gbps), Gen2 (3.0Gbps),
and Gen1 (1.5Gbps). Otherwise during long IO stress test, the PHY will
report disparity error and etc. In addition, during COMRESET, there can
be error reported in the register PORT_SCR_ERR. For SERR_DISPARITY and
SERR_10B_8B_ERR, the PHY receiver line must be reseted. Also during long
reboot cycle regression, sometimes the PHY reports link down even if the
device is present because of speed negotiation failure. so need to retry
the COMRESET to get the link up. The following algorithm is followed to

.. _`xgene_ahci_do_hardreset.alg-part-1`:

Alg Part 1
----------


1. Start the PHY at Gen3 speed (default setting)
2. Issue the COMRESET
3. If no link, go to Alg Part 3
4. If link up, determine if the negotiated speed matches the PHY
configured speed
5. If they matched, go to Alg Part 2
6. If they do not matched and first time, configure the PHY for the linked
up disk speed and repeat step 2
7. Go to Alg Part 2

.. _`xgene_ahci_do_hardreset.alg-part-2`:

Alg Part 2
----------

1. On link up, if there are any SERR_DISPARITY and SERR_10B_8B_ERR error
reported in the register PORT_SCR_ERR, then reset the PHY receiver line
2. Go to Alg Part 4

.. _`xgene_ahci_do_hardreset.alg-part-3`:

Alg Part 3
----------

1. Check the PORT_SCR_STAT to see whether device presence detected but PHY
communication establishment failed and maximum link down attempts are
less than Max attempts 3 then goto Alg Part 1.
2. Go to Alg Part 4.

.. _`xgene_ahci_do_hardreset.alg-part-4`:

Alg Part 4
----------

1. Clear any pending from register PORT_SCR_ERR.

.. _`xgene_ahci_do_hardreset.note`:

NOTE
----

For the initial version, we will NOT support Gen1/Gen2. In addition
and until the underlying PHY supports an method to reset the receiver
line, on detection of SERR_DISPARITY or SERR_10B_8B_ERR errors,
an warning message will be printed.

.. _`xgene_ahci_pmp_softreset`:

xgene_ahci_pmp_softreset
========================

.. c:function:: int xgene_ahci_pmp_softreset(struct ata_link *link, unsigned int *class, unsigned long deadline)

    Issue the softreset to the drives connected to Port Multiplier.

    :param link:
        link to reset
    :type link: struct ata_link \*

    :param class:
        Return value to indicate class of device
    :type class: unsigned int \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`xgene_ahci_pmp_softreset.description`:

Description
-----------

Due to H/W errata, the controller is unable to save the PMP
field fetched from command header before sending the H2D FIS.
When the device returns the PMP port field in the D2H FIS, there is
a mismatch and results in command completion failure. The workaround
is to write the pmp value to PxFBS.DEV field before issuing any command
to PMP.

.. _`xgene_ahci_softreset`:

xgene_ahci_softreset
====================

.. c:function:: int xgene_ahci_softreset(struct ata_link *link, unsigned int *class, unsigned long deadline)

    Issue the softreset to the drive.

    :param link:
        link to reset
    :type link: struct ata_link \*

    :param class:
        Return value to indicate class of device
    :type class: unsigned int \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`xgene_ahci_softreset.description`:

Description
-----------

Due to H/W errata, the controller is unable to save the PMP
field fetched from command header before sending the H2D FIS.
When the device returns the PMP port field in the D2H FIS, there is
a mismatch and results in command completion failure. The workaround
is to write the pmp value to PxFBS.DEV field before issuing any command
to PMP. Here is the algorithm to detect PMP :

1. Save the PxFBS value
2. Program PxFBS.DEV with pmp value send by framework. Framework sends
0xF for both PMP/NON-PMP initially
3. Issue softreset
4. If signature class is PMP goto 6
5. restore the original PxFBS and goto 3
6. return

.. _`xgene_ahci_handle_broken_edge_irq`:

xgene_ahci_handle_broken_edge_irq
=================================

.. c:function:: int xgene_ahci_handle_broken_edge_irq(struct ata_host *host, u32 irq_masked)

    Handle the broken irq.

    :param host:
        *undescribed*
    :type host: struct ata_host \*

    :param irq_masked:
        HOST_IRQ_STAT value
    :type irq_masked: u32

.. _`xgene_ahci_handle_broken_edge_irq.description`:

Description
-----------

For hardware with broken edge trigger latch
the HOST_IRQ_STAT register misses the edge interrupt
when clearing of HOST_IRQ_STAT register and hardware
reporting the PORT_IRQ_STAT register at the
same clock cycle.
As such, the algorithm below outlines the workaround.

1. Read HOST_IRQ_STAT register and save the state.
2. Clear the HOST_IRQ_STAT register.
3. Read back the HOST_IRQ_STAT register.
4. If HOST_IRQ_STAT register equals to zero, then
traverse the rest of port's PORT_IRQ_STAT register
to check if an interrupt is triggered at that point else
go to step 6.
5. If PORT_IRQ_STAT register of rest ports is not equal to zero
then update the state of HOST_IRQ_STAT saved in step 1.
6. Handle port interrupts.
7. Exit

.. This file was automatic generated / don't edit.

