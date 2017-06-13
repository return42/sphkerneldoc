.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/host/pci-ftpci100.c

.. _`faraday_pci_variant`:

struct faraday_pci_variant
==========================

.. c:type:: struct faraday_pci_variant

    encodes IP block differences

.. _`faraday_pci_variant.definition`:

Definition
----------

.. code-block:: c

    struct faraday_pci_variant {
        bool cascaded_irq;
    }

.. _`faraday_pci_variant.members`:

Members
-------

cascaded_irq
    this host has cascaded IRQs from an interrupt controller
    embedded in the host bridge.

.. This file was automatic generated / don't edit.

