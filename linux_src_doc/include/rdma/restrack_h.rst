.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/restrack.h

.. _`rdma_restrack_type`:

enum rdma_restrack_type
=======================

.. c:type:: enum rdma_restrack_type

    HW objects to track

.. _`rdma_restrack_type.definition`:

Definition
----------

.. code-block:: c

    enum rdma_restrack_type {
        RDMA_RESTRACK_PD,
        RDMA_RESTRACK_CQ,
        RDMA_RESTRACK_QP,
        RDMA_RESTRACK_CM_ID,
        RDMA_RESTRACK_MR,
        RDMA_RESTRACK_MAX
    };

.. _`rdma_restrack_type.constants`:

Constants
---------

RDMA_RESTRACK_PD
    Protection domain (PD)

RDMA_RESTRACK_CQ
    Completion queue (CQ)

RDMA_RESTRACK_QP
    Queue pair (QP)

RDMA_RESTRACK_CM_ID
    Connection Manager ID (CM_ID)

RDMA_RESTRACK_MR
    Memory Region (MR)

RDMA_RESTRACK_MAX
    Last entry, used for array dclarations

.. _`rdma_restrack_root`:

struct rdma_restrack_root
=========================

.. c:type:: struct rdma_restrack_root

    main resource tracking management entity, per-device

.. _`rdma_restrack_root.definition`:

Definition
----------

.. code-block:: c

    struct rdma_restrack_root {
        struct rw_semaphore rwsem;
        DECLARE_HASHTABLE(hash, RDMA_RESTRACK_HASH_BITS);
        int (*fill_res_entry)(struct sk_buff *msg, struct rdma_restrack_entry *entry);
    }

.. _`rdma_restrack_root.members`:

Members
-------

rwsem
    *undescribed*

hash
    global database for all resources per-device

fill_res_entry
    driver-specific fill function
    Allows rdma drivers to add their own restrack attributes.

.. _`rdma_restrack_entry`:

struct rdma_restrack_entry
==========================

.. c:type:: struct rdma_restrack_entry

    metadata per-entry

.. _`rdma_restrack_entry.definition`:

Definition
----------

.. code-block:: c

    struct rdma_restrack_entry {
        bool valid;
        struct kref kref;
        struct completion comp;
        struct task_struct *task;
        const char *kern_name;
        struct hlist_node node;
        enum rdma_restrack_type type;
    }

.. _`rdma_restrack_entry.members`:

Members
-------

valid
    validity indicator
    The entries are filled during rdma_restrack_add,
    can be attempted to be free during rdma_restrack_del.

    As an example for that, see mlx5 QPs with type MLX5_IB_QPT_HW_GSI

kref
    *undescribed*

comp
    *undescribed*

task
    owner of resource tracking entity
    There are two types of entities: created by user and created
    by kernel.

    This is relevant for the entities created by users.
    For the entities created by kernel, this pointer will be NULL.

kern_name
    name of owner for the kernel created entities.

node
    hash table entry

type
    various objects in restrack database

.. _`rdma_restrack_init`:

rdma_restrack_init
==================

.. c:function:: void rdma_restrack_init(struct rdma_restrack_root *res)

    initialize resource tracking

    :param res:
        resource tracking root
    :type res: struct rdma_restrack_root \*

.. _`rdma_restrack_clean`:

rdma_restrack_clean
===================

.. c:function:: void rdma_restrack_clean(struct rdma_restrack_root *res)

    clean resource tracking

    :param res:
        resource tracking root
    :type res: struct rdma_restrack_root \*

.. _`rdma_restrack_count`:

rdma_restrack_count
===================

.. c:function:: int rdma_restrack_count(struct rdma_restrack_root *res, enum rdma_restrack_type type, struct pid_namespace *ns)

    the current usage of specific object

    :param res:
        resource entry
    :type res: struct rdma_restrack_root \*

    :param type:
        actual type of object to operate
    :type type: enum rdma_restrack_type

    :param ns:
        PID namespace
    :type ns: struct pid_namespace \*

.. _`rdma_restrack_add`:

rdma_restrack_add
=================

.. c:function:: void rdma_restrack_add(struct rdma_restrack_entry *res)

    add object to the reource tracking database

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

.. _`rdma_restrack_del`:

rdma_restrack_del
=================

.. c:function:: void rdma_restrack_del(struct rdma_restrack_entry *res)

    delete object from the reource tracking database

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

.. _`rdma_is_kernel_res`:

rdma_is_kernel_res
==================

.. c:function:: bool rdma_is_kernel_res(struct rdma_restrack_entry *res)

    check the owner of resource

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

.. _`rdma_restrack_get`:

rdma_restrack_get
=================

.. c:function:: int rdma_restrack_get(struct rdma_restrack_entry *res)

    grab to protect resource from release

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

.. _`rdma_restrack_put`:

rdma_restrack_put
=================

.. c:function:: int rdma_restrack_put(struct rdma_restrack_entry *res)

    release resource

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

.. _`rdma_restrack_set_task`:

rdma_restrack_set_task
======================

.. c:function:: void rdma_restrack_set_task(struct rdma_restrack_entry *res, const char *caller)

    set the task for this resource

    :param res:
        resource entry
    :type res: struct rdma_restrack_entry \*

    :param caller:
        kernel name, the current task will be used if the caller is NULL.
    :type caller: const char \*

.. This file was automatic generated / don't edit.

