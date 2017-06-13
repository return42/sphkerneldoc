.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/rockchip_thermal.c

.. _`soc_max_sensors`:

SOC_MAX_SENSORS
===============

.. c:function::  SOC_MAX_SENSORS()

.. _`soc_max_sensors.two-sensors`:

Two sensors
-----------

CPU and GPU sensor.

.. _`chip_tsadc_table`:

struct chip_tsadc_table
=======================

.. c:type:: struct chip_tsadc_table

    hold information about chip-specific differences

.. _`chip_tsadc_table.definition`:

Definition
----------

.. code-block:: c

    struct chip_tsadc_table {
        const struct tsadc_table *id;
        unsigned int length;
        u32 data_mask;
        enum adc_sort_mode mode;
    }

.. _`chip_tsadc_table.members`:

Members
-------

id
    conversion table

length
    size of conversion table

data_mask
    mask to apply on data inputs

mode
    sort mode of this adc variant (incrementing or decrementing)

.. _`rockchip_tsadc_chip`:

struct rockchip_tsadc_chip
==========================

.. c:type:: struct rockchip_tsadc_chip

    hold the private data of tsadc chip

.. _`rockchip_tsadc_chip.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_tsadc_chip {
        int chn_id;
        int chn_num;
        int tshut_temp;
        enum tshut_mode tshut_mode;
        enum tshut_polarity tshut_polarity;
        void (*initialize)(struct regmap *grf,void __iomem *reg, enum tshut_polarity p);
        void (*irq_ack)(void __iomem *reg);
        void (*control)(void __iomem *reg, bool on);
        int (*get_temp)(const struct chip_tsadc_table *table,int chn, void __iomem *reg, int *temp);
        int (*set_alarm_temp)(const struct chip_tsadc_table *table,int chn, void __iomem *reg, int temp);
        int (*set_tshut_temp)(const struct chip_tsadc_table *table,int chn, void __iomem *reg, int temp);
        void (*set_tshut_mode)(int chn, void __iomem *reg, enum tshut_mode m);
        struct chip_tsadc_table table;
    }

.. _`rockchip_tsadc_chip.members`:

Members
-------

chn_id
    the sensor id of chip correspond to the channel

chn_num
    the channel number of tsadc chip

tshut_temp
    the hardware-controlled shutdown temperature value

tshut_mode
    the hardware-controlled shutdown mode (0:CRU 1:GPIO)

tshut_polarity
    the hardware-controlled active polarity (0:LOW 1:HIGH)

initialize
    SoC special initialize tsadc controller method

irq_ack
    clear the interrupt

control
    *undescribed*

get_temp
    get the temperature

set_alarm_temp
    set the high temperature interrupt

set_tshut_temp
    set the hardware-controlled shutdown temperature

set_tshut_mode
    set the hardware-controlled shutdown mode

table
    the chip-specific conversion table

.. _`rockchip_thermal_sensor`:

struct rockchip_thermal_sensor
==============================

.. c:type:: struct rockchip_thermal_sensor

    hold the information of thermal sensor

.. _`rockchip_thermal_sensor.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_thermal_sensor {
        struct rockchip_thermal_data *thermal;
        struct thermal_zone_device *tzd;
        int id;
    }

.. _`rockchip_thermal_sensor.members`:

Members
-------

thermal
    pointer to the platform/configuration data

tzd
    pointer to a thermal zone

id
    identifier of the thermal sensor

.. _`rockchip_thermal_data`:

struct rockchip_thermal_data
============================

.. c:type:: struct rockchip_thermal_data

    hold the private data of thermal driver

.. _`rockchip_thermal_data.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_thermal_data {
        const struct rockchip_tsadc_chip *chip;
        struct platform_device *pdev;
        struct reset_control *reset;
        struct rockchip_thermal_sensor sensors;
        struct clk *clk;
        struct clk *pclk;
        struct regmap *grf;
        void __iomem *regs;
        int tshut_temp;
        enum tshut_mode tshut_mode;
        enum tshut_polarity tshut_polarity;
    }

.. _`rockchip_thermal_data.members`:

Members
-------

chip
    pointer to the platform/configuration data

pdev
    platform device of thermal

reset
    the reset controller of tsadc

sensors
    the thermal sensor

clk
    the controller clock is divided by the exteral 24MHz

pclk
    the advanced peripherals bus clock

grf
    the general register file will be used to do static set by software

regs
    the base address of tsadc controller

tshut_temp
    the hardware-controlled shutdown temperature value

tshut_mode
    the hardware-controlled shutdown mode (0:CRU 1:GPIO)

tshut_polarity
    the hardware-controlled active polarity (0:LOW 1:HIGH)

.. _`tsadcv2_user_con`:

TSADCV2_USER_CON
================

.. c:function::  TSADCV2_USER_CON()

.. _`tsadcv2_user_con.description`:

Description
-----------

TSADCV2\_\* are used for RK3288 SoCs, the other chips can reuse it.
TSADCV3\_\* are used for newer SoCs than RK3288. (e.g: RK3228, RK3399)

.. _`tsadc_table`:

struct tsadc_table
==================

.. c:type:: struct tsadc_table

    code to temperature conversion table

.. _`tsadc_table.definition`:

Definition
----------

.. code-block:: c

    struct tsadc_table {
        u32 code;
        int temp;
    }

.. _`tsadc_table.members`:

Members
-------

code
    the value of adc channel

temp
    the temperature

.. _`tsadc_table.note`:

Note
----

code to temperature mapping of the temperature sensor is a piece wise linear
curve.Any temperature, code faling between to 2 give temperatures can be
linearly interpolated.
Code to Temperature mapping should be updated based on manufacturer results.

.. _`rk_tsadcv2_initialize`:

rk_tsadcv2_initialize
=====================

.. c:function:: void rk_tsadcv2_initialize(struct regmap *grf, void __iomem *regs, enum tshut_polarity tshut_polarity)

    initialize TASDC Controller.

    :param struct regmap \*grf:
        *undescribed*

    :param void __iomem \*regs:
        *undescribed*

    :param enum tshut_polarity tshut_polarity:
        *undescribed*

.. _`rk_tsadcv2_initialize.description`:

Description
-----------

(1) Set TSADC_V2_AUTO_PERIOD:
Configure the interleave between every two accessing of
TSADC in normal operation.

(2) Set TSADCV2_AUTO_PERIOD_HT:
Configure the interleave between every two accessing of
TSADC after the temperature is higher than COM_SHUT or COM_INT.

(3) Set TSADCV2_HIGH_INT_DEBOUNCE and TSADC_HIGHT_TSHUT_DEBOUNCE:
If the temperature is higher than COMP_INT or COMP_SHUT for
"debounce" times, TSADC controller will generate interrupt or TSHUT.

.. _`rk_tsadcv3_initialize`:

rk_tsadcv3_initialize
=====================

.. c:function:: void rk_tsadcv3_initialize(struct regmap *grf, void __iomem *regs, enum tshut_polarity tshut_polarity)

    initialize TASDC Controller.

    :param struct regmap \*grf:
        *undescribed*

    :param void __iomem \*regs:
        *undescribed*

    :param enum tshut_polarity tshut_polarity:
        *undescribed*

.. _`rk_tsadcv3_initialize.description`:

Description
-----------

(1) The tsadc control power sequence.

(2) Set TSADC_V2_AUTO_PERIOD:
Configure the interleave between every two accessing of
TSADC in normal operation.

(2) Set TSADCV2_AUTO_PERIOD_HT:
Configure the interleave between every two accessing of
TSADC after the temperature is higher than COM_SHUT or COM_INT.

(3) Set TSADCV2_HIGH_INT_DEBOUNCE and TSADC_HIGHT_TSHUT_DEBOUNCE:
If the temperature is higher than COMP_INT or COMP_SHUT for
"debounce" times, TSADC controller will generate interrupt or TSHUT.

.. _`rk_tsadcv3_control`:

rk_tsadcv3_control
==================

.. c:function:: void rk_tsadcv3_control(void __iomem *regs, bool enable)

    the tsadc controller is enabled or disabled.

    :param void __iomem \*regs:
        *undescribed*

    :param bool enable:
        *undescribed*

.. _`rk_tsadcv3_control.note`:

NOTE
----

TSADC controller works at auto mode, and some SoCs need set the
tsadc_q_sel bit on TSADCV2_AUTO_CON[1]. The (1024 - tsadc_q) as output
adc value if setting this bit to enable.

.. _`rockchip_thermal_reset_controller`:

rockchip_thermal_reset_controller
=================================

.. c:function:: void rockchip_thermal_reset_controller(struct reset_control *reset)

    :param struct reset_control \*reset:
        *undescribed*

.. This file was automatic generated / don't edit.

