.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/power/charger-manager.h

.. _`charger_cable`:

struct charger_cable
====================

.. c:type:: struct charger_cable


.. _`charger_cable.definition`:

Definition
----------

.. code-block:: c

    struct charger_cable {
        const char *extcon_name;
        const char *name;
        struct extcon_specific_cable_nb extcon_dev;
        struct work_struct wq;
        struct notifier_block nb;
        bool attached;
        struct charger_regulator *charger;
        int min_uA;
        int max_uA;
        struct charger_manager *cm;
    }

.. _`charger_cable.members`:

Members
-------

extcon_name
    the name of extcon device.

name
    the name of charger cable(external connector).

extcon_dev
    the extcon device.

wq
    the workqueue to control charger according to the state of
    charger cable. If charger cable is attached, enable charger.
    But if charger cable is detached, disable charger.

nb
    the notifier block to receive changed state from EXTCON
    (External Connector) when charger cable is attached/detached.

attached
    the state of charger cable.

charger
    the instance of struct charger_regulator.

min_uA
    *undescribed*

max_uA
    *undescribed*

cm
    the Charger Manager representing the battery.

.. _`charger_cable.true`:

true
----

the charger cable is attached

.. _`charger_cable.false`:

false
-----

the charger cable is detached

.. _`charger_regulator`:

struct charger_regulator
========================

.. c:type:: struct charger_regulator


.. _`charger_regulator.definition`:

Definition
----------

.. code-block:: c

    struct charger_regulator {
        const char *regulator_name;
        struct regulator *consumer;
        int externally_control;
        struct charger_cable *cables;
        int num_cables;
        struct attribute_group attr_g;
        struct device_attribute attr_name;
        struct device_attribute attr_state;
        struct device_attribute attr_externally_control;
        struct attribute  *attrs[4];
        struct charger_manager *cm;
    }

.. _`charger_regulator.members`:

Members
-------

regulator_name
    the name of regulator for using charger.

consumer
    the regulator consumer for the charger.

externally_control
    Set if the charger-manager cannot control charger,
    the charger will be maintained with disabled state.

cables
    the array of charger cables to enable/disable charger
    and set current limit according to constraint data of
    struct charger_cable if only charger cable included
    in the array of charger cables is attached/detached.

num_cables
    the number of charger cables.

attr_g
    Attribute group for the charger(regulator)

attr_name
    "name" sysfs entry

attr_state
    "state" sysfs entry

attr_externally_control
    "externally_control" sysfs entry

attrs
    Arrays pointing to attr_name/state/externally_control for attr_g

cm
    *undescribed*

.. _`charger_desc`:

struct charger_desc
===================

.. c:type:: struct charger_desc


.. _`charger_desc.definition`:

Definition
----------

.. code-block:: c

    struct charger_desc {
        const char *psy_name;
        enum polling_modes polling_mode;
        unsigned int polling_interval_ms;
        unsigned int fullbatt_vchkdrop_ms;
        unsigned int fullbatt_vchkdrop_uV;
        unsigned int fullbatt_uV;
        unsigned int fullbatt_soc;
        unsigned int fullbatt_full_capacity;
        enum data_source battery_present;
        const char **psy_charger_stat;
        int num_charger_regulators;
        struct charger_regulator *charger_regulators;
        const char *psy_fuel_gauge;
        const char *thermal_zone;
        int temp_min;
        int temp_max;
        int temp_diff;
        bool measure_battery_temp;
        u32 charging_max_duration_ms;
        u32 discharging_max_duration_ms;
    }

.. _`charger_desc.members`:

Members
-------

psy_name
    the name of power-supply-class for charger manager

polling_mode
    Determine which polling mode will be used

polling_interval_ms
    interval in millisecond at which
    charger manager will monitor battery health

fullbatt_vchkdrop_ms
    *undescribed*

fullbatt_vchkdrop_uV
    Check voltage drop after the battery is fully charged.
    If it has dropped more than fullbatt_vchkdrop_uV after
    fullbatt_vchkdrop_ms, CM will restart charging.

fullbatt_uV
    voltage in microvolt
    If VBATT >= fullbatt_uV, it is assumed to be full.

fullbatt_soc
    state of Charge in %
    If state of Charge >= fullbatt_soc, it is assumed to be full.

fullbatt_full_capacity
    full capacity measure
    If full capacity of battery >= fullbatt_full_capacity,
    it is assumed to be full.

battery_present
    Specify where information for existence of battery can be obtained

psy_charger_stat
    the names of power-supply for chargers

num_charger_regulators
    *undescribed*

charger_regulators
    array of charger regulators

psy_fuel_gauge
    the name of power-supply for fuel gauge

thermal_zone
    the name of thermal zone for battery

temp_min
    Minimum battery temperature for charging.

temp_max
    Maximum battery temperature for charging.

temp_diff
    Temperature difference to restart charging.

measure_battery_temp
    *undescribed*

charging_max_duration_ms
    Maximum possible duration for charging
    If whole charging duration exceed 'charging_max_duration_ms',
    cm stop charging.

discharging_max_duration_ms
    Maximum possible duration for discharging with charger cable
    after full-batt. If discharging duration exceed 'discharging
    max_duration_ms', cm start charging.

.. _`charger_desc.true`:

true
----

measure battery temperature

.. _`charger_desc.false`:

false
-----

measure ambient temperature

.. _`charger_manager`:

struct charger_manager
======================

.. c:type:: struct charger_manager


.. _`charger_manager.definition`:

Definition
----------

.. code-block:: c

    struct charger_manager {
        struct list_head entry;
        struct device *dev;
        struct charger_desc *desc;
    #ifdef CONFIG_THERMAL
        struct thermal_zone_device *tzd_batt;
    #endif
        bool charger_enabled;
        unsigned long fullbatt_vchk_jiffies_at;
        struct delayed_work fullbatt_vchk_work;
        int emergency_stop;
        char psy_name_buf[PSY_NAME_MAX + 1];
        struct power_supply_desc charger_psy_desc;
        struct power_supply *charger_psy;
        u64 charging_start_time;
        u64 charging_end_time;
    }

.. _`charger_manager.members`:

Members
-------

entry
    entry for list

dev
    device pointer

desc
    instance of charger_desc

tzd_batt
    thermal zone device for battery

charger_enabled
    the state of charger

fullbatt_vchk_jiffies_at
    jiffies at the time full battery check will occur.

fullbatt_vchk_work
    work queue for full battery check

emergency_stop
    When setting true, stop charging

psy_name_buf
    the name of power-supply-class for charger manager

charger_psy_desc
    *undescribed*

charger_psy
    power_supply for charger manager

charging_start_time
    saved start time of enabling charging

charging_end_time
    saved end time of disabling charging

.. This file was automatic generated / don't edit.

