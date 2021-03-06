.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/cgroup-v1.c

.. _`cgroup_attach_task_all`:

cgroup_attach_task_all
======================

.. c:function:: int cgroup_attach_task_all(struct task_struct *from, struct task_struct *tsk)

    attach task 'tsk' to all cgroups of task 'from'

    :param from:
        attach to all cgroups of a given task
    :type from: struct task_struct \*

    :param tsk:
        the task to be attached
    :type tsk: struct task_struct \*

.. _`cgroup_transfer_tasks`:

cgroup_transfer_tasks
=====================

.. c:function:: int cgroup_transfer_tasks(struct cgroup *to, struct cgroup *from)

    move tasks from one cgroup to another

    :param to:
        cgroup to which the tasks will be moved
    :type to: struct cgroup \*

    :param from:
        cgroup in which the tasks currently reside
    :type from: struct cgroup \*

.. _`cgroup_transfer_tasks.description`:

Description
-----------

Locking rules between \ :c:func:`cgroup_post_fork`\  and the migration path
guarantee that, if a task is forking while being migrated, the new child
is guaranteed to be either visible in the source cgroup after the
parent's migration is complete or put into the target cgroup.  No task
can slip out of migration through forking.

.. _`cgroup_task_count`:

cgroup_task_count
=================

.. c:function:: int cgroup_task_count(const struct cgroup *cgrp)

    count the number of tasks in a cgroup.

    :param cgrp:
        the cgroup in question
    :type cgrp: const struct cgroup \*

.. _`cgroupstats_build`:

cgroupstats_build
=================

.. c:function:: int cgroupstats_build(struct cgroupstats *stats, struct dentry *dentry)

    build and fill cgroupstats

    :param stats:
        cgroupstats to fill information into
    :type stats: struct cgroupstats \*

    :param dentry:
        A dentry entry belonging to the cgroup for which stats have
        been requested.
    :type dentry: struct dentry \*

.. _`cgroupstats_build.description`:

Description
-----------

Build and fill cgroupstats so that taskstats can export it to user
space.

.. This file was automatic generated / don't edit.

