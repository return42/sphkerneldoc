.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/abx500_chargalg.c

.. _`abx500_charge_curr_maximization`:

struct abx500_charge_curr_maximization
======================================

.. c:type:: struct abx500_charge_curr_maximization

    Charger maximization parameters

.. _`abx500_charge_curr_maximization.definition`:

Definition
----------

.. code-block:: c

    struct abx500_charge_curr_maximization {
        int original_iset;
        int current_iset;
        int test_delta_i;
        int condition_cnt;
        int max_current;
        int wait_cnt;
        u8 level;
    }

.. _`abx500_charge_curr_maximization.members`:

Members
-------

original_iset
    the non optimized/maximised charger current

current_iset
    the charging current used at this moment

test_delta_i
    the delta between the current we want to charge and the

condition_cnt
    number of iterations needed before a new charger current

max_current
    maximum charger current

wait_cnt
    to avoid too fast current step down in case of charger
    voltage collapse, we insert this delay between step
    down

level
    tells in how many steps the charging current has been

.. _`abx500_chargalg`:

struct abx500_chargalg
======================

.. c:type:: struct abx500_chargalg

    abx500 Charging algorithm device information

.. _`abx500_chargalg.definition`:

Definition
----------

.. code-block:: c

    struct abx500_chargalg {
        struct device *dev;
        int charge_status;
        int eoc_cnt;
        bool maintenance_chg;
        int t_hyst_norm;
        int t_hyst_lowhigh;
        enum abx500_chargalg_states charge_state;
        struct abx500_charge_curr_maximization ccm;
        struct abx500_chargalg_charger_info chg_info;
        struct abx500_chargalg_battery_data batt_data;
        struct abx500_chargalg_suspension_status susp_status;
        struct ab8500 *parent;
        struct abx500_chargalg_current_step_status curr_status;
        struct abx500_bm_data *bm;
        struct power_supply *chargalg_psy;
        struct ux500_charger *ac_chg;
        struct ux500_charger *usb_chg;
        struct abx500_chargalg_events events;
        struct workqueue_struct *chargalg_wq;
        struct delayed_work chargalg_periodic_work;
        struct delayed_work chargalg_wd_work;
        struct work_struct chargalg_work;
        struct hrtimer safety_timer;
        struct hrtimer maintenance_timer;
        struct kobject chargalg_kobject;
    }

.. _`abx500_chargalg.members`:

Members
-------

dev
    pointer to the structure device

charge_status
    battery operating status

eoc_cnt
    counter used to determine end-of_charge

maintenance_chg
    indicate if maintenance charge is active
    \ ``t_hyst_norm``\          temperature hysteresis when the temperature has been
    over or under normal limits
    \ ``t_hyst_lowhigh``\       temperature hysteresis when the temperature has been
    over or under the high or low limits

t_hyst_norm
    *undescribed*

t_hyst_lowhigh
    *undescribed*

charge_state
    current state of the charging algorithm
    \ ``ccm``\                  charging current maximization parameters

ccm
    *undescribed*

chg_info
    information about connected charger types

batt_data
    data of the battery

susp_status
    current charger suspension status

parent
    pointer to the struct abx500

curr_status
    Current step status for over-current protection

bm
    Platform specific battery management information

chargalg_psy
    structure that holds the battery properties exposed by
    the charging algorithm

ac_chg
    *undescribed*

usb_chg
    *undescribed*

events
    structure for information about events triggered

chargalg_wq
    work queue for running the charging algorithm

chargalg_periodic_work
    work to run the charging algorithm periodically

chargalg_wd_work
    work to kick the charger watchdog periodically

chargalg_work
    work to run the charging algorithm instantly

safety_timer
    charging safety timer

maintenance_timer
    maintenance charging timer

chargalg_kobject
    structure of type kobject

.. _`abx500_chargalg_safety_timer_expired`:

abx500_chargalg_safety_timer_expired
====================================

.. c:function:: enum hrtimer_restart abx500_chargalg_safety_timer_expired(struct hrtimer *timer)

    Expiration of the safety timer

    :param struct hrtimer \*timer:
        pointer to the hrtimer structure

.. _`abx500_chargalg_safety_timer_expired.description`:

Description
-----------

This function gets called when the safety timer for the charger
expires

.. _`abx500_chargalg_maintenance_timer_expired`:

abx500_chargalg_maintenance_timer_expired
=========================================

.. c:function:: enum hrtimer_restart abx500_chargalg_maintenance_timer_expired(struct hrtimer *timer)

    Expiration of the maintenance timer

    :param struct hrtimer \*timer:
        pointer to the timer structure

.. _`abx500_chargalg_maintenance_timer_expired.description`:

Description
-----------

This function gets called when the maintenence timer
expires

.. _`abx500_chargalg_state_to`:

abx500_chargalg_state_to
========================

.. c:function:: void abx500_chargalg_state_to(struct abx500_chargalg *di, enum abx500_chargalg_states state)

    Change charge state

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param enum abx500_chargalg_states state:
        *undescribed*

.. _`abx500_chargalg_state_to.description`:

Description
-----------

This function gets called when a charge state change should occur

.. _`abx500_chargalg_check_charger_connection`:

abx500_chargalg_check_charger_connection
========================================

.. c:function:: int abx500_chargalg_check_charger_connection(struct abx500_chargalg *di)

    Check charger connection change

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_check_charger_connection.description`:

Description
-----------

This function will check if there is a change in the charger connection
and change charge state accordingly. AC has precedence over USB.

.. _`abx500_chargalg_check_current_step_status`:

abx500_chargalg_check_current_step_status
=========================================

.. c:function:: void abx500_chargalg_check_current_step_status(struct abx500_chargalg *di)

    Check charging current step status.

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_check_current_step_status.description`:

Description
-----------

This function will check if there is a change in the charging current step
and change charge state accordingly.

.. _`abx500_chargalg_start_safety_timer`:

abx500_chargalg_start_safety_timer
==================================

.. c:function:: void abx500_chargalg_start_safety_timer(struct abx500_chargalg *di)

    Start charging safety timer

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_start_safety_timer.description`:

Description
-----------

The safety timer is used to avoid overcharging of old or bad batteries.
There are different timers for AC and USB

.. _`abx500_chargalg_stop_safety_timer`:

abx500_chargalg_stop_safety_timer
=================================

.. c:function:: void abx500_chargalg_stop_safety_timer(struct abx500_chargalg *di)

    Stop charging safety timer

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_stop_safety_timer.description`:

Description
-----------

The safety timer is stopped whenever the NORMAL state is exited

.. _`abx500_chargalg_start_maintenance_timer`:

abx500_chargalg_start_maintenance_timer
=======================================

.. c:function:: void abx500_chargalg_start_maintenance_timer(struct abx500_chargalg *di, int duration)

    Start charging maintenance timer

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param int duration:
        duration of ther maintenance timer in hours

.. _`abx500_chargalg_start_maintenance_timer.description`:

Description
-----------

The maintenance timer is used to maintain the charge in the battery once
the battery is considered full. These timers are chosen to match the
discharge curve of the battery

.. _`abx500_chargalg_stop_maintenance_timer`:

abx500_chargalg_stop_maintenance_timer
======================================

.. c:function:: void abx500_chargalg_stop_maintenance_timer(struct abx500_chargalg *di)

    Stop maintenance timer

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_stop_maintenance_timer.description`:

Description
-----------

The maintenance timer is stopped whenever maintenance ends or when another
state is entered

.. _`abx500_chargalg_kick_watchdog`:

abx500_chargalg_kick_watchdog
=============================

.. c:function:: int abx500_chargalg_kick_watchdog(struct abx500_chargalg *di)

    Kick charger watchdog

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_kick_watchdog.description`:

Description
-----------

The charger watchdog have to be kicked periodically whenever the charger is
on, else the ABB will reset the system

.. _`abx500_chargalg_ac_en`:

abx500_chargalg_ac_en
=====================

.. c:function:: int abx500_chargalg_ac_en(struct abx500_chargalg *di, int enable, int vset, int iset)

    Turn on/off the AC charger

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param int enable:
        charger on/off

    :param int vset:
        requested charger output voltage

    :param int iset:
        requested charger output current

.. _`abx500_chargalg_ac_en.description`:

Description
-----------

The AC charger will be turned on/off with the requested charge voltage and
current

.. _`abx500_chargalg_usb_en`:

abx500_chargalg_usb_en
======================

.. c:function:: int abx500_chargalg_usb_en(struct abx500_chargalg *di, int enable, int vset, int iset)

    Turn on/off the USB charger

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param int enable:
        charger on/off

    :param int vset:
        requested charger output voltage

    :param int iset:
        requested charger output current

.. _`abx500_chargalg_usb_en.description`:

Description
-----------

The USB charger will be turned on/off with the requested charge voltage and
current

.. _`ab8540_chargalg_usb_pre_chg_en`:

ab8540_chargalg_usb_pre_chg_en
==============================

.. c:function:: int ab8540_chargalg_usb_pre_chg_en(struct abx500_chargalg *di, bool enable)

    Enable/ disable USB pre-charge

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param bool enable:
        USB pre-charge enable/disable

.. _`ab8540_chargalg_usb_pre_chg_en.description`:

Description
-----------

The USB USB pre-charge will be enable/ disable

.. _`abx500_chargalg_update_chg_curr`:

abx500_chargalg_update_chg_curr
===============================

.. c:function:: int abx500_chargalg_update_chg_curr(struct abx500_chargalg *di, int iset)

    Update charger current

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param int iset:
        requested charger output current

.. _`abx500_chargalg_update_chg_curr.description`:

Description
-----------

The charger output current will be updated for the charger
that is currently in use

.. _`abx500_chargalg_stop_charging`:

abx500_chargalg_stop_charging
=============================

.. c:function:: void abx500_chargalg_stop_charging(struct abx500_chargalg *di)

    Stop charging

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_stop_charging.description`:

Description
-----------

This function is called from any state where charging should be stopped.
All charging is disabled and all status parameters and timers are changed
accordingly

.. _`abx500_chargalg_hold_charging`:

abx500_chargalg_hold_charging
=============================

.. c:function:: void abx500_chargalg_hold_charging(struct abx500_chargalg *di)

    Pauses charging

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_hold_charging.description`:

Description
-----------

This function is called in the case where maintenance charging has been
disabled and instead a battery voltage mode is entered to check when the
battery voltage has reached a certain recharge voltage

.. _`abx500_chargalg_start_charging`:

abx500_chargalg_start_charging
==============================

.. c:function:: void abx500_chargalg_start_charging(struct abx500_chargalg *di, int vset, int iset)

    Start the charger

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

    :param int vset:
        requested charger output voltage

    :param int iset:
        requested charger output current

.. _`abx500_chargalg_start_charging.description`:

Description
-----------

A charger will be enabled depending on the requested charger type that was
detected previously.

.. _`abx500_chargalg_check_temp`:

abx500_chargalg_check_temp
==========================

.. c:function:: void abx500_chargalg_check_temp(struct abx500_chargalg *di)

    Check battery temperature ranges

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_check_temp.description`:

Description
-----------

The battery temperature is checked against the predefined limits and the
charge state is changed accordingly

.. _`abx500_chargalg_check_charger_voltage`:

abx500_chargalg_check_charger_voltage
=====================================

.. c:function:: void abx500_chargalg_check_charger_voltage(struct abx500_chargalg *di)

    Check charger voltage

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_check_charger_voltage.description`:

Description
-----------

Charger voltage is checked against maximum limit

.. _`abx500_chargalg_end_of_charge`:

abx500_chargalg_end_of_charge
=============================

.. c:function:: void abx500_chargalg_end_of_charge(struct abx500_chargalg *di)

    Check if end-of-charge criteria is fulfilled

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_end_of_charge.description`:

Description
-----------

End-of-charge criteria is fulfilled when the battery voltage is above a
certain limit and the battery current is below a certain limit for a
predefined number of consecutive seconds. If true, the battery is full

.. _`abx500_chargalg_chg_curr_maxim`:

abx500_chargalg_chg_curr_maxim
==============================

.. c:function:: enum maxim_ret abx500_chargalg_chg_curr_maxim(struct abx500_chargalg *di)

    increases the charger current to compensate for the system load \ ``di``\           pointer to the abx500_chargalg structure

    :param struct abx500_chargalg \*di:
        *undescribed*

.. _`abx500_chargalg_chg_curr_maxim.description`:

Description
-----------

This maximization function is used to raise the charger current to get the
battery current as close to the optimal value as possible. The battery
current during charging is affected by the system load

.. _`abx500_chargalg_external_power_changed`:

abx500_chargalg_external_power_changed
======================================

.. c:function:: void abx500_chargalg_external_power_changed(struct power_supply *psy)

    callback for power supply changes

    :param struct power_supply \*psy:
        pointer to the structure power_supply

.. _`abx500_chargalg_external_power_changed.description`:

Description
-----------

This function is the entry point of the pointer external_power_changed
of the structure power_supply.
This function gets executed when there is a change in any external power
supply that this driver needs to be notified of.

.. _`abx500_chargalg_algorithm`:

abx500_chargalg_algorithm
=========================

.. c:function:: void abx500_chargalg_algorithm(struct abx500_chargalg *di)

    Main function for the algorithm

    :param struct abx500_chargalg \*di:
        pointer to the abx500_chargalg structure

.. _`abx500_chargalg_algorithm.description`:

Description
-----------

This is the main control function for the charging algorithm.
It is called periodically or when something happens that will
trigger a state change

.. _`abx500_chargalg_periodic_work`:

abx500_chargalg_periodic_work
=============================

.. c:function:: void abx500_chargalg_periodic_work(struct work_struct *work)

    Periodic work for the algorithm

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`abx500_chargalg_periodic_work.description`:

Description
-----------

Work queue function for the charging algorithm

.. _`abx500_chargalg_wd_work`:

abx500_chargalg_wd_work
=======================

.. c:function:: void abx500_chargalg_wd_work(struct work_struct *work)

    periodic work to kick the charger watchdog

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`abx500_chargalg_wd_work.description`:

Description
-----------

Work queue function for kicking the charger watchdog

.. _`abx500_chargalg_work`:

abx500_chargalg_work
====================

.. c:function:: void abx500_chargalg_work(struct work_struct *work)

    Work to run the charging algorithm instantly

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`abx500_chargalg_work.description`:

Description
-----------

Work queue function for calling the charging algorithm

.. _`abx500_chargalg_get_property`:

abx500_chargalg_get_property
============================

.. c:function:: int abx500_chargalg_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    get the chargalg properties

    :param struct power_supply \*psy:
        pointer to the power_supply structure

    :param enum power_supply_property psp:
        pointer to the power_supply_property structure

    :param union power_supply_propval \*val:
        pointer to the power_supply_propval union

.. _`abx500_chargalg_get_property.description`:

Description
-----------

This function gets called when an application tries to get the
chargalg properties by reading the sysfs files.

.. _`abx500_chargalg_get_property.status`:

status
------

charging/discharging/full/unknown

.. _`abx500_chargalg_get_property.health`:

health
------

health of the battery
Returns error code in case of failure else 0 on success

.. _`abx500_chargalg_sysfs_exit`:

abx500_chargalg_sysfs_exit
==========================

.. c:function:: void abx500_chargalg_sysfs_exit(struct abx500_chargalg *di)

    de-init of sysfs entry

    :param struct abx500_chargalg \*di:
        pointer to the struct abx500_chargalg

.. _`abx500_chargalg_sysfs_exit.description`:

Description
-----------

This function removes the entry in sysfs.

.. _`abx500_chargalg_sysfs_init`:

abx500_chargalg_sysfs_init
==========================

.. c:function:: int abx500_chargalg_sysfs_init(struct abx500_chargalg *di)

    init of sysfs entry

    :param struct abx500_chargalg \*di:
        pointer to the struct abx500_chargalg

.. _`abx500_chargalg_sysfs_init.description`:

Description
-----------

This function adds an entry in sysfs.
Returns error code in case of failure else 0(on success)

.. This file was automatic generated / don't edit.

