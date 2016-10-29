.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regset.h

.. _`user_regset_active_fn`:

user_regset_active_fn
=====================

.. c:function:: int user_regset_active_fn(struct task_struct *target, const struct user_regset *regset)

    type of \ ``active``\  function in \ :c:type:`struct user_regset <user_regset>`\ 

    :param struct task_struct \*target:
        thread being examined

    :param const struct user_regset \*regset:
        regset being examined

.. _`user_regset_active_fn.description`:

Description
-----------

Return -\ ``ENODEV``\  if not available on the hardware found.
Return \ ``0``\  if no interesting state in this thread.
Return >\ ``0``\  number of \ ``size``\  units of interesting state.
Any get call fetching state beyond that number will
see the default initialization state for this data,
so a caller that knows what the default state is need
not copy it all out.
This call is optional; the pointer is \ ``NULL``\  if there
is no inexpensive check to yield a value < \ ``n``\ .

.. _`user_regset_get_fn`:

user_regset_get_fn
==================

.. c:function:: int user_regset_get_fn(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, void *kbuf, void __user *ubuf)

    type of \ ``get``\  function in \ :c:type:`struct user_regset <user_regset>`\ 

    :param struct task_struct \*target:
        thread being examined

    :param const struct user_regset \*regset:
        regset being examined

    :param unsigned int pos:
        offset into the regset data to access, in bytes

    :param unsigned int count:
        amount of data to copy, in bytes

    :param void \*kbuf:
        if not \ ``NULL``\ , a kernel-space pointer to copy into

    :param void __user \*ubuf:
        if \ ``kbuf``\  is \ ``NULL``\ , a user-space pointer to copy into

.. _`user_regset_get_fn.description`:

Description
-----------

Fetch register values.  Return \ ``0``\  on success; -\ ``EIO``\  or -\ ``ENODEV``\ 
are usual failure returns.  The \ ``pos``\  and \ ``count``\  values are in
bytes, but must be properly aligned.  If \ ``kbuf``\  is non-null, that
buffer is used and \ ``ubuf``\  is ignored.  If \ ``kbuf``\  is \ ``NULL``\ , then
ubuf gives a userland pointer to access directly, and an -\ ``EFAULT``\ 
return value is possible.

.. _`user_regset_set_fn`:

user_regset_set_fn
==================

.. c:function:: int user_regset_set_fn(struct task_struct *target, const struct user_regset *regset, unsigned int pos, unsigned int count, const void *kbuf, const void __user *ubuf)

    type of \ ``set``\  function in \ :c:type:`struct user_regset <user_regset>`\ 

    :param struct task_struct \*target:
        thread being examined

    :param const struct user_regset \*regset:
        regset being examined

    :param unsigned int pos:
        offset into the regset data to access, in bytes

    :param unsigned int count:
        amount of data to copy, in bytes

    :param const void \*kbuf:
        if not \ ``NULL``\ , a kernel-space pointer to copy from

    :param const void __user \*ubuf:
        if \ ``kbuf``\  is \ ``NULL``\ , a user-space pointer to copy from

.. _`user_regset_set_fn.description`:

Description
-----------

Store register values.  Return \ ``0``\  on success; -\ ``EIO``\  or -\ ``ENODEV``\ 
are usual failure returns.  The \ ``pos``\  and \ ``count``\  values are in
bytes, but must be properly aligned.  If \ ``kbuf``\  is non-null, that
buffer is used and \ ``ubuf``\  is ignored.  If \ ``kbuf``\  is \ ``NULL``\ , then
ubuf gives a userland pointer to access directly, and an -\ ``EFAULT``\ 
return value is possible.

.. _`user_regset_writeback_fn`:

user_regset_writeback_fn
========================

.. c:function:: int user_regset_writeback_fn(struct task_struct *target, const struct user_regset *regset, int immediate)

    type of \ ``writeback``\  function in \ :c:type:`struct user_regset <user_regset>`\ 

    :param struct task_struct \*target:
        thread being examined

    :param const struct user_regset \*regset:
        regset being examined

    :param int immediate:
        zero if writeback at completion of next context switch is OK

.. _`user_regset_writeback_fn.description`:

Description
-----------

This call is optional; usually the pointer is \ ``NULL``\ .  When
provided, there is some user memory associated with this regset's
hardware, such as memory backing cached register data on register
window machines; the regset's data controls what user memory is
used (e.g. via the stack pointer value).

Write register data back to user memory.  If the \ ``immediate``\  flag
is nonzero, it must be written to the user memory so uaccess or
\ :c:func:`access_process_vm`\  can see it when this call returns; if zero,
then it must be written back by the time the task completes a
context switch (as synchronized with \ :c:func:`wait_task_inactive`\ ).
Return \ ``0``\  on success or if there was nothing to do, -\ ``EFAULT``\  for
a memory problem (bad stack pointer or whatever), or -\ ``EIO``\  for a
hardware problem.

.. _`user_regset`:

struct user_regset
==================

.. c:type:: struct user_regset

    accessible thread CPU state

.. _`user_regset.definition`:

Definition
----------

.. code-block:: c

    struct user_regset {
        user_regset_get_fn *get;
        user_regset_set_fn *set;
        user_regset_active_fn *active;
        user_regset_writeback_fn *writeback;
        unsigned int n;
        unsigned int size;
        unsigned int align;
        unsigned int bias;
        unsigned int core_note_type;
    }

.. _`user_regset.members`:

Members
-------

get
    Function to fetch values.

set
    Function to store values.

active
    Function to report if regset is active, or \ ``NULL``\ .

writeback
    Function to write data back to user memory, or \ ``NULL``\ .

n
    Number of slots (registers).

size
    Size in bytes of a slot (register).

align
    Required alignment, in bytes.

bias
    Bias from natural indexing.

core_note_type
    ELF note \ ``n_type``\  value used in core dumps.

.. _`user_regset.description`:

Description
-----------

This data structure describes a machine resource we call a register set.
This is part of the state of an individual thread, not necessarily
actual CPU registers per se.  A register set consists of a number of
similar slots, given by \ ``n``\ .  Each slot is \ ``size``\  bytes, and aligned to
\ ``align``\  bytes (which is at least \ ``size``\ ).

These functions must be called only on the current thread or on a
thread that is in \ ``TASK_STOPPED``\  or \ ``TASK_TRACED``\  state, that we are
guaranteed will not be woken up and return to user mode, and that we
have called \ :c:func:`wait_task_inactive`\  on.  (The target thread always might
wake up for SIGKILL while these functions are working, in which case
that thread's user_regset state might be scrambled.)

The \ ``pos``\  argument must be aligned according to \ ``align``\ ; the \ ``count``\ 
argument must be a multiple of \ ``size``\ .  These functions are not
responsible for checking for invalid arguments.

When there is a natural value to use as an index, \ ``bias``\  gives the
difference between the natural index and the slot index for the
register set.  For example, x86 GDT segment descriptors form a regset;
the segment selector produces a natural index, but only a subset of
that index space is available as a regset (the TLS slots); subtracting
\ ``bias``\  from a segment selector index value computes the regset slot.

If nonzero, \ ``core_note_type``\  gives the n_type field (NT\_\* value)
of the core file note in which this regset's data appears.
NT_PRSTATUS is a special case in that the regset data starts at
offsetof(struct elf_prstatus, pr_reg) into the note data; that is
part of the per-machine ELF formats userland knows about.  In
other cases, the core file note contains exactly the whole regset
(\ ``n``\  \* \ ``size``\ ) and nothing else.  The core file note is normally
omitted when there is an \ ``active``\  function and it returns zero.

.. _`user_regset_view`:

struct user_regset_view
=======================

.. c:type:: struct user_regset_view

    available regsets

.. _`user_regset_view.definition`:

Definition
----------

.. code-block:: c

    struct user_regset_view {
        const char *name;
        const struct user_regset *regsets;
        unsigned int n;
        u32 e_flags;
        u16 e_machine;
        u8 ei_osabi;
    }

.. _`user_regset_view.members`:

Members
-------

name
    Identifier, e.g. UTS_MACHINE string.

regsets
    Array of \ ``n``\  regsets available in this view.

n
    Number of elements in \ ``regsets``\ .

e_flags
    ELF header \ ``e_flags``\  value written in core dumps.

e_machine
    ELF header \ ``e_machine``\  \ ``EM``\ \_\* value written in core dumps.

ei_osabi
    ELF header \ ``e_ident``\ [\ ``EI_OSABI``\ ] value written in core dumps.

.. _`user_regset_view.description`:

Description
-----------

A regset view is a collection of regsets (\ :c:type:`struct user_regset <user_regset>`\ ,
above).  This describes all the state of a thread that can be seen
from a given architecture/ABI environment.  More than one view might
refer to the same \ :c:type:`struct user_regset <user_regset>`\ , or more than one regset
might refer to the same machine-specific state in the thread.  For
example, a 32-bit thread's state could be examined from the 32-bit
view or from the 64-bit view.  Either method reaches the same thread
register state, doing appropriate widening or truncation.

.. _`task_user_regset_view`:

task_user_regset_view
=====================

.. c:function:: const struct user_regset_view *task_user_regset_view(struct task_struct *tsk)

    Return the process's native regset view.

    :param struct task_struct \*tsk:
        a thread of the process in question

.. _`task_user_regset_view.description`:

Description
-----------

Return the \ :c:type:`struct user_regset_view <user_regset_view>`\  that is native for the given process.
For example, what it would access when it called \ :c:func:`ptrace`\ .
Throughout the life of the process, this only changes at exec.

.. _`copy_regset_to_user`:

copy_regset_to_user
===================

.. c:function:: int copy_regset_to_user(struct task_struct *target, const struct user_regset_view *view, unsigned int setno, unsigned int offset, unsigned int size, void __user *data)

    fetch a thread's user_regset data into user memory

    :param struct task_struct \*target:
        thread to be examined

    :param const struct user_regset_view \*view:
        \ :c:type:`struct user_regset_view <user_regset_view>`\  describing user thread machine state

    :param unsigned int setno:
        index in \ ``view``\ ->regsets

    :param unsigned int offset:
        offset into the regset data, in bytes

    :param unsigned int size:
        amount of data to copy, in bytes

    :param void __user \*data:
        user-mode pointer to copy into

.. _`copy_regset_from_user`:

copy_regset_from_user
=====================

.. c:function:: int copy_regset_from_user(struct task_struct *target, const struct user_regset_view *view, unsigned int setno, unsigned int offset, unsigned int size, const void __user *data)

    store into thread's user_regset data from user memory

    :param struct task_struct \*target:
        thread to be examined

    :param const struct user_regset_view \*view:
        \ :c:type:`struct user_regset_view <user_regset_view>`\  describing user thread machine state

    :param unsigned int setno:
        index in \ ``view``\ ->regsets

    :param unsigned int offset:
        offset into the regset data, in bytes

    :param unsigned int size:
        amount of data to copy, in bytes

    :param const void __user \*data:
        user-mode pointer to copy from

.. This file was automatic generated / don't edit.
