
.. _API-struct-hrtimer:

==============
struct hrtimer
==============

*man struct hrtimer(9)*

*4.6.0-rc1*

the basic hrtimer structure


Synopsis
========

.. code-block:: c

    struct hrtimer {
      struct timerqueue_node node;
      ktime_t _softexpires;
      enum hrtimer_restart      (* function) (struct hrtimer *);
      struct hrtimer_clock_base * base;
      u8 state;
      u8 is_rel;
    #ifdef CONFIG_TIMER_STATS
      int start_pid;
      void * start_site;
      char start_comm[16];
    #endif
    };


Members
=======

node
    timerqueue node, which also manages node.expires, the absolute expiry time in the hrtimers internal representation. The time is related to the clock on which the timer is
    based. Is setup by adding slack to the _softexpires value. For non range timers identical to _softexpires.

_softexpires
    the absolute earliest expiry time of the hrtimer. The time which was given as expiry time when the timer was armed.

function
    timer expiry callback function

base
    pointer to the timer base (per cpu and per clock)

state
    state information (See bit values above)

is_rel
    Set if the timer was armed relative

start_pid
    timer statistics field to store the pid of the task which started the timer

start_site
    timer statistics field to store the site where the timer was started

start_comm[16]
    timer statistics field to store the name of the process which started the timer


Description
===========

The hrtimer structure must be initialized by ``hrtimer_init``
