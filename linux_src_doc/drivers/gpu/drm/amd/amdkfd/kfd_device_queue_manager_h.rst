.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdkfd/kfd_device_queue_manager.h

.. _`device_queue_manager_ops`:

struct device_queue_manager_ops
===============================

.. c:type:: struct device_queue_manager_ops


.. _`device_queue_manager_ops.definition`:

Definition
----------

.. code-block:: c

    struct device_queue_manager_ops {
        int (*create_queue)(struct device_queue_manager *dqm,struct queue *q,struct qcm_process_device *qpd, int *allocate_vmid);
        int (*destroy_queue)(struct device_queue_manager *dqm,struct qcm_process_device *qpd, struct queue *q);
        int (*update_queue)(struct device_queue_manager *dqm, struct queue *q);
        struct mqd_manager * (*get_mqd_manager)(struct device_queue_manager *dqm, enum KFD_MQD_TYPE type);
        int (*register_process)(struct device_queue_manager *dqm, struct qcm_process_device *qpd);
        int (*unregister_process)(struct device_queue_manager *dqm, struct qcm_process_device *qpd);
        int (*initialize)(struct device_queue_manager *dqm);
        int (*start)(struct device_queue_manager *dqm);
        int (*stop)(struct device_queue_manager *dqm);
        void (*uninitialize)(struct device_queue_manager *dqm);
        int (*create_kernel_queue)(struct device_queue_manager *dqm,struct kernel_queue *kq, struct qcm_process_device *qpd);
        void (*destroy_kernel_queue)(struct device_queue_manager *dqm,struct kernel_queue *kq, struct qcm_process_device *qpd);
        bool (*set_cache_memory_policy)(struct device_queue_manager *dqm,struct qcm_process_device *qpd,enum cache_policy default_policy,enum cache_policy alternate_policy,void __user *alternate_aperture_base, uint64_t alternate_aperture_size);
    }

.. _`device_queue_manager_ops.members`:

Members
-------

create_queue
    Queue creation routine.

destroy_queue
    Queue destruction routine.

update_queue
    Queue update routine.

get_mqd_manager
    Returns the mqd manager according to the mqd type.

register_process
    This routine associates a specific process with device.

unregister_process
    destroys the associations between process to device.

initialize
    Initializes the pipelines and memory module for that device.

start
    Initializes the resources/modules the the device needs for queues
    execution. This function is called on device initialization and after the
    system woke up after suspension.

stop
    This routine stops execution of all the active queue running on the
    H/W and basically this function called on system suspend.

uninitialize
    Destroys all the device queue manager resources allocated in
    initialize routine.

create_kernel_queue
    Creates kernel queue. Used for debug queue.

destroy_kernel_queue
    Destroys kernel queue. Used for debug queue.

set_cache_memory_policy
    Sets memory policy (cached/ non cached) for the
    memory apertures.

.. _`device_queue_manager`:

struct device_queue_manager
===========================

.. c:type:: struct device_queue_manager


.. _`device_queue_manager.definition`:

Definition
----------

.. code-block:: c

    struct device_queue_manager {
        struct device_queue_manager_ops ops;
        struct device_queue_manager_asic_ops ops_asic_specific;
        struct mqd_manager *mqds[KFD_MQD_TYPE_MAX];
        struct packet_manager packets;
        struct kfd_dev *dev;
        struct mutex lock;
        struct list_head queues;
        unsigned int processes_count;
        unsigned int queue_count;
        unsigned int sdma_queue_count;
        unsigned int total_queue_count;
        unsigned int next_pipe_to_allocate;
        unsigned int *allocated_queues;
        unsigned int sdma_bitmap;
        unsigned int vmid_bitmap;
        uint64_t pipelines_addr;
        struct kfd_mem_obj *pipeline_mem;
        uint64_t fence_gpu_addr;
        unsigned int *fence_addr;
        struct kfd_mem_obj *fence_mem;
        bool active_runlist;
    }

.. _`device_queue_manager.members`:

Members
-------

ops
    *undescribed*

ops_asic_specific
    *undescribed*

mqds
    *undescribed*

packets
    *undescribed*

dev
    *undescribed*

lock
    *undescribed*

queues
    *undescribed*

processes_count
    *undescribed*

queue_count
    *undescribed*

sdma_queue_count
    *undescribed*

total_queue_count
    *undescribed*

next_pipe_to_allocate
    *undescribed*

allocated_queues
    *undescribed*

sdma_bitmap
    *undescribed*

vmid_bitmap
    *undescribed*

pipelines_addr
    *undescribed*

pipeline_mem
    *undescribed*

fence_gpu_addr
    *undescribed*

fence_addr
    *undescribed*

fence_mem
    *undescribed*

active_runlist
    *undescribed*

.. _`device_queue_manager.description`:

Description
-----------

This struct is a base class for the kfd queues scheduler in the
device level. The device base class should expose the basic operations
for queue creation and queue destruction. This base class hides the
scheduling mode of the driver and the specific implementation of the
concrete device. This class is the only class in the queues scheduler
that configures the H/W.

.. This file was automatic generated / don't edit.

