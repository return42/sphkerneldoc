.. -*- coding: utf-8; mode: rst -*-

==========
kfd_priv.h
==========


.. _`kfd_sched_policy`:

enum kfd_sched_policy
=====================

.. c:type:: kfd_sched_policy

    


.. _`kfd_sched_policy.definition`:

Definition
----------

.. code-block:: c

    enum kfd_sched_policy {
      KFD_SCHED_POLICY_HWS,
      KFD_SCHED_POLICY_HWS_NO_OVERSUBSCRIPTION,
      KFD_SCHED_POLICY_NO_HWS
    };


.. _`kfd_sched_policy.constants`:

Constants
---------

:``KFD_SCHED_POLICY_HWS``:
    H/W scheduling policy known as command processor (cp)
    scheduling. In this scheduling mode we're using the firmware code to
    schedule the user mode queues and kernel queues such as HIQ and DIQ.
    the HIQ queue is used as a special queue that dispatches the configuration
    to the cp and the user mode queues list that are currently running.
    the DIQ queue is a debugging queue that dispatches debugging commands to the
    firmware.
    in this scheduling mode user mode queues over subscription feature is
    enabled.

:``KFD_SCHED_POLICY_HWS_NO_OVERSUBSCRIPTION``:
    The same as above but the over
    subscription feature disabled.

:``KFD_SCHED_POLICY_NO_HWS``:
    no H/W scheduling policy is a mode which directly
    set the command processor registers and sets the queues "manually". This
    mode is used \*ONLY\* for debugging proposes.


.. _`kfd_preempt_type_filter`:

enum kfd_preempt_type_filter
============================

.. c:type:: kfd_preempt_type_filter

    


.. _`kfd_preempt_type_filter.definition`:

Definition
----------

.. code-block:: c

    enum kfd_preempt_type_filter {
      KFD_PREEMPT_TYPE_FILTER_SINGLE_QUEUE,
      KFD_PREEMPT_TYPE_FILTER_ALL_QUEUES,
      KFD_PREEMPT_TYPE_FILTER_DYNAMIC_QUEUES,
      KFD_PREEMPT_TYPE_FILTER_BY_PASID
    };


.. _`kfd_preempt_type_filter.constants`:

Constants
---------

:``KFD_PREEMPT_TYPE_FILTER_SINGLE_QUEUE``:
    Preempts single queue.

:``KFD_PREEMPT_TYPE_FILTER_ALL_QUEUES``:
-- undescribed --

:``KFD_PREEMPT_TYPE_FILTER_DYNAMIC_QUEUES``:
-- undescribed --

:``KFD_PREEMPT_TYPE_FILTER_BY_PASID``:
-- undescribed --


.. _`kfd_queue_type`:

enum kfd_queue_type
===================

.. c:type:: kfd_queue_type

    


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

:``KFD_QUEUE_TYPE_COMPUTE``:
    Regular user mode queue type.

:``KFD_QUEUE_TYPE_SDMA``:
    Sdma user mode queue type.

:``KFD_QUEUE_TYPE_HIQ``:
    HIQ queue type.

:``KFD_QUEUE_TYPE_DIQ``:
    DIQ queue type.


.. _`queue_properties`:

struct queue_properties
=======================

.. c:type:: queue_properties

    


.. _`queue_properties.definition`:

Definition
----------

.. code-block:: c

  struct queue_properties {
    enum kfd_queue_type type;
    unsigned int queue_id;
    uint64_t queue_address;
    uint64_t queue_size;
    uint32_t priority;
    uint32_t queue_percent;
    uint32_t * read_ptr;
    uint32_t * write_ptr;
    uint32_t __iomem * doorbell_ptr;
    uint32_t doorbell_off;
    bool is_interop;
    bool is_active;
    unsigned int vmid;
  };


.. _`queue_properties.members`:

Members
-------

:``type``:
    The queue type.

:``queue_id``:
    Queue identifier.

:``queue_address``:
    Queue ring buffer address.

:``queue_size``:
    Queue ring buffer size.

:``priority``:
    Defines the queue priority relative to other queues in the
    process.
    This is just an indication and HW scheduling may override the priority as
    necessary while keeping the relative prioritization.
    the priority granularity is from 0 to f which f is the highest priority.
    currently all queues are initialized with the highest priority.

:``queue_percent``:
    This field is partially implemented and currently a zero in
    this field defines that the queue is non active.

:``read_ptr``:
    User space address which points to the number of dwords the
    cp read from the ring buffer. This field updates automatically by the H/W.

:``write_ptr``:
    Defines the number of dwords written to the ring buffer.

:``doorbell_ptr``:
    This field aim is to notify the H/W of new packet written to
    the queue ring buffer. This field should be similar to write_ptr and the user
    should update this field after he updated the write_ptr.

:``doorbell_off``:
    The doorbell offset in the doorbell pci-bar.

:``is_interop``:
    Defines if this is a interop queue. Interop queue means that the
    queue can access both graphics and compute resources.

:``is_active``:
    Defines if the queue is active or not.

:``vmid``:
    If the scheduling mode is no cp scheduling the field defines the vmid
    of the queue.




.. _`queue_properties.description`:

Description
-----------

This structure represents the queue properties for each queue no matter if
it's user mode or kernel mode queue.



.. _`queue`:

struct queue
============

.. c:type:: queue

    


.. _`queue.definition`:

Definition
----------

.. code-block:: c

  struct queue {
    struct list_head list;
    void * mqd;
    struct kfd_mem_obj * mqd_mem_obj;
    uint64_t gart_mqd_addr;
    struct queue_properties properties;
    uint32_t mec;
    uint32_t pipe;
    uint32_t queue;
    struct kfd_process * process;
    struct kfd_dev * device;
  };


.. _`queue.members`:

Members
-------

:``list``:
    Queue linked list.

:``mqd``:
    The queue MQD.

:``mqd_mem_obj``:
    The MQD local gpu memory object.

:``gart_mqd_addr``:
    The MQD gart mc address.

:``properties``:
    The queue properties.

:``mec``:
    Used only in no cp scheduling mode and identifies to micro engine id
    that the queue should be execute on.

:``pipe``:
    Used only in no cp scheduling mode and identifies the queue's pipe id.

:``queue``:
    Used only in no cp scheduliong mode and identifies the queue's slot.

:``process``:
    The kfd process that created this queue.

:``device``:
    The kfd device that created this queue.




.. _`queue.description`:

Description
-----------

This structure represents user mode compute queues.
It contains all the necessary data to handle such queues.



.. _`amdkfd_ioctl_t`:

amdkfd_ioctl_t
==============

.. c:function:: typedef int amdkfd_ioctl_t (struct file *filep, struct kfd_process *p, void *data)

    :param struct file \*filep:

        *undescribed*

    :param struct kfd_process \*p:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`amdkfd_ioctl_t.description`:

Description
-----------


\param filep pointer to file structure.
\param p amdkfd process pointer.
\param data pointer to arg that was copied from user.

