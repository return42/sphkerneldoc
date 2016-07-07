.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/yama/yama_lsm.c

.. _`yama_relation_cleanup`:

yama_relation_cleanup
=====================

.. c:function:: void yama_relation_cleanup(struct work_struct *work)

    remove invalid entries from the relation list

    :param struct work_struct \*work:
        *undescribed*

.. _`yama_ptracer_add`:

yama_ptracer_add
================

.. c:function:: int yama_ptracer_add(struct task_struct *tracer, struct task_struct *tracee)

    add/replace an exception for this tracer/tracee pair

    :param struct task_struct \*tracer:
        the task_struct of the process doing the ptrace

    :param struct task_struct \*tracee:
        the task_struct of the process to be ptraced

.. _`yama_ptracer_add.description`:

Description
-----------

Each tracee can have, at most, one tracer registered. Each time this
is called, the prior registered tracer will be replaced for the tracee.

Returns 0 if relationship was added, -ve on error.

.. _`yama_ptracer_del`:

yama_ptracer_del
================

.. c:function:: void yama_ptracer_del(struct task_struct *tracer, struct task_struct *tracee)

    remove exceptions related to the given tasks

    :param struct task_struct \*tracer:
        remove any relation where tracer task matches

    :param struct task_struct \*tracee:
        remove any relation where tracee task matches

.. _`yama_task_free`:

yama_task_free
==============

.. c:function:: void yama_task_free(struct task_struct *task)

    check for task_pid to remove from exception list

    :param struct task_struct \*task:
        task being removed

.. _`yama_task_prctl`:

yama_task_prctl
===============

.. c:function:: int yama_task_prctl(int option, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5)

    check for Yama-specific prctl operations

    :param int option:
        operation

    :param unsigned long arg2:
        argument

    :param unsigned long arg3:
        argument

    :param unsigned long arg4:
        argument

    :param unsigned long arg5:
        argument

.. _`yama_task_prctl.description`:

Description
-----------

Return 0 on success, -ve on error.  -ENOSYS is returned when Yama
does not handle the given option.

.. _`task_is_descendant`:

task_is_descendant
==================

.. c:function:: int task_is_descendant(struct task_struct *parent, struct task_struct *child)

    walk up a process family tree looking for a match

    :param struct task_struct \*parent:
        the process to compare against while walking up from child

    :param struct task_struct \*child:
        the process to start from while looking upwards for parent

.. _`task_is_descendant.description`:

Description
-----------

Returns 1 if child is a descendant of parent, 0 if not.

.. _`ptracer_exception_found`:

ptracer_exception_found
=======================

.. c:function:: int ptracer_exception_found(struct task_struct *tracer, struct task_struct *tracee)

    tracer registered as exception for this tracee

    :param struct task_struct \*tracer:
        the task_struct of the process attempting ptrace

    :param struct task_struct \*tracee:
        the task_struct of the process to be ptraced

.. _`ptracer_exception_found.description`:

Description
-----------

Returns 1 if tracer has is ptracer exception ancestor for tracee.

.. _`yama_ptrace_access_check`:

yama_ptrace_access_check
========================

.. c:function:: int yama_ptrace_access_check(struct task_struct *child, unsigned int mode)

    validate PTRACE_ATTACH calls

    :param struct task_struct \*child:
        task that current task is attempting to ptrace

    :param unsigned int mode:
        ptrace attach mode

.. _`yama_ptrace_access_check.description`:

Description
-----------

Returns 0 if following the ptrace is allowed, -ve on error.

.. _`yama_ptrace_traceme`:

yama_ptrace_traceme
===================

.. c:function:: int yama_ptrace_traceme(struct task_struct *parent)

    validate PTRACE_TRACEME calls

    :param struct task_struct \*parent:
        task that will become the ptracer of the current task

.. _`yama_ptrace_traceme.description`:

Description
-----------

Returns 0 if following the ptrace is allowed, -ve on error.

.. This file was automatic generated / don't edit.

