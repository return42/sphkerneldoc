.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/events/hw_breakpoint.c

.. _`register_user_hw_breakpoint`:

register_user_hw_breakpoint
===========================

.. c:function:: struct perf_event *register_user_hw_breakpoint(struct perf_event_attr *attr, perf_overflow_handler_t triggered, void *context, struct task_struct *tsk)

    register a hardware breakpoint for user space

    :param attr:
        breakpoint attributes
    :type attr: struct perf_event_attr \*

    :param triggered:
        callback to trigger when we hit the breakpoint
    :type triggered: perf_overflow_handler_t

    :param context:
        *undescribed*
    :type context: void \*

    :param tsk:
        pointer to 'task_struct' of the process to which the address belongs
    :type tsk: struct task_struct \*

.. _`modify_user_hw_breakpoint`:

modify_user_hw_breakpoint
=========================

.. c:function:: int modify_user_hw_breakpoint(struct perf_event *bp, struct perf_event_attr *attr)

    modify a user-space hardware breakpoint

    :param bp:
        the breakpoint structure to modify
    :type bp: struct perf_event \*

    :param attr:
        new breakpoint attributes
    :type attr: struct perf_event_attr \*

.. _`unregister_hw_breakpoint`:

unregister_hw_breakpoint
========================

.. c:function:: void unregister_hw_breakpoint(struct perf_event *bp)

    unregister a user-space hardware breakpoint

    :param bp:
        the breakpoint structure to unregister
    :type bp: struct perf_event \*

.. _`register_wide_hw_breakpoint`:

register_wide_hw_breakpoint
===========================

.. c:function:: struct perf_event * __percpu *  register_wide_hw_breakpoint(struct perf_event_attr *attr, perf_overflow_handler_t triggered, void *context)

    register a wide breakpoint in the kernel

    :param attr:
        breakpoint attributes
    :type attr: struct perf_event_attr \*

    :param triggered:
        callback to trigger when we hit the breakpoint
    :type triggered: perf_overflow_handler_t

    :param context:
        *undescribed*
    :type context: void \*

.. _`register_wide_hw_breakpoint.description`:

Description
-----------

\ ``return``\  a set of per_cpu pointers to perf events

.. _`unregister_wide_hw_breakpoint`:

unregister_wide_hw_breakpoint
=============================

.. c:function:: void unregister_wide_hw_breakpoint(struct perf_event * __percpu *cpu_events)

    unregister a wide breakpoint in the kernel

    :param cpu_events:
        the per cpu set of events to unregister
    :type cpu_events: struct perf_event \* __percpu \*

.. This file was automatic generated / don't edit.

