.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/kernel/smp.c

.. _`init_ipi`:

init_ipi
========

.. c:function:: void init_ipi( void)

    Initialise the IPI mechanism

    :param  void:
        no arguments

.. _`mn10300_ipi_shutdown`:

mn10300_ipi_shutdown
====================

.. c:function:: void mn10300_ipi_shutdown(unsigned int irq)

    Shut down handling of an IPI

    :param unsigned int irq:
        The IPI to be shut down.

.. _`mn10300_ipi_enable`:

mn10300_ipi_enable
==================

.. c:function:: void mn10300_ipi_enable(unsigned int irq)

    Enable an IPI

    :param unsigned int irq:
        The IPI to be enabled.

.. _`mn10300_ipi_disable`:

mn10300_ipi_disable
===================

.. c:function:: void mn10300_ipi_disable(unsigned int irq)

    Disable an IPI

    :param unsigned int irq:
        The IPI to be disabled.

.. _`mn10300_ipi_ack`:

mn10300_ipi_ack
===============

.. c:function:: void mn10300_ipi_ack(struct irq_data *d)

    Acknowledge an IPI interrupt in the PIC

    :param struct irq_data \*d:
        *undescribed*

.. _`mn10300_ipi_ack.description`:

Description
-----------

Clear the interrupt detection flag for the IPI on the appropriate interrupt
channel in the PIC.

.. _`mn10300_ipi_nop`:

mn10300_ipi_nop
===============

.. c:function:: void mn10300_ipi_nop(struct irq_data *d)

    Dummy IPI action

    :param struct irq_data \*d:
        *undescribed*

.. _`send_ipi_mask`:

send_IPI_mask
=============

.. c:function:: void send_IPI_mask(const cpumask_t *cpumask, int irq)

    Send IPIs to all CPUs in list

    :param const cpumask_t \*cpumask:
        The list of CPUs to target.

    :param int irq:
        The IPI request to be sent.

.. _`send_ipi_mask.description`:

Description
-----------

Send the specified IPI to all the CPUs in the list, not waiting for them to
finish before returning.  The caller is responsible for synchronisation if
that is needed.

.. _`send_ipi_self`:

send_IPI_self
=============

.. c:function:: void send_IPI_self(int irq)

    Send an IPI to this CPU.

    :param int irq:
        The IPI request to be sent.

.. _`send_ipi_self.description`:

Description
-----------

Send the specified IPI to the current CPU.

.. _`send_ipi_allbutself`:

send_IPI_allbutself
===================

.. c:function:: void send_IPI_allbutself(int irq)

    Send IPIs to all the other CPUs.

    :param int irq:
        The IPI request to be sent.

.. _`send_ipi_allbutself.description`:

Description
-----------

Send the specified IPI to all CPUs in the system barring the current one,
not waiting for them to finish before returning.  The caller is responsible
for synchronisation if that is needed.

.. _`smp_send_reschedule`:

smp_send_reschedule
===================

.. c:function:: void smp_send_reschedule(int cpu)

    Send reschedule IPI to a CPU

    :param int cpu:
        The CPU to target.

.. _`smp_nmi_call_function`:

smp_nmi_call_function
=====================

.. c:function:: int smp_nmi_call_function(smp_call_func_t func, void *info, int wait)

    Send a call function NMI IPI to all CPUs

    :param smp_call_func_t func:
        The function to ask to be run.

    :param void \*info:
        The context data to pass to that function.

    :param int wait:
        If true, wait (atomically) until function is run on all CPUs.

.. _`smp_nmi_call_function.description`:

Description
-----------

Send a non-maskable request to all CPUs in the system, requesting them to
run the specified function with the given context data, and, potentially, to
wait for completion of that function on all CPUs.

Returns 0 if successful, -ETIMEDOUT if we were asked to wait, but hit the
timeout.

.. _`smp_jump_to_debugger`:

smp_jump_to_debugger
====================

.. c:function:: void smp_jump_to_debugger( void)

    Make other CPUs enter the debugger by sending an IPI

    :param  void:
        no arguments

.. _`smp_jump_to_debugger.description`:

Description
-----------

Send a non-maskable request to all other CPUs in the system, instructing
them to jump into the debugger.  The caller is responsible for checking that
the other CPUs responded to the instruction.

The caller should make sure that this CPU's debugger IPI is disabled.

.. _`stop_this_cpu`:

stop_this_cpu
=============

.. c:function:: void stop_this_cpu(void *unused)

    Callback to stop a CPU.

    :param void \*unused:
        Callback context (ignored).

.. _`smp_send_stop`:

smp_send_stop
=============

.. c:function:: void smp_send_stop( void)

    Send a stop request to all CPUs.

    :param  void:
        no arguments

.. _`smp_reschedule_interrupt`:

smp_reschedule_interrupt
========================

.. c:function:: irqreturn_t smp_reschedule_interrupt(int irq, void *dev_id)

    Reschedule IPI handler

    :param int irq:
        The interrupt number.

    :param void \*dev_id:
        The device ID.

.. _`smp_reschedule_interrupt.description`:

Description
-----------

Returns IRQ_HANDLED to indicate we handled the interrupt successfully.

.. _`smp_call_function_interrupt`:

smp_call_function_interrupt
===========================

.. c:function:: irqreturn_t smp_call_function_interrupt(int irq, void *dev_id)

    Call function IPI handler

    :param int irq:
        The interrupt number.

    :param void \*dev_id:
        The device ID.

.. _`smp_call_function_interrupt.description`:

Description
-----------

Returns IRQ_HANDLED to indicate we handled the interrupt successfully.

.. _`smp_nmi_call_function_interrupt`:

smp_nmi_call_function_interrupt
===============================

.. c:function:: void smp_nmi_call_function_interrupt( void)

    Non-maskable call function IPI handler

    :param  void:
        no arguments

.. _`smp_ipi_timer_interrupt`:

smp_ipi_timer_interrupt
=======================

.. c:function:: irqreturn_t smp_ipi_timer_interrupt(int irq, void *dev_id)

    Local timer IPI handler

    :param int irq:
        The interrupt number.

    :param void \*dev_id:
        The device ID.

.. _`smp_ipi_timer_interrupt.description`:

Description
-----------

Returns IRQ_HANDLED to indicate we handled the interrupt successfully.

.. _`smp_cpu_init`:

smp_cpu_init
============

.. c:function:: void smp_cpu_init( void)

    Initialise AP in start_secondary.

    :param  void:
        no arguments

.. _`smp_cpu_init.description`:

Description
-----------

For this Application Processor, set up init_mm, initialise FPU and set
interrupt level 0-6 setting.

.. _`smp_prepare_cpu_init`:

smp_prepare_cpu_init
====================

.. c:function:: void smp_prepare_cpu_init( void)

    Initialise CPU in startup_secondary

    :param  void:
        no arguments

.. _`smp_prepare_cpu_init.description`:

Description
-----------

Set interrupt level 0-6 setting and init ICR of the kernel debugger.

.. _`start_secondary`:

start_secondary
===============

.. c:function:: int start_secondary(void *unused)

    Activate a secondary CPU (AP)

    :param void \*unused:
        Thread parameter (ignored).

.. _`smp_prepare_cpus`:

smp_prepare_cpus
================

.. c:function:: void smp_prepare_cpus(unsigned int max_cpus)

    Boot up secondary CPUs (APs)

    :param unsigned int max_cpus:
        Maximum number of CPUs to boot.

.. _`smp_prepare_cpus.description`:

Description
-----------

Call do_boot_cpu, and boot up APs.

.. _`smp_store_cpu_info`:

smp_store_cpu_info
==================

.. c:function:: void smp_store_cpu_info(int cpu)

    Save a CPU's information

    :param int cpu:
        The CPU to save for.

.. _`smp_store_cpu_info.description`:

Description
-----------

Save boot_cpu_data and jiffy for the specified CPU.

.. _`smp_tune_scheduling`:

smp_tune_scheduling
===================

.. c:function:: void smp_tune_scheduling( void)

    Set time slice value

    :param  void:
        no arguments

.. _`smp_tune_scheduling.description`:

Description
-----------

Nothing to do here.

.. _`do_boot_cpu`:

do_boot_cpu
===========

.. c:function:: int do_boot_cpu(int phy_id)

    Boot up one CPU

    :param int phy_id:
        Physical ID of CPU to boot.

.. _`do_boot_cpu.description`:

Description
-----------

Send an IPI to a secondary CPU to boot it.  Returns 0 on success, 1
otherwise.

.. _`smp_show_cpu_info`:

smp_show_cpu_info
=================

.. c:function:: void smp_show_cpu_info(int cpu)

    Show SMP CPU information

    :param int cpu:
        The CPU of interest.

.. _`smp_callin`:

smp_callin
==========

.. c:function:: void smp_callin( void)

    Set cpu_callin_map of the current CPU ID

    :param  void:
        no arguments

.. _`smp_online`:

smp_online
==========

.. c:function:: void smp_online( void)

    Set cpu_online_mask

    :param  void:
        no arguments

.. _`smp_cpus_done`:

smp_cpus_done
=============

.. c:function:: void smp_cpus_done(unsigned int max_cpus)

    :param unsigned int max_cpus:
        Maximum CPU count.

.. _`smp_cpus_done.description`:

Description
-----------

Do nothing.

.. _`__cpu_up`:

\__cpu_up
=========

.. c:function:: int __cpu_up(unsigned int cpu, struct task_struct *tidle)

    Set smp_commenced_mask for the nominated CPU

    :param unsigned int cpu:
        The target CPU.

    :param struct task_struct \*tidle:
        *undescribed*

.. _`setup_profiling_timer`:

setup_profiling_timer
=====================

.. c:function:: int setup_profiling_timer(unsigned int multiplier)

    Set up the profiling timer \ ``multiplier``\  - The frequency multiplier to use

    :param unsigned int multiplier:
        *undescribed*

.. _`setup_profiling_timer.description`:

Description
-----------

The frequency of the profiling timer can be changed by writing a multiplier
value into /proc/profile.

.. _`hotplug_cpu_nmi_call_function`:

hotplug_cpu_nmi_call_function
=============================

.. c:function:: int hotplug_cpu_nmi_call_function(cpumask_t cpumask, smp_call_func_t func, void *info, int wait)

    Call a function on other CPUs for hotplug

    :param cpumask_t cpumask:
        List of target CPUs.

    :param smp_call_func_t func:
        The function to call on those CPUs.

    :param void \*info:
        The context data for the function to be called.

    :param int wait:
        Whether to wait for the calls to complete.

.. _`hotplug_cpu_nmi_call_function.description`:

Description
-----------

Non-maskably call a function on another CPU for hotplug purposes.

This function must be called with maskable interrupts disabled.

.. This file was automatic generated / don't edit.

