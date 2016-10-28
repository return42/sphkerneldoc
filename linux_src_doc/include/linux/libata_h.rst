.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/libata.h

.. _`ata_ncq_enabled`:

ata_ncq_enabled
===============

.. c:function:: int ata_ncq_enabled(struct ata_device *dev)

    Test whether NCQ is enabled

    :param struct ata_device \*dev:
        ATA device to test for

.. _`ata_ncq_enabled.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_ncq_enabled.return`:

Return
------

1 if NCQ is enabled for \ ``dev``\ , 0 otherwise.

.. _`ata_sff_busy_wait`:

ata_sff_busy_wait
=================

.. c:function:: u8 ata_sff_busy_wait(struct ata_port *ap, unsigned int bits, unsigned int max)

    Wait for a port status register

    :param struct ata_port \*ap:
        Port to wait for.

    :param unsigned int bits:
        bits that must be clear

    :param unsigned int max:
        number of 10uS waits to perform

.. _`ata_sff_busy_wait.description`:

Description
-----------

Waits up to max\*10 microseconds for the selected bits in the port's
status register to be cleared.
Returns final value of status register.

.. _`ata_sff_busy_wait.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_wait_idle`:

ata_wait_idle
=============

.. c:function:: u8 ata_wait_idle(struct ata_port *ap)

    Wait for a port to be idle.

    :param struct ata_port \*ap:
        Port to wait for.

.. _`ata_wait_idle.description`:

Description
-----------

Waits up to 10ms for port's BUSY and DRQ signals to clear.
Returns final value of status register.

.. _`ata_wait_idle.locking`:

LOCKING
-------

Inherited from caller.

.. This file was automatic generated / don't edit.

