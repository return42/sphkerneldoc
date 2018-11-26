.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/fork.c

.. _`set_mm_exe_file`:

set_mm_exe_file
===============

.. c:function:: void set_mm_exe_file(struct mm_struct *mm, struct file *new_exe_file)

    change a reference to the mm's executable file

    :param mm:
        *undescribed*
    :type mm: struct mm_struct \*

    :param new_exe_file:
        *undescribed*
    :type new_exe_file: struct file \*

.. _`set_mm_exe_file.description`:

Description
-----------

This changes mm's executable file (shown as symlink /proc/[pid]/exe).

Main users are \ :c:func:`mmput`\  and \ :c:func:`sys_execve`\ . Callers prevent concurrent

.. _`set_mm_exe_file.invocations`:

invocations
-----------

in \ :c:func:`mmput`\  nobody alive left, in execve task is single
threaded. sys_prctl(PR_SET_MM_MAP/EXE_FILE) also needs to set the
mm->exe_file, but does so without using \ :c:func:`set_mm_exe_file`\  in order
to do avoid the need for any locks.

.. _`get_mm_exe_file`:

get_mm_exe_file
===============

.. c:function:: struct file *get_mm_exe_file(struct mm_struct *mm)

    acquire a reference to the mm's executable file

    :param mm:
        *undescribed*
    :type mm: struct mm_struct \*

.. _`get_mm_exe_file.description`:

Description
-----------

Returns \ ``NULL``\  if mm has no associated executable file.
User must release file via \ :c:func:`fput`\ .

.. _`get_task_exe_file`:

get_task_exe_file
=================

.. c:function:: struct file *get_task_exe_file(struct task_struct *task)

    acquire a reference to the task's executable file

    :param task:
        *undescribed*
    :type task: struct task_struct \*

.. _`get_task_exe_file.description`:

Description
-----------

Returns \ ``NULL``\  if task's mm (if any) has no associated executable file or
this is a kernel thread with borrowed mm (see the comment above get_task_mm).
User must release file via \ :c:func:`fput`\ .

.. _`get_task_mm`:

get_task_mm
===========

.. c:function:: struct mm_struct *get_task_mm(struct task_struct *task)

    acquire a reference to the task's mm

    :param task:
        *undescribed*
    :type task: struct task_struct \*

.. _`get_task_mm.description`:

Description
-----------

Returns \ ``NULL``\  if the task has no mm.  Checks PF_KTHREAD (meaning
this kernel workthread has transiently adopted a user mm with use_mm,
to do its AIO) is not set and if so returns a reference to it, after
bumping up the use count.  User must release the mm via \ :c:func:`mmput`\ 
after use.  Typically used by /proc and ptrace.

.. This file was automatic generated / don't edit.

