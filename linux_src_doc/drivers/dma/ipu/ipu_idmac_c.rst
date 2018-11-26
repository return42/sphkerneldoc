.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ipu/ipu_idmac.c

.. _`ipu_enable_channel`:

ipu_enable_channel
==================

.. c:function:: int ipu_enable_channel(struct idmac *idmac, struct idmac_channel *ichan)

    enable an IPU channel.

    :param idmac:
        IPU DMAC context.
    :type idmac: struct idmac \*

    :param ichan:
        IDMAC channel.
    :type ichan: struct idmac_channel \*

.. _`ipu_init_channel_buffer`:

ipu_init_channel_buffer
=======================

.. c:function:: int ipu_init_channel_buffer(struct idmac_channel *ichan, enum pixel_fmt pixel_fmt, uint16_t width, uint16_t height, uint32_t stride, enum ipu_rotate_mode rot_mode, dma_addr_t phyaddr_0, dma_addr_t phyaddr_1)

    initialize a buffer for logical IPU channel.

    :param ichan:
        IDMAC channel.
    :type ichan: struct idmac_channel \*

    :param pixel_fmt:
        pixel format of buffer. Pixel format is a FOURCC ASCII code.
    :type pixel_fmt: enum pixel_fmt

    :param width:
        width of buffer in pixels.
    :type width: uint16_t

    :param height:
        height of buffer in pixels.
    :type height: uint16_t

    :param stride:
        stride length of buffer in pixels.
    :type stride: uint32_t

    :param rot_mode:
        rotation mode of buffer. A rotation setting other than
        IPU_ROTATE_VERT_FLIP should only be used for input buffers of
        rotation channels.
    :type rot_mode: enum ipu_rotate_mode

    :param phyaddr_0:
        buffer 0 physical address.
    :type phyaddr_0: dma_addr_t

    :param phyaddr_1:
        buffer 1 physical address. Setting this to a value other than
        NULL enables double buffering mode.
    :type phyaddr_1: dma_addr_t

.. _`ipu_select_buffer`:

ipu_select_buffer
=================

.. c:function:: void ipu_select_buffer(enum ipu_channel channel, int buffer_n)

    mark a channel's buffer as ready.

    :param channel:
        channel ID.
    :type channel: enum ipu_channel

    :param buffer_n:
        buffer number to mark ready.
    :type buffer_n: int

.. _`ipu_update_channel_buffer`:

ipu_update_channel_buffer
=========================

.. c:function:: void ipu_update_channel_buffer(struct idmac_channel *ichan, int buffer_n, dma_addr_t phyaddr)

    update physical address of a channel buffer.

    :param ichan:
        IDMAC channel.
    :type ichan: struct idmac_channel \*

    :param buffer_n:
        buffer number to update.
        0 or 1 are the only valid values.
    :type buffer_n: int

    :param phyaddr:
        buffer physical address.
    :type phyaddr: dma_addr_t

.. _`ipu_init_channel`:

ipu_init_channel
================

.. c:function:: int ipu_init_channel(struct idmac *idmac, struct idmac_channel *ichan)

    initialize an IPU channel.

    :param idmac:
        IPU DMAC context.
    :type idmac: struct idmac \*

    :param ichan:
        pointer to the channel object.
        \ ``return``\       0 on success or negative error code on failure.
    :type ichan: struct idmac_channel \*

.. _`ipu_uninit_channel`:

ipu_uninit_channel
==================

.. c:function:: void ipu_uninit_channel(struct idmac *idmac, struct idmac_channel *ichan)

    uninitialize an IPU channel.

    :param idmac:
        IPU DMAC context.
    :type idmac: struct idmac \*

    :param ichan:
        pointer to the channel object.
    :type ichan: struct idmac_channel \*

.. _`ipu_disable_channel`:

ipu_disable_channel
===================

.. c:function:: int ipu_disable_channel(struct idmac *idmac, struct idmac_channel *ichan, bool wait_for_stop)

    disable an IPU channel.

    :param idmac:
        IPU DMAC context.
    :type idmac: struct idmac \*

    :param ichan:
        channel object pointer.
    :type ichan: struct idmac_channel \*

    :param wait_for_stop:
        flag to set whether to wait for channel end of frame or
        return immediately.
    :type wait_for_stop: bool

.. This file was automatic generated / don't edit.

