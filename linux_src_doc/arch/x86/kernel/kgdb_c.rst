.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/kgdb.c

.. _`sleeping_thread_to_gdb_regs`:

sleeping_thread_to_gdb_regs
===========================

.. c:function:: void sleeping_thread_to_gdb_regs(unsigned long *gdb_regs, struct task_struct *p)

    Convert ptrace regs to GDB regs

    :param unsigned long \*gdb_regs:
        A pointer to hold the registers in the order GDB wants.

    :param struct task_struct \*p:
        The \ :c:type:`struct task_struct <task_struct>`\  of the desired process.

.. _`sleeping_thread_to_gdb_regs.description`:

Description
-----------

Convert the register values of the sleeping process in \ ``p``\  to
the format that GDB expects.
This function is called when kgdb does not have access to the
\ :c:type:`struct pt_regs <pt_regs>`\  and therefore it should fill the gdb registers
\ ``gdb_regs``\  with what has been saved in \ :c:type:`struct thread_struct <thread_struct>`\ 
thread field during switch_to.

.. _`kgdb_disable_hw_debug`:

kgdb_disable_hw_debug
=====================

.. c:function:: void kgdb_disable_hw_debug(struct pt_regs *regs)

    Disable hardware debugging while we in kgdb.

    :param struct pt_regs \*regs:
        Current \ :c:type:`struct pt_regs <pt_regs>`\ .

.. _`kgdb_disable_hw_debug.description`:

Description
-----------

This function will be called if the particular architecture must
disable hardware debugging while it is processing gdb packets or
handling exception.

.. _`kgdb_roundup_cpus`:

kgdb_roundup_cpus
=================

.. c:function:: void kgdb_roundup_cpus(unsigned long flags)

    Get other CPUs into a holding pattern

    :param unsigned long flags:
        Current IRQ state

.. _`kgdb_roundup_cpus.description`:

Description
-----------

On SMP systems, we need to get the attention of the other CPUs
and get them be in a known state.  This should do what is needed
to get the other CPUs to call \ :c:func:`kgdb_wait`\ . Note that on some arches,
the NMI approach is not used for rounding up all the CPUs. For example,
in case of MIPS, \ :c:func:`smp_call_function`\  is used to roundup CPUs. In
this case, we have to make sure that interrupts are enabled before
calling \ :c:func:`smp_call_function`\ . The argument to this function is
the flags that will be used when restoring the interrupts. There is
\ :c:func:`local_irq_save`\  call before \ :c:func:`kgdb_roundup_cpus`\ .

On non-SMP systems, this is not called.

.. _`kgdb_arch_handle_exception`:

kgdb_arch_handle_exception
==========================

.. c:function:: int kgdb_arch_handle_exception(int e_vector, int signo, int err_code, char *remcomInBuffer, char *remcomOutBuffer, struct pt_regs *linux_regs)

    Handle architecture specific GDB packets.

    :param int e_vector:
        The error vector of the exception that happened.

    :param int signo:
        The signal number of the exception that happened.

    :param int err_code:
        The error code of the exception that happened.

    :param char \*remcomInBuffer:
        The buffer of the packet we have read.

    :param char \*remcomOutBuffer:
        The buffer of \ ``BUFMAX``\  bytes to write a packet into.

    :param struct pt_regs \*linux_regs:
        The \ :c:type:`struct pt_regs <pt_regs>`\  of the current process.

.. _`kgdb_arch_handle_exception.description`:

Description
-----------

This function MUST handle the 'c' and 's' command packets,
as well packets to set / remove a hardware breakpoint, if used.
If there are additional packets which the hardware needs to handle,
they are handled here.  The code should return -1 if it wants to
process more packets, and a \ ``0``\  or \ ``1``\  if it wants to exit from the
kgdb callback.

.. _`kgdb_arch_init`:

kgdb_arch_init
==============

.. c:function:: int kgdb_arch_init( void)

    Perform any architecture specific initialization.

    :param  void:
        no arguments

.. _`kgdb_arch_init.description`:

Description
-----------

This function will handle the initialization of any architecture
specific callbacks.

.. _`kgdb_arch_exit`:

kgdb_arch_exit
==============

.. c:function:: void kgdb_arch_exit( void)

    Perform any architecture specific uninitalization.

    :param  void:
        no arguments

.. _`kgdb_arch_exit.description`:

Description
-----------

This function will handle the uninitalization of any architecture
specific callbacks, for dynamic registration and unregistration.

.. This file was automatic generated / don't edit.

