.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-vadc-common.h

.. _`vadc_map_pt`:

struct vadc_map_pt
==================

.. c:type:: struct vadc_map_pt

    Map the graph representation for ADC channel

.. _`vadc_map_pt.definition`:

Definition
----------

.. code-block:: c

    struct vadc_map_pt {
        s32 x;
        s32 y;
    }

.. _`vadc_map_pt.members`:

Members
-------

x
    Represent the ADC digitized code.

y
    Represent the physical data which can be temperature, voltage,
    resistance.

.. _`vadc_linear_graph`:

struct vadc_linear_graph
========================

.. c:type:: struct vadc_linear_graph

    Represent ADC characteristics.

.. _`vadc_linear_graph.definition`:

Definition
----------

.. code-block:: c

    struct vadc_linear_graph {
        s32 dy;
        s32 dx;
        s32 gnd;
    }

.. _`vadc_linear_graph.members`:

Members
-------

dy
    numerator slope to calculate the gain.

dx
    denominator slope to calculate the gain.

gnd
    A/D word of the ground reference used for the channel.

.. _`vadc_linear_graph.description`:

Description
-----------

Each ADC device has different offset and gain parameters which are
computed to calibrate the device.

.. _`vadc_prescale_ratio`:

struct vadc_prescale_ratio
==========================

.. c:type:: struct vadc_prescale_ratio

    Represent scaling ratio for ADC input.

.. _`vadc_prescale_ratio.definition`:

Definition
----------

.. code-block:: c

    struct vadc_prescale_ratio {
        u32 num;
        u32 den;
    }

.. _`vadc_prescale_ratio.members`:

Members
-------

num
    the inverse numerator of the gain applied to the input channel.

den
    the inverse denominator of the gain applied to the input channel.

.. _`vadc_scale_fn_type`:

enum vadc_scale_fn_type
=======================

.. c:type:: enum vadc_scale_fn_type

    Scaling function to convert ADC code to physical scaled units for the channel.

.. _`vadc_scale_fn_type.definition`:

Definition
----------

.. code-block:: c

    enum vadc_scale_fn_type {
        SCALE_DEFAULT,
        SCALE_THERM_100K_PULLUP,
        SCALE_PMIC_THERM,
        SCALE_XOTHERM,
        SCALE_PMI_CHG_TEMP,
        SCALE_HW_CALIB_DEFAULT,
        SCALE_HW_CALIB_THERM_100K_PULLUP,
        SCALE_HW_CALIB_XOTHERM,
        SCALE_HW_CALIB_PMIC_THERM,
        SCALE_HW_CALIB_PM5_CHG_TEMP,
        SCALE_HW_CALIB_PM5_SMB_TEMP,
        SCALE_HW_CALIB_INVALID
    };

.. _`vadc_scale_fn_type.constants`:

Constants
---------

SCALE_DEFAULT
    *undescribed*

SCALE_THERM_100K_PULLUP
    *undescribed*

SCALE_PMIC_THERM
    *undescribed*

SCALE_XOTHERM
    *undescribed*

SCALE_PMI_CHG_TEMP
    *undescribed*

SCALE_HW_CALIB_DEFAULT
    *undescribed*

SCALE_HW_CALIB_THERM_100K_PULLUP
    *undescribed*

SCALE_HW_CALIB_XOTHERM
    *undescribed*

SCALE_HW_CALIB_PMIC_THERM
    *undescribed*

SCALE_HW_CALIB_PM5_CHG_TEMP
    *undescribed*

SCALE_HW_CALIB_PM5_SMB_TEMP
    *undescribed*

SCALE_HW_CALIB_INVALID
    *undescribed*

.. _`vadc_scale_fn_type.scale_default`:

SCALE_DEFAULT
-------------

Default scaling to convert raw adc code to voltage (uV).

.. _`vadc_scale_fn_type.scale_therm_100k_pullup`:

SCALE_THERM_100K_PULLUP
-----------------------

Returns temperature in millidegC.
Uses a mapping table with 100K pullup.

.. _`vadc_scale_fn_type.scale_pmic_therm`:

SCALE_PMIC_THERM
----------------

Returns result in milli degree's Centigrade.

.. _`vadc_scale_fn_type.scale_xotherm`:

SCALE_XOTHERM
-------------

Returns XO thermistor voltage in millidegC.

.. _`vadc_scale_fn_type.scale_pmi_chg_temp`:

SCALE_PMI_CHG_TEMP
------------------

Conversion for PMI CHG temp

.. _`vadc_scale_fn_type.scale_hw_calib_default`:

SCALE_HW_CALIB_DEFAULT
----------------------

Default scaling to convert raw adc code to
voltage (uV) with hardware applied offset/slope values to adc code.

.. _`vadc_scale_fn_type.scale_hw_calib_therm_100k_pullup`:

SCALE_HW_CALIB_THERM_100K_PULLUP
--------------------------------

Returns temperature in millidegC using
lookup table. The hardware applies offset/slope to adc code.

.. _`vadc_scale_fn_type.scale_hw_calib_xotherm`:

SCALE_HW_CALIB_XOTHERM
----------------------

Returns XO thermistor voltage in millidegC using
100k pullup. The hardware applies offset/slope to adc code.

.. _`vadc_scale_fn_type.scale_hw_calib_pmic_therm`:

SCALE_HW_CALIB_PMIC_THERM
-------------------------

Returns result in milli degree's Centigrade.
The hardware applies offset/slope to adc code.

.. _`vadc_scale_fn_type.scale_hw_calib_pm5_chg_temp`:

SCALE_HW_CALIB_PM5_CHG_TEMP
---------------------------

Returns result in millidegrees for PMIC5
charger temperature.

.. _`vadc_scale_fn_type.scale_hw_calib_pm5_smb_temp`:

SCALE_HW_CALIB_PM5_SMB_TEMP
---------------------------

Returns result in millidegrees for PMIC5
SMB1390 temperature.

.. This file was automatic generated / don't edit.

