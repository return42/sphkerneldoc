.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/dmaengine.c

.. _`dev_to_dma_chan`:

dev_to_dma_chan
===============

.. c:function:: struct dma_chan *dev_to_dma_chan(struct device *dev)

    convert a device pointer to the its sysfs container object \ ``dev``\  - device node

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dev_to_dma_chan.description`:

Description
-----------

Must be called under dma_list_mutex

.. _`balance_ref_count`:

balance_ref_count
=================

.. c:function:: void balance_ref_count(struct dma_chan *chan)

    catch up the channel reference count \ ``chan``\  - channel to balance ->client_count versus dmaengine_ref_count

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`balance_ref_count.description`:

Description
-----------

balance_ref_count must be called under dma_list_mutex

.. _`dma_chan_get`:

dma_chan_get
============

.. c:function:: int dma_chan_get(struct dma_chan *chan)

    try to grab a dma channel's parent driver module \ ``chan``\  - channel to grab

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`dma_chan_get.description`:

Description
-----------

Must be called under dma_list_mutex

.. _`dma_chan_put`:

dma_chan_put
============

.. c:function:: void dma_chan_put(struct dma_chan *chan)

    drop a reference to a dma channel's parent driver module \ ``chan``\  - channel to release

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`dma_chan_put.description`:

Description
-----------

Must be called under dma_list_mutex

.. _`dma_find_channel`:

dma_find_channel
================

.. c:function:: struct dma_chan *dma_find_channel(enum dma_transaction_type tx_type)

    find a channel to carry out the operation

    :param tx_type:
        transaction type
    :type tx_type: enum dma_transaction_type

.. _`dma_issue_pending_all`:

dma_issue_pending_all
=====================

.. c:function:: void dma_issue_pending_all( void)

    flush all pending operations across all channels

    :param void:
        no arguments
    :type void: 

.. _`dma_chan_is_local`:

dma_chan_is_local
=================

.. c:function:: bool dma_chan_is_local(struct dma_chan *chan, int cpu)

    returns true if the channel is in the same numa-node as the cpu

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`min_chan`:

min_chan
========

.. c:function:: struct dma_chan *min_chan(enum dma_transaction_type cap, int cpu)

    returns the channel with min count and in the same numa-node as the cpu

    :param cap:
        capability to match
    :type cap: enum dma_transaction_type

    :param cpu:
        cpu index which the channel should be close to
    :type cpu: int

.. _`min_chan.description`:

Description
-----------

If some channels are close to the given cpu, the one with the lowest
reference count is returned. Otherwise, cpu is ignored and only the
reference count is taken into account.
Must be called under dma_list_mutex.

.. _`dma_channel_rebalance`:

dma_channel_rebalance
=====================

.. c:function:: void dma_channel_rebalance( void)

    redistribute the available channels

    :param void:
        no arguments
    :type void: 

.. _`dma_channel_rebalance.description`:

Description
-----------

Optimize for cpu isolation (each cpu gets a dedicated channel for an
operation type) in the SMP case,  and operation isolation (avoid
multi-tasking channels) in the non-SMP case.  Must be called under
dma_list_mutex.

.. _`dma_get_slave_channel`:

dma_get_slave_channel
=====================

.. c:function:: struct dma_chan *dma_get_slave_channel(struct dma_chan *chan)

    try to get specific channel exclusively

    :param chan:
        target channel
    :type chan: struct dma_chan \*

.. _`__dma_request_channel`:

\__dma_request_channel
======================

.. c:function:: struct dma_chan *__dma_request_channel(const dma_cap_mask_t *mask, dma_filter_fn fn, void *fn_param)

    try to allocate an exclusive channel

    :param mask:
        capabilities that the channel must satisfy
    :type mask: const dma_cap_mask_t \*

    :param fn:
        optional callback to disposition available channels
    :type fn: dma_filter_fn

    :param fn_param:
        opaque parameter to pass to dma_filter_fn
    :type fn_param: void \*

.. _`__dma_request_channel.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or NULL.

.. _`dma_request_chan`:

dma_request_chan
================

.. c:function:: struct dma_chan *dma_request_chan(struct device *dev, const char *name)

    try to allocate an exclusive slave channel

    :param dev:
        pointer to client device structure
    :type dev: struct device \*

    :param name:
        slave channel name
    :type name: const char \*

.. _`dma_request_chan.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or an error pointer.

.. _`dma_request_slave_channel`:

dma_request_slave_channel
=========================

.. c:function:: struct dma_chan *dma_request_slave_channel(struct device *dev, const char *name)

    try to allocate an exclusive slave channel

    :param dev:
        pointer to client device structure
    :type dev: struct device \*

    :param name:
        slave channel name
    :type name: const char \*

.. _`dma_request_slave_channel.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or NULL.

.. _`dma_request_chan_by_mask`:

dma_request_chan_by_mask
========================

.. c:function:: struct dma_chan *dma_request_chan_by_mask(const dma_cap_mask_t *mask)

    allocate a channel satisfying certain capabilities

    :param mask:
        capabilities that the channel must satisfy
    :type mask: const dma_cap_mask_t \*

.. _`dma_request_chan_by_mask.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or an error pointer.

.. _`dmaengine_get`:

dmaengine_get
=============

.. c:function:: void dmaengine_get( void)

    register interest in dma_channels

    :param void:
        no arguments
    :type void: 

.. _`dmaengine_put`:

dmaengine_put
=============

.. c:function:: void dmaengine_put( void)

    let dma drivers be removed when ref_count == 0

    :param void:
        no arguments
    :type void: 

.. _`dma_async_device_register`:

dma_async_device_register
=========================

.. c:function:: int dma_async_device_register(struct dma_device *device)

    registers DMA devices found

    :param device:
        \ :c:type:`struct dma_device <dma_device>`\ 
    :type device: struct dma_device \*

.. _`dma_async_device_unregister`:

dma_async_device_unregister
===========================

.. c:function:: void dma_async_device_unregister(struct dma_device *device)

    unregister a DMA device

    :param device:
        \ :c:type:`struct dma_device <dma_device>`\ 
    :type device: struct dma_device \*

.. _`dma_async_device_unregister.description`:

Description
-----------

This routine is called by dma driver exit routines, dmaengine holds module
references to prevent it being called while channels are in use.

.. _`dmaenginem_async_device_register`:

dmaenginem_async_device_register
================================

.. c:function:: int dmaenginem_async_device_register(struct dma_device *device)

    registers DMA devices found

    :param device:
        \ :c:type:`struct dma_device <dma_device>`\ 
    :type device: struct dma_device \*

.. _`dmaenginem_async_device_register.description`:

Description
-----------

The operation is managed and will be undone on driver detach.

.. This file was automatic generated / don't edit.

