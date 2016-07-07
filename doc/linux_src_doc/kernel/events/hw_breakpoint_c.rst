.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/events/hw_breakpoint.c

.. _`register_user_hw_breakpoint`:

register_user_hw_breakpoint
===========================

.. c:function:: struct perf_event *register_user_hw_breakpoint(struct perf_event_attr *attr, perf_overflow_handler_t triggered, void *context, struct task_struct *tsk)

    register a hardware breakpoint for user space

    :param struct perf_event_attr \*attr:
        breakpoint attributes

    :param perf_overflow_handler_t triggered:
        callback to trigger when we hit the breakpoint

    :param void \*context:
        *undescribed*

    :param struct task_struct \*tsk:
        pointer to 'task_struct' of the process to which the address belongs

.. _`modify_user_hw_breakpoint`:

modify_user_hw_breakpoint
=========================

.. c:function:: int modify_user_hw_breakpoint(struct perf_event *bp, struct perf_event_attr *attr)

    modify a user-space hardware breakpoint

    :param struct perf_event \*bp:
        the breakpoint structure to modify

    :param struct perf_event_attr \*attr:
        new breakpoint attributes

.. _`unregister_hw_breakpoint`:

unregister_hw_breakpoint
========================

.. c:function:: void unregister_hw_breakpoint(struct perf_event *bp)

    unregister a user-space hardware breakpoint

    :param struct perf_event \*bp:
        the breakpoint structure to unregister

.. _`unregister_wide_hw_breakpoint`:

unregister_wide_hw_breakpoint
=============================

.. c:function:: void unregister_wide_hw_breakpoint(struct perf_event * __percpu *cpu_events)

    unregister a wide breakpoint in the kernel

    :param struct perf_event \* __percpu \*cpu_events:
        the per cpu set of events to unregister

.. This file was automatic generated / don't edit.

