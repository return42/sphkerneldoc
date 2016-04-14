.. -*- coding: utf-8; mode: rst -*-

======
kgdb.h
======

.. _`kgdb_skipexception`:

kgdb_skipexception
==================

.. c:function:: int kgdb_skipexception (int exception, struct pt_regs *regs)

    (optional) exit kgdb_handle_exception early

    :param int exception:
        Exception vector number

    :param struct pt_regs \*regs:
        Current :c:type:`struct pt_regs <pt_regs>`.


.. _`kgdb_skipexception.description`:

Description
-----------

On some architectures it is required to skip a breakpoint
exception when it occurs after a breakpoint has been removed.
This can be implemented in the architecture specific portion of kgdb.


.. _`kgdb_breakpoint`:

kgdb_breakpoint
===============

.. c:function:: void kgdb_breakpoint ( void)

    compiled in breakpoint

    :param void:
        no arguments


.. _`kgdb_breakpoint.description`:

Description
-----------


This will be implemented as a static inline per architecture.  This
function is called by the kgdb core to execute an architecture
specific trap to cause kgdb to enter the exception processing.


.. _`kgdb_arch_init`:

kgdb_arch_init
==============

.. c:function:: int kgdb_arch_init ( void)

    Perform any architecture specific initalization.

    :param void:
        no arguments


.. _`kgdb_arch_init.description`:

Description
-----------


This function will handle the initalization of any architecture
specific callbacks.


.. _`kgdb_arch_exit`:

kgdb_arch_exit
==============

.. c:function:: void kgdb_arch_exit ( void)

    Perform any architecture specific uninitalization.

    :param void:
        no arguments


.. _`kgdb_arch_exit.description`:

Description
-----------


This function will handle the uninitalization of any architecture
specific callbacks, for dynamic registration and unregistration.


.. _`pt_regs_to_gdb_regs`:

pt_regs_to_gdb_regs
===================

.. c:function:: void pt_regs_to_gdb_regs (unsigned long *gdb_regs, struct pt_regs *regs)

    Convert ptrace regs to GDB regs

    :param unsigned long \*gdb_regs:
        A pointer to hold the registers in the order GDB wants.

    :param struct pt_regs \*regs:
        The :c:type:`struct pt_regs <pt_regs>` of the current process.


.. _`pt_regs_to_gdb_regs.description`:

Description
-----------

Convert the pt_regs in ``regs`` into the format for registers that
GDB expects, stored in ``gdb_regs``\ .


.. _`sleeping_thread_to_gdb_regs`:

sleeping_thread_to_gdb_regs
===========================

.. c:function:: void sleeping_thread_to_gdb_regs (unsigned long *gdb_regs, struct task_struct *p)

    Convert ptrace regs to GDB regs

    :param unsigned long \*gdb_regs:
        A pointer to hold the registers in the order GDB wants.

    :param struct task_struct \*p:
        The :c:type:`struct task_struct <task_struct>` of the desired process.


.. _`sleeping_thread_to_gdb_regs.description`:

Description
-----------

Convert the register values of the sleeping process in ``p`` to
the format that GDB expects.
This function is called when kgdb does not have access to the
:c:type:`struct pt_regs <pt_regs>` and therefore it should fill the gdb registers
``gdb_regs`` with what has        been saved in :c:type:`struct thread_struct <thread_struct>`
thread field during switch_to.


.. _`gdb_regs_to_pt_regs`:

gdb_regs_to_pt_regs
===================

.. c:function:: void gdb_regs_to_pt_regs (unsigned long *gdb_regs, struct pt_regs *regs)

    Convert GDB regs to ptrace regs.

    :param unsigned long \*gdb_regs:
        A pointer to hold the registers we've received from GDB.

    :param struct pt_regs \*regs:
        A pointer to a :c:type:`struct pt_regs <pt_regs>` to hold these values in.


.. _`gdb_regs_to_pt_regs.description`:

Description
-----------

Convert the GDB regs in ``gdb_regs`` into the pt_regs, and store them
in ``regs``\ .


.. _`kgdb_arch_handle_exception`:

kgdb_arch_handle_exception
==========================

.. c:function:: int kgdb_arch_handle_exception (int vector, int signo, int err_code, char *remcom_in_buffer, char *remcom_out_buffer, struct pt_regs *regs)

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
        The buffer of ``BUFMAX`` bytes to write a packet into.

    :param struct pt_regs \*regs:
        The :c:type:`struct pt_regs <pt_regs>` of the current process.


.. _`kgdb_arch_handle_exception.description`:

Description
-----------

This function MUST handle the 'c' and 's' command packets,
as well packets to set / remove a hardware breakpoint, if used.
If there are additional packets which the hardware needs to handle,
they are handled here.  The code should return -1 if it wants to
process more packets, and a ``0`` or ``1`` if it wants to exit from the
kgdb callback.


.. _`kgdb_roundup_cpus`:

kgdb_roundup_cpus
=================

.. c:function:: void kgdb_roundup_cpus (unsigned long flags)

    Get other CPUs into a holding pattern

    :param unsigned long flags:
        Current IRQ state


.. _`kgdb_roundup_cpus.description`:

Description
-----------

On SMP systems, we need to get the attention of the other CPUs
and get them into a known state.  This should do what is needed
to get the other CPUs to call :c:func:`kgdb_wait`. Note that on some arches,
the NMI approach is not used for rounding up all the CPUs. For example,
in case of MIPS, :c:func:`smp_call_function` is used to roundup CPUs. In
this case, we have to make sure that interrupts are enabled before
calling :c:func:`smp_call_function`. The argument to this function is
the flags that will be used when restoring the interrupts. There is
:c:func:`local_irq_save` call before :c:func:`kgdb_roundup_cpus`.

On non-SMP systems, this is not called.


.. _`kgdb_arch_set_pc`:

kgdb_arch_set_pc
================

.. c:function:: void kgdb_arch_set_pc (struct pt_regs *regs, unsigned long pc)

    Generic call back to the program counter

    :param struct pt_regs \*regs:
        Current :c:type:`struct pt_regs <pt_regs>`.

    :param unsigned long pc:
        The new value for the program counter


.. _`kgdb_arch_set_pc.description`:

Description
-----------

This function handles updating the program counter and requires an
architecture specific implementation.


.. _`kgdb_arch_late`:

kgdb_arch_late
==============

.. c:function:: void kgdb_arch_late ( void)

    Perform any architecture specific initalization.

    :param void:
        no arguments


.. _`kgdb_arch_late.description`:

Description
-----------


This function will handle the late initalization of any
architecture specific callbacks.  This is an optional function for
handling things like late initialization of hw breakpoints.  The
default implementation does nothing.


.. _`kgdb_arch`:

struct kgdb_arch
================

.. c:type:: struct kgdb_arch

    Describe architecture specific values.



Definition
----------

.. code-block:: c

  struct kgdb_arch {
    unsigned char gdb_bpt_instr[BREAK_INSTR_SIZE];
    unsigned long flags;
    int (* set_breakpoint) (unsigned long, char *);
    int (* remove_breakpoint) (unsigned long, char *);
    int (* set_hw_breakpoint) (unsigned long, int, enum kgdb_bptype);
    int (* remove_hw_breakpoint) (unsigned long, int, enum kgdb_bptype);
    void (* disable_hw_break) (struct pt_regs *regs);
    void (* remove_all_hw_break) (void);
    void (* correct_hw_break) (void);
    void (* enable_nmi) (bool on);
  };



Members
-------

:``gdb_bpt_instr[BREAK_INSTR_SIZE]``:
    The instruction to trigger a breakpoint.

:``flags``:
    Flags for the breakpoint, currently just ``KGDB_HW_BREAKPOINT``\ .

:``set_breakpoint``:
    Allow an architecture to specify how to set a software
    breakpoint.

:``remove_breakpoint``:
    Allow an architecture to specify how to remove a
    software breakpoint.

:``set_hw_breakpoint``:
    Allow an architecture to specify how to set a hardware
    breakpoint.

:``remove_hw_breakpoint``:
    Allow an architecture to specify how to remove a
    hardware breakpoint.

:``disable_hw_break``:
    Allow an architecture to specify how to disable
    hardware breakpoints for a single cpu.

:``remove_all_hw_break``:
    Allow an architecture to specify how to remove all
    hardware breakpoints.

:``correct_hw_break``:
    Allow an architecture to specify how to correct the
    hardware debug registers.

:``enable_nmi``:
    Manage NMI-triggered entry to KGDB



.. _`kgdb_io`:

struct kgdb_io
==============

.. c:type:: struct kgdb_io

    Describe the interface for an I/O driver to talk with KGDB.



Definition
----------

.. code-block:: c

  struct kgdb_io {
    const char * name;
    int (* read_char) (void);
    void (* write_char) (u8);
    void (* flush) (void);
    int (* init) (void);
    void (* pre_exception) (void);
    void (* post_exception) (void);
    int is_console;
  };



Members
-------

:``name``:
    Name of the I/O driver.

:``read_char``:
    Pointer to a function that will return one char.

:``write_char``:
    Pointer to a function that will write one char.

:``flush``:
    Pointer to a function that will flush any pending writes.

:``init``:
    Pointer to a function that will initialize the device.

:``pre_exception``:
    Pointer to a function that will do any prep work for
    the I/O driver.

:``post_exception``:
    Pointer to a function that will do any cleanup work
    for the I/O driver.

:``is_console``:
    1 if the end device is a console 0 if the I/O device is
    not a console


