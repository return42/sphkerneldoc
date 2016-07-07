.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/aec62xx.c

.. _`aec62xx_init_one`:

aec62xx_init_one
================

.. c:function:: int aec62xx_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a AEC is found

    :param struct pci_dev \*dev:
        the aec62xx device

    :param const struct pci_device_id \*id:
        the matching pci id

.. _`aec62xx_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. _`aec62xx_init_one.note`:

NOTE
----

since we're going to modify the 'name' field for AEC-6[26]80[R]
chips, pass a local copy of 'struct ide_port_info' down the call chain.

.. This file was automatic generated / don't edit.

