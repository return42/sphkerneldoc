.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/trigger/ledtrig-cpu.c

.. _`ledtrig_cpu`:

ledtrig_cpu
===========

.. c:function:: void ledtrig_cpu(enum cpu_led_event ledevt)

    emit a CPU event as a trigger

    :param ledevt:
        *undescribed*
    :type ledevt: enum cpu_led_event

.. _`ledtrig_cpu.description`:

Description
-----------

Emit a CPU event on a CPU core, which will trigger a
bound LED to turn on or turn off.

.. This file was automatic generated / don't edit.

