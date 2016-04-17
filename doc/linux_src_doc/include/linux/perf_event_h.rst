.. -*- coding: utf-8; mode: rst -*-

============
perf_event.h
============


.. _`hw_perf_event`:

struct hw_perf_event
====================

.. c:type:: hw_perf_event

    performance event hardware details:


.. _`hw_perf_event.definition`:

Definition
----------

.. code-block:: c

  struct hw_perf_event {
    #ifdef CONFIG_PERF_EVENTS
    union {unnamed_union};
    #define PERF_HES_STOPPED	0x01
    #define PERF_HES_UPTODATE	0x02
    #define PERF_HES_ARCH		0x04
    #endif
  };


.. _`hw_perf_event.members`:

Members
-------

:``{unnamed_union}``:
    anonymous




.. _`perf_pmu_cap_no_interrupt`:

PERF_PMU_CAP_NO_INTERRUPT
=========================

.. c:function:: PERF_PMU_CAP_NO_INTERRUPT ()



.. _`pmu`:

struct pmu
==========

.. c:type:: pmu

    generic performance monitoring unit


.. _`pmu.definition`:

Definition
----------

.. code-block:: c

  struct pmu {
    #define PERF_EF_START	0x01
    #define PERF_EF_RELOAD	0x02
    #define PERF_EF_UPDATE	0x04
  };


.. _`pmu.members`:

Members
-------




.. _`perf_event_active_state`:

enum perf_event_active_state
============================

.. c:type:: perf_event_active_state

    the states of a event


.. _`perf_event_active_state.definition`:

Definition
----------

.. code-block:: c

    enum perf_event_active_state {
      PERF_EVENT_STATE_DEAD,
      PERF_EVENT_STATE_EXIT,
      PERF_EVENT_STATE_ERROR,
      PERF_EVENT_STATE_OFF,
      PERF_EVENT_STATE_INACTIVE,
      PERF_EVENT_STATE_ACTIVE
    };


.. _`perf_event_active_state.constants`:

Constants
---------

:``PERF_EVENT_STATE_DEAD``:
-- undescribed --

:``PERF_EVENT_STATE_EXIT``:
-- undescribed --

:``PERF_EVENT_STATE_ERROR``:
-- undescribed --

:``PERF_EVENT_STATE_OFF``:
-- undescribed --

:``PERF_EVENT_STATE_INACTIVE``:
-- undescribed --

:``PERF_EVENT_STATE_ACTIVE``:
-- undescribed --


.. _`perf_event`:

struct perf_event
=================

.. c:type:: perf_event

    performance event kernel representation:


.. _`perf_event.definition`:

Definition
----------

.. code-block:: c

  struct perf_event {
    #ifdef CONFIG_PERF_EVENTS
    #ifdef CONFIG_EVENT_TRACING
    #ifdef CONFIG_FUNCTION_TRACER
    #endif
    #endif
    #ifdef CONFIG_CGROUP_PERF
    #endif
    #endif
  };


.. _`perf_event.members`:

Members
-------




.. _`perf_event_context`:

struct perf_event_context
=========================

.. c:type:: perf_event_context

    event context structure


.. _`perf_event_context.definition`:

Definition
----------

.. code-block:: c

  struct perf_event_context {
  };


.. _`perf_event_context.members`:

Members
-------




.. _`perf_cpu_context`:

struct perf_cpu_context
=======================

.. c:type:: perf_cpu_context

    per cpu event context structure


.. _`perf_cpu_context.definition`:

Definition
----------

.. code-block:: c

  struct perf_cpu_context {
  };


.. _`perf_cpu_context.members`:

Members
-------


