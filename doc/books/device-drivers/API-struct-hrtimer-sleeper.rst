.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hrtimer-sleeper:

======================
struct hrtimer_sleeper
======================

*man struct hrtimer_sleeper(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
