.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cypress.c

.. _`cy82c693_set_piomode`:

cy82c693_set_piomode
====================

.. c:function:: void cy82c693_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`cy82c693_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup.

.. _`cy82c693_set_dmamode`:

cy82c693_set_dmamode
====================

.. c:function:: void cy82c693_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`cy82c693_set_dmamode.description`:

Description
-----------

Called to do the DMA mode setup.

.. This file was automatic generated / don't edit.

