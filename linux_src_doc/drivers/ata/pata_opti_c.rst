.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_opti.c

.. _`opti_pre_reset`:

opti_pre_reset
==============

.. c:function:: int opti_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`opti_pre_reset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`opti_write_reg`:

opti_write_reg
==============

.. c:function:: void opti_write_reg(struct ata_port *ap, u8 val, int reg)

    control register setup

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param val:
        *undescribed*
    :type val: u8

    :param reg:
        control register number
    :type reg: int

.. _`opti_write_reg.description`:

Description
-----------

The Opti uses magic 'trapdoor' register accesses to do configuration
rather than using PCI space as other controllers do. The double inw
on the error register activates configuration mode. We can then write
the control register

.. _`opti_set_piomode`:

opti_set_piomode
================

.. c:function:: void opti_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`opti_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Timing numbers are taken from
the FreeBSD driver then pre computed to keep the code clean. There
are two tables depending on the hardware clock speed.

.. This file was automatic generated / don't edit.

