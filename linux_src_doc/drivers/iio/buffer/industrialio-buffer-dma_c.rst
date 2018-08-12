.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/buffer/industrialio-buffer-dma.c

.. _`iio_dma_buffer_block_done`:

iio_dma_buffer_block_done
=========================

.. c:function:: void iio_dma_buffer_block_done(struct iio_dma_buffer_block *block)

    Indicate that a block has been completed

    :param struct iio_dma_buffer_block \*block:
        The completed block

.. _`iio_dma_buffer_block_done.description`:

Description
-----------

Should be called when the DMA controller has finished handling the block to
pass back ownership of the block to the queue.

.. _`iio_dma_buffer_block_list_abort`:

iio_dma_buffer_block_list_abort
===============================

.. c:function:: void iio_dma_buffer_block_list_abort(struct iio_dma_buffer_queue *queue, struct list_head *list)

    Indicate that a list block has been aborted

    :param struct iio_dma_buffer_queue \*queue:
        Queue for which to complete blocks.

    :param struct list_head \*list:
        List of aborted blocks. All blocks in this list must be from \ ``queue``\ .

.. _`iio_dma_buffer_block_list_abort.description`:

Description
-----------

Typically called from the \ :c:func:`abort`\  callback after the DMA controller has been
stopped. This will set bytes_used to 0 for each block in the list and then
hand the blocks back to the queue.

.. _`iio_dma_buffer_request_update`:

iio_dma_buffer_request_update
=============================

.. c:function:: int iio_dma_buffer_request_update(struct iio_buffer *buffer)

    DMA buffer request_update callback

    :param struct iio_buffer \*buffer:
        The buffer which to request an update

.. _`iio_dma_buffer_request_update.description`:

Description
-----------

Should be used as the \ :c:func:`iio_dma_buffer_request_update`\  callback for
iio_buffer_access_ops struct for DMA buffers.

.. _`iio_dma_buffer_enable`:

iio_dma_buffer_enable
=====================

.. c:function:: int iio_dma_buffer_enable(struct iio_buffer *buffer, struct iio_dev *indio_dev)

    Enable DMA buffer

    :param struct iio_buffer \*buffer:
        IIO buffer to enable

    :param struct iio_dev \*indio_dev:
        IIO device the buffer is attached to

.. _`iio_dma_buffer_enable.description`:

Description
-----------

Needs to be called when the device that the buffer is attached to starts
sampling. Typically should be the iio_buffer_access_ops enable callback.

This will allocate the DMA buffers and start the DMA transfers.

.. _`iio_dma_buffer_disable`:

iio_dma_buffer_disable
======================

.. c:function:: int iio_dma_buffer_disable(struct iio_buffer *buffer, struct iio_dev *indio_dev)

    Disable DMA buffer

    :param struct iio_buffer \*buffer:
        IIO DMA buffer to disable

    :param struct iio_dev \*indio_dev:
        IIO device the buffer is attached to

.. _`iio_dma_buffer_disable.description`:

Description
-----------

Needs to be called when the device that the buffer is attached to stops
sampling. Typically should be the iio_buffer_access_ops disable callback.

.. _`iio_dma_buffer_read`:

iio_dma_buffer_read
===================

.. c:function:: int iio_dma_buffer_read(struct iio_buffer *buffer, size_t n, char __user *user_buffer)

    DMA buffer read callback

    :param struct iio_buffer \*buffer:
        Buffer to read form

    :param size_t n:
        Number of bytes to read

    :param char __user \*user_buffer:
        Userspace buffer to copy the data to

.. _`iio_dma_buffer_read.description`:

Description
-----------

Should be used as the read_first_n callback for iio_buffer_access_ops
struct for DMA buffers.

.. _`iio_dma_buffer_data_available`:

iio_dma_buffer_data_available
=============================

.. c:function:: size_t iio_dma_buffer_data_available(struct iio_buffer *buf)

    DMA buffer data_available callback

    :param struct iio_buffer \*buf:
        Buffer to check for data availability

.. _`iio_dma_buffer_data_available.description`:

Description
-----------

Should be used as the data_available callback for iio_buffer_access_ops
struct for DMA buffers.

.. _`iio_dma_buffer_set_bytes_per_datum`:

iio_dma_buffer_set_bytes_per_datum
==================================

.. c:function:: int iio_dma_buffer_set_bytes_per_datum(struct iio_buffer *buffer, size_t bpd)

    DMA buffer set_bytes_per_datum callback

    :param struct iio_buffer \*buffer:
        Buffer to set the bytes-per-datum for

    :param size_t bpd:
        The new bytes-per-datum value

.. _`iio_dma_buffer_set_bytes_per_datum.description`:

Description
-----------

Should be used as the set_bytes_per_datum callback for iio_buffer_access_ops
struct for DMA buffers.

.. _`iio_dma_buffer_set_length`:

iio_dma_buffer_set_length
=========================

.. c:function:: int iio_dma_buffer_set_length(struct iio_buffer *buffer, unsigned int length)

    DMA buffer set_length callback

    :param struct iio_buffer \*buffer:
        Buffer to set the length for

    :param unsigned int length:
        The new buffer length

.. _`iio_dma_buffer_set_length.description`:

Description
-----------

Should be used as the set_length callback for iio_buffer_access_ops
struct for DMA buffers.

.. _`iio_dma_buffer_init`:

iio_dma_buffer_init
===================

.. c:function:: int iio_dma_buffer_init(struct iio_dma_buffer_queue *queue, struct device *dev, const struct iio_dma_buffer_ops *ops)

    Initialize DMA buffer queue

    :param struct iio_dma_buffer_queue \*queue:
        Buffer to initialize

    :param struct device \*dev:
        DMA device

    :param const struct iio_dma_buffer_ops \*ops:
        DMA buffer queue callback operations

.. _`iio_dma_buffer_init.description`:

Description
-----------

The DMA device will be used by the queue to do DMA memory allocations. So it
should refer to the device that will perform the DMA to ensure that
allocations are done from a memory region that can be accessed by the device.

.. _`iio_dma_buffer_exit`:

iio_dma_buffer_exit
===================

.. c:function:: void iio_dma_buffer_exit(struct iio_dma_buffer_queue *queue)

    Cleanup DMA buffer queue

    :param struct iio_dma_buffer_queue \*queue:
        Buffer to cleanup

.. _`iio_dma_buffer_exit.description`:

Description
-----------

After this function has completed it is safe to free any resources that are
associated with the buffer and are accessed inside the callback operations.

.. _`iio_dma_buffer_release`:

iio_dma_buffer_release
======================

.. c:function:: void iio_dma_buffer_release(struct iio_dma_buffer_queue *queue)

    Release final buffer resources

    :param struct iio_dma_buffer_queue \*queue:
        Buffer to release

.. _`iio_dma_buffer_release.description`:

Description
-----------

Frees resources that can't yet be freed in \ :c:func:`iio_dma_buffer_exit`\ . Should be
called in the buffers release callback implementation right before freeing
the memory associated with the buffer.

.. This file was automatic generated / don't edit.

