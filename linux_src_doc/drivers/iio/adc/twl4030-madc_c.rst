.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/twl4030-madc.c

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
        struct twl4030_madc_request requests;
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

    :param struct twl4030_madc_data \*madc:
        pointer to struct twl4030_madc_data

    :param u8 reg:
        lsb of ADC Channel

.. _`twl4030_madc_channel_raw_read.return`:

Return
------

0 on success, an error code otherwise.

.. _`twl4030_madc_set_current_generator`:

twl4030_madc_set_current_generator
==================================

.. c:function:: int twl4030_madc_set_current_generator(struct twl4030_madc_data *madc, int chan, int on)

    setup bias current

    :param struct twl4030_madc_data \*madc:
        pointer to twl4030_madc_data struct

    :param int chan:
        can be one of the two values:
        0 - Enables bias current for main battery type reading
        1 - Enables bias current for main battery temperature sensing

    :param int on:
        enable or disable chan.

.. _`twl4030_madc_set_current_generator.description`:

Description
-----------

Function to enable or disable bias current for
main battery type reading or temperature sensing

.. This file was automatic generated / don't edit.

