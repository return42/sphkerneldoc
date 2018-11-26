.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/twl4030-madc.c

.. _`twl4030_madc_request`:

struct twl4030_madc_request
===========================

.. c:type:: struct twl4030_madc_request

    madc request packet for channel conversion

.. _`twl4030_madc_request.definition`:

Definition
----------

.. code-block:: c

    struct twl4030_madc_request {
        unsigned long channels;
        bool do_avg;
        u16 method;
        u16 type;
        bool active;
        bool result_pending;
        bool raw;
        int rbuf[TWL4030_MADC_MAX_CHANNELS];
    }

.. _`twl4030_madc_request.members`:

Members
-------

channels
    16 bit bitmap for individual channels

do_avg
    sample the input channel for 4 consecutive cycles

method
    RT, SW1, SW2

type
    Polling or interrupt based method

active
    Flag if request is active

result_pending
    Flag from irq handler, that result is ready

raw
    Return raw value, do not convert it

rbuf
    Result buffer

.. _`twl4030_madc_data`:

struct twl4030_madc_data
========================

.. c:type:: struct twl4030_madc_data

    a container for madc info

.. _`twl4030_madc_data.definition`:

Definition
----------

.. code-block:: c

    struct twl4030_madc_data {
        struct device *dev;
        struct mutex lock;
        struct regulator *usb3v1;
        struct twl4030_madc_request requests[TWL4030_MADC_NUM_METHODS];
        bool use_second_irq;
        u8 imr;
        u8 isr;
    }

.. _`twl4030_madc_data.members`:

Members
-------

dev
    Pointer to device structure for madc

lock
    Mutex protecting this data structure

usb3v1
    *undescribed*

requests
    Array of request struct corresponding to SW1, SW2 and RT

use_second_irq
    IRQ selection (main or co-processor)

imr
    Interrupt mask register of MADC

isr
    Interrupt status register of MADC

.. _`twl4030_madc_channel_raw_read`:

twl4030_madc_channel_raw_read
=============================

.. c:function:: int twl4030_madc_channel_raw_read(struct twl4030_madc_data *madc, u8 reg)

    Function to read a particular channel value

    :param madc:
        pointer to struct twl4030_madc_data
    :type madc: struct twl4030_madc_data \*

    :param reg:
        lsb of ADC Channel
    :type reg: u8

.. _`twl4030_madc_channel_raw_read.return`:

Return
------

0 on success, an error code otherwise.

.. _`twl4030_madc_set_current_generator`:

twl4030_madc_set_current_generator
==================================

.. c:function:: int twl4030_madc_set_current_generator(struct twl4030_madc_data *madc, int chan, int on)

    setup bias current

    :param madc:
        pointer to twl4030_madc_data struct
    :type madc: struct twl4030_madc_data \*

    :param chan:
        can be one of the two values:
        0 - Enables bias current for main battery type reading
        1 - Enables bias current for main battery temperature sensing
    :type chan: int

    :param on:
        enable or disable chan.
    :type on: int

.. _`twl4030_madc_set_current_generator.description`:

Description
-----------

Function to enable or disable bias current for
main battery type reading or temperature sensing

.. This file was automatic generated / don't edit.

