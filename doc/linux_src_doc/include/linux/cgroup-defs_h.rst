.. -*- coding: utf-8; mode: rst -*-

=============
cgroup-defs.h
=============


.. _`cgroup_threadgroup_change_begin`:

cgroup_threadgroup_change_begin
===============================

.. c:function:: void cgroup_threadgroup_change_begin (struct task_struct *tsk)

    threadgroup exclusion for cgroups

    :param struct task_struct \*tsk:
        target task



.. _`cgroup_threadgroup_change_begin.description`:

Description
-----------

Called from :c:func:`threadgroup_change_begin` and allows cgroup operations to
synchronize against threadgroup changes using a percpu_rw_semaphore.



.. _`cgroup_threadgroup_change_end`:

cgroup_threadgroup_change_end
=============================

.. c:function:: void cgroup_threadgroup_change_end (struct task_struct *tsk)

    threadgroup exclusion for cgroups

    :param struct task_struct \*tsk:
        target task



.. _`cgroup_threadgroup_change_end.description`:

Description
-----------

Called from :c:func:`threadgroup_change_end`.  Counterpart of
:c:func:`cgroup_threadcgroup_change_begin`.

