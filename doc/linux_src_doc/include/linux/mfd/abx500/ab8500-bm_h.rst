.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/abx500/ab8500-bm.h

.. _`res_to_temp`:

struct res_to_temp
==================

.. c:type:: struct res_to_temp

    defines one point in a temp to res curve. To be used in battery packs that combines the identification resistor with a NTC resistor.

.. _`res_to_temp.definition`:

Definition
----------

.. code-block:: c

    struct res_to_temp {
        int temp;
        int resist;
    }

.. _`res_to_temp.members`:

Members
-------

temp
    battery pack temperature in Celcius

resist
    NTC resistor net total resistance

.. _`batres_vs_temp`:

struct batres_vs_temp
=====================

.. c:type:: struct batres_vs_temp

    defines one point in a temp vs battery internal resistance curve.

.. _`batres_vs_temp.definition`:

Definition
----------

.. code-block:: c

    struct batres_vs_temp {
        int temp;
        int resist;
    }

.. _`batres_vs_temp.members`:

Members
-------

temp
    battery pack temperature in Celcius

resist
    battery internal reistance in mOhm

.. _`ab8500_fg_parameters`:

struct ab8500_fg_parameters
===========================

.. c:type:: struct ab8500_fg_parameters

    Fuel gauge algorithm parameters, in seconds if not specified

.. _`ab8500_fg_parameters.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_fg_parameters {
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
        int battok_falling_th_sel0;
        int battok_raising_th_sel1;
        int user_cap_limit;
        int maint_thres;
        bool pcut_enable;
        u8 pcut_max_time;
        u8 pcut_flag_time;
        u8 pcut_max_restart;
        u8 pcut_debunce_time;
    }

.. _`ab8500_fg_parameters.members`:

Members
-------

recovery_sleep_timer
    Time between measurements while recovering

recovery_total_time
    Total recovery time

init_timer
    Measurement interval during startup

init_discard_time
    Time we discard voltage measurement at startup

init_total_time
    Total init time during startup

high_curr_time
    Time current has to be high to go to recovery

accu_charging
    FG accumulation time while charging

accu_high_curr
    FG accumulation time in high current mode

high_curr_threshold
    High current threshold, in mA

lowbat_threshold
    Low battery threshold, in mV
    \ ``battok_falling_th_sel0``\       Threshold in mV for battOk signal sel0
    Resolution in 50 mV step.
    \ ``battok_raising_th_sel1``\       Threshold in mV for battOk signal sel1
    Resolution in 50 mV step.
    \ ``user_cap_limit``\               Capacity reported from user must be within this
    limit to be considered as sane, in percentage
    points.
    \ ``maint_thres``\                  This is the threshold where we stop reporting
    battery full while in maintenance, in per cent

battok_falling_th_sel0
    *undescribed*

battok_raising_th_sel1
    *undescribed*

user_cap_limit
    *undescribed*

maint_thres
    *undescribed*

pcut_enable
    Enable power cut feature in ab8505

pcut_max_time
    Max time threshold

pcut_flag_time
    Flagtime threshold

pcut_max_restart
    Max number of restarts

pcut_debunce_time
    Sets battery debounce time

.. _`ab8500_maxim_parameters`:

struct ab8500_maxim_parameters
==============================

.. c:type:: struct ab8500_maxim_parameters

    struct used by the board config.

.. _`ab8500_maxim_parameters.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_maxim_parameters {
        bool ena_maxi;
        int chg_curr;
        int wait_cycles;
        int charger_curr_step;
    }

.. _`ab8500_maxim_parameters.members`:

Members
-------

ena_maxi
    *undescribed*

chg_curr
    *undescribed*

wait_cycles
    *undescribed*

charger_curr_step
    *undescribed*

.. _`ab8500_bm_capacity_levels`:

struct ab8500_bm_capacity_levels
================================

.. c:type:: struct ab8500_bm_capacity_levels

    ab8500 capacity level data

.. _`ab8500_bm_capacity_levels.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_bm_capacity_levels {
        int critical;
        int low;
        int normal;
        int high;
        int full;
    }

.. _`ab8500_bm_capacity_levels.members`:

Members
-------

critical
    critical capacity level in percent

low
    low capacity level in percent

normal
    normal capacity level in percent

high
    high capacity level in percent

full
    full capacity level in percent

.. _`ab8500_bm_charger_parameters`:

struct ab8500_bm_charger_parameters
===================================

.. c:type:: struct ab8500_bm_charger_parameters

    Charger specific parameters

.. _`ab8500_bm_charger_parameters.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_bm_charger_parameters {
        int usb_volt_max;
        int usb_curr_max;
        int ac_volt_max;
        int ac_curr_max;
    }

.. _`ab8500_bm_charger_parameters.members`:

Members
-------

usb_volt_max
    maximum allowed USB charger voltage in mV

usb_curr_max
    maximum allowed USB charger current in mA

ac_volt_max
    maximum allowed AC charger voltage in mV

ac_curr_max
    maximum allowed AC charger current in mA

.. _`ab8500_bm_data`:

struct ab8500_bm_data
=====================

.. c:type:: struct ab8500_bm_data

    ab8500 battery management data \ ``temp_under``\           under this temp, charging is stopped \ ``temp_low``\             between this temp and temp_under charging is reduced \ ``temp_high``\            between this temp and temp_over charging is reduced \ ``temp_over``\            over this temp, charging is stopped \ ``temp_interval_chg``\    temperature measurement interval in s when charging \ ``temp_interval_nochg``\  temperature measurement interval in s when not charging \ ``main_safety_tmr_h``\    safety timer for main charger \ ``usb_safety_tmr_h``\     safety timer for usb charger \ ``bkup_bat_v``\           voltage which we charge the backup battery with \ ``bkup_bat_i``\           current which we charge the backup battery with \ ``no_maintenance``\       indicates that maintenance charging is disabled \ ``capacity_scaling``\     indicates whether capacity scaling is to be used \ ``adc_therm``\            placement of thermistor, batctrl or battemp adc \ ``chg_unknown_bat``\      flag to enable charging of unknown batteries \ ``enable_overshoot``\     flag to enable VBAT overshoot control \ ``fg_res``\               resistance of FG resistor in 0.1mOhm \ ``n_btypes``\             number of elements in array bat_type \ ``batt_id``\              index of the identified battery in array bat_type \ ``interval_charging``\    charge alg cycle period time when charging (sec) \ ``interval_not_charging``\  charge alg cycle period time when not charging (sec) \ ``temp_hysteresis``\      temperature hysteresis \ ``gnd_lift_resistance``\  Battery ground to phone ground resistance (mOhm)

.. _`ab8500_bm_data.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_bm_data {
        int temp_under;
        int temp_low;
        int temp_high;
        int temp_over;
        int temp_interval_chg;
        int temp_interval_nochg;
        int main_safety_tmr_h;
        int usb_safety_tmr_h;
        int bkup_bat_v;
        int bkup_bat_i;
        bool no_maintenance;
        bool capacity_scaling;
        bool chg_unknown_bat;
        bool enable_overshoot;
        enum abx500_adc_therm adc_therm;
        int fg_res;
        int n_btypes;
        int batt_id;
        int interval_charging;
        int interval_not_charging;
        int temp_hysteresis;
        int gnd_lift_resistance;
        const struct ab8500_maxim_parameters *maxi;
        const struct ab8500_bm_capacity_levels *cap_levels;
        const struct ab8500_bm_charger_parameters *chg_params;
        const struct ab8500_fg_parameters *fg_params;
    }

.. _`ab8500_bm_data.members`:

Members
-------

temp_under
    *undescribed*

temp_low
    *undescribed*

temp_high
    *undescribed*

temp_over
    *undescribed*

temp_interval_chg
    *undescribed*

temp_interval_nochg
    *undescribed*

main_safety_tmr_h
    *undescribed*

usb_safety_tmr_h
    *undescribed*

bkup_bat_v
    *undescribed*

bkup_bat_i
    *undescribed*

no_maintenance
    *undescribed*

capacity_scaling
    *undescribed*

chg_unknown_bat
    *undescribed*

enable_overshoot
    *undescribed*

adc_therm
    *undescribed*

fg_res
    *undescribed*

n_btypes
    *undescribed*

batt_id
    *undescribed*

interval_charging
    *undescribed*

interval_not_charging
    *undescribed*

temp_hysteresis
    *undescribed*

gnd_lift_resistance
    *undescribed*

maxi
    maximization parameters
    \ ``cap_levels``\           capacity in percent for the different capacity levels
    \ ``bat_type``\             table of supported battery types
    \ ``chg_params``\           charger parameters
    \ ``fg_params``\            fuel gauge parameters

cap_levels
    *undescribed*

chg_params
    *undescribed*

fg_params
    *undescribed*

.. This file was automatic generated / don't edit.

