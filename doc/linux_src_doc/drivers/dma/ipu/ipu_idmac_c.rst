.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ipu/ipu_idmac.c

.. _`ipu_enable_channel`:

ipu_enable_channel
==================

.. c:function:: int ipu_enable_channel(struct idmac *idmac, struct idmac_channel *ichan)

    enable an IPU channel.

    :param struct idmac \*idmac:
        IPU DMAC context.

    :param struct idmac_channel \*ichan:
        IDMAC channel.

.. _`ipu_init_channel_buffer`:

ipu_init_channel_buffer
=======================

.. c:function:: int ipu_init_channel_buffer(struct idmac_channel *ichan, enum pixel_fmt pixel_fmt, uint16_t width, uint16_t height, uint32_t stride, enum ipu_rotate_mode rot_mode, dma_addr_t phyaddr_0, dma_addr_t phyaddr_1)

    initialize a buffer for logical IPU channel.

    :param struct idmac_channel \*ichan:
        IDMAC channel.

    :param enum pixel_fmt pixel_fmt:
        pixel format of buffer. Pixel format is a FOURCC ASCII code.

    :param uint16_t width:
        width of buffer in pixels.

    :param uint16_t height:
        height of buffer in pixels.

    :param uint32_t stride:
        stride length of buffer in pixels.

    :param enum ipu_rotate_mode rot_mode:
        rotation mode of buffer. A rotation setting other than
        IPU_ROTATE_VERT_FLIP should only be used for input buffers of
        rotation channels.

    :param dma_addr_t phyaddr_0:
        buffer 0 physical address.

    :param dma_addr_t phyaddr_1:
        buffer 1 physical address. Setting this to a value other than
        NULL enables double buffering mode.

.. _`ipu_select_buffer`:

ipu_select_buffer
=================

.. c:function:: void ipu_select_buffer(enum ipu_channel channel, int buffer_n)

    mark a channel's buffer as ready.

    :param enum ipu_channel channel:
        channel ID.

    :param int buffer_n:
        buffer number to mark ready.

.. _`ipu_update_channel_buffer`:

ipu_update_channel_buffer
=========================

.. c:function:: void ipu_update_channel_buffer(struct idmac_channel *ichan, int buffer_n, dma_addr_t phyaddr)

    update physical address of a channel buffer.

    :param struct idmac_channel \*ichan:
        IDMAC channel.

    :param int buffer_n:
        buffer number to update.
        0 or 1 are the only valid values.

    :param dma_addr_t phyaddr:
        buffer physical address.

.. _`ipu_init_channel`:

ipu_init_channel
================

.. c:function:: int ipu_init_channel(struct idmac *idmac, struct idmac_channel *ichan)

    initialize an IPU channel.

    :param struct idmac \*idmac:
        IPU DMAC context.

    :param struct idmac_channel \*ichan:
        pointer to the channel object.
        \ ``return``\       0 on success or negative error code on failure.

.. _`ipu_uninit_channel`:

ipu_uninit_channel
==================

.. c:function:: void ipu_uninit_channel(struct idmac *idmac, struct idmac_channel *ichan)

    uninitialize an IPU channel.

    :param struct idmac \*idmac:
        IPU DMAC context.

    :param struct idmac_channel \*ichan:
        pointer to the channel object.

.. _`ipu_disable_channel`:

ipu_disable_channel
===================

.. c:function:: int ipu_disable_channel(struct idmac *idmac, struct idmac_channel *ichan, bool wait_for_stop)

    disable an IPU channel.

    :param struct idmac \*idmac:
        IPU DMAC context.

    :param struct idmac_channel \*ichan:
        channel object pointer.

    :param bool wait_for_stop:
        flag to set whether to wait for channel end of frame or
        return immediately.

.. This file was automatic generated / don't edit.

