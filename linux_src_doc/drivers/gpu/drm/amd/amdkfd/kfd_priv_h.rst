.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdkfd/kfd_priv.h

.. _`kfd_unmap_queues_filter`:

enum kfd_unmap_queues_filter
============================

.. c:type:: enum kfd_unmap_queues_filter


.. _`kfd_unmap_queues_filter.definition`:

Definition
----------

.. code-block:: c

    enum kfd_unmap_queues_filter {
        KFD_UNMAP_QUEUES_FILTER_SINGLE_QUEUE,
        KFD_UNMAP_QUEUES_FILTER_ALL_QUEUES,
        KFD_UNMAP_QUEUES_FILTER_DYNAMIC_QUEUES,
        KFD_UNMAP_QUEUES_FILTER_BY_PASID
    };

.. _`kfd_unmap_queues_filter.constants`:

Constants
---------

KFD_UNMAP_QUEUES_FILTER_SINGLE_QUEUE
    Preempts single queue.

KFD_UNMAP_QUEUES_FILTER_ALL_QUEUES
    Preempts all queues in the
    running queues list.

KFD_UNMAP_QUEUES_FILTER_DYNAMIC_QUEUES
    *undescribed*

KFD_UNMAP_QUEUES_FILTER_BY_PASID
    Preempts queues that belongs to
    specific process.

.. _`kfd_queue_type`:

enum kfd_queue_type
===================

.. c:type:: enum kfd_queue_type


.. _`kfd_queue_type.definition`:

Definition
----------

.. code-block:: c

    enum kfd_queue_type {
        KFD_QUEUE_TYPE_COMPUTE,
        KFD_QUEUE_TYPE_SDMA,
        KFD_QUEUE_TYPE_HIQ,
        KFD_QUEUE_TYPE_DIQ
    };

.. _`kfd_queue_type.constants`:

Constants
---------

KFD_QUEUE_TYPE_COMPUTE
    Regular user mode queue type.

KFD_QUEUE_TYPE_SDMA
    Sdma user mode queue type.

KFD_QUEUE_TYPE_HIQ
    HIQ queue type.

KFD_QUEUE_TYPE_DIQ
    DIQ queue type.

.. _`queue_properties`:

struct queue_properties
=======================

.. c:type:: struct queue_properties


.. _`queue_properties.definition`:

Definition
----------

.. code-block:: c

    struct queue_properties {
        enum kfd_queue_type type;
        enum kfd_queue_format format;
        unsigned int queue_id;
        uint64_t queue_address;
        uint64_t queue_size;
        uint32_t priority;
        uint32_t queue_percent;
        uint32_t *read_ptr;
        uint32_t *write_ptr;
        void __iomem *doorbell_ptr;
        uint32_t doorbell_off;
        bool is_interop;
        bool is_evicted;
        bool is_active;
        unsigned int vmid;
        uint32_t sdma_engine_id;
        uint32_t sdma_queue_id;
        uint32_t sdma_vm_addr;
        uint64_t eop_ring_buffer_address;
        uint32_t eop_ring_buffer_size;
        uint64_t ctx_save_restore_area_address;
        uint32_t ctx_save_restore_area_size;
        uint32_t ctl_stack_size;
        uint64_t tba_addr;
        uint64_t tma_addr;
        uint32_t cu_mask_count;
        uint32_t *cu_mask;
    }

.. _`queue_properties.members`:

Members
-------

type
    The queue type.

format
    *undescribed*

queue_id
    Queue identifier.

queue_address
    Queue ring buffer address.

queue_size
    Queue ring buffer size.

priority
    Defines the queue priority relative to other queues in the
    process.
    This is just an indication and HW scheduling may override the priority as
    necessary while keeping the relative prioritization.
    the priority granularity is from 0 to f which f is the highest priority.
    currently all queues are initialized with the highest priority.

queue_percent
    This field is partially implemented and currently a zero in
    this field defines that the queue is non active.

read_ptr
    User space address which points to the number of dwords the
    cp read from the ring buffer. This field updates automatically by the H/W.

write_ptr
    Defines the number of dwords written to the ring buffer.

doorbell_ptr
    This field aim is to notify the H/W of new packet written to
    the queue ring buffer. This field should be similar to write_ptr and the
    user should update this field after he updated the write_ptr.

doorbell_off
    The doorbell offset in the doorbell pci-bar.

is_interop
    Defines if this is a interop queue. Interop queue means that
    the queue can access both graphics and compute resources.

is_evicted
    Defines if the queue is evicted. Only active queues
    are evicted, rendering them inactive.

is_active
    Defines if the queue is active or not. \ ``is_active``\  and
    \ ``is_evicted``\  are protected by the DQM lock.

vmid
    If the scheduling mode is no cp scheduling the field defines the vmid
    of the queue.

sdma_engine_id
    *undescribed*

sdma_queue_id
    *undescribed*

sdma_vm_addr
    *undescribed*

eop_ring_buffer_address
    *undescribed*

eop_ring_buffer_size
    *undescribed*

ctx_save_restore_area_address
    *undescribed*

ctx_save_restore_area_size
    *undescribed*

ctl_stack_size
    *undescribed*

tba_addr
    *undescribed*

tma_addr
    *undescribed*

cu_mask_count
    *undescribed*

cu_mask
    *undescribed*

.. _`queue_properties.description`:

Description
-----------

This structure represents the queue properties for each queue no matter if
it's user mode or kernel mode queue.

.. _`queue`:

struct queue
============

.. c:type:: struct queue


.. _`queue.definition`:

Definition
----------

.. code-block:: c

    struct queue {
        struct list_head list;
        void *mqd;
        struct kfd_mem_obj *mqd_mem_obj;
        uint64_t gart_mqd_addr;
        struct queue_properties properties;
        uint32_t mec;
        uint32_t pipe;
        uint32_t queue;
        unsigned int sdma_id;
        unsigned int doorbell_id;
        struct kfd_process *process;
        struct kfd_dev *device;
    }

.. _`queue.members`:

Members
-------

list
    Queue linked list.

mqd
    The queue MQD.

mqd_mem_obj
    The MQD local gpu memory object.

gart_mqd_addr
    The MQD gart mc address.

properties
    The queue properties.

mec
    Used only in no cp scheduling mode and identifies to micro engine id
    that the queue should be execute on.

pipe
    Used only in no cp scheduling mode and identifies the queue's pipe
    id.

queue
    Used only in no cp scheduliong mode and identifies the queue's slot.

sdma_id
    *undescribed*

doorbell_id
    *undescribed*

process
    The kfd process that created this queue.

device
    The kfd device that created this queue.

.. _`queue.description`:

Description
-----------

This structure represents user mode compute queues.
It contains all the necessary data to handle such queues.

.. _`amdkfd_ioctl_t`:

amdkfd_ioctl_t
==============

.. c:function:: int amdkfd_ioctl_t(struct file *filep, struct kfd_process *p, void *data)

    :param filep:
        *undescribed*
    :type filep: struct file \*

    :param p:
        *undescribed*
    :type p: struct kfd_process \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`amdkfd_ioctl_t.description`:

Description
-----------

\param filep pointer to file structure.
\param p amdkfd process pointer.
\param data pointer to arg that was copied from user.

.. This file was automatic generated / don't edit.

