.. -*- coding: utf-8; mode: rst -*-

=================
extcon-adc-jack.h
=================


.. _`adc_jack_cond`:

struct adc_jack_cond
====================

.. c:type:: adc_jack_cond

    condition to use an extcon state


.. _`adc_jack_cond.definition`:

Definition
----------

.. code-block:: c

  struct adc_jack_cond {
    u32 state;
    u32 min_adc;
    u32 max_adc;
  };


.. _`adc_jack_cond.members`:

Members
-------

:``state``:
    the corresponding extcon state (if 0, this struct
    denotes the last adc_jack_cond element among the array)

:``min_adc``:
    min adc value for this condition

:``max_adc``:
    max adc value for this condition




.. _`adc_jack_cond.description`:

Description
-----------

For example, if { .state = 0x3, .min_adc = 100, .max_adc = 200}, it means
that if ADC value is between (inclusive) 100 and 200, than the cable 0 and
1 are attached (1<<0 | 1<<1 == 0x3)

Note that you don't need to describe condition for "no cable attached"
because when no adc_jack_cond is met, state = 0 is automatically chosen.



.. _`adc_jack_pdata`:

struct adc_jack_pdata
=====================

.. c:type:: adc_jack_pdata

    platform data for adc jack device.


.. _`adc_jack_pdata.definition`:

Definition
----------

.. code-block:: c

  struct adc_jack_pdata {
    const char * name;
    const char * consumer_channel;
    const enum extcon * cable_names;
    unsigned long irq_flags;
    unsigned long handling_delay_ms;
  };


.. _`adc_jack_pdata.members`:

Members
-------

:``name``:
    name of the extcon device. If null, "adc-jack" is used.

:``consumer_channel``:
    Unique name to identify the channel on the consumer
    side. This typically describes the channels used within
    the consumer. E.g. 'battery_voltage'

:``cable_names``:
    array of extcon id for supported cables.

:``irq_flags``:
    irq flags used for the ``irq``

:``handling_delay_ms``:
    in some devices, we need to read ADC value some
    milli-seconds after the interrupt occurs. You may
    describe such delays with ``handling_delay_ms``\ , which
    is rounded-off by jiffies.


