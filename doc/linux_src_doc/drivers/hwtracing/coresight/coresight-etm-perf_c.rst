.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etm-perf.c

.. _`etm_event_data`:

struct etm_event_data
=====================

.. c:type:: struct etm_event_data

    Coresight specifics associated to an event

.. _`etm_event_data.definition`:

Definition
----------

.. code-block:: c

    struct etm_event_data {
        struct work_struct work;
        cpumask_t mask;
        void *snk_config;
        struct list_head **path;
    }

.. _`etm_event_data.members`:

Members
-------

work
    Handle to free allocated memory outside IRQ context.

mask
    Hold the CPU(s) this event was set for.

snk_config
    The sink configuration.

path
    An array of path, each slot for one CPU.

.. This file was automatic generated / don't edit.

