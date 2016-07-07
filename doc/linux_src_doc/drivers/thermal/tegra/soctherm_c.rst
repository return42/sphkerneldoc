.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/tegra/soctherm.c

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
trip points , using "critical" type trip_temp from thermal
zone.
After they have been configured, THERMTRIP will take action
when the configured SoC thermal sensor group reaches a
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

.. This file was automatic generated / don't edit.

