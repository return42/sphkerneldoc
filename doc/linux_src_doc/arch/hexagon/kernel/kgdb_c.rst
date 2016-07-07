.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/kernel/kgdb.c

.. _`hexagon_kgdb_nmi_hook`:

hexagon_kgdb_nmi_hook
=====================

.. c:function:: void hexagon_kgdb_nmi_hook(void *ignored)

    Get other CPUs into a holding pattern

    :param void \*ignored:
        *undescribed*

.. _`hexagon_kgdb_nmi_hook.description`:

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

.. c:function:: int kgdb_arch_handle_exception(int vector, int signo, int err_code, char *remcom_in_buffer, char *remcom_out_buffer, struct pt_regs *linux_regs)

    Handle architecture specific GDB packets.

    :param int vector:
        The error vector of the exception that happened.

    :param int signo:
        The signal number of the exception that happened.

    :param int err_code:
        The error code of the exception that happened.

    :param char \*remcom_in_buffer:
        The buffer of the packet we have read.

    :param char \*remcom_out_buffer:
        The buffer of \ ``BUFMAX``\  bytes to write a packet into.

    :param struct pt_regs \*linux_regs:
        *undescribed*

.. _`kgdb_arch_handle_exception.description`:

Description
-----------

This function MUST handle the 'c' and 's' command packets,
as well packets to set / remove a hardware breakpoint, if used.
If there are additional packets which the hardware needs to handle,
they are handled here.  The code should return -1 if it wants to
process more packets, and a \ ``0``\  or \ ``1``\  if it wants to exit from the
kgdb callback.

Not yet working.

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

