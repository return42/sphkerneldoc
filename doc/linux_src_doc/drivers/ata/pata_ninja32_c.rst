.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_ninja32.c

.. _`ninja32_set_piomode`:

ninja32_set_piomode
===================

.. c:function:: void ninja32_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`ninja32_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Our timing registers are shared
but we want to set the PIO timing by default.

.. This file was automatic generated / don't edit.

