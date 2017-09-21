.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/ti-adc084s021.c

.. _`adc084s021_driver_name`:

ADC084S021_DRIVER_NAME
======================

.. c:function::  ADC084S021_DRIVER_NAME()

.. _`adc084s021_driver_name.description`:

Description
-----------

Driver for Texas Instruments' ADC084S021 ADC chip.

.. _`adc084s021_driver_name.datasheets-can-be-found-here`:

Datasheets can be found here
----------------------------

http://www.ti.com/lit/ds/symlink/adc084s021.pdf

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

.. _`adc084s021_adc_conversion`:

adc084s021_adc_conversion
=========================

.. c:function:: int adc084s021_adc_conversion(struct adc084s021 *adc, void *data)

    :param struct adc084s021 \*adc:
        The ADC SPI data.

    :param void \*data:
        Buffer for converted data.

.. _`adc084s021_buffer_trigger_handler`:

adc084s021_buffer_trigger_handler
=================================

.. c:function:: irqreturn_t adc084s021_buffer_trigger_handler(int irq, void *pollfunc)

    :param int irq:
        The interrupt number (not used).

    :param void \*pollfunc:
        Pointer to the poll func.

.. This file was automatic generated / don't edit.

