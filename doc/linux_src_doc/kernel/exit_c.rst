.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/exit.c

.. _`wait_task_stopped`:

wait_task_stopped
=================

.. c:function:: int wait_task_stopped(struct wait_opts *wo, int ptrace, struct task_struct *p)

    Wait for \ ``TASK_STOPPED``\  or \ ``TASK_TRACED``\ 

    :param struct wait_opts \*wo:
        wait options

    :param int ptrace:
        is the wait for ptrace

    :param struct task_struct \*p:
        task to wait for

.. _`wait_task_stopped.description`:

Description
-----------

Handle \ :c:func:`sys_wait4`\  work for \ ``p``\  in state \ ``TASK_STOPPED``\  or \ ``TASK_TRACED``\ .

.. _`wait_task_stopped.context`:

Context
-------

read_lock(\ :c:type:`struct tasklist_lock <tasklist_lock>`), which is released if return value is
non-zero.  Also, grabs and releases \ ``p``\ ->sighand->siglock.

.. _`wait_task_stopped.return`:

Return
------

0 if wait condition didn't exist and search for other wait conditions
should continue.  Non-zero return, -errno on failure and \ ``p``\ 's pid on
success, implies that tasklist_lock is released and wait condition
search should terminate.

.. This file was automatic generated / don't edit.

