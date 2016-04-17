.. -*- coding: utf-8; mode: rst -*-

===========
pm_wakeup.h
===========


.. _`wakeup_source`:

struct wakeup_source
====================

.. c:type:: wakeup_source

    Representation of wakeup sources


.. _`wakeup_source.definition`:

Definition
----------

.. code-block:: c

  struct wakeup_source {
    const char * name;
    struct list_head entry;
    spinlock_t lock;
    struct wake_irq * wakeirq;
    struct timer_list timer;
    unsigned long timer_expires;
    ktime_t total_time;
    ktime_t max_time;
    ktime_t last_time;
    ktime_t prevent_sleep_time;
    unsigned long event_count;
    unsigned long active_count;
    unsigned long relax_count;
    unsigned long expire_count;
    unsigned long wakeup_count;
    bool active:1;
  };


.. _`wakeup_source.members`:

Members
-------

:``name``:
    Name of the wakeup source

:``entry``:
    Wakeup source list entry

:``lock``:
    Wakeup source lock

:``wakeirq``:
    Optional device specific wakeirq

:``timer``:
    Wakeup timer list

:``timer_expires``:
    Wakeup timer expiration

:``total_time``:
    Total time this wakeup source has been active.

:``max_time``:
    Maximum time this wakeup source has been continuously active.

:``last_time``:
    Monotonic clock when the wakeup source's was touched last time.

:``prevent_sleep_time``:
    Total time this source has been preventing autosleep.

:``event_count``:
    Number of signaled wakeup events.

:``active_count``:
    Number of times the wakeup source was activated.

:``relax_count``:
    Number of times the wakeup source was deactivated.

:``expire_count``:
    Number of times the wakeup source's timeout has expired.

:``wakeup_count``:
    Number of times the wakeup source might abort suspend.

:``active``:
    Status of the wakeup source.


