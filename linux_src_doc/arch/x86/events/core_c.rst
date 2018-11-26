.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/events/core.c

.. _`x86_perf_rdpmc_index`:

x86_perf_rdpmc_index
====================

.. c:function:: int x86_perf_rdpmc_index(struct perf_event *event)

    Return PMC counter used for event

    :param event:
        the perf_event to which the PMC counter was assigned
    :type event: struct perf_event \*

.. _`x86_perf_rdpmc_index.description`:

Description
-----------

The counter assigned to this performance event may change if interrupts
are enabled. This counter should thus never be used while interrupts are
enabled. Before this function is used to obtain the assigned counter the
event should be checked for validity using, for example,
\ :c:func:`perf_event_read_local`\ , within the same interrupt disabled section in
which this counter is planned to be used.

.. _`x86_perf_rdpmc_index.return`:

Return
------

The index of the performance monitoring counter assigned to
\ ``perf_event``\ .

.. This file was automatic generated / don't edit.

