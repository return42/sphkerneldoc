.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/freezer.c

.. _`freezing_slow_path`:

freezing_slow_path
==================

.. c:function:: bool freezing_slow_path(struct task_struct *p)

    slow path for testing whether a task needs to be frozen

    :param p:
        task to be tested
    :type p: struct task_struct \*

.. _`freezing_slow_path.description`:

Description
-----------

This function is called by \ :c:func:`freezing`\  if system_freezing_cnt isn't zero
and tests whether \ ``p``\  needs to enter and stay in frozen state.  Can be
called under any context.  The freezers are responsible for ensuring the
target tasks see the updated state.

.. _`freeze_task`:

freeze_task
===========

.. c:function:: bool freeze_task(struct task_struct *p)

    send a freeze request to given task

    :param p:
        task to send the request to
    :type p: struct task_struct \*

.. _`freeze_task.description`:

Description
-----------

If \ ``p``\  is freezing, the freeze request is sent either by sending a fake
signal (if it's not a kernel thread) or waking it up (if it's a kernel
thread).

.. _`freeze_task.return`:

Return
------

\ ``false``\ , if \ ``p``\  is not freezing or already frozen; \ ``true``\ , otherwise

.. _`set_freezable`:

set_freezable
=============

.. c:function:: bool set_freezable( void)

    make \ ``current``\  freezable

    :param void:
        no arguments
    :type void: 

.. _`set_freezable.description`:

Description
-----------

Mark \ ``current``\  freezable and enter refrigerator if necessary.

.. This file was automatic generated / don't edit.

