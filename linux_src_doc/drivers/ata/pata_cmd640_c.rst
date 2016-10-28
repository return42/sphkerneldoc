.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cmd640.c

.. _`cmd640_set_piomode`:

cmd640_set_piomode
==================

.. c:function:: void cmd640_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA port

    :param struct ata_device \*adev:
        ATA device

.. _`cmd640_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup.

.. _`cmd640_qc_issue`:

cmd640_qc_issue
===============

.. c:function:: unsigned int cmd640_qc_issue(struct ata_queued_cmd *qc)

    command preparation hook

    :param struct ata_queued_cmd \*qc:
        Command to be issued

.. _`cmd640_qc_issue.description`:

Description
-----------

Channel 1 has shared timings. We must reprogram the
clock each drive 2/3 switch we do.

.. _`cmd640_port_start`:

cmd640_port_start
=================

.. c:function:: int cmd640_port_start(struct ata_port *ap)

    port setup

    :param struct ata_port \*ap:
        ATA port being set up

.. _`cmd640_port_start.description`:

Description
-----------

The CMD640 needs to maintain private data structures so we
allocate space here.

.. This file was automatic generated / don't edit.

