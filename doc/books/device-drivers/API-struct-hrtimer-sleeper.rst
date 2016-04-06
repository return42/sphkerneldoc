
.. _API-struct-hrtimer-sleeper:

======================
struct hrtimer_sleeper
======================

*man struct hrtimer_sleeper(9)*

*4.6.0-rc1*

simple sleeper structure


Synopsis
========

.. code-block:: c

    struct hrtimer_sleeper {
      struct hrtimer timer;
      struct task_struct * task;
    };


Members
=======

timer
    embedded timer structure

task
    task to wake up


Description
===========

task is set to NULL, when the timer expires.
