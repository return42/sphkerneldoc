.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_amd.c

.. _`timing_setup`:

timing_setup
============

.. c:function:: void timing_setup(struct ata_port *ap, struct ata_device *adev, int offset, int speed, int clock)

    shared timing computation and load

    :param ap:
        ATA port being set up
    :type ap: struct ata_port \*

    :param adev:
        drive being configured
    :type adev: struct ata_device \*

    :param offset:
        port offset
    :type offset: int

    :param speed:
        target speed
    :type speed: int

    :param clock:
        clock multiplier (number of times 33MHz for this part)
    :type clock: int

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

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

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

    :param ap:
        port
    :type ap: struct ata_port \*

.. _`amd_cable_detect.description`:

Description
-----------

AMD controller/BIOS setups record the cable type in word 0x42

.. _`amd_fifo_setup`:

amd_fifo_setup
==============

.. c:function:: void amd_fifo_setup(struct ata_port *ap)

    set the PIO FIFO for ATA/ATAPI

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

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

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`amd33_set_piomode.description`:

Description
-----------

Program the AMD registers for PIO mode.

.. _`amd33_set_dmamode`:

amd33_set_dmamode
=================

.. c:function:: void amd33_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

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

    :param link:
        *undescribed*
    :type link: struct ata_link \*

    :param deadline:
        *undescribed*
    :type deadline: unsigned long

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

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`nv100_set_piomode.description`:

Description
-----------

Program the AMD registers for PIO mode.

.. _`nv100_set_dmamode`:

nv100_set_dmamode
=================

.. c:function:: void nv100_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`nv100_set_dmamode.description`:

Description
-----------

Program the MWDMA/UDMA modes for the AMD and Nvidia
chipset.

.. This file was automatic generated / don't edit.

