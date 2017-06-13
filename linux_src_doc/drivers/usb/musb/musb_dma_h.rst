.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/musb/musb_dma.h

.. _`dma_channel`:

struct dma_channel
==================

.. c:type:: struct dma_channel

    A DMA channel.

.. _`dma_channel.definition`:

Definition
----------

.. code-block:: c

    struct dma_channel {
        void *private_data;
        size_t max_len;
        size_t actual_len;
        enum dma_channel_status status;
        bool desired_mode;
        bool rx_packet_done;
    }

.. _`dma_channel.members`:

Members
-------

private_data
    channel-private data

max_len
    the maximum number of bytes the channel can move in one
    transaction (typically representing many USB maximum-sized packets)

actual_len
    how many bytes have been transferred

status
    current channel status (updated e.g. on interrupt)

desired_mode
    true if mode 1 is desired; false if mode 0 is desired

rx_packet_done
    *undescribed*

.. _`dma_channel.description`:

Description
-----------

channels are associated with an endpoint for the duration of at least
one usb transfer.

.. _`dma_controller`:

struct dma_controller
=====================

.. c:type:: struct dma_controller

    A DMA Controller.

.. _`dma_controller.definition`:

Definition
----------

.. code-block:: c

    struct dma_controller {
        struct musb *musb;
        struct dma_channel *(*channel_alloc)(struct dma_controller *,struct musb_hw_ep *, u8 is_tx);
        void (*channel_release)(struct dma_channel *);
        int (*channel_program)(struct dma_channel *channel,u16 maxpacket, u8 mode,dma_addr_t dma_addr,u32 length);
        int (*channel_abort)(struct dma_channel *);
        int (*is_compatible)(struct dma_channel *channel,u16 maxpacket,void *buf, u32 length);
        void (*dma_callback)(struct dma_controller *);
    }

.. _`dma_controller.members`:

Members
-------

musb
    the usb controller

channel_alloc
    call this to allocate a DMA channel

channel_release
    call this to release a DMA channel

channel_program
    *undescribed*

channel_abort
    call this to abort a pending DMA transaction,
    returning it to FREE (but allocated) state

is_compatible
    *undescribed*

dma_callback
    invoked on DMA completion, useful to run platform
    code such IRQ acknowledgment.

.. _`dma_controller.description`:

Description
-----------

Controllers manage dma channels.

.. This file was automatic generated / don't edit.

