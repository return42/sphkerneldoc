.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/irqdesc.h

.. _`irq_desc`:

struct irq_desc
===============

.. c:type:: struct irq_desc

    interrupt descriptor

.. _`irq_desc.definition`:

Definition
----------

.. code-block:: c

    struct irq_desc {
        struct irq_common_data irq_common_data;
        struct irq_data irq_data;
        unsigned int __percpu *kstat_irqs;
        irq_flow_handler_t handle_irq;
        #ifdef CONFIG_IRQ_PREFLOW_FASTEOI
        irq_preflow_handler_t preflow_handler;
        #endif
        struct irqaction *action;
        unsigned int status_use_accessors;
        unsigned int core_internal_state__do_not_mess_with_it;
        unsigned int depth;
        unsigned int wake_depth;
        unsigned int irq_count;
        unsigned long last_unhandled;
        unsigned int irqs_unhandled;
        atomic_t threads_handled;
        int threads_handled_last;
        raw_spinlock_t lock;
        struct cpumask *percpu_enabled;
        const struct cpumask *percpu_affinity;
        #ifdef CONFIG_SMP
        const struct cpumask *affinity_hint;
        struct irq_affinity_notify *affinity_notify;
        #ifdef CONFIG_GENERIC_PENDING_IRQ
        cpumask_var_t pending_mask;
        #endif
        #endif
        unsigned long threads_oneshot;
        atomic_t threads_active;
        wait_queue_head_t wait_for_threads;
        #ifdef CONFIG_PM_SLEEP
        unsigned int nr_actions;
        unsigned int no_suspend_depth;
        unsigned int cond_suspend_depth;
        unsigned int force_resume_depth;
        #endif
        #ifdef CONFIG_PROC_FS
        struct proc_dir_entry *dir;
        #endif
        #ifdef CONFIG_SPARSE_IRQ
        struct rcu_head rcu;
        #endif
        int parent_irq;
        struct module *owner;
        const char *name;
    }

.. _`irq_desc.members`:

Members
-------

irq_common_data
    per irq and chip data passed down to chip functions

irq_data
    *undescribed*

kstat_irqs
    irq stats per cpu

handle_irq
    highlevel irq-events handler

preflow_handler
    handler called before the flow handler (currently used by sparc)

action
    the irq action chain

status_use_accessors
    *undescribed*

core_internal_state__do_not_mess_with_it
    core internal status information

depth
    disable-depth, for nested \ :c:func:`irq_disable`\  calls

wake_depth
    enable depth, for multiple \ :c:func:`irq_set_irq_wake`\  callers

irq_count
    stats field to detect stalled irqs

last_unhandled
    aging timer for unhandled count

irqs_unhandled
    stats field for spurious unhandled interrupts

threads_handled
    stats field for deferred spurious detection of threaded handlers

threads_handled_last
    comparator field for deferred spurious detection of theraded handlers

lock
    locking for SMP

percpu_enabled
    *undescribed*

percpu_affinity
    *undescribed*

affinity_hint
    hint to user space for preferred irq affinity

affinity_notify
    context for notification of affinity changes

pending_mask
    pending rebalanced interrupts

threads_oneshot
    bitfield to handle shared oneshot threads

threads_active
    number of irqaction threads currently running

wait_for_threads
    wait queue for sync_irq to wait for threaded handlers

nr_actions
    number of installed actions on this descriptor

no_suspend_depth
    number of irqactions on a irq descriptor with
    IRQF_NO_SUSPEND set

cond_suspend_depth
    *undescribed*

force_resume_depth
    number of irqactions on a irq descriptor with
    IRQF_FORCE_RESUME set

dir
    /proc/irq/ procfs entry

rcu
    rcu head for delayed free

parent_irq
    *undescribed*

owner
    *undescribed*

name
    flow handler name for /proc/interrupts output

.. _`irq_set_handler_locked`:

irq_set_handler_locked
======================

.. c:function:: void irq_set_handler_locked(struct irq_data *data, irq_flow_handler_t handler)

    Set irq handler from a locked region

    :param struct irq_data \*data:
        Pointer to the irq_data structure which identifies the irq

    :param irq_flow_handler_t handler:
        Flow control handler function for this interrupt

.. _`irq_set_handler_locked.description`:

Description
-----------

Sets the handler in the irq descriptor associated to \ ``data``\ .

Must be called with irq_desc locked and valid parameters. Typical
call site is the \ :c:func:`irq_set_type`\  callback.

.. _`irq_set_chip_handler_name_locked`:

irq_set_chip_handler_name_locked
================================

.. c:function:: void irq_set_chip_handler_name_locked(struct irq_data *data, struct irq_chip *chip, irq_flow_handler_t handler, const char *name)

    Set chip, handler and name from a locked region

    :param struct irq_data \*data:
        Pointer to the irq_data structure for which the chip is set

    :param struct irq_chip \*chip:
        Pointer to the new irq chip

    :param irq_flow_handler_t handler:
        Flow control handler function for this interrupt

    :param const char \*name:
        Name of the interrupt

.. _`irq_set_chip_handler_name_locked.description`:

Description
-----------

Replace the irq chip at the proper hierarchy level in \ ``data``\  and
sets the handler and name in the associated irq descriptor.

Must be called with irq_desc locked and valid parameters.

.. This file was automatic generated / don't edit.

