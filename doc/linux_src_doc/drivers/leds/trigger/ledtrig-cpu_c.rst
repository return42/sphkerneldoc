.. -*- coding: utf-8; mode: rst -*-

=============
ledtrig-cpu.c
=============


.. _`ledtrig_cpu`:

ledtrig_cpu
===========

.. c:function:: void ledtrig_cpu (enum cpu_led_event ledevt)

    emit a CPU event as a trigger

    :param enum cpu_led_event ledevt:

        *undescribed*



.. _`ledtrig_cpu.description`:

Description
-----------

Emit a CPU event on a CPU core, which will trigger a
binded LED to turn on or turn off.

