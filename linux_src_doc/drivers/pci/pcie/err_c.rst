.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/err.c

.. _`default_reset_link`:

default_reset_link
==================

.. c:function:: pci_ers_result_t default_reset_link(struct pci_dev *dev)

    default reset function

    :param dev:
        pointer to pci_dev data structure
    :type dev: struct pci_dev \*

.. _`default_reset_link.description`:

Description
-----------

Invoked when performing link reset on a Downstream Port or a
Root Port with no aer driver.

.. This file was automatic generated / don't edit.

