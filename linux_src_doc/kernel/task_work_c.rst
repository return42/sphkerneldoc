.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/task_work.c

.. _`task_work_add`:

task_work_add
=============

.. c:function:: int task_work_add(struct task_struct *task, struct callback_head *work, bool notify)

    ask the \ ``task``\  to execute \ ``work``\ ->\ :c:func:`func`\ 

    :param struct task_struct \*task:
        the task which should run the callback

    :param struct callback_head \*work:
        the callback to run

    :param bool notify:
        send the notification if true

.. _`task_work_add.description`:

Description
-----------

Queue \ ``work``\  for \ :c:func:`task_work_run`\  below and notify the \ ``task``\  if \ ``notify``\ .
Fails if the \ ``task``\  is exiting/exited and thus it can't process this \ ``work``\ .
Otherwise \ ``work``\ ->\ :c:func:`func`\  will be called when the \ ``task``\  returns from kernel
mode or exits.

This is like the signal handler which runs in kernel mode, but it doesn't
try to wake up the \ ``task``\ .

.. _`task_work_add.note`:

Note
----

there is no ordering guarantee on works queued here.

.. _`task_work_add.return`:

Return
------

0 if succeeds or -ESRCH.

.. _`task_work_cancel`:

task_work_cancel
================

.. c:function:: struct callback_head *task_work_cancel(struct task_struct *task, task_work_func_t func)

    cancel a pending work added by \ :c:func:`task_work_add`\ 

    :param struct task_struct \*task:
        the task which should execute the work

    :param task_work_func_t func:
        identifies the work to remove

.. _`task_work_cancel.description`:

Description
-----------

Find the last queued pending work with ->func == \ ``func``\  and remove
it from queue.

.. _`task_work_cancel.return`:

Return
------

The found work or NULL if not found.

.. _`task_work_run`:

task_work_run
=============

.. c:function:: void task_work_run( void)

    execute the works added by \ :c:func:`task_work_add`\ 

    :param  void:
        no arguments

.. _`task_work_run.description`:

Description
-----------

Flush the pending works. Should be used by the core kernel code.
Called before the task returns to the user-mode or stops, or when
it exits. In the latter case \ :c:func:`task_work_add`\  can no longer add the
new work after \ :c:func:`task_work_run`\  returns.

.. This file was automatic generated / don't edit.

