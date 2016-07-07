.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/adau17x1.h

.. _`adau17x1_micbias_voltage`:

enum adau17x1_micbias_voltage
=============================

.. c:type:: enum adau17x1_micbias_voltage

    Microphone bias voltage

.. _`adau17x1_micbias_voltage.definition`:

Definition
----------

.. code-block:: c

    enum adau17x1_micbias_voltage {
        ADAU17X1_MICBIAS_0_90_AVDD,
        ADAU17X1_MICBIAS_0_65_AVDD
    };

.. _`adau17x1_micbias_voltage.constants`:

Constants
---------

ADAU17X1_MICBIAS_0_90_AVDD
    0.9 \* AVDD

ADAU17X1_MICBIAS_0_65_AVDD
    0.65 \* AVDD

.. _`adau1761_digmic_jackdet_pin_mode`:

enum adau1761_digmic_jackdet_pin_mode
=====================================

.. c:type:: enum adau1761_digmic_jackdet_pin_mode

    Configuration of the JACKDET/MICIN pin

.. _`adau1761_digmic_jackdet_pin_mode.definition`:

Definition
----------

.. code-block:: c

    enum adau1761_digmic_jackdet_pin_mode {
        ADAU1761_DIGMIC_JACKDET_PIN_MODE_NONE,
        ADAU1761_DIGMIC_JACKDET_PIN_MODE_DIGMIC,
        ADAU1761_DIGMIC_JACKDET_PIN_MODE_JACKDETECT
    };

.. _`adau1761_digmic_jackdet_pin_mode.constants`:

Constants
---------

ADAU1761_DIGMIC_JACKDET_PIN_MODE_NONE
    Disable the pin

ADAU1761_DIGMIC_JACKDET_PIN_MODE_DIGMIC
    Configure the pin for usage as
    digital microphone input.

ADAU1761_DIGMIC_JACKDET_PIN_MODE_JACKDETECT
    Configure the pin for jack
    insertion detection.

.. _`adau1761_output_mode`:

enum adau1761_output_mode
=========================

.. c:type:: enum adau1761_output_mode

    Output mode configuration

.. _`adau1761_output_mode.definition`:

Definition
----------

.. code-block:: c

    enum adau1761_output_mode {
        ADAU1761_OUTPUT_MODE_HEADPHONE,
        ADAU1761_OUTPUT_MODE_HEADPHONE_CAPLESS,
        ADAU1761_OUTPUT_MODE_LINE
    };

.. _`adau1761_output_mode.constants`:

Constants
---------

ADAU1761_OUTPUT_MODE_HEADPHONE
    Headphone output

ADAU1761_OUTPUT_MODE_HEADPHONE_CAPLESS
    Capless headphone output

ADAU1761_OUTPUT_MODE_LINE
    Line output

.. _`adau1761_platform_data`:

struct adau1761_platform_data
=============================

.. c:type:: struct adau1761_platform_data

    ADAU1761 Codec driver platform data

.. _`adau1761_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct adau1761_platform_data {
        bool input_differential;
        enum adau1761_output_mode lineout_mode;
        enum adau1761_output_mode headphone_mode;
        enum adau1761_digmic_jackdet_pin_mode digmic_jackdetect_pin_mode;
        enum adau1761_jackdetect_debounce_time jackdetect_debounce_time;
        bool jackdetect_active_low;
        enum adau17x1_micbias_voltage micbias_voltage;
    }

.. _`adau1761_platform_data.members`:

Members
-------

input_differential
    If true the input pins will be configured in
    differential mode.

lineout_mode
    Output mode for the LOUT/ROUT pins

headphone_mode
    Output mode for the LHP/RHP pins

digmic_jackdetect_pin_mode
    JACKDET/MICIN pin configuration

jackdetect_debounce_time
    Jack insertion detection debounce time.

jackdetect_active_low
    If true the jack insertion detection is active low.
    Othwise it will be active high.

micbias_voltage
    Microphone voltage bias

.. _`adau1761_platform_data.note`:

Note
----

This value will only be used, if the JACKDET/MICIN pin is configured
for jack insertion detection.

.. _`adau1781_platform_data`:

struct adau1781_platform_data
=============================

.. c:type:: struct adau1781_platform_data

    ADAU1781 Codec driver platform data

.. _`adau1781_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct adau1781_platform_data {
        bool left_input_differential;
        bool right_input_differential;
        bool use_dmic;
        enum adau17x1_micbias_voltage micbias_voltage;
    }

.. _`adau1781_platform_data.members`:

Members
-------

left_input_differential
    If true configure the left input as
    differential input.

right_input_differential
    If true configure the right input as differntial
    input.

use_dmic
    If true configure the MIC pins as digital microphone pins instead
    of analog microphone pins.

micbias_voltage
    Microphone voltage bias

.. This file was automatic generated / don't edit.

