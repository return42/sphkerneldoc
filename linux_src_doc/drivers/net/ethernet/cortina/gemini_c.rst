.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cortina/gemini.c

.. _`gmac_queue_page`:

struct gmac_queue_page
======================

.. c:type:: struct gmac_queue_page

    page buffer per-page info

.. _`gmac_queue_page.definition`:

Definition
----------

.. code-block:: c

    struct gmac_queue_page {
        struct page *page;
        dma_addr_t mapping;
    }

.. _`gmac_queue_page.members`:

Members
-------

page
    *undescribed*

mapping
    *undescribed*

.. _`geth_fill_freeq`:

geth_fill_freeq
===============

.. c:function:: unsigned int geth_fill_freeq(struct gemini_ethernet *geth, bool refill)

    Fill the freeq with empty fragments to use

    :param geth:
        the ethernet adapter
    :type geth: struct gemini_ethernet \*

    :param refill:
        whether to reset the queue by filling in all freeq entries or
        just refill it, usually the interrupt to refill the queue happens when
        the queue is half empty.
    :type refill: bool

.. _`geth_cleanup_freeq`:

geth_cleanup_freeq
==================

.. c:function:: void geth_cleanup_freeq(struct gemini_ethernet *geth)

    cleanup the DMA mappings and free the queue

    :param geth:
        the Gemini global ethernet state
    :type geth: struct gemini_ethernet \*

.. _`geth_resize_freeq`:

geth_resize_freeq
=================

.. c:function:: int geth_resize_freeq(struct gemini_ethernet_port *port)

    resize the software queue depth

    :param port:
        the port requesting the change
    :type port: struct gemini_ethernet_port \*

.. _`geth_resize_freeq.description`:

Description
-----------

This gets called at least once during \ :c:func:`probe`\  so the device queue gets
"resized" from the hardware defaults. Since both ports/net devices share
the same hardware queue, some synchronization between the ports is
needed.

.. _`gmac_get_intr_flags`:

gmac_get_intr_flags
===================

.. c:function:: u32 gmac_get_intr_flags(struct net_device *netdev, int i)

    get interrupt status flags for a port from

    :param netdev:
        the net device for the port to get flags from
    :type netdev: struct net_device \*

    :param i:
        the interrupt status register 0..4
    :type i: int

.. This file was automatic generated / don't edit.

