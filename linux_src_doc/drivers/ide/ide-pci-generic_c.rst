.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-pci-generic.c

.. _`generic_init_one`:

generic_init_one
================

.. c:function:: int generic_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a PIIX is found

    :param dev:
        the generic device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`generic_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. This file was automatic generated / don't edit.

