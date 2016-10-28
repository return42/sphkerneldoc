.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/hw_breakpoint.c

.. _`hw_breakpoint_slot_setup`:

hw_breakpoint_slot_setup
========================

.. c:function:: int hw_breakpoint_slot_setup(struct perf_event **slots, int max_slots, struct perf_event *bp, enum hw_breakpoint_ops ops)

    Find and setup a perf slot according to operations

    :param struct perf_event \*\*slots:
        pointer to array of slots

    :param int max_slots:
        max number of slots

    :param struct perf_event \*bp:
        perf_event to setup

    :param enum hw_breakpoint_ops ops:
        operation to be carried out on the slot

.. _`hw_breakpoint_slot_setup.return`:

Return
------

slot index on success
-ENOSPC if no slot is available/matches
-EINVAL on wrong operations parameter

.. This file was automatic generated / don't edit.

