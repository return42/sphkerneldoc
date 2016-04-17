.. -*- coding: utf-8; mode: rst -*-

==========
knav_dma.c
==========


.. _`knav_dma_open_channel`:

knav_dma_open_channel
=====================

.. c:function:: void *knav_dma_open_channel (struct device *dev, const char *name, struct knav_dma_cfg *config)

    try to setup an exclusive slave channel

    :param struct device \*dev:
        pointer to client device structure

    :param const char \*name:
        slave channel name

    :param struct knav_dma_cfg \*config:
        dma configuration parameters



.. _`knav_dma_open_channel.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or NULL.



.. _`knav_dma_close_channel`:

knav_dma_close_channel
======================

.. c:function:: void knav_dma_close_channel (void *channel)

    Destroy a dma channel

    :param void \*channel:

        *undescribed*



.. _`knav_dma_close_channel.channel`:

channel
-------

dma channel handle

