.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdkfd/kfd_kernel_queue.h

.. _`kernel_queue_ops`:

struct kernel_queue_ops
=======================

.. c:type:: struct kernel_queue_ops


.. _`kernel_queue_ops.definition`:

Definition
----------

.. code-block:: c

    struct kernel_queue_ops {
        bool (* initialize) (struct kernel_queue *kq, struct kfd_dev *dev,enum kfd_queue_type type, unsigned int queue_size);
        void (* uninitialize) (struct kernel_queue *kq);
        int (* acquire_packet_buffer) (struct kernel_queue *kq,size_t packet_size_in_dwords,unsigned int **buffer_ptr);
        void (* submit_packet) (struct kernel_queue *kq);
        void (* rollback_packet) (struct kernel_queue *kq);
    }

.. _`kernel_queue_ops.members`:

Members
-------

initialize
    Initialize a kernel queue, including allocations of GART memory
    needed for the queue.

uninitialize
    Uninitialize a kernel queue and free all its memory usages.

acquire_packet_buffer
    Returns a pointer to the location in the kernel
    queue ring buffer where the calling function can write its packet. It is
    Guaranteed that there is enough space for that packet. It also updates the
    pending write pointer to that location so subsequent calls to
    acquire_packet_buffer will get a correct write pointer

submit_packet
    Update the write pointer and doorbell of a kernel queue.

rollback_packet
    This routine is called if we failed to build an acquired
    packet for some reason. It just overwrites the pending wptr with the current
    one

.. This file was automatic generated / don't edit.

