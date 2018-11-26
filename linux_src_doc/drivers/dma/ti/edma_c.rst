.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ti/edma.c

.. _`edma_alloc_slot`:

edma_alloc_slot
===============

.. c:function:: int edma_alloc_slot(struct edma_cc *ecc, int slot)

    allocate DMA parameter RAM

    :param ecc:
        pointer to edma_cc struct
    :type ecc: struct edma_cc \*

    :param slot:
        specific slot to allocate; negative for "any unused slot"
    :type slot: int

.. _`edma_alloc_slot.description`:

Description
-----------

This allocates a parameter RAM slot, initializing it to hold a
dummy transfer.  Slots allocated using this routine have not been
mapped to a hardware DMA channel, and will normally be used by
linking to them from a slot associated with a DMA channel.

Normal use is to pass EDMA_SLOT_ANY as the \ ``slot``\ , but specific
slots may be allocated on behalf of DSP firmware.

Returns the number of the slot, else negative errno.

.. _`edma_link`:

edma_link
=========

.. c:function:: void edma_link(struct edma_cc *ecc, unsigned from, unsigned to)

    link one parameter RAM slot to another

    :param ecc:
        pointer to edma_cc struct
    :type ecc: struct edma_cc \*

    :param from:
        parameter RAM slot originating the link
    :type from: unsigned

    :param to:
        parameter RAM slot which is the link target
    :type to: unsigned

.. _`edma_link.description`:

Description
-----------

The originating slot should not be part of any active DMA transfer.

.. _`edma_get_position`:

edma_get_position
=================

.. c:function:: dma_addr_t edma_get_position(struct edma_cc *ecc, unsigned slot, bool dst)

    returns the current transfer point

    :param ecc:
        pointer to edma_cc struct
    :type ecc: struct edma_cc \*

    :param slot:
        parameter RAM slot being examined
    :type slot: unsigned

    :param dst:
        true selects the dest position, false the source
    :type dst: bool

.. _`edma_get_position.description`:

Description
-----------

Returns the position of the current active slot

.. This file was automatic generated / don't edit.

