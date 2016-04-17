.. -*- coding: utf-8; mode: rst -*-

==========================
kfd_device_queue_manager.h
==========================


.. _`device_queue_manager_ops`:

struct device_queue_manager_ops
===============================

.. c:type:: device_queue_manager_ops

    


.. _`device_queue_manager_ops.definition`:

Definition
----------

.. code-block:: c

  struct device_queue_manager_ops {
    int (* create_queue) (struct device_queue_manager *dqm,struct queue *q,struct qcm_process_device *qpd,int *allocate_vmid);
    int (* destroy_queue) (struct device_queue_manager *dqm,struct qcm_process_device *qpd,struct queue *q);
    int (* update_queue) (struct device_queue_manager *dqm,struct queue *q);
    struct mqd_manager * (* get_mqd_manager) (struct device_queue_manager *dqm,enum KFD_MQD_TYPE type);
    int (* register_process) (struct device_queue_manager *dqm,struct qcm_process_device *qpd);
    int (* unregister_process) (struct device_queue_manager *dqm,struct qcm_process_device *qpd);
    int (* initialize) (struct device_queue_manager *dqm);
    int (* start) (struct device_queue_manager *dqm);
    int (* stop) (struct device_queue_manager *dqm);
    void (* uninitialize) (struct device_queue_manager *dqm);
    int (* create_kernel_queue) (struct device_queue_manager *dqm,struct kernel_queue *kq,struct qcm_process_device *qpd);
    void (* destroy_kernel_queue) (struct device_queue_manager *dqm,struct kernel_queue *kq,struct qcm_process_device *qpd);
    bool (* set_cache_memory_policy) (struct device_queue_manager *dqm,struct qcm_process_device *qpd,enum cache_policy default_policy,enum cache_policy alternate_policy,void __user *alternate_aperture_base,uint64_t alternate_aperture_size);
  };


.. _`device_queue_manager_ops.members`:

Members
-------

:``create_queue``:
    Queue creation routine.

:``destroy_queue``:
    Queue destruction routine.

:``update_queue``:
    Queue update routine.

:``get_mqd_manager``:
    Returns the mqd manager according to the mqd type.

:``register_process``:
    This routine associates a specific process with device.

:``unregister_process``:
    destroys the associations between process to device.

:``initialize``:
    Initializes the pipelines and memory module for that device.

:``start``:
    Initializes the resources/modules the the device needs for queues
    execution. This function is called on device initialization and after the
    system woke up after suspension.

:``stop``:
    This routine stops execution of all the active queue running on the
    H/W and basically this function called on system suspend.

:``uninitialize``:
    Destroys all the device queue manager resources allocated in
    initialize routine.

:``create_kernel_queue``:
    Creates kernel queue. Used for debug queue.

:``destroy_kernel_queue``:
    Destroys kernel queue. Used for debug queue.

:``set_cache_memory_policy``:
    Sets memory policy (cached/ non cached) for the
    memory apertures.




.. _`device_queue_manager`:

struct device_queue_manager
===========================

.. c:type:: device_queue_manager

    


.. _`device_queue_manager.definition`:

Definition
----------

.. code-block:: c

  struct device_queue_manager {
  };


.. _`device_queue_manager.members`:

Members
-------




.. _`device_queue_manager.description`:

Description
-----------


This struct is a base class for the kfd queues scheduler in the
device level. The device base class should expose the basic operations
for queue creation and queue destruction. This base class hides the
scheduling mode of the driver and the specific implementation of the
concrete device. This class is the only class in the queues scheduler
that configures the H/W.

