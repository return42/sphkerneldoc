.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_mpiix.c

.. _`mpiix_set_piomode`:

mpiix_set_piomode
=================

.. c:function:: void mpiix_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`mpiix_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. The MPIIX allows us to program the
IORDY sample point (2-5 clocks), recovery (1-4 clocks) and whether
prefetching or IORDY are used.

This would get very ugly because we can only program timing for one
device at a time, the other gets PIO0. Fortunately libata calls
our qc_issue command before a command is issued so we can flip the
timings back and forth to reduce the pain.

.. _`mpiix_qc_issue`:

mpiix_qc_issue
==============

.. c:function:: unsigned int mpiix_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`mpiix_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary. Our logic also clears TIME0/TIME1 for the other device so
that, even if we get this wrong, cycles to the other device will
be made PIO0.

.. This file was automatic generated / don't edit.

