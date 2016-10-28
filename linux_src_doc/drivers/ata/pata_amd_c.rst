.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_amd.c

.. _`timing_setup`:

timing_setup
============

.. c:function:: void timing_setup(struct ata_port *ap, struct ata_device *adev, int offset, int speed, int clock)

    shared timing computation and load

    :param struct ata_port \*ap:
        ATA port being set up

    :param struct ata_device \*adev:
        drive being configured

    :param int offset:
        port offset

    :param int speed:
        target speed

    :param int clock:
        clock multiplier (number of times 33MHz for this part)

.. _`timing_setup.description`:

Description
-----------

Perform the actual timing set up for Nvidia or AMD PATA devices.
The actual devices vary so they all call into this helper function
providing the clock multipler and offset (because AMD and Nvidia put
the ports at different locations).

.. _`amd_pre_reset`:

amd_pre_reset
=============

.. c:function:: int amd_pre_reset(struct ata_link *link, unsigned long deadline)

    perform reset handling

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`amd_pre_reset.description`:

Description
-----------

Reset sequence checking enable bits to see which ports are
active.

.. _`amd_cable_detect`:

amd_cable_detect
================

.. c:function:: int amd_cable_detect(struct ata_port *ap)

    report cable type

    :param struct ata_port \*ap:
        port

.. _`amd_cable_detect.description`:

Description
-----------

AMD controller/BIOS setups record the cable type in word 0x42

.. _`amd_fifo_setup`:

amd_fifo_setup
==============

.. c:function:: void amd_fifo_setup(struct ata_port *ap)

    set the PIO FIFO for ATA/ATAPI

    :param struct ata_port \*ap:
        ATA interface

.. _`amd_fifo_setup.description`:

Description
-----------

Set the PCI fifo for this device according to the devices present
on the bus at this point in time. We need to turn the post write buffer
off for ATAPI devices as we may need to issue a word sized write to the
device as the final I/O

.. _`amd33_set_piomode`:

amd33_set_piomode
=================

.. c:function:: void amd33_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`amd33_set_piomode.description`:

Description
-----------

Program the AMD registers for PIO mode.

.. _`amd33_set_dmamode`:

amd33_set_dmamode
=================

.. c:function:: void amd33_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`amd33_set_dmamode.description`:

Description
-----------

Program the MWDMA/UDMA modes for the AMD and Nvidia
chipset.

.. _`nv_pre_reset`:

nv_pre_reset
============

.. c:function:: int nv_pre_reset(struct ata_link *link, unsigned long deadline)

    cable detection

    :param struct ata_link \*link:
        *undescribed*

    :param unsigned long deadline:
        *undescribed*

.. _`nv_pre_reset.description`:

Description
-----------

Perform cable detection. The BIOS stores this in PCI config
space for us.

.. _`nv100_set_piomode`:

nv100_set_piomode
=================

.. c:function:: void nv100_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`nv100_set_piomode.description`:

Description
-----------

Program the AMD registers for PIO mode.

.. _`nv100_set_dmamode`:

nv100_set_dmamode
=================

.. c:function:: void nv100_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`nv100_set_dmamode.description`:

Description
-----------

Program the MWDMA/UDMA modes for the AMD and Nvidia
chipset.

.. This file was automatic generated / don't edit.

