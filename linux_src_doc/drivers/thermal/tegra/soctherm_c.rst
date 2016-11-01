.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/tegra/soctherm.c

.. _`clk_writel`:

clk_writel
==========

.. c:function:: void clk_writel(struct tegra_soctherm *ts, u32 value, u32 reg)

    writes a value to a CAR register

    :param struct tegra_soctherm \*ts:
        pointer to a struct tegra_soctherm

    :param u32 value:
        *undescribed*

    :param u32 reg:
        the register offset

.. _`clk_writel.description`:

Description
-----------

Writes \ ``v``\  to \ ``reg``\ .  No return value.

.. _`clk_readl`:

clk_readl
=========

.. c:function:: u32 clk_readl(struct tegra_soctherm *ts, u32 reg)

    reads specified register from CAR IP block

    :param struct tegra_soctherm \*ts:
        pointer to a struct tegra_soctherm

    :param u32 reg:
        register address to be read

.. _`clk_readl.return`:

Return
------

the value of the register

.. _`ccroc_writel`:

ccroc_writel
============

.. c:function:: void ccroc_writel(struct tegra_soctherm *ts, u32 value, u32 reg)

    writes a value to a CCROC register

    :param struct tegra_soctherm \*ts:
        pointer to a struct tegra_soctherm

    :param u32 value:
        *undescribed*

    :param u32 reg:
        the register offset

.. _`ccroc_writel.description`:

Description
-----------

Writes \ ``v``\  to \ ``reg``\ .  No return value.

.. _`ccroc_readl`:

ccroc_readl
===========

.. c:function:: u32 ccroc_readl(struct tegra_soctherm *ts, u32 reg)

    reads specified register from CCROC IP block

    :param struct tegra_soctherm \*ts:
        pointer to a struct tegra_soctherm

    :param u32 reg:
        register address to be read

.. _`ccroc_readl.return`:

Return
------

the value of the register

.. _`enforce_temp_range`:

enforce_temp_range
==================

.. c:function:: int enforce_temp_range(struct device *dev, int trip_temp)

    check and enforce temperature range [min, max]

    :param struct device \*dev:
        *undescribed*

    :param int trip_temp:
        the trip temperature to check

.. _`enforce_temp_range.description`:

Description
-----------

Checks and enforces the permitted temperature range that SOC_THERM
HW can support This is
done while taking care of precision.

.. _`enforce_temp_range.return`:

Return
------

The precision adjusted capped temperature in millicelsius.

.. _`thermtrip_program`:

thermtrip_program
=================

.. c:function:: int thermtrip_program(struct device *dev, const struct tegra_tsensor_group *sg, int trip_temp)

    Configures the hardware to shut down the system if a given sensor group reaches a given temperature

    :param struct device \*dev:
        ptr to the struct device for the SOC_THERM IP block

    :param const struct tegra_tsensor_group \*sg:
        pointer to the sensor group to set the thermtrip temperature for

    :param int trip_temp:
        the temperature in millicelsius to trigger the thermal trip at

.. _`thermtrip_program.description`:

Description
-----------

Sets the thermal trip threshold of the given sensor group to be the
\ ``trip_temp``\ .  If this threshold is crossed, the hardware will shut
down.

Note that, although \ ``trip_temp``\  is specified in millicelsius, the
hardware is programmed in degrees Celsius.

.. _`thermtrip_program.return`:

Return
------

0 upon success, or \ ``-EINVAL``\  upon failure.

.. _`throttrip_program`:

throttrip_program
=================

.. c:function:: int throttrip_program(struct device *dev, const struct tegra_tsensor_group *sg, struct soctherm_throt_cfg *stc, int trip_temp)

    Configures the hardware to throttle the pulse if a given sensor group reaches a given temperature

    :param struct device \*dev:
        ptr to the struct device for the SOC_THERM IP block

    :param const struct tegra_tsensor_group \*sg:
        pointer to the sensor group to set the thermtrip temperature for

    :param struct soctherm_throt_cfg \*stc:
        pointer to the throttle need to be triggered

    :param int trip_temp:
        the temperature in millicelsius to trigger the thermal trip at

.. _`throttrip_program.description`:

Description
-----------

Sets the thermal trip threshold and throttle event of the given sensor
group. If this threshold is crossed, the hardware will trigger the
throttle.

Note that, although \ ``trip_temp``\  is specified in millicelsius, the
hardware is programmed in degrees Celsius.

.. _`throttrip_program.return`:

Return
------

0 upon success, or \ ``-EINVAL``\  upon failure.

.. _`tegra_soctherm_set_hwtrips`:

tegra_soctherm_set_hwtrips
==========================

.. c:function:: int tegra_soctherm_set_hwtrips(struct device *dev, const struct tegra_tsensor_group *sg, struct thermal_zone_device *tz)

    set HW trip point from DT data

    :param struct device \*dev:
        struct device \* of the SOC_THERM instance

    :param const struct tegra_tsensor_group \*sg:
        *undescribed*

    :param struct thermal_zone_device \*tz:
        *undescribed*

.. _`tegra_soctherm_set_hwtrips.description`:

Description
-----------

Configure the SOC_THERM HW trip points, setting "THERMTRIP"
"THROTTLE" trip points , using "critical" or "hot" type trip_temp
from thermal zone.
After they have been configured, THERMTRIP or THROTTLE will take
action when the configured SoC thermal sensor group reaches a
certain temperature.

.. _`tegra_soctherm_set_hwtrips.return`:

Return
------

0 upon success, or a negative error code on failure.
"Success" does not mean that trips was enabled; it could also
mean that no node was found in DT.
THERMTRIP has been enabled successfully when a message similar to

.. _`tegra_soctherm_set_hwtrips.this-one-appears-on-the-serial-console`:

this one appears on the serial console
--------------------------------------

"thermtrip: will shut down when sensor group XXX reaches YYYYYY mC"
THROTTLE has been enabled successfully when a message similar to

""throttrip: will throttle when sensor group XXX reaches YYYYYY mC"

.. _`soctherm_init_hw_throt_cdev`:

soctherm_init_hw_throt_cdev
===========================

.. c:function:: void soctherm_init_hw_throt_cdev(struct platform_device *pdev)

    Parse the HW throttle configurations and register them as cooling devices.

    :param struct platform_device \*pdev:
        *undescribed*

.. _`throttlectl_cpu_level_cfg`:

throttlectl_cpu_level_cfg
=========================

.. c:function:: void throttlectl_cpu_level_cfg(struct tegra_soctherm *ts, int level)

    programs CCROC NV_THERM level config

    :param struct tegra_soctherm \*ts:
        *undescribed*

    :param int level:
        describing the level LOW/MED/HIGH of throttling

.. _`throttlectl_cpu_level_cfg.description`:

Description
-----------

It's necessary to set up the CPU-local CCROC NV_THERM instance with
the M/N values desired for each level. This function does this.

This function pre-programs the CCROC NV_THERM levels in terms of
pre-configured "Low", "Medium" or "Heavy" throttle levels which are
mapped to THROT_LEVEL_LOW, THROT_LEVEL_MED and THROT_LEVEL_HVY.

.. _`throttlectl_cpu_level_select`:

throttlectl_cpu_level_select
============================

.. c:function:: void throttlectl_cpu_level_select(struct tegra_soctherm *ts, enum soctherm_throttle_id throt)

    program CPU pulse skipper config

    :param struct tegra_soctherm \*ts:
        *undescribed*

    :param enum soctherm_throttle_id throt:
        the LIGHT/HEAVY of throttle event id

.. _`throttlectl_cpu_level_select.description`:

Description
-----------

Pulse skippers are used to throttle clock frequencies.  This
function programs the pulse skippers based on \ ``throt``\  and platform
data.  This function is used on SoCs which have CPU-local pulse
skipper control, such as T13x. It programs soctherm's interface to
Denver:CCROC NV_THERM in terms of Low, Medium and HIGH throttling
vectors. PSKIP_BYPASS mode is set as required per HW spec.

.. _`throttlectl_cpu_mn`:

throttlectl_cpu_mn
==================

.. c:function:: void throttlectl_cpu_mn(struct tegra_soctherm *ts, enum soctherm_throttle_id throt)

    program CPU pulse skipper configuration

    :param struct tegra_soctherm \*ts:
        *undescribed*

    :param enum soctherm_throttle_id throt:
        the LIGHT/HEAVY of throttle event id

.. _`throttlectl_cpu_mn.description`:

Description
-----------

Pulse skippers are used to throttle clock frequencies.  This
function programs the pulse skippers based on \ ``throt``\  and platform
data.  This function is used for CPUs that have "remote" pulse
skipper control, e.g., the CPU pulse skipper is controlled by the
SOC_THERM IP block.  (SOC_THERM is located outside the CPU
complex.)

.. _`soctherm_throttle_program`:

soctherm_throttle_program
=========================

.. c:function:: void soctherm_throttle_program(struct tegra_soctherm *ts, enum soctherm_throttle_id throt)

    programs pulse skippers' configuration

    :param struct tegra_soctherm \*ts:
        *undescribed*

    :param enum soctherm_throttle_id throt:
        the LIGHT/HEAVY of the throttle event id.

.. _`soctherm_throttle_program.description`:

Description
-----------

Pulse skippers are used to throttle clock frequencies.
This function programs the pulse skippers.

.. This file was automatic generated / don't edit.

