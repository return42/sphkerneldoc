.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/interrupt.h

.. _`irqaction`:

struct irqaction
================

.. c:type:: struct irqaction

    per interrupt action descriptor

.. _`irqaction.definition`:

Definition
----------

.. code-block:: c

    struct irqaction {
        irq_handler_t handler;
        void *dev_id;
        void __percpu *percpu_dev_id;
        struct irqaction *next;
        irq_handler_t thread_fn;
        struct task_struct *thread;
        struct irqaction *secondary;
        unsigned int irq;
        unsigned int flags;
        unsigned long thread_flags;
        unsigned long thread_mask;
        const char *name;
        struct proc_dir_entry *dir;
    }

.. _`irqaction.members`:

Members
-------

handler
    interrupt handler function

dev_id
    cookie to identify the device

percpu_dev_id
    cookie to identify the device

next
    pointer to the next irqaction for shared interrupts

thread_fn
    interrupt handler function for threaded interrupts

thread
    thread pointer for threaded interrupts

secondary
    pointer to secondary irqaction (force threading)

irq
    interrupt number

flags
    flags (see IRQF\_\* above)

thread_flags
    flags related to \ ``thread``\ 

thread_mask
    bitmask for keeping track of \ ``thread``\  activity

name
    name of the device

dir
    pointer to the proc/irq/NN/name entry

.. _`irq_affinity_notify`:

struct irq_affinity_notify
==========================

.. c:type:: struct irq_affinity_notify

    context for notification of IRQ affinity changes

.. _`irq_affinity_notify.definition`:

Definition
----------

.. code-block:: c

    struct irq_affinity_notify {
        unsigned int irq;
        struct kref kref;
        struct work_struct work;
        void (*notify)(struct irq_affinity_notify *, const cpumask_t *mask);
        void (*release)(struct kref *ref);
    }

.. _`irq_affinity_notify.members`:

Members
-------

irq
    Interrupt to which notification applies

kref
    Reference count, for internal use

work
    Work item, for internal use

notify
    Function to be called on change.  This will be
    called in process context.

release
    Function to be called on release.  This will be
    called in process context.  Once registered, the
    structure must only be freed when this function is
    called or later.

.. _`irq_set_affinity`:

irq_set_affinity
================

.. c:function:: int irq_set_affinity(unsigned int irq, const struct cpumask *cpumask)

    Set the irq affinity of a given irq

    :param unsigned int irq:
        Interrupt to set affinity

    :param const struct cpumask \*cpumask:
        cpumask

.. _`irq_set_affinity.description`:

Description
-----------

Fails if cpumask does not contain an online CPU

.. _`irq_force_affinity`:

irq_force_affinity
==================

.. c:function:: int irq_force_affinity(unsigned int irq, const struct cpumask *cpumask)

    Force the irq affinity of a given irq

    :param unsigned int irq:
        Interrupt to set affinity

    :param const struct cpumask \*cpumask:
        cpumask

.. _`irq_force_affinity.description`:

Description
-----------

Same as irq_set_affinity, but without checking the mask against
online cpus.

Solely for low level cpu hotplug code, where we need to make per
cpu interrupts affine before the cpu becomes online.

.. This file was automatic generated / don't edit.

