.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/manage.c

.. _`synchronize_hardirq`:

synchronize_hardirq
===================

.. c:function:: bool synchronize_hardirq(unsigned int irq)

    wait for pending hard IRQ handlers (on other CPUs)

    :param irq:
        interrupt number to wait for
    :type irq: unsigned int

.. _`synchronize_hardirq.description`:

Description
-----------

     This function waits for any pending hard IRQ handlers for this
     interrupt to complete before returning. If you use this
     function while holding a resource the IRQ handler may need you
     will deadlock. It does not take associated threaded handlers
     into account.

     Do not use this for shutdown scenarios where you must be sure
     that all parts (hardirq and threaded handler) have completed.

.. _`synchronize_hardirq.return`:

Return
------

false if a threaded handler is active.

     This function may be called - with care - from IRQ context.

.. _`synchronize_irq`:

synchronize_irq
===============

.. c:function:: void synchronize_irq(unsigned int irq)

    wait for pending IRQ handlers (on other CPUs)

    :param irq:
        interrupt number to wait for
    :type irq: unsigned int

.. _`synchronize_irq.description`:

Description
-----------

     This function waits for any pending IRQ handlers for this interrupt
     to complete before returning. If you use this function while
     holding a resource the IRQ handler may need you will deadlock.

     This function may be called - with care - from IRQ context.

.. _`irq_can_set_affinity`:

irq_can_set_affinity
====================

.. c:function:: int irq_can_set_affinity(unsigned int irq)

    Check if the affinity of a given irq can be set

    :param irq:
        Interrupt to check
    :type irq: unsigned int

.. _`irq_can_set_affinity_usr`:

irq_can_set_affinity_usr
========================

.. c:function:: bool irq_can_set_affinity_usr(unsigned int irq)

    Check if affinity of a irq can be set from user space

    :param irq:
        Interrupt to check
    :type irq: unsigned int

.. _`irq_can_set_affinity_usr.description`:

Description
-----------

Like \ :c:func:`irq_can_set_affinity`\  above, but additionally checks for the
AFFINITY_MANAGED flag.

.. _`irq_set_thread_affinity`:

irq_set_thread_affinity
=======================

.. c:function:: void irq_set_thread_affinity(struct irq_desc *desc)

    Notify irq threads to adjust affinity

    :param desc:
        irq descriptor which has affitnity changed
    :type desc: struct irq_desc \*

.. _`irq_set_thread_affinity.description`:

Description
-----------

     We just set IRQTF_AFFINITY and delegate the affinity setting
     to the interrupt thread itself. We can not call
     \ :c:func:`set_cpus_allowed_ptr`\  here as we hold desc->lock and this
     code can be called from hard interrupt context.

.. _`irq_set_affinity_notifier`:

irq_set_affinity_notifier
=========================

.. c:function:: int irq_set_affinity_notifier(unsigned int irq, struct irq_affinity_notify *notify)

    control notification of IRQ affinity changes

    :param irq:
        Interrupt for which to enable/disable notification
    :type irq: unsigned int

    :param notify:
        Context for notification, or \ ``NULL``\  to disable
        notification.  Function pointers must be initialised;
        the other fields will be initialised by this function.
    :type notify: struct irq_affinity_notify \*

.. _`irq_set_affinity_notifier.description`:

Description
-----------

     Must be called in process context.  Notification may only be enabled
     after the IRQ is allocated and must be disabled before the IRQ is
     freed using \ :c:func:`free_irq`\ .

.. _`irq_set_vcpu_affinity`:

irq_set_vcpu_affinity
=====================

.. c:function:: int irq_set_vcpu_affinity(unsigned int irq, void *vcpu_info)

    Set vcpu affinity for the interrupt

    :param irq:
        interrupt number to set affinity
    :type irq: unsigned int

    :param vcpu_info:
        vCPU specific data or pointer to a percpu array of vCPU
        specific data for percpu_devid interrupts
    :type vcpu_info: void \*

.. _`irq_set_vcpu_affinity.description`:

Description
-----------

     This function uses the vCPU specific data to set the vCPU
     affinity for an irq. The vCPU specific data is passed from
     outside, such as KVM. One example code path is as below:
     KVM -> IOMMU -> \ :c:func:`irq_set_vcpu_affinity`\ .

.. _`disable_irq_nosync`:

disable_irq_nosync
==================

.. c:function:: void disable_irq_nosync(unsigned int irq)

    disable an irq without waiting

    :param irq:
        Interrupt to disable
    :type irq: unsigned int

.. _`disable_irq_nosync.description`:

Description
-----------

     Disable the selected interrupt line.  Disables and Enables are
     nested.
     Unlike \ :c:func:`disable_irq`\ , this function does not ensure existing
     instances of the IRQ handler have completed before returning.

     This function may be called from IRQ context.

.. _`disable_irq`:

disable_irq
===========

.. c:function:: void disable_irq(unsigned int irq)

    disable an irq and wait for completion

    :param irq:
        Interrupt to disable
    :type irq: unsigned int

.. _`disable_irq.description`:

Description
-----------

     Disable the selected interrupt line.  Enables and Disables are
     nested.
     This function waits for any pending IRQ handlers for this interrupt
     to complete before returning. If you use this function while
     holding a resource the IRQ handler may need you will deadlock.

     This function may be called - with care - from IRQ context.

.. _`disable_hardirq`:

disable_hardirq
===============

.. c:function:: bool disable_hardirq(unsigned int irq)

    disables an irq and waits for hardirq completion

    :param irq:
        Interrupt to disable
    :type irq: unsigned int

.. _`disable_hardirq.description`:

Description
-----------

     Disable the selected interrupt line.  Enables and Disables are
     nested.
     This function waits for any pending hard IRQ handlers for this
     interrupt to complete before returning. If you use this function while
     holding a resource the hard IRQ handler may need you will deadlock.

     When used to optimistically disable an interrupt from atomic context
     the return value must be checked.

.. _`disable_hardirq.return`:

Return
------

false if a threaded handler is active.

     This function may be called - with care - from IRQ context.

.. _`enable_irq`:

enable_irq
==========

.. c:function:: void enable_irq(unsigned int irq)

    enable handling of an irq

    :param irq:
        Interrupt to enable
    :type irq: unsigned int

.. _`enable_irq.description`:

Description
-----------

     Undoes the effect of one call to \ :c:func:`disable_irq`\ .  If this
     matches the last disable, processing of interrupts on this
     IRQ line is re-enabled.

     This function may be called from IRQ context only when
     desc->irq_data.chip->bus_lock and desc->chip->bus_sync_unlock are NULL !

.. _`irq_set_irq_wake`:

irq_set_irq_wake
================

.. c:function:: int irq_set_irq_wake(unsigned int irq, unsigned int on)

    control irq power management wakeup

    :param irq:
        interrupt to control
    :type irq: unsigned int

    :param on:
        enable/disable power management wakeup
    :type on: unsigned int

.. _`irq_set_irq_wake.description`:

Description
-----------

     Enable/disable power management wakeup mode, which is
     disabled by default.  Enables and disables must match,
     just as they match for non-wakeup mode support.

     Wakeup mode lets this IRQ wake the system from sleep
     states like "suspend to RAM".

.. _`irq_wake_thread`:

irq_wake_thread
===============

.. c:function:: void irq_wake_thread(unsigned int irq, void *dev_id)

    wake the irq thread for the action identified by dev_id

    :param irq:
        Interrupt line
    :type irq: unsigned int

    :param dev_id:
        Device identity for which the thread should be woken
    :type dev_id: void \*

.. _`setup_irq`:

setup_irq
=========

.. c:function:: int setup_irq(unsigned int irq, struct irqaction *act)

    setup an interrupt

    :param irq:
        Interrupt line to setup
    :type irq: unsigned int

    :param act:
        irqaction for the interrupt
    :type act: struct irqaction \*

.. _`setup_irq.description`:

Description
-----------

Used to statically setup interrupts in the early boot process.

.. _`remove_irq`:

remove_irq
==========

.. c:function:: void remove_irq(unsigned int irq, struct irqaction *act)

    free an interrupt

    :param irq:
        Interrupt line to free
    :type irq: unsigned int

    :param act:
        irqaction for the interrupt
    :type act: struct irqaction \*

.. _`remove_irq.description`:

Description
-----------

Used to remove interrupts statically setup by the early boot process.

.. _`free_irq`:

free_irq
========

.. c:function:: const void *free_irq(unsigned int irq, void *dev_id)

    free an interrupt allocated with request_irq

    :param irq:
        Interrupt line to free
    :type irq: unsigned int

    :param dev_id:
        Device identity to free
    :type dev_id: void \*

.. _`free_irq.description`:

Description
-----------

     Remove an interrupt handler. The handler is removed and if the
     interrupt line is no longer in use by any driver it is disabled.
     On a shared IRQ the caller must ensure the interrupt is disabled
     on the card it drives before calling this function. The function
     does not return until any executing interrupts for this IRQ
     have completed.

     This function must not be called from interrupt context.

     Returns the devname argument passed to request_irq.

.. _`request_threaded_irq`:

request_threaded_irq
====================

.. c:function:: int request_threaded_irq(unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char *devname, void *dev_id)

    allocate an interrupt line

    :param irq:
        Interrupt line to allocate
    :type irq: unsigned int

    :param handler:
        Function to be called when the IRQ occurs.
        Primary handler for threaded interrupts
        If NULL and thread_fn != NULL the default
        primary handler is installed
    :type handler: irq_handler_t

    :param thread_fn:
        Function called from the irq handler thread
        If NULL, no irq thread is created
    :type thread_fn: irq_handler_t

    :param irqflags:
        Interrupt type flags
    :type irqflags: unsigned long

    :param devname:
        An ascii name for the claiming device
    :type devname: const char \*

    :param dev_id:
        A cookie passed back to the handler function
    :type dev_id: void \*

.. _`request_threaded_irq.description`:

Description
-----------

     This call allocates interrupt resources and enables the
     interrupt line and IRQ handling. From the point this
     call is made your handler function may be invoked. Since
     your handler function must clear any interrupt the board
     raises, you must take care both to initialise your hardware
     and to set up the interrupt handler in the right order.

     If you want to set up a threaded irq handler for your device
     then you need to supply \ ``handler``\  and \ ``thread_fn``\ . \ ``handler``\  is
     still called in hard interrupt context and has to check
     whether the interrupt originates from the device. If yes it
     needs to disable the interrupt on the device and return
     IRQ_WAKE_THREAD which will wake up the handler thread and run
     \ ``thread_fn``\ . This split handler design is necessary to support
     shared interrupts.

     Dev_id must be globally unique. Normally the address of the
     device data structure is used as the cookie. Since the handler
     receives this value it makes sense to use it.

     If your interrupt is shared you must pass a non NULL dev_id
     as this is required when freeing the interrupt.

.. _`request_threaded_irq.flags`:

Flags
-----


     IRQF_SHARED             Interrupt is shared
     IRQF_TRIGGER_*          Specify active edge(s) or level

.. _`request_any_context_irq`:

request_any_context_irq
=======================

.. c:function:: int request_any_context_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char *name, void *dev_id)

    allocate an interrupt line

    :param irq:
        Interrupt line to allocate
    :type irq: unsigned int

    :param handler:
        Function to be called when the IRQ occurs.
        Threaded handler for threaded interrupts.
    :type handler: irq_handler_t

    :param flags:
        Interrupt type flags
    :type flags: unsigned long

    :param name:
        An ascii name for the claiming device
    :type name: const char \*

    :param dev_id:
        A cookie passed back to the handler function
    :type dev_id: void \*

.. _`request_any_context_irq.description`:

Description
-----------

     This call allocates interrupt resources and enables the
     interrupt line and IRQ handling. It selects either a
     hardirq or threaded handling method depending on the
     context.

     On failure, it returns a negative value. On success,
     it returns either IRQC_IS_HARDIRQ or IRQC_IS_NESTED.

.. _`irq_percpu_is_enabled`:

irq_percpu_is_enabled
=====================

.. c:function:: bool irq_percpu_is_enabled(unsigned int irq)

    Check whether the per cpu irq is enabled

    :param irq:
        Linux irq number to check for
    :type irq: unsigned int

.. _`irq_percpu_is_enabled.description`:

Description
-----------

Must be called from a non migratable context. Returns the enable
state of a per cpu interrupt on the current cpu.

.. _`remove_percpu_irq`:

remove_percpu_irq
=================

.. c:function:: void remove_percpu_irq(unsigned int irq, struct irqaction *act)

    free a per-cpu interrupt

    :param irq:
        Interrupt line to free
    :type irq: unsigned int

    :param act:
        irqaction for the interrupt
    :type act: struct irqaction \*

.. _`remove_percpu_irq.description`:

Description
-----------

Used to remove interrupts statically setup by the early boot process.

.. _`free_percpu_irq`:

free_percpu_irq
===============

.. c:function:: void free_percpu_irq(unsigned int irq, void __percpu *dev_id)

    free an interrupt allocated with request_percpu_irq

    :param irq:
        Interrupt line to free
    :type irq: unsigned int

    :param dev_id:
        Device identity to free
    :type dev_id: void __percpu \*

.. _`free_percpu_irq.description`:

Description
-----------

     Remove a percpu interrupt handler. The handler is removed, but
     the interrupt line is not disabled. This must be done on each
     CPU before calling this function. The function does not return
     until any executing interrupts for this IRQ have completed.

     This function must not be called from interrupt context.

.. _`setup_percpu_irq`:

setup_percpu_irq
================

.. c:function:: int setup_percpu_irq(unsigned int irq, struct irqaction *act)

    setup a per-cpu interrupt

    :param irq:
        Interrupt line to setup
    :type irq: unsigned int

    :param act:
        irqaction for the interrupt
    :type act: struct irqaction \*

.. _`setup_percpu_irq.description`:

Description
-----------

Used to statically setup per-cpu interrupts in the early boot process.

.. _`__request_percpu_irq`:

__request_percpu_irq
====================

.. c:function:: int __request_percpu_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char *devname, void __percpu *dev_id)

    allocate a percpu interrupt line

    :param irq:
        Interrupt line to allocate
    :type irq: unsigned int

    :param handler:
        Function to be called when the IRQ occurs.
    :type handler: irq_handler_t

    :param flags:
        Interrupt type flags (IRQF_TIMER only)
    :type flags: unsigned long

    :param devname:
        An ascii name for the claiming device
    :type devname: const char \*

    :param dev_id:
        A percpu cookie passed back to the handler function
    :type dev_id: void __percpu \*

.. _`__request_percpu_irq.description`:

Description
-----------

     This call allocates interrupt resources and enables the
     interrupt on the local CPU. If the interrupt is supposed to be
     enabled on other CPUs, it has to be done on each CPU using
     \ :c:func:`enable_percpu_irq`\ .

     Dev_id must be globally unique. It is a per-cpu variable, and
     the handler gets called with the interrupted CPU's instance of
     that variable.

.. _`irq_get_irqchip_state`:

irq_get_irqchip_state
=====================

.. c:function:: int irq_get_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool *state)

    returns the irqchip state of a interrupt.

    :param irq:
        Interrupt line that is forwarded to a VM
    :type irq: unsigned int

    :param which:
        One of IRQCHIP_STATE_* the caller wants to know about
    :type which: enum irqchip_irq_state

    :param state:
        a pointer to a boolean where the state is to be storeed
    :type state: bool \*

.. _`irq_get_irqchip_state.description`:

Description
-----------

     This call snapshots the internal irqchip state of an
     interrupt, returning into \ ``state``\  the bit corresponding to
     stage \ ``which``\ 

     This function should be called with preemption disabled if the
     interrupt controller has per-cpu registers.

.. _`irq_set_irqchip_state`:

irq_set_irqchip_state
=====================

.. c:function:: int irq_set_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool val)

    set the state of a forwarded interrupt.

    :param irq:
        Interrupt line that is forwarded to a VM
    :type irq: unsigned int

    :param which:
        State to be restored (one of IRQCHIP_STATE_*)
    :type which: enum irqchip_irq_state

    :param val:
        Value corresponding to \ ``which``\ 
    :type val: bool

.. _`irq_set_irqchip_state.description`:

Description
-----------

     This call sets the internal irqchip state of an interrupt,
     depending on the value of \ ``which``\ .

     This function should be called with preemption disabled if the
     interrupt controller has per-cpu registers.

.. This file was automatic generated / don't edit.

