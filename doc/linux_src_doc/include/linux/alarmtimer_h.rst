.. -*- coding: utf-8; mode: rst -*-

============
alarmtimer.h
============


.. _`alarm`:

struct alarm
============

.. c:type:: alarm

    Alarm timer structure


.. _`alarm.definition`:

Definition
----------

.. code-block:: c

  struct alarm {
    struct timerqueue_node node;
    enum alarmtimer_restart	(* function) (struct alarm *, ktime_t now);
    enum alarmtimer_type type;
    void * data;
  };


.. _`alarm.members`:

Members
-------

:``node``:
    timerqueue node for adding to the event list this value
    also includes the expiration time.

:``function``:
    Function pointer to be executed when the timer fires.

:``type``:
    Alarm type (BOOTTIME/REALTIME)

:``data``:
    Internal data value.


