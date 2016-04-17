.. -*- coding: utf-8; mode: rst -*-

==========
at91_adc.h
==========


.. _`at91_adc_trigger`:

struct at91_adc_trigger
=======================

.. c:type:: at91_adc_trigger

    description of triggers


.. _`at91_adc_trigger.definition`:

Definition
----------

.. code-block:: c

  struct at91_adc_trigger {
    const char * name;
    u8 value;
    bool is_external;
  };


.. _`at91_adc_trigger.members`:

Members
-------

:``name``:
    name of the trigger advertised to the user

:``value``:
    value to set in the ADC's trigger setup register

:``is_external``:
    Does the trigger rely on an external pin?




.. _`at91_adc_data`:

struct at91_adc_data
====================

.. c:type:: at91_adc_data

    platform data for ADC driver


.. _`at91_adc_data.definition`:

Definition
----------

.. code-block:: c

  struct at91_adc_data {
    unsigned long channels_used;
    u8 startup_time;
    struct at91_adc_trigger * trigger_list;
    u8 trigger_number;
    bool use_external_triggers;
    u16 vref;
    enum atmel_adc_ts_type touchscreen_type;
  };


.. _`at91_adc_data.members`:

Members
-------

:``channels_used``:
    channels in use on the board as a bitmask

:``startup_time``:
    startup time of the ADC in microseconds

:``trigger_list``:
    Triggers available in the ADC

:``trigger_number``:
    Number of triggers available in the ADC

:``use_external_triggers``:
    does the board has external triggers availables

:``vref``:
    Reference voltage for the ADC in millivolts

:``touchscreen_type``:
    If a touchscreen is connected, its type (4 or 5 wires)


