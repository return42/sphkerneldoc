.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etm-perf.h

.. _`etm_filter`:

struct etm_filter
=================

.. c:type:: struct etm_filter

    single instruction range or start/stop configuration.

.. _`etm_filter.definition`:

Definition
----------

.. code-block:: c

    struct etm_filter {
        unsigned long start_addr;
        unsigned long stop_addr;
        enum etm_addr_type type;
    }

.. _`etm_filter.members`:

Members
-------

start_addr
    The address to start tracing on.

stop_addr
    The address to stop tracing on.

type
    Is this a range or start/stop filter.

.. _`etm_filters`:

struct etm_filters
==================

.. c:type:: struct etm_filters

    set of filters for a session

.. _`etm_filters.definition`:

Definition
----------

.. code-block:: c

    struct etm_filters {
        struct etm_filter etm_filter[ETM_ADDR_CMP_MAX];
        unsigned int nr_filters;
        bool ssstatus;
    }

.. _`etm_filters.members`:

Members
-------

etm_filter
    All the filters for this session.

nr_filters
    Number of filters

ssstatus
    Status of the start/stop logic.

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
        struct list_head * __percpu *path;
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

