.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ti/knav_dma.c

.. _`knav_dma_open_channel`:

knav_dma_open_channel
=====================

.. c:function:: void *knav_dma_open_channel(struct device *dev, const char *name, struct knav_dma_cfg *config)

    try to setup an exclusive slave channel

    :param dev:
        pointer to client device structure
    :type dev: struct device \*

    :param name:
        slave channel name
    :type name: const char \*

    :param config:
        dma configuration parameters
    :type config: struct knav_dma_cfg \*

.. _`knav_dma_open_channel.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or error.

.. _`knav_dma_close_channel`:

knav_dma_close_channel
======================

.. c:function:: void knav_dma_close_channel(void *channel)

    Destroy a dma channel

    :param channel:
        *undescribed*
    :type channel: void \*

.. _`knav_dma_close_channel.channel`:

channel
-------

dma channel handle

.. This file was automatic generated / don't edit.

