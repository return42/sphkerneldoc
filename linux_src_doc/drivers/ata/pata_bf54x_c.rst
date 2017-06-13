.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_bf54x.c

.. _`bfin_set_piomode`:

bfin_set_piomode
================

.. c:function:: void bfin_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        um

.. _`bfin_set_piomode.description`:

Description
-----------

Set PIO mode for device.

.. _`bfin_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`bfin_set_dmamode`:

bfin_set_dmamode
================

.. c:function:: void bfin_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        um

.. _`bfin_set_dmamode.description`:

Description
-----------

Set UDMA mode for device.

.. _`bfin_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`bfin_tf_load`:

bfin_tf_load
============

.. c:function:: void bfin_tf_load(struct ata_port *ap, const struct ata_taskfile *tf)

    send taskfile registers to host controller

    :param struct ata_port \*ap:
        Port to which output is sent

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set

.. _`bfin_tf_load.note`:

Note
----

Original code is \ :c:func:`ata_sff_tf_load`\ .

.. _`bfin_check_status`:

bfin_check_status
=================

.. c:function:: u8 bfin_check_status(struct ata_port *ap)

    Read device status reg & clear interrupt

    :param struct ata_port \*ap:
        port where the device is

.. _`bfin_check_status.note`:

Note
----

Original code is \ :c:func:`ata_check_status`\ .

.. _`bfin_tf_read`:

bfin_tf_read
============

.. c:function:: void bfin_tf_read(struct ata_port *ap, struct ata_taskfile *tf)

    input device's ATA taskfile shadow registers

    :param struct ata_port \*ap:
        Port from which input is read

    :param struct ata_taskfile \*tf:
        ATA taskfile register set for storing input

.. _`bfin_tf_read.note`:

Note
----

Original code is \ :c:func:`ata_sff_tf_read`\ .

.. _`bfin_exec_command`:

bfin_exec_command
=================

.. c:function:: void bfin_exec_command(struct ata_port *ap, const struct ata_taskfile *tf)

    issue ATA command to host controller

    :param struct ata_port \*ap:
        port to which command is being issued

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set

.. _`bfin_exec_command.note`:

Note
----

Original code is \ :c:func:`ata_sff_exec_command`\ .

.. _`bfin_check_altstatus`:

bfin_check_altstatus
====================

.. c:function:: u8 bfin_check_altstatus(struct ata_port *ap)

    Read device alternate status reg

    :param struct ata_port \*ap:
        port where the device is

.. _`bfin_dev_select`:

bfin_dev_select
===============

.. c:function:: void bfin_dev_select(struct ata_port *ap, unsigned int device)

    Select device 0/1 on ATA bus

    :param struct ata_port \*ap:
        ATA channel to manipulate

    :param unsigned int device:
        ATA device (numbered from zero) to select

.. _`bfin_dev_select.note`:

Note
----

Original code is \ :c:func:`ata_sff_dev_select`\ .

.. _`bfin_set_devctl`:

bfin_set_devctl
===============

.. c:function:: void bfin_set_devctl(struct ata_port *ap, u8 ctl)

    Write device control reg

    :param struct ata_port \*ap:
        port where the device is

    :param u8 ctl:
        value to write

.. _`bfin_bmdma_setup`:

bfin_bmdma_setup
================

.. c:function:: void bfin_bmdma_setup(struct ata_queued_cmd *qc)

    Set up IDE DMA transaction

    :param struct ata_queued_cmd \*qc:
        Info associated with this ATA transaction.

.. _`bfin_bmdma_setup.note`:

Note
----

Original code is \ :c:func:`ata_bmdma_setup`\ .

.. _`bfin_bmdma_start`:

bfin_bmdma_start
================

.. c:function:: void bfin_bmdma_start(struct ata_queued_cmd *qc)

    Start an IDE DMA transaction

    :param struct ata_queued_cmd \*qc:
        Info associated with this ATA transaction.

.. _`bfin_bmdma_start.note`:

Note
----

Original code is \ :c:func:`ata_bmdma_start`\ .

.. _`bfin_bmdma_stop`:

bfin_bmdma_stop
===============

.. c:function:: void bfin_bmdma_stop(struct ata_queued_cmd *qc)

    Stop IDE DMA transfer

    :param struct ata_queued_cmd \*qc:
        Command we are ending DMA for

.. _`bfin_devchk`:

bfin_devchk
===========

.. c:function:: unsigned int bfin_devchk(struct ata_port *ap, unsigned int device)

    PATA device presence detection

    :param struct ata_port \*ap:
        ATA channel to examine

    :param unsigned int device:
        Device to examine (starting at zero)

.. _`bfin_devchk.note`:

Note
----

Original code is \ :c:func:`ata_devchk`\ .

.. _`bfin_bus_post_reset`:

bfin_bus_post_reset
===================

.. c:function:: void bfin_bus_post_reset(struct ata_port *ap, unsigned int devmask)

    PATA device post reset

    :param struct ata_port \*ap:
        *undescribed*

    :param unsigned int devmask:
        *undescribed*

.. _`bfin_bus_post_reset.note`:

Note
----

Original code is \ :c:func:`ata_bus_post_reset`\ .

.. _`bfin_bus_softreset`:

bfin_bus_softreset
==================

.. c:function:: unsigned int bfin_bus_softreset(struct ata_port *ap, unsigned int devmask)

    PATA device software reset

    :param struct ata_port \*ap:
        *undescribed*

    :param unsigned int devmask:
        *undescribed*

.. _`bfin_bus_softreset.note`:

Note
----

Original code is \ :c:func:`ata_bus_softreset`\ .

.. _`bfin_softreset`:

bfin_softreset
==============

.. c:function:: int bfin_softreset(struct ata_link *link, unsigned int *classes, unsigned long deadline)

    reset host port via ATA SRST

    :param struct ata_link \*link:
        *undescribed*

    :param unsigned int \*classes:
        resulting classes of attached devices

    :param unsigned long deadline:
        *undescribed*

.. _`bfin_softreset.note`:

Note
----

Original code is \ :c:func:`ata_sff_softreset`\ .

.. _`bfin_bmdma_status`:

bfin_bmdma_status
=================

.. c:function:: unsigned char bfin_bmdma_status(struct ata_port *ap)

    Read IDE DMA status

    :param struct ata_port \*ap:
        Port associated with this ATA transaction.

.. _`bfin_data_xfer`:

bfin_data_xfer
==============

.. c:function:: unsigned int bfin_data_xfer(struct ata_queued_cmd *qc, unsigned char *buf, unsigned int buflen, int rw)

    Transfer data by PIO

    :param struct ata_queued_cmd \*qc:
        queued command

    :param unsigned char \*buf:
        data buffer

    :param unsigned int buflen:
        buffer length

    :param int rw:
        *undescribed*

.. _`bfin_data_xfer.note`:

Note
----

Original code is \ :c:func:`ata_sff_data_xfer`\ .

.. _`bfin_irq_clear`:

bfin_irq_clear
==============

.. c:function:: void bfin_irq_clear(struct ata_port *ap)

    Clear ATAPI interrupt.

    :param struct ata_port \*ap:
        Port associated with this ATA transaction.

.. _`bfin_irq_clear.note`:

Note
----

Original code is \ :c:func:`ata_bmdma_irq_clear`\ .

.. _`bfin_thaw`:

bfin_thaw
=========

.. c:function:: void bfin_thaw(struct ata_port *ap)

    Thaw DMA controller port

    :param struct ata_port \*ap:
        port to thaw

.. _`bfin_thaw.note`:

Note
----

Original code is \ :c:func:`ata_sff_thaw`\ .

.. _`bfin_postreset`:

bfin_postreset
==============

.. c:function:: void bfin_postreset(struct ata_link *link, unsigned int *classes)

    standard postreset callback

    :param struct ata_link \*link:
        *undescribed*

    :param unsigned int \*classes:
        classes of attached devices

.. _`bfin_postreset.note`:

Note
----

Original code is \ :c:func:`ata_sff_postreset`\ .

.. _`bfin_reset_controller`:

bfin_reset_controller
=====================

.. c:function:: int bfin_reset_controller(struct ata_host *host)

    initialize BF54x ATAPI controller.

    :param struct ata_host \*host:
        *undescribed*

.. _`bfin_atapi_probe`:

bfin_atapi_probe
================

.. c:function:: int bfin_atapi_probe(struct platform_device *pdev)

    attach a bfin atapi interface

    :param struct platform_device \*pdev:
        platform device

.. _`bfin_atapi_probe.description`:

Description
-----------

Register a bfin atapi interface.

.. _`bfin_atapi_probe.platform-devices-are-expected-to-contain-2-resources-per-port`:

Platform devices are expected to contain 2 resources per port
-------------------------------------------------------------


- I/O Base (IORESOURCE_IO)
- IRQ      (IORESOURCE_IRQ)

.. _`bfin_atapi_remove`:

bfin_atapi_remove
=================

.. c:function:: int bfin_atapi_remove(struct platform_device *pdev)

    unplug a bfin atapi interface

    :param struct platform_device \*pdev:
        platform device

.. _`bfin_atapi_remove.description`:

Description
-----------

A bfin atapi device has been unplugged. Perform the needed
cleanup. Also called on module unload for any active devices.

.. This file was automatic generated / don't edit.

