.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/acpi_dma.h

.. _`acpi_dma_spec`:

struct acpi_dma_spec
====================

.. c:type:: struct acpi_dma_spec

    slave device DMA resources

.. _`acpi_dma_spec.definition`:

Definition
----------

.. code-block:: c

    struct acpi_dma_spec {
        int chan_id;
        int slave_id;
        struct device *dev;
    }

.. _`acpi_dma_spec.members`:

Members
-------

chan_id
    channel unique id

slave_id
    request line unique id

dev
    struct device of the DMA controller to be used in the filter
    function

.. _`acpi_dma`:

struct acpi_dma
===============

.. c:type:: struct acpi_dma

    representation of the registered DMAC

.. _`acpi_dma.definition`:

Definition
----------

.. code-block:: c

    struct acpi_dma {
        struct list_head dma_controllers;
        struct device *dev;
        struct dma_chan *(*acpi_dma_xlate)(struct acpi_dma_spec *, struct acpi_dma *);
        void *data;
        unsigned short base_request_line;
        unsigned short end_request_line;
    }

.. _`acpi_dma.members`:

Members
-------

dma_controllers
    linked list node

dev
    struct device of this controller

acpi_dma_xlate
    callback function to find a suitable channel

data
    private data used by a callback function

base_request_line
    first supported request line (CSRT)

end_request_line
    last supported request line (CSRT)

.. This file was automatic generated / don't edit.

