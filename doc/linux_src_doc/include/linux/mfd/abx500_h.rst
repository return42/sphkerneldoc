.. -*- coding: utf-8; mode: rst -*-

========
abx500.h
========


.. _`abx500_init_settings`:

struct abx500_init_settings
===========================

.. c:type:: abx500_init_settings

    


.. _`abx500_init_settings.definition`:

Definition
----------

.. code-block:: c

  struct abx500_init_settings {
  };


.. _`abx500_init_settings.members`:

Members
-------




.. _`abx500_init_settings.description`:

Description
-----------

Initial value of the registers for driver to use during setup.



.. _`abx500_res_to_temp`:

struct abx500_res_to_temp
=========================

.. c:type:: abx500_res_to_temp

    defines one point in a temp to res curve. To be used in battery packs that combines the identification resistor with a NTC resistor.


.. _`abx500_res_to_temp.definition`:

Definition
----------

.. code-block:: c

  struct abx500_res_to_temp {
    int temp;
    int resist;
  };


.. _`abx500_res_to_temp.members`:

Members
-------

:``temp``:
    battery pack temperature in Celcius

:``resist``:
    NTC resistor net total resistance




.. _`abx500_v_to_cap`:

struct abx500_v_to_cap
======================

.. c:type:: abx500_v_to_cap

    Table for translating voltage to capacity


.. _`abx500_v_to_cap.definition`:

Definition
----------

.. code-block:: c

  struct abx500_v_to_cap {
    int voltage;
    int capacity;
  };


.. _`abx500_v_to_cap.members`:

Members
-------

:``voltage``:
    Voltage in mV

:``capacity``:
    Capacity in percent




.. _`abx500_fg_parameters`:

struct abx500_fg_parameters
===========================

.. c:type:: abx500_fg_parameters

    Fuel gauge algorithm parameters, in seconds if not specified


.. _`abx500_fg_parameters.definition`:

Definition
----------

.. code-block:: c

  struct abx500_fg_parameters {
    int recovery_sleep_timer;
    int recovery_total_time;
    int init_timer;
    int init_discard_time;
    int init_total_time;
    int high_curr_time;
    int accu_charging;
    int accu_high_curr;
    int high_curr_threshold;
    int lowbat_threshold;
    int overbat_threshold;
    bool pcut_enable;
    u8 pcut_max_time;
    u8 pcut_flag_time;
    u8 pcut_max_restart;
    u8 pcut_debounce_time;
  };


.. _`abx500_fg_parameters.members`:

Members
-------

:``recovery_sleep_timer``:
    Time between measurements while recovering

:``recovery_total_time``:
    Total recovery time

:``init_timer``:
    Measurement interval during startup

:``init_discard_time``:
    Time we discard voltage measurement at startup

:``init_total_time``:
    Total init time during startup

:``high_curr_time``:
    Time current has to be high to go to recovery

:``accu_charging``:
    FG accumulation time while charging

:``accu_high_curr``:
    FG accumulation time in high current mode

:``high_curr_threshold``:
    High current threshold, in mA

:``lowbat_threshold``:
    Low battery threshold, in mV

:``overbat_threshold``:
    Over battery threshold, in mV
    ``battok_falling_th_sel0``        Threshold in mV for battOk signal sel0
    Resolution in 50 mV step.

    ``battok_raising_th_sel1``        Threshold in mV for battOk signal sel1
    Resolution in 50 mV step.

    ``user_cap_limit``                Capacity reported from user must be within this
    limit to be considered as sane, in percentage
    points.

    ``maint_thres``                        This is the threshold where we stop reporting
    battery full while in maintenance, in per cent

:``pcut_enable``:
    Enable power cut feature in ab8505

:``pcut_max_time``:
    Max time threshold

:``pcut_flag_time``:
    Flagtime threshold

:``pcut_max_restart``:
    Max number of restarts

:``pcut_debounce_time``:
    Sets battery debounce time




.. _`abx500_maxim_parameters`:

struct abx500_maxim_parameters
==============================

.. c:type:: abx500_maxim_parameters

    struct used by the board config.


.. _`abx500_maxim_parameters.definition`:

Definition
----------

.. code-block:: c

  struct abx500_maxim_parameters {
  };


.. _`abx500_maxim_parameters.members`:

Members
-------




.. _`abx500_battery_type`:

struct abx500_battery_type
==========================

.. c:type:: abx500_battery_type

    different batteries supported


.. _`abx500_battery_type.definition`:

Definition
----------

.. code-block:: c

  struct abx500_battery_type {
    int name;
    int resis_high;
    int resis_low;
    int charge_full_design;
    int nominal_voltage;
    int termination_vol;
    int normal_cur_lvl;
    int normal_vol_lvl;
    int maint_a_cur_lvl;
    int maint_a_vol_lvl;
    int maint_a_chg_timer_h;
    int maint_b_cur_lvl;
    int maint_b_vol_lvl;
    int maint_b_chg_timer_h;
    int low_high_cur_lvl;
    int low_high_vol_lvl;
    int battery_resistance;
    const struct abx500_res_to_temp * r_to_t_tbl;
    int n_v_cap_tbl_elements;
    const struct abx500_v_to_cap * v_to_cap_tbl;
  };


.. _`abx500_battery_type.members`:

Members
-------

:``name``:
    battery technology

:``resis_high``:
    battery upper resistance limit

:``resis_low``:
    battery lower resistance limit

:``charge_full_design``:
    Maximum battery capacity in mAh

:``nominal_voltage``:
    Nominal voltage of the battery in mV

:``termination_vol``:
    max voltage upto which battery can be charged
    ``termination_curr``                battery charging termination current in mA
    ``recharge_cap``                battery capacity limit that will trigger a new
    full charging cycle in the case where maintenan-
    -ce charging has been disabled

:``normal_cur_lvl``:
    charger current in normal state in mA

:``normal_vol_lvl``:
    charger voltage in normal state in mV

:``maint_a_cur_lvl``:
    charger current in maintenance A state in mA

:``maint_a_vol_lvl``:
    charger voltage in maintenance A state in mV

:``maint_a_chg_timer_h``:
    charge time in maintenance A state

:``maint_b_cur_lvl``:
    charger current in maintenance B state in mA

:``maint_b_vol_lvl``:
    charger voltage in maintenance B state in mV

:``maint_b_chg_timer_h``:
    charge time in maintenance B state

:``low_high_cur_lvl``:
    charger current in temp low/high state in mA

:``low_high_vol_lvl``:
    charger voltage in temp low/high state in mV'

:``battery_resistance``:
    battery inner resistance in mOhm.

:``r_to_t_tbl``:
    table containing resistance to temp points

:``n_v_cap_tbl_elements``:
    number of elements in v_to_cap_tbl

:``v_to_cap_tbl``:
    Voltage to capacity (in %) table
    ``n_batres_tbl_elements``        number of elements in the batres_tbl
    ``batres_tbl``                        battery internal resistance vs temperature table




.. _`abx500_bm_capacity_levels`:

struct abx500_bm_capacity_levels
================================

.. c:type:: abx500_bm_capacity_levels

    abx500 capacity level data


.. _`abx500_bm_capacity_levels.definition`:

Definition
----------

.. code-block:: c

  struct abx500_bm_capacity_levels {
    int critical;
    int low;
    int normal;
    int high;
    int full;
  };


.. _`abx500_bm_capacity_levels.members`:

Members
-------

:``critical``:
    critical capacity level in percent

:``low``:
    low capacity level in percent

:``normal``:
    normal capacity level in percent

:``high``:
    high capacity level in percent

:``full``:
    full capacity level in percent




.. _`abx500_bm_charger_parameters`:

struct abx500_bm_charger_parameters
===================================

.. c:type:: abx500_bm_charger_parameters

    Charger specific parameters


.. _`abx500_bm_charger_parameters.definition`:

Definition
----------

.. code-block:: c

  struct abx500_bm_charger_parameters {
    int usb_volt_max;
    int usb_curr_max;
    int ac_volt_max;
    int ac_curr_max;
  };


.. _`abx500_bm_charger_parameters.members`:

Members
-------

:``usb_volt_max``:
    maximum allowed USB charger voltage in mV

:``usb_curr_max``:
    maximum allowed USB charger current in mA

:``ac_volt_max``:
    maximum allowed AC charger voltage in mV

:``ac_curr_max``:
    maximum allowed AC charger current in mA




.. _`abx500_bm_data`:

struct abx500_bm_data
=====================

.. c:type:: abx500_bm_data

    abx500 battery management data @temp_under under this temp, charging is stopped @temp_low between this temp and temp_under charging is reduced @temp_high between this temp and temp_over charging is reduced @temp_over over this temp, charging is stopped @temp_now present battery temperature @temp_interval_chg temperature measurement interval in s when charging @temp_interval_nochg temperature measurement interval in s when not charging @main_safety_tmr_h safety timer for main charger @usb_safety_tmr_h safety timer for usb charger @bkup_bat_v voltage which we charge the backup battery with @bkup_bat_i current which we charge the backup battery with @no_maintenance indicates that maintenance charging is disabled @capacity_scaling indicates whether capacity scaling is to be used @abx500_adc_therm placement of thermistor, batctrl or battemp adc @chg_unknown_bat flag to enable charging of unknown batteries @enable_overshoot flag to enable VBAT overshoot control @auto_trig flag to enable auto adc trigger @fg_res resistance of FG resistor in 0.1mOhm @n_btypes number of elements in array bat_type @batt_id index of the identified battery in array bat_type @interval_charging charge alg cycle period time when charging (sec) @interval_not_charging charge alg cycle period time when not charging (sec) @temp_hysteresis temperature hysteresis @gnd_lift_resistance Battery ground to phone ground resistance (mOhm) @n_chg_out_curr number of elements in array chg_output_curr @n_chg_in_curr number of elements in array chg_input_curr @chg_output_curr charger output current level map @chg_input_curr charger input current level map @maxi maximization parameters @cap_levels capacity in percent for the different capacity levels @bat_type table of supported battery types @chg_params charger parameters @fg_params fuel gauge parameters


.. _`abx500_bm_data.definition`:

Definition
----------

.. code-block:: c

  struct abx500_bm_data {
  };


.. _`abx500_bm_data.members`:

Members
-------




.. _`abx500_mask_and_set_register_interruptible`:

abx500_mask_and_set_register_interruptible
==========================================

.. c:function:: int abx500_mask_and_set_register_interruptible (struct device *dev, u8 bank, u8 reg, u8 bitmask, u8 bitvalues)

    Modifies selected bits of a target register

    :param struct device \*dev:
        The AB sub device.

    :param u8 bank:
        The i2c bank number.

    :param u8 reg:

        *undescribed*

    :param u8 bitmask:
        The bit mask to use.

    :param u8 bitvalues:
        The new bit values.



.. _`abx500_mask_and_set_register_interruptible.updates-the-value-of-an-ab-register`:

Updates the value of an AB register
-----------------------------------

value -> ((value & ~bitmask) | (bitvalues & bitmask))

