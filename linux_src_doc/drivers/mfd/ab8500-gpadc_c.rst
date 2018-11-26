.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/ab8500-gpadc.c

.. _`adc_cal_data`:

struct adc_cal_data
===================

.. c:type:: struct adc_cal_data

    Table for storing gain and offset for the calibrated ADC channels

.. _`adc_cal_data.definition`:

Definition
----------

.. code-block:: c

    struct adc_cal_data {
        s64 gain;
        s64 offset;
        u16 otp_calib_hi;
        u16 otp_calib_lo;
    }

.. _`adc_cal_data.members`:

Members
-------

gain
    Gain of the ADC channel

offset
    Offset of the ADC channel

otp_calib_hi
    *undescribed*

otp_calib_lo
    *undescribed*

.. _`ab8500_gpadc`:

struct ab8500_gpadc
===================

.. c:type:: struct ab8500_gpadc

    AB8500 GPADC device information

.. _`ab8500_gpadc.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_gpadc {
        struct device *dev;
        struct list_head node;
        struct ab8500 *parent;
        struct completion ab8500_gpadc_complete;
        struct mutex ab8500_gpadc_lock;
        struct regulator *regu;
        int irq_sw;
        int irq_hw;
        struct adc_cal_data cal_data[NBR_CAL_INPUTS];
    }

.. _`ab8500_gpadc.members`:

Members
-------

dev
    pointer to the struct device

node
    a list of AB8500 GPADCs, hence prepared for

parent
    pointer to the struct ab8500

ab8500_gpadc_complete
    pointer to the struct completion, to indicate
    the completion of gpadc conversion

ab8500_gpadc_lock
    structure of type mutex

regu
    pointer to the struct regulator

irq_sw
    interrupt number that is used by gpadc for Sw
    conversion

irq_hw
    interrupt number that is used by gpadc for Hw
    conversion
    \ ``cal_data``\                     array of ADC calibration data structs

cal_data
    *undescribed*

.. _`ab8500_gpadc_get`:

ab8500_gpadc_get
================

.. c:function:: struct ab8500_gpadc *ab8500_gpadc_get(char *name)

    returns a reference to the primary AB8500 GPADC (i.e. the first GPADC in the instance list)

    :param name:
        *undescribed*
    :type name: char \*

.. _`ab8500_gpadc_ad_to_voltage`:

ab8500_gpadc_ad_to_voltage
==========================

.. c:function:: int ab8500_gpadc_ad_to_voltage(struct ab8500_gpadc *gpadc, u8 channel, int ad_value)

    Convert a raw ADC value to a voltage

    :param gpadc:
        *undescribed*
    :type gpadc: struct ab8500_gpadc \*

    :param channel:
        *undescribed*
    :type channel: u8

    :param ad_value:
        *undescribed*
    :type ad_value: int

.. _`ab8500_gpadc_sw_hw_convert`:

ab8500_gpadc_sw_hw_convert
==========================

.. c:function:: int ab8500_gpadc_sw_hw_convert(struct ab8500_gpadc *gpadc, u8 channel, u8 avg_sample, u8 trig_edge, u8 trig_timer, u8 conv_type)

    gpadc conversion

    :param gpadc:
        *undescribed*
    :type gpadc: struct ab8500_gpadc \*

    :param channel:
        analog channel to be converted to digital data
    :type channel: u8

    :param avg_sample:
        number of ADC sample to average
    :type avg_sample: u8

    :param trig_edge:
        *undescribed*
    :type trig_edge: u8

    :param trig_timer:
        selected ADC trigger delay timer
    :type trig_timer: u8

    :param conv_type:
        selected conversion type (HW or SW conversion)
    :type conv_type: u8

.. _`ab8500_gpadc_sw_hw_convert.description`:

Description
-----------

This function converts the selected analog i/p to digital
data.

.. _`ab8500_gpadc_read_raw`:

ab8500_gpadc_read_raw
=====================

.. c:function:: int ab8500_gpadc_read_raw(struct ab8500_gpadc *gpadc, u8 channel, u8 avg_sample, u8 trig_edge, u8 trig_timer, u8 conv_type)

    gpadc read

    :param gpadc:
        *undescribed*
    :type gpadc: struct ab8500_gpadc \*

    :param channel:
        analog channel to be read
    :type channel: u8

    :param avg_sample:
        number of ADC sample to average
    :type avg_sample: u8

    :param trig_edge:
        selected trig edge
    :type trig_edge: u8

    :param trig_timer:
        selected ADC trigger delay timer
    :type trig_timer: u8

    :param conv_type:
        selected conversion type (HW or SW conversion)
    :type conv_type: u8

.. _`ab8500_gpadc_read_raw.description`:

Description
-----------

This function obtains the raw ADC value for an hardware conversion,
this then needs to be converted by calling \ :c:func:`ab8500_gpadc_ad_to_voltage`\ 

.. _`ab8500_bm_gpadcconvend_handler`:

ab8500_bm_gpadcconvend_handler
==============================

.. c:function:: irqreturn_t ab8500_bm_gpadcconvend_handler(int irq, void *_gpadc)

    isr for gpadc conversion completion

    :param irq:
        irq number
    :type irq: int

    :param _gpadc:
        *undescribed*
    :type _gpadc: void \*

.. _`ab8500_bm_gpadcconvend_handler.description`:

Description
-----------

This is a interrupt service routine for gpadc conversion completion.
Notifies the gpadc completion is completed and the converted raw value
can be read from the registers.
Returns IRQ status(IRQ_HANDLED)

.. _`ab8540_gpadc_get_otp`:

ab8540_gpadc_get_otp
====================

.. c:function:: void ab8540_gpadc_get_otp(struct ab8500_gpadc *gpadc, u16 *vmain_l, u16 *vmain_h, u16 *btemp_l, u16 *btemp_h, u16 *vbat_l, u16 *vbat_h, u16 *ibat_l, u16 *ibat_h)

    returns OTP values

    :param gpadc:
        *undescribed*
    :type gpadc: struct ab8500_gpadc \*

    :param vmain_l:
        *undescribed*
    :type vmain_l: u16 \*

    :param vmain_h:
        *undescribed*
    :type vmain_h: u16 \*

    :param btemp_l:
        *undescribed*
    :type btemp_l: u16 \*

    :param btemp_h:
        *undescribed*
    :type btemp_h: u16 \*

    :param vbat_l:
        *undescribed*
    :type vbat_l: u16 \*

    :param vbat_h:
        *undescribed*
    :type vbat_h: u16 \*

    :param ibat_l:
        *undescribed*
    :type ibat_l: u16 \*

    :param ibat_h:
        *undescribed*
    :type ibat_h: u16 \*

.. This file was automatic generated / don't edit.

