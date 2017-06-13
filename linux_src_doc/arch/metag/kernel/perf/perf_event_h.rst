.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/kernel/perf/perf_event.h

.. _`cpu_hw_events`:

struct cpu_hw_events
====================

.. c:type:: struct cpu_hw_events

    a processor core's performance events

.. _`cpu_hw_events.definition`:

Definition
----------

.. code-block:: c

    struct cpu_hw_events {
        struct perf_event  *events;
        unsigned long used_mask;
        raw_spinlock_t pmu_lock;
    }

.. _`cpu_hw_events.members`:

Members
-------

events
    an array of perf_events active for a given index.

used_mask
    a bitmap of in-use counters.

pmu_lock
    a perf counter lock

.. _`cpu_hw_events.description`:

Description
-----------

This is a per-cpu/core structure that maintains a record of its
performance counters' state.

.. _`metag_pmu`:

struct metag_pmu
================

.. c:type:: struct metag_pmu

    the Meta PMU structure

.. _`metag_pmu.definition`:

Definition
----------

.. code-block:: c

    struct metag_pmu {
        struct pmu pmu;
        const char *name;
        u32 version;
        irqreturn_t (*handle_irq)(int irq_num, void *dev);
        void (*enable)(struct hw_perf_event *evt, int idx);
        void (*disable)(struct hw_perf_event *evt, int idx);
        u64 (*read)(int idx);
        void (*write)(int idx, u32 val);
        int (*event_map)(int idx);
        const int cache_events;
        u32 max_period;
        int max_events;
        atomic_t active_events;
        struct mutex reserve_mutex;
    }

.. _`metag_pmu.members`:

Members
-------

pmu
    core pmu structure

name
    pmu name

version
    core version

handle_irq
    overflow interrupt handler

enable
    enable a counter

disable
    disable a counter

read
    read the value of a counter

write
    write a value to a counter

event_map
    kernel event to counter event id map

cache_events
    kernel cache counter to core cache counter map

max_period
    maximum value of the counter before overflow

max_events
    maximum number of counters available at any one time

active_events
    number of active counters

reserve_mutex
    counter reservation mutex

.. _`metag_pmu.description`:

Description
-----------

This describes the main functionality and data used by the performance
event core.

.. This file was automatic generated / don't edit.

