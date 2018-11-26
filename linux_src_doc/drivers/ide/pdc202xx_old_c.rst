.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/pdc202xx_old.c

.. _`pdc202xx_init_one`:

pdc202xx_init_one
=================

.. c:function:: int pdc202xx_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a PDC202xx is found

    :param dev:
        the pdc202xx device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`pdc202xx_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. This file was automatic generated / don't edit.

