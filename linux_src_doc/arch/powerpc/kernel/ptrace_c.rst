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

.. _`tm_cgpr_active`:

tm_cgpr_active
==============

.. c:function:: int tm_cgpr_active(struct task_struct *target, const struct user_regset *regset)

    get active number of registers in CGPR

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

.. _`tm_cgpr_active.description`:

Description
-----------

This function checks for the active number of available
regisers in transaction checkpointed GPR category.

.. _`tm_cgpr_get`:

tm_cgpr_get
===========

.. c:function:: int tm_cgpr_get(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    get CGPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param void \*kbuf:
        Kernel buffer to copy from.

    :param void __user \*ubuf:
        User buffer to copy into.

.. _`tm_cgpr_get.description`:

Description
-----------

This function gets transaction checkpointed GPR registers.

When the transaction is active, 'ckpt_regs' holds all the checkpointed
GPR register values for the current transaction to fall back on if it
aborts in between. This function gets those checkpointed GPR registers.
The userspace interface buffer layout is as follows.

struct data {
struct pt_regs ckpt_regs;
};

.. _`tm_cfpr_active`:

tm_cfpr_active
==============

.. c:function:: int tm_cfpr_active(struct task_struct *target, const struct user_regset *regset)

    get active number of registers in CFPR

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

.. _`tm_cfpr_active.description`:

Description
-----------

This function checks for the active number of available
regisers in transaction checkpointed FPR category.

.. _`tm_cfpr_get`:

tm_cfpr_get
===========

.. c:function:: int tm_cfpr_get(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    get CFPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param void \*kbuf:
        Kernel buffer to copy from.

    :param void __user \*ubuf:
        User buffer to copy into.

.. _`tm_cfpr_get.description`:

Description
-----------

This function gets in transaction checkpointed FPR registers.

When the transaction is active 'ckfp_state' holds the checkpointed
values for the current transaction to fall back on if it aborts
in between. This function gets those checkpointed FPR registers.
The userspace interface buffer layout is as follows.

struct data {
u64     fpr[32];
u64     fpscr;
};

.. _`tm_cfpr_set`:

tm_cfpr_set
===========

.. c:function:: int tm_cfpr_set(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, const void *kbuf, const void __user *ubuf)

    set CFPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param const void \*kbuf:
        Kernel buffer to copy into.

    :param const void __user \*ubuf:
        User buffer to copy from.

.. _`tm_cfpr_set.description`:

Description
-----------

This function sets in transaction checkpointed FPR registers.

When the transaction is active 'ckfp_state' holds the checkpointed
FPR register values for the current transaction to fall back on
if it aborts in between. This function sets these checkpointed
FPR registers. The userspace interface buffer layout is as follows.

struct data {
u64     fpr[32];
u64     fpscr;
};

.. _`tm_cvmx_active`:

tm_cvmx_active
==============

.. c:function:: int tm_cvmx_active(struct task_struct *target, const struct user_regset *regset)

    get active number of registers in CVMX

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

.. _`tm_cvmx_active.description`:

Description
-----------

This function checks for the active number of available
regisers in checkpointed VMX category.

.. _`tm_cvmx_get`:

tm_cvmx_get
===========

.. c:function:: int tm_cvmx_get(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    get CMVX registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param void \*kbuf:
        Kernel buffer to copy from.

    :param void __user \*ubuf:
        User buffer to copy into.

.. _`tm_cvmx_get.description`:

Description
-----------

This function gets in transaction checkpointed VMX registers.

When the transaction is active 'ckvr_state' and 'ckvrsave' hold
the checkpointed values for the current transaction to fall
back on if it aborts in between. The userspace interface buffer
layout is as follows.

struct data {
vector128       vr[32];
vector128       vscr;
vector128       vrsave;
};

.. _`tm_cvmx_set`:

tm_cvmx_set
===========

.. c:function:: int tm_cvmx_set(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, const void *kbuf, const void __user *ubuf)

    set CMVX registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param const void \*kbuf:
        Kernel buffer to copy into.

    :param const void __user \*ubuf:
        User buffer to copy from.

.. _`tm_cvmx_set.description`:

Description
-----------

This function sets in transaction checkpointed VMX registers.

When the transaction is active 'ckvr_state' and 'ckvrsave' hold
the checkpointed values for the current transaction to fall
back on if it aborts in between. The userspace interface buffer
layout is as follows.

struct data {
vector128       vr[32];
vector128       vscr;
vector128       vrsave;
};

.. _`tm_cvsx_active`:

tm_cvsx_active
==============

.. c:function:: int tm_cvsx_active(struct task_struct *target, const struct user_regset *regset)

    get active number of registers in CVSX

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

.. _`tm_cvsx_active.description`:

Description
-----------

This function checks for the active number of available
regisers in transaction checkpointed VSX category.

.. _`tm_cvsx_get`:

tm_cvsx_get
===========

.. c:function:: int tm_cvsx_get(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    get CVSX registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param void \*kbuf:
        Kernel buffer to copy from.

    :param void __user \*ubuf:
        User buffer to copy into.

.. _`tm_cvsx_get.description`:

Description
-----------

This function gets in transaction checkpointed VSX registers.

When the transaction is active 'ckfp_state' holds the checkpointed
values for the current transaction to fall back on if it aborts
in between. This function gets those checkpointed VSX registers.
The userspace interface buffer layout is as follows.

struct data {
u64     vsx[32];
};

.. _`tm_cvsx_set`:

tm_cvsx_set
===========

.. c:function:: int tm_cvsx_set(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, const void *kbuf, const void __user *ubuf)

    set CFPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param const void \*kbuf:
        Kernel buffer to copy into.

    :param const void __user \*ubuf:
        User buffer to copy from.

.. _`tm_cvsx_set.description`:

Description
-----------

This function sets in transaction checkpointed VSX registers.

When the transaction is active 'ckfp_state' holds the checkpointed
VSX register values for the current transaction to fall back on
if it aborts in between. This function sets these checkpointed
FPR registers. The userspace interface buffer layout is as follows.

struct data {
u64     vsx[32];
};

.. _`tm_spr_active`:

tm_spr_active
=============

.. c:function:: int tm_spr_active(struct task_struct *target, const struct user_regset *regset)

    get active number of registers in TM SPR

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

.. _`tm_spr_active.description`:

Description
-----------

This function checks the active number of available
regisers in the transactional memory SPR category.

.. _`tm_spr_get`:

tm_spr_get
==========

.. c:function:: int tm_spr_get(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    get the TM related SPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param void \*kbuf:
        Kernel buffer to copy from.

    :param void __user \*ubuf:
        User buffer to copy into.

.. _`tm_spr_get.description`:

Description
-----------

This function gets transactional memory related SPR registers.
The userspace interface buffer layout is as follows.

struct {
u64             tm_tfhar;
u64             tm_texasr;
u64             tm_tfiar;
};

.. _`tm_spr_set`:

tm_spr_set
==========

.. c:function:: int tm_spr_set(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, const void *kbuf, const void __user *ubuf)

    set the TM related SPR registers

    :param struct task_struct \*target:
        The target task.

    :param const struct user_regset \*regset:
        The user regset structure.

    :param unsigned int pos:
        The buffer position.

    :param unsigned int count:
        Number of bytes to copy.

    :param const void \*kbuf:
        Kernel buffer to copy into.

    :param const void __user \*ubuf:
        User buffer to copy from.

.. _`tm_spr_set.description`:

Description
-----------

This function sets transactional memory related SPR registers.
The userspace interface buffer layout is as follows.

struct {
u64             tm_tfhar;
u64             tm_texasr;
u64             tm_tfiar;
};

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

