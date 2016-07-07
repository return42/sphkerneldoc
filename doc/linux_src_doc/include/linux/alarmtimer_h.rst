.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/alarmtimer.h

.. _`alarm`:

struct alarm
============

.. c:type:: struct alarm

    Alarm timer structure

.. _`alarm.definition`:

Definition
----------

.. code-block:: c

    struct alarm {
        struct timerqueue_node node;
        struct hrtimer timer;
        enum alarmtimer_restart (* function) (struct alarm *, ktime_t now);
        enum alarmtimer_type type;
        int state;
        void *data;
    }

.. _`alarm.members`:

Members
-------

node
    timerqueue node for adding to the event list this value
    also includes the expiration time.

timer
    *undescribed*

function
    Function pointer to be executed when the timer fires.

type
    Alarm type (BOOTTIME/REALTIME)

state
    *undescribed*

data
    Internal data value.

.. This file was automatic generated / don't edit.

