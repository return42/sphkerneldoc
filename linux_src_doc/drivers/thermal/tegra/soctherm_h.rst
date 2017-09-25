.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/tegra/soctherm.h

.. _`tegra_tsensor_group`:

struct tegra_tsensor_group
==========================

.. c:type:: struct tegra_tsensor_group

    SOC_THERM sensor group data

.. _`tegra_tsensor_group.definition`:

Definition
----------

.. code-block:: c

    struct tegra_tsensor_group {
        const char *name;
        u8 id;
        u16 sensor_temp_offset;
        u32 sensor_temp_mask;
        u32 pdiv, pdiv_ate, pdiv_mask;
        u32 pllx_hotspot_diff, pllx_hotspot_mask;
        u32 thermtrip_enable_mask;
        u32 thermtrip_any_en_mask;
        u32 thermtrip_threshold_mask;
        u16 thermctl_lvl0_offset;
        u32 thermctl_lvl0_up_thresh_mask;
        u32 thermctl_lvl0_dn_thresh_mask;
    }

.. _`tegra_tsensor_group.members`:

Members
-------

name
    short name of the temperature sensor group

id
    numeric ID of the temperature sensor group

sensor_temp_offset
    offset of the SENSOR_TEMP\* register

sensor_temp_mask
    bit mask for this sensor group in SENSOR_TEMP\* register

pdiv
    the sensor count post-divider to use during runtime

pdiv_ate
    the sensor count post-divider used during automated test

pdiv_mask
    register bitfield mask for the PDIV field for this sensor

pllx_hotspot_diff
    hotspot offset from the PLLX sensor, must be 0 for

pllx_hotspot_mask
    register bitfield mask for the HOTSPOT field

thermtrip_enable_mask
    *undescribed*

thermtrip_any_en_mask
    *undescribed*

thermtrip_threshold_mask
    *undescribed*

thermctl_lvl0_offset
    *undescribed*

thermctl_lvl0_up_thresh_mask
    *undescribed*

thermctl_lvl0_dn_thresh_mask
    *undescribed*

.. This file was automatic generated / don't edit.

