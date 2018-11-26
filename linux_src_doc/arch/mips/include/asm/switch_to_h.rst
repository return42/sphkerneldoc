.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/switch_to.h

.. _`resume`:

resume
======

.. c:function:: struct task_struct *resume(struct task_struct *prev, struct task_struct *next, struct thread_info *next_ti)

    resume execution of a task

    :param prev:
        The task previously executed.
    :type prev: struct task_struct \*

    :param next:
        The task to begin executing.
    :type next: struct task_struct \*

    :param next_ti:
        task_thread_info(next).
    :type next_ti: struct thread_info \*

.. _`resume.description`:

Description
-----------

This function is used whilst scheduling to save the context of prev & load
the context of next. Returns prev.

.. This file was automatic generated / don't edit.

