.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_ns87410.c

.. _`ns87410_pre_reset`:

ns87410_pre_reset
=================

.. c:function:: int ns87410_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ns87410_pre_reset.description`:

Description
-----------

Check enabled ports

.. _`ns87410_set_piomode`:

ns87410_set_piomode
===================

.. c:function:: void ns87410_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`ns87410_set_piomode.description`:

Description
-----------

Program timing data. This is kept per channel not per device,
and only affects the data port.

.. _`ns87410_qc_issue`:

ns87410_qc_issue
================

.. c:function:: unsigned int ns87410_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`ns87410_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary.

.. This file was automatic generated / don't edit.

