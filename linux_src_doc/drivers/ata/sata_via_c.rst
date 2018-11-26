.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/sata_via.c

.. _`svia_tf_load`:

svia_tf_load
============

.. c:function:: void svia_tf_load(struct ata_port *ap, const struct ata_taskfile *tf)

    send taskfile registers to host controller

    :param ap:
        Port to which output is sent
    :type ap: struct ata_port \*

    :param tf:
        ATA taskfile register set
    :type tf: const struct ata_taskfile \*

.. _`svia_tf_load.description`:

Description
-----------

Outputs ATA taskfile to standard ATA host controller.

This is to fix the internal bug of via chipsets, which will
reset the device register after changing the IEN bit on ctl
register.

.. _`vt6420_prereset`:

vt6420_prereset
===============

.. c:function:: int vt6420_prereset(struct ata_link *link, unsigned long deadline)

    prereset for vt6420

    :param link:
        target ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`vt6420_prereset.description`:

Description
-----------

SCR registers on vt6420 are pieces of shit and may hang the
whole machine completely if accessed with the wrong timing.
To avoid such catastrophe, vt6420 doesn't provide generic SCR
access operations, but uses SStatus and SControl only during
boot probing in controlled way.

As the old (pre EH update) probing code is proven to work, we
strictly follow the access pattern.

.. _`vt6420_prereset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`vt6420_prereset.return`:

Return
------

0 on success, -errno otherwise.

.. This file was automatic generated / don't edit.

