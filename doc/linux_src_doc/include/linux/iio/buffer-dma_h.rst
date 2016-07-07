.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/buffer-dma.h

.. _`iio_block_state`:

enum iio_block_state
====================

.. c:type:: enum iio_block_state

    State of a struct iio_dma_buffer_block

.. _`iio_block_state.definition`:

Definition
----------

.. code-block:: c

    enum iio_block_state {
        IIO_BLOCK_STATE_DEQUEUED,
        IIO_BLOCK_STATE_QUEUED,
        IIO_BLOCK_STATE_ACTIVE,
        IIO_BLOCK_STATE_DONE,
        IIO_BLOCK_STATE_DEAD
    };

.. _`iio_block_state.constants`:

Constants
---------

IIO_BLOCK_STATE_DEQUEUED
    Block is not queued

IIO_BLOCK_STATE_QUEUED
    Block is on the incoming queue

IIO_BLOCK_STATE_ACTIVE
    Block is currently being processed by the DMA

IIO_BLOCK_STATE_DONE
    Block is on the outgoing queue

IIO_BLOCK_STATE_DEAD
    Block has been marked as to be freed

.. _`iio_dma_buffer_block`:

struct iio_dma_buffer_block
===========================

.. c:type:: struct iio_dma_buffer_block

    IIO buffer block

.. _`iio_dma_buffer_block.definition`:

Definition
----------

.. code-block:: c

    struct iio_dma_buffer_block {
        struct list_head head;
        size_t bytes_used;
        void *vaddr;
        dma_addr_t phys_addr;
        size_t size;
        struct iio_dma_buffer_queue *queue;
        struct kref kref;
        enum iio_block_state state;
    }

.. _`iio_dma_buffer_block.members`:

Members
-------

head
    List head

bytes_used
    Number of bytes that contain valid data

vaddr
    Virutal address of the blocks memory

phys_addr
    Physical address of the blocks memory

size
    Total size of the block in bytes

queue
    Parent DMA buffer queue

kref
    kref used to manage the lifetime of block

state
    Current state of the block

.. _`iio_dma_buffer_queue_fileio`:

struct iio_dma_buffer_queue_fileio
==================================

.. c:type:: struct iio_dma_buffer_queue_fileio

    FileIO state for the DMA buffer

.. _`iio_dma_buffer_queue_fileio.definition`:

Definition
----------

.. code-block:: c

    struct iio_dma_buffer_queue_fileio {
        struct iio_dma_buffer_block  *blocks[2];
        struct iio_dma_buffer_block *active_block;
        size_t pos;
        size_t block_size;
    }

.. _`iio_dma_buffer_queue_fileio.members`:

Members
-------

blocks
    Buffer blocks used for fileio

active_block
    Block being used in \ :c:func:`read`\ 

pos
    Read offset in the active block

block_size
    Size of each block

.. _`iio_dma_buffer_queue`:

struct iio_dma_buffer_queue
===========================

.. c:type:: struct iio_dma_buffer_queue

    DMA buffer base structure

.. _`iio_dma_buffer_queue.definition`:

Definition
----------

.. code-block:: c

    struct iio_dma_buffer_queue {
        struct iio_buffer buffer;
        struct device *dev;
        const struct iio_dma_buffer_ops *ops;
        struct mutex lock;
        spinlock_t list_lock;
        struct list_head incoming;
        struct list_head outgoing;
        bool active;
        struct iio_dma_buffer_queue_fileio fileio;
    }

.. _`iio_dma_buffer_queue.members`:

Members
-------

buffer
    IIO buffer base structure

dev
    Parent device

ops
    DMA buffer callbacks

lock
    Protects the incoming list, active and the fields in the fileio
    substruct

list_lock
    Protects lists that contain blocks which can be modified in
    atomic context as well as blocks on those lists. This is the outgoing queue
    list and typically also a list of active blocks in the part that handles
    the DMA controller

incoming
    List of buffers on the incoming queue

outgoing
    List of buffers on the outgoing queue

active
    Whether the buffer is currently active

fileio
    FileIO state

.. _`iio_dma_buffer_ops`:

struct iio_dma_buffer_ops
=========================

.. c:type:: struct iio_dma_buffer_ops

    DMA buffer callback operations

.. _`iio_dma_buffer_ops.definition`:

Definition
----------

.. code-block:: c

    struct iio_dma_buffer_ops {
        int (* submit) (struct iio_dma_buffer_queue *queue,struct iio_dma_buffer_block *block);
        void (* abort) (struct iio_dma_buffer_queue *queue);
    }

.. _`iio_dma_buffer_ops.members`:

Members
-------

submit
    Called when a block is submitted to the DMA controller

abort
    Should abort all pending transfers

.. This file was automatic generated / don't edit.

