.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/hw_breakpoint.c

.. _`hw_breakpoint_slot_setup`:

hw_breakpoint_slot_setup
========================

.. c:function:: int hw_breakpoint_slot_setup(struct perf_event **slots, int max_slots, struct perf_event *bp, enum hw_breakpoint_ops ops)

    Find and setup a perf slot according to operations

    :param slots:
        pointer to array of slots
    :type slots: struct perf_event \*\*

    :param max_slots:
        max number of slots
    :type max_slots: int

    :param bp:
        perf_event to setup
    :type bp: struct perf_event \*

    :param ops:
        operation to be carried out on the slot
    :type ops: enum hw_breakpoint_ops

.. _`hw_breakpoint_slot_setup.return`:

Return
------

slot index on success
-ENOSPC if no slot is available/matches
-EINVAL on wrong operations parameter

.. This file was automatic generated / don't edit.

