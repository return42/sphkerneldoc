.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/samsung/exynos_tmu.h

.. _`exynos_tmu_platform_data`:

struct exynos_tmu_platform_data
===============================

.. c:type:: struct exynos_tmu_platform_data


.. _`exynos_tmu_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos_tmu_platform_data {
        u8 gain;
        u8 reference_voltage;
        u8 noise_cancel_mode;
        u32 efuse_value;
        u32 min_efuse_value;
        u32 max_efuse_value;
        u8 first_point_trim;
        u8 second_point_trim;
        u8 default_temp_offset;
        enum soc_type type;
        u32 cal_type;
    }

.. _`exynos_tmu_platform_data.members`:

Members
-------

gain
    gain of amplifier in the positive-TC generator block
    0 < gain <= 15

reference_voltage
    reference voltage of amplifier
    in the positive-TC generator block
    0 < reference_voltage <= 31

noise_cancel_mode
    noise cancellation mode
    000, 100, 101, 110 and 111 can be different modes

efuse_value
    platform defined fuse value

min_efuse_value
    minimum valid trimming data

max_efuse_value
    maximum valid trimming data

first_point_trim
    *undescribed*

second_point_trim
    *undescribed*

default_temp_offset
    default temperature offset in case of no trimming

type
    determines the type of SOC

cal_type
    calibration type for temperature

.. _`exynos_tmu_platform_data.description`:

Description
-----------

This structure is required for configuration of exynos_tmu driver.

.. This file was automatic generated / don't edit.

