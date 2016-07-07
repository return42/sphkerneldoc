.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_legacy.c

.. _`legacy_probe_add`:

legacy_probe_add
================

.. c:function:: int legacy_probe_add(unsigned long port, unsigned int irq, enum controller type, unsigned long private)

    Add interface to probe list

    :param unsigned long port:
        Controller port

    :param unsigned int irq:
        IRQ number

    :param enum controller type:
        Controller type

    :param unsigned long private:
        Controller specific info

.. _`legacy_probe_add.description`:

Description
-----------

Add an entry into the probe list for ATA controllers. This is used
to add the default ISA slots and then to build up the table
further according to other ISA/VLB/Weird device scans

An I/O port list is used to keep ordering stable and sane, as we
don't have any good way to talk about ordering otherwise

.. _`legacy_set_mode`:

legacy_set_mode
===============

.. c:function:: int legacy_set_mode(struct ata_link *link, struct ata_device **unused)

    mode setting

    :param struct ata_link \*link:
        IDE link

    :param struct ata_device \*\*unused:
        Device that failed when error is returned

.. _`legacy_set_mode.description`:

Description
-----------

Use a non standard set_mode function. We don't want to be tuned.

The BIOS configured everything. Our job is not to fiddle. Just use
whatever PIO the hardware is using and leave it at that. When we
get some kind of nice user driven API for control then we can
expand on this as per hdparm in the base kernel.

.. _`opti_syscfg`:

opti_syscfg
===========

.. c:function:: u8 opti_syscfg(u8 reg)

    read OPTI chipset configuration

    :param u8 reg:
        Configuration register to read

.. _`opti_syscfg.description`:

Description
-----------

Returns the value of an OPTI system board configuration register.

.. _`opti82c46x_qc_issue`:

opti82c46x_qc_issue
===================

.. c:function:: unsigned int opti82c46x_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`opti82c46x_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings. The
MVB has a single set of timing registers and these are shared
across channels. As there are two registers we really ought to
track the last two used values as a sort of register window. For
now we just reload on a channel switch. On the single channel
setup this condition never fires so we do nothing extra.

.. _`opti82c46x_qc_issue.fixme`:

FIXME
-----

dual channel needs ->serialize support

.. _`qdi65x0_set_piomode`:

qdi65x0_set_piomode
===================

.. c:function:: void qdi65x0_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup for QDI65x0

    :param struct ata_port \*ap:
        Port

    :param struct ata_device \*adev:
        Device

.. _`qdi65x0_set_piomode.description`:

Description
-----------

In single channel mode the 6580 has one clock per device and we can
avoid the requirement to clock switch. We also have to load the timing
into the right clock according to whether we are master or slave.

In dual channel mode the 6580 has one clock per channel and we have
to software clockswitch in qc_issue.

.. _`qdi_qc_issue`:

qdi_qc_issue
============

.. c:function:: unsigned int qdi_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`qdi_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings.

.. _`probe_chip_type`:

probe_chip_type
===============

.. c:function:: int probe_chip_type(struct legacy_probe *probe)

    Discover controller

    :param struct legacy_probe \*probe:
        Probe entry to check

.. _`probe_chip_type.description`:

Description
-----------

Probe an ATA port and identify the type of controller. We don't
check if the controller appears to be driveless at this point.

.. _`legacy_init_one`:

legacy_init_one
===============

.. c:function:: int legacy_init_one(struct legacy_probe *probe)

    attach a legacy interface

    :param struct legacy_probe \*probe:
        *undescribed*

.. _`legacy_init_one.description`:

Description
-----------

Register an ISA bus IDE interface. Such interfaces are PIO and we
assume do not support IRQ sharing.

.. _`legacy_check_special_cases`:

legacy_check_special_cases
==========================

.. c:function:: void legacy_check_special_cases(struct pci_dev *p, int *primary, int *secondary)

    ATA special cases

    :param struct pci_dev \*p:
        PCI device to check

    :param int \*primary:
        *undescribed*

    :param int \*secondary:
        *undescribed*

.. _`legacy_check_special_cases.description`:

Description
-----------

A small number of vendors implemented early PCI ATA interfaces
on bridge logic without the ATA interface being PCI visible.
Where we have a matching PCI driver we must skip the relevant
device here. If we don't know about it then the legacy driver
is the right driver anyway.

.. _`legacy_init`:

legacy_init
===========

.. c:function:: int legacy_init( void)

    attach legacy interfaces

    :param  void:
        no arguments

.. _`legacy_init.description`:

Description
-----------

Attach legacy IDE interfaces by scanning the usual IRQ/port suspects.
Right now we do not scan the ide0 and ide1 address but should do so
for non PCI systems or systems with no PCI IDE legacy mode devices.
If you fix that note there are special cases to consider like VLB
drivers and CS5510/20.

.. This file was automatic generated / don't edit.

