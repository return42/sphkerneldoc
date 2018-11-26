.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cgroup-defs.h

.. _`cgroup_threadgroup_change_begin`:

cgroup_threadgroup_change_begin
===============================

.. c:function:: void cgroup_threadgroup_change_begin(struct task_struct *tsk)

    threadgroup exclusion for cgroups

    :param tsk:
        target task
    :type tsk: struct task_struct \*

.. _`cgroup_threadgroup_change_begin.description`:

Description
-----------

Allows cgroup operations to synchronize against threadgroup changes
using a percpu_rw_semaphore.

.. _`cgroup_threadgroup_change_end`:

cgroup_threadgroup_change_end
=============================

.. c:function:: void cgroup_threadgroup_change_end(struct task_struct *tsk)

    threadgroup exclusion for cgroups

    :param tsk:
        target task
    :type tsk: struct task_struct \*

.. _`cgroup_threadgroup_change_end.description`:

Description
-----------

Counterpart of \ :c:func:`cgroup_threadcgroup_change_begin`\ .

.. This file was automatic generated / don't edit.

