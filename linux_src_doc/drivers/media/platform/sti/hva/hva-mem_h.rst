.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/sti/hva/hva-mem.h

.. _`hva_buffer`:

struct hva_buffer
=================

.. c:type:: struct hva_buffer

    hva buffer

.. _`hva_buffer.definition`:

Definition
----------

.. code-block:: c

    struct hva_buffer {
        const char *name;
        dma_addr_t paddr;
        void *vaddr;
        u32 size;
    }

.. _`hva_buffer.members`:

Members
-------

name
    name of requester

paddr
    physical address (for hardware)

vaddr
    virtual address (kernel can read/write)

size
    size of buffer

.. This file was automatic generated / don't edit.

