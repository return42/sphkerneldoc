.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/ptrace.c

.. _`regs_query_register_offset`:

regs_query_register_offset
==========================

.. c:function:: int regs_query_register_offset(const char *name)

    query register offset from its name

    :param const char \*name:
        the name of a register

.. _`regs_query_register_offset.description`:

Description
-----------

\ :c:func:`regs_query_register_offset`\  returns the offset of a register in struct
pt_regs from its name. If the name is invalid, this returns -EINVAL;

.. _`regs_query_register_name`:

regs_query_register_name
========================

.. c:function:: const char *regs_query_register_name(unsigned int offset)

    query register name from its offset

    :param unsigned int offset:
        the offset of a register in struct pt_regs.

.. _`regs_query_register_name.description`:

Description
-----------

\ :c:func:`regs_query_register_name`\  returns the name of a register from its
offset in struct pt_regs. If the \ ``offset``\  is invalid, this returns NULL;

.. _`do_syscall_trace_enter`:

do_syscall_trace_enter
======================

.. c:function:: long do_syscall_trace_enter(struct pt_regs *regs)

    Do syscall tracing on kernel entry.

    :param struct pt_regs \*regs:
        the pt_regs of the task to trace (current)

.. _`do_syscall_trace_enter.description`:

Description
-----------

Performs various types of tracing on syscall entry. This includes seccomp,
ptrace, syscall tracepoints and audit.

The pt_regs are potentially visible to userspace via ptrace, so their
contents is ABI.

One or more of the tracers may modify the contents of pt_regs, in particular
to modify arguments or even the syscall number itself.

It's also possible that a tracer can choose to reject the system call. In
that case this function will return an illegal syscall number, and will put
an appropriate return value in regs->r3.

.. _`do_syscall_trace_enter.return`:

Return
------

the (possibly changed) syscall number.

.. This file was automatic generated / don't edit.

