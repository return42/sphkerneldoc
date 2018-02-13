.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/padata.h

.. _`padata_priv`:

struct padata_priv
==================

.. c:type:: struct padata_priv

    Embedded to the users data structure.

.. _`padata_priv.definition`:

Definition
----------

.. code-block:: c

    struct padata_priv {
        struct list_head list;
        struct parallel_data *pd;
        int cb_cpu;
        int cpu;
        int info;
        void (*parallel)(struct padata_priv *padata);
        void (*serial)(struct padata_priv *padata);
    }

.. _`padata_priv.members`:

Members
-------

list
    List entry, to attach to the padata lists.

pd
    Pointer to the internal control structure.

cb_cpu
    Callback cpu for serializatioon.

cpu
    Cpu for parallelization.

info
    Used to pass information from the parallel to the serial function.

parallel
    Parallel execution function.

serial
    Serial complete function.

.. _`padata_list`:

struct padata_list
==================

.. c:type:: struct padata_list


.. _`padata_list.definition`:

Definition
----------

.. code-block:: c

    struct padata_list {
        struct list_head list;
        spinlock_t lock;
    }

.. _`padata_list.members`:

Members
-------

list
    List head.

lock
    List lock.

.. _`padata_serial_queue`:

struct padata_serial_queue
==========================

.. c:type:: struct padata_serial_queue

    The percpu padata serial queue

.. _`padata_serial_queue.definition`:

Definition
----------

.. code-block:: c

    struct padata_serial_queue {
        struct padata_list serial;
        struct work_struct work;
        struct parallel_data *pd;
    }

.. _`padata_serial_queue.members`:

Members
-------

serial
    List to wait for serialization after reordering.

work
    work struct for serialization.

pd
    Backpointer to the internal control structure.

.. _`padata_parallel_queue`:

struct padata_parallel_queue
============================

.. c:type:: struct padata_parallel_queue

    The percpu padata parallel queue

.. _`padata_parallel_queue.definition`:

Definition
----------

.. code-block:: c

    struct padata_parallel_queue {
        struct padata_list parallel;
        struct padata_list reorder;
        struct parallel_data *pd;
        struct work_struct work;
        struct work_struct reorder_work;
        atomic_t num_obj;
        int cpu_index;
    }

.. _`padata_parallel_queue.members`:

Members
-------

parallel
    List to wait for parallelization.

reorder
    List to wait for reordering after parallel processing.

pd
    Backpointer to the internal control structure.

work
    work struct for parallelization.

reorder_work
    work struct for reordering.

num_obj
    Number of objects that are processed by this cpu.

cpu_index
    Index of the cpu.

.. _`padata_cpumask`:

struct padata_cpumask
=====================

.. c:type:: struct padata_cpumask

    The cpumasks for the parallel/serial workers

.. _`padata_cpumask.definition`:

Definition
----------

.. code-block:: c

    struct padata_cpumask {
        cpumask_var_t pcpu;
        cpumask_var_t cbcpu;
    }

.. _`padata_cpumask.members`:

Members
-------

pcpu
    cpumask for the parallel workers.

cbcpu
    cpumask for the serial (callback) workers.

.. _`parallel_data`:

struct parallel_data
====================

.. c:type:: struct parallel_data

    Internal control structure, covers everything that depends on the cpumask in use.

.. _`parallel_data.definition`:

Definition
----------

.. code-block:: c

    struct parallel_data {
        struct padata_instance *pinst;
        struct padata_parallel_queue __percpu *pqueue;
        struct padata_serial_queue __percpu *squeue;
        atomic_t reorder_objects;
        atomic_t refcnt;
        atomic_t seq_nr;
        struct padata_cpumask cpumask;
        spinlock_t lock ____cacheline_aligned;
        unsigned int processed;
        struct timer_list timer;
    }

.. _`parallel_data.members`:

Members
-------

pinst
    padata instance.

pqueue
    percpu padata queues used for parallelization.

squeue
    percpu padata queues used for serialuzation.

reorder_objects
    Number of objects waiting in the reorder queues.

refcnt
    Number of objects holding a reference on this parallel_data.

seq_nr
    *undescribed*

cpumask
    The cpumasks in use for parallel and serial workers.

\____cacheline_aligned
    *undescribed*

processed
    Number of already processed objects.

timer
    Reorder timer.

.. _`padata_instance`:

struct padata_instance
======================

.. c:type:: struct padata_instance

    The overall control structure.

.. _`padata_instance.definition`:

Definition
----------

.. code-block:: c

    struct padata_instance {
        struct hlist_node node;
        struct workqueue_struct *wq;
        struct parallel_data *pd;
        struct padata_cpumask cpumask;
        struct blocking_notifier_head cpumask_change_notifier;
        struct kobject kobj;
        struct mutex lock;
        u8 flags;
    #define PADATA_INIT 1
    #define PADATA_RESET 2
    #define PADATA_INVALID 4
    }

.. _`padata_instance.members`:

Members
-------

node
    *undescribed*

wq
    The workqueue in use.

pd
    The internal control structure.

cpumask
    User supplied cpumasks for parallel and serial works.

cpumask_change_notifier
    Notifiers chain for user-defined notify
    callbacks that will be called when either \ ``pcpu``\  or \ ``cbcpu``\ 
    or both cpumasks change.

kobj
    padata instance kernel object.

lock
    padata instance lock.

flags
    padata flags.

.. This file was automatic generated / don't edit.

