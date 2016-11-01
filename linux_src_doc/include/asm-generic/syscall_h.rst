.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/syscall.h

.. _`syscall_get_nr`:

syscall_get_nr
==============

.. c:function:: int syscall_get_nr(struct task_struct *task, struct pt_regs *regs)

    find what system call a task is executing

    :param struct task_struct \*task:
        task of interest, must be blocked

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

.. _`syscall_get_nr.description`:

Description
-----------

If \ ``task``\  is executing a system call or is at system call
tracing about to attempt one, returns the system call number.
If \ ``task``\  is not executing a system call, i.e. it's blocked
inside the kernel for a fault or signal, returns -1.

Note this returns int even on 64-bit machines.  Only 32 bits of
system call number can be meaningful.  If the actual arch value
is 64 bits, this truncates to 32 bits so 0xffffffff means -1.

It's only valid to call this when \ ``task``\  is known to be blocked.

.. _`syscall_rollback`:

syscall_rollback
================

.. c:function:: void syscall_rollback(struct task_struct *task, struct pt_regs *regs)

    roll back registers after an aborted system call

    :param struct task_struct \*task:
        task of interest, must be in system call exit tracing

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

.. _`syscall_rollback.description`:

Description
-----------

It's only valid to call this when \ ``task``\  is stopped for system
call exit tracing (due to TIF_SYSCALL_TRACE or TIF_SYSCALL_AUDIT),
after \ :c:func:`tracehook_report_syscall_entry`\  returned nonzero to prevent
the system call from taking place.

This rolls back the register state in \ ``regs``\  so it's as if the
system call instruction was a no-op.  The registers containing
the system call number and arguments are as they were before the
system call instruction.  This may not be the same as what the
register state looked like at system call entry tracing.

.. _`syscall_get_error`:

syscall_get_error
=================

.. c:function:: long syscall_get_error(struct task_struct *task, struct pt_regs *regs)

    check result of traced system call

    :param struct task_struct \*task:
        task of interest, must be blocked

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

.. _`syscall_get_error.description`:

Description
-----------

Returns 0 if the system call succeeded, or -ERRORCODE if it failed.

It's only valid to call this when \ ``task``\  is stopped for tracing on exit
from a system call, due to \ ``TIF_SYSCALL_TRACE``\  or \ ``TIF_SYSCALL_AUDIT``\ .

.. _`syscall_get_return_value`:

syscall_get_return_value
========================

.. c:function:: long syscall_get_return_value(struct task_struct *task, struct pt_regs *regs)

    get the return value of a traced system call

    :param struct task_struct \*task:
        task of interest, must be blocked

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

.. _`syscall_get_return_value.description`:

Description
-----------

Returns the return value of the successful system call.
This value is meaningless if \ :c:func:`syscall_get_error`\  returned nonzero.

It's only valid to call this when \ ``task``\  is stopped for tracing on exit
from a system call, due to \ ``TIF_SYSCALL_TRACE``\  or \ ``TIF_SYSCALL_AUDIT``\ .

.. _`syscall_set_return_value`:

syscall_set_return_value
========================

.. c:function:: void syscall_set_return_value(struct task_struct *task, struct pt_regs *regs, int error, long val)

    change the return value of a traced system call

    :param struct task_struct \*task:
        task of interest, must be blocked

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

    :param int error:
        negative error code, or zero to indicate success

    :param long val:
        user return value if \ ``error``\  is zero

.. _`syscall_set_return_value.description`:

Description
-----------

This changes the results of the system call that user mode will see.
If \ ``error``\  is zero, the user sees a successful system call with a
return value of \ ``val``\ .  If \ ``error``\  is nonzero, it's a negated errno
code; the user sees a failed system call with this errno code.

It's only valid to call this when \ ``task``\  is stopped for tracing on exit
from a system call, due to \ ``TIF_SYSCALL_TRACE``\  or \ ``TIF_SYSCALL_AUDIT``\ .

.. _`syscall_get_arguments`:

syscall_get_arguments
=====================

.. c:function:: void syscall_get_arguments(struct task_struct *task, struct pt_regs *regs, unsigned int i, unsigned int n, unsigned long *args)

    extract system call parameter values

    :param struct task_struct \*task:
        task of interest, must be blocked

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

    :param unsigned int i:
        argument index [0,5]

    :param unsigned int n:
        number of arguments; n+i must be [1,6].

    :param unsigned long \*args:
        array filled with argument values

.. _`syscall_get_arguments.description`:

Description
-----------

Fetches \ ``n``\  arguments to the system call starting with the \ ``i``\ 'th argument
(from 0 through 5).  Argument \ ``i``\  is stored in \ ``args``\ [0], and so on.
An arch inline version is probably optimal when \ ``i``\  and \ ``n``\  are constants.

It's only valid to call this when \ ``task``\  is stopped for tracing on
entry to a system call, due to \ ``TIF_SYSCALL_TRACE``\  or \ ``TIF_SYSCALL_AUDIT``\ .
It's invalid to call this with \ ``i``\  + \ ``n``\  > 6; we only support system calls
taking up to 6 arguments.

.. _`syscall_set_arguments`:

syscall_set_arguments
=====================

.. c:function:: void syscall_set_arguments(struct task_struct *task, struct pt_regs *regs, unsigned int i, unsigned int n, const unsigned long *args)

    change system call parameter value

    :param struct task_struct \*task:
        task of interest, must be in system call entry tracing

    :param struct pt_regs \*regs:
        task_pt_regs() of \ ``task``\ 

    :param unsigned int i:
        argument index [0,5]

    :param unsigned int n:
        number of arguments; n+i must be [1,6].

    :param const unsigned long \*args:
        array of argument values to store

.. _`syscall_set_arguments.description`:

Description
-----------

Changes \ ``n``\  arguments to the system call starting with the \ ``i``\ 'th argument.
Argument \ ``i``\  gets value \ ``args``\ [0], and so on.
An arch inline version is probably optimal when \ ``i``\  and \ ``n``\  are constants.

It's only valid to call this when \ ``task``\  is stopped for tracing on
entry to a system call, due to \ ``TIF_SYSCALL_TRACE``\  or \ ``TIF_SYSCALL_AUDIT``\ .
It's invalid to call this with \ ``i``\  + \ ``n``\  > 6; we only support system calls
taking up to 6 arguments.

.. _`syscall_get_arch`:

syscall_get_arch
================

.. c:function:: int syscall_get_arch( void)

    return the AUDIT_ARCH for the current system call

    :param  void:
        no arguments

.. _`syscall_get_arch.description`:

Description
-----------

Returns the AUDIT_ARCH\_\* based on the system call convention in use.

It's only valid to call this when current is stopped on entry to a system
call, due to \ ``TIF_SYSCALL_TRACE``\ , \ ``TIF_SYSCALL_AUDIT``\ , or \ ``TIF_SECCOMP``\ .

Architectures which permit CONFIG_HAVE_ARCH_SECCOMP_FILTER must
provide an implementation of this.

.. This file was automatic generated / don't edit.

