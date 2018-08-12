.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c

.. _`power_dpm_state`:

power_dpm_state
===============

This is a legacy interface and is only provided for backwards compatibility.
The amdgpu driver provides a sysfs API for adjusting certain power
related parameters.  The file power_dpm_state is used for this.
It accepts the following arguments:
- battery
- balanced
- performance

battery

On older GPUs, the vbios provided a special power state for battery
operation.  Selecting battery switched to this state.  This is no
longer provided on newer GPUs so the option does nothing in that case.

balanced

On older GPUs, the vbios provided a special power state for balanced
operation.  Selecting balanced switched to this state.  This is no
longer provided on newer GPUs so the option does nothing in that case.

performance

On older GPUs, the vbios provided a special power state for performance
operation.  Selecting performance switched to this state.  This is no
longer provided on newer GPUs so the option does nothing in that case.

.. _`power_dpm_force_performance_level`:

power_dpm_force_performance_level
=================================

The amdgpu driver provides a sysfs API for adjusting certain power
related parameters.  The file power_dpm_force_performance_level is
used for this.  It accepts the following arguments:
- auto
- low
- high
- manual
- GPU fan
- profile_standard
- profile_min_sclk
- profile_min_mclk
- profile_peak

auto

When auto is selected, the driver will attempt to dynamically select
the optimal power profile for current conditions in the driver.

low

When low is selected, the clocks are forced to the lowest power state.

high

When high is selected, the clocks are forced to the highest power state.

manual

When manual is selected, the user can manually adjust which power states
are enabled for each clock domain via the sysfs pp_dpm_mclk, pp_dpm_sclk,
and pp_dpm_pcie files and adjust the power state transition heuristics
via the pp_power_profile_mode sysfs file.

profile_standard
profile_min_sclk
profile_min_mclk
profile_peak

When the profiling modes are selected, clock and power gating are
disabled and the clocks are set for different profiling cases. This
mode is recommended for profiling specific work loads where you do
not want clock or power gating for clock fluctuation to interfere
with your results. profile_standard sets the clocks to a fixed clock
level which varies from asic to asic.  profile_min_sclk forces the sclk
to the lowest level.  profile_min_mclk forces the mclk to the lowest level.
profile_peak sets all clocks (mclk, sclk, pcie) to the highest levels.

.. _`pp_table`:

pp_table
========

The amdgpu driver provides a sysfs API for uploading new powerplay
tables.  The file pp_table is used for this.  Reading the file
will dump the current power play table.  Writing to the file
will attempt to upload a new powerplay table and re-initialize
powerplay using that new table.

.. _`pp_od_clk_voltage`:

pp_od_clk_voltage
=================

The amdgpu driver provides a sysfs API for adjusting the clocks and voltages
in each power level within a power state.  The pp_od_clk_voltage is used for
this.

Reading the file will display:
- a list of engine clock levels and voltages labeled OD_SCLK
- a list of memory clock levels and voltages labeled OD_MCLK
- a list of valid ranges for sclk, mclk, and voltage labeled OD_RANGE

To manually adjust these settings, first select manual using
power_dpm_force_performance_level. Enter a new value for each
level by writing a string that contains "s/m level clock voltage" to
the file.  E.g., "s 1 500 820" will update sclk level 1 to be 500 MHz
at 820 mV; "m 0 350 810" will update mclk level 0 to be 350 MHz at
810 mV.  When you have edited all of the states as needed, write
"c" (commit) to the file to commit your changes.  If you want to reset to the
default power levels, write "r" (reset) to the file to reset them.

.. _`pp_dpm_sclk-pp_dpm_mclk-pp_dpm_pcie`:

pp_dpm_sclk pp_dpm_mclk pp_dpm_pcie
===================================

The amdgpu driver provides a sysfs API for adjusting what power levels
are enabled for a given power state.  The files pp_dpm_sclk, pp_dpm_mclk,
and pp_dpm_pcie are used for this.

Reading back the files will show you the available power levels within
the power state and the clock information for those levels.

To manually adjust these states, first select manual using
power_dpm_force_performance_level.
Secondly,Enter a new value for each level by inputing a string that
contains " echo xx xx xx > pp_dpm_sclk/mclk/pcie"
E.g., echo 4 5 6 to > pp_dpm_sclk will enable sclk levels 4, 5, and 6.

.. _`pp_power_profile_mode`:

pp_power_profile_mode
=====================

The amdgpu driver provides a sysfs API for adjusting the heuristics
related to switching between power levels in a power state.  The file
pp_power_profile_mode is used for this.

Reading this file outputs a list of all of the predefined power profiles
and the relevant heuristics settings for that profile.

To select a profile or create a custom profile, first select manual using
power_dpm_force_performance_level.  Writing the number of a predefined
profile to pp_power_profile_mode will enable those heuristics.  To
create a custom set of heuristics, write a string of numbers to the file
starting with the number of the custom profile along with a setting
for each heuristic parameter.  Due to differences across asic families
the heuristic parameters vary from family to family.

.. _`hwmon`:

hwmon
=====

The amdgpu driver exposes the following sensor interfaces:
- GPU temperature (via the on-die sensor)
- GPU voltage
- Northbridge voltage (APUs only)
- GPU power
- GPU fan

hwmon interfaces for GPU temperature:
- temp1_input: the on die GPU temperature in millidegrees Celsius
- temp1_crit: temperature critical max value in millidegrees Celsius
- temp1_crit_hyst: temperature hysteresis for critical limit in millidegrees Celsius

hwmon interfaces for GPU voltage:
- in0_input: the voltage on the GPU in millivolts
- in1_input: the voltage on the Northbridge in millivolts

hwmon interfaces for GPU power:
- power1_average: average power used by the GPU in microWatts
- power1_cap_min: minimum cap supported in microWatts
- power1_cap_max: maximum cap supported in microWatts
- power1_cap: selected power cap in microWatts

hwmon interfaces for GPU fan:
- pwm1: pulse width modulation fan level (0-255)
- pwm1_enable: pulse width modulation fan control method
0: no fan speed control
1: manual fan speed control using pwm interface
2: automatic fan speed control
- pwm1_min: pulse width modulation fan control minimum level (0)
- pwm1_max: pulse width modulation fan control maximum level (255)
- fan1_input: fan speed in RPM

You can use hwmon tools like sensors to view this information on your system.

.. This file was automatic generated / don't edit.

