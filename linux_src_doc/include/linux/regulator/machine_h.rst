.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regulator/machine.h

.. _`regulator_state`:

struct regulator_state
======================

.. c:type:: struct regulator_state

    regulator state during low power system states

.. _`regulator_state.definition`:

Definition
----------

.. code-block:: c

    struct regulator_state {
        int uV;
        int min_uV;
        int max_uV;
        unsigned int mode;
        int enabled;
        bool changeable;
    }

.. _`regulator_state.members`:

Members
-------

uV
    Default operating voltage during suspend, it can be adjusted
    among <min_uV, max_uV>.

min_uV
    Minimum suspend voltage may be set.

max_uV
    Maximum suspend voltage may be set.

mode
    Operating mode during suspend.

enabled
    operations during suspend.
    - DO_NOTHING_IN_SUSPEND
    - DISABLE_IN_SUSPEND
    - ENABLE_IN_SUSPEND

changeable
    Is this state can be switched between enabled/disabled,

.. _`regulator_state.description`:

Description
-----------

This describes a regulators state during a system wide low power
state.  One of enabled or disabled must be set for the
configuration to be applied.

.. _`regulation_constraints`:

struct regulation_constraints
=============================

.. c:type:: struct regulation_constraints

    regulator operating constraints.

.. _`regulation_constraints.definition`:

Definition
----------

.. code-block:: c

    struct regulation_constraints {
        const char *name;
        int min_uV;
        int max_uV;
        int uV_offset;
        int min_uA;
        int max_uA;
        int ilim_uA;
        int system_load;
        int max_spread;
        unsigned int valid_modes_mask;
        unsigned int valid_ops_mask;
        int input_uV;
        struct regulator_state state_disk;
        struct regulator_state state_mem;
        struct regulator_state state_standby;
        suspend_state_t initial_state;
        unsigned int initial_mode;
        unsigned int ramp_delay;
        unsigned int settling_time;
        unsigned int settling_time_up;
        unsigned int settling_time_down;
        unsigned int enable_time;
        unsigned int active_discharge;
        unsigned always_on:1;
        unsigned boot_on:1;
        unsigned apply_uV:1;
        unsigned ramp_disable:1;
        unsigned soft_start:1;
        unsigned pull_down:1;
        unsigned over_current_protection:1;
    }

.. _`regulation_constraints.members`:

Members
-------

name
    Descriptive name for the constraints, used for display purposes.

min_uV
    Smallest voltage consumers may set.

max_uV
    Largest voltage consumers may set.

uV_offset
    Offset applied to voltages from consumer to compensate for
    voltage drops.

min_uA
    Smallest current consumers may set.

max_uA
    Largest current consumers may set.

ilim_uA
    Maximum input current.

system_load
    Load that isn't captured by any consumer requests.

max_spread
    Max possible spread between coupled regulators

valid_modes_mask
    Mask of modes which may be configured by consumers.

valid_ops_mask
    Operations which may be performed by consumers.

input_uV
    Input voltage for regulator when supplied by another regulator.

state_disk
    State for regulator when system is suspended in disk mode.

state_mem
    State for regulator when system is suspended in mem mode.

state_standby
    State for regulator when system is suspended in standby
    mode.

initial_state
    Suspend state to set by default.

initial_mode
    Mode to set at startup.

ramp_delay
    Time to settle down after voltage change (unit: uV/us)

settling_time
    Time to settle down after voltage change when voltage
    change is non-linear (unit: microseconds).

settling_time_up
    Time to settle down after voltage increase when voltage
    change is non-linear (unit: microseconds).

settling_time_down
    Time to settle down after voltage decrease when
    voltage change is non-linear (unit: microseconds).

enable_time
    Turn-on time of the rails (unit: microseconds)

active_discharge
    Enable/disable active discharge. The enum
    regulator_active_discharge values are used for
    initialisation.

always_on
    Set if the regulator should never be disabled.

boot_on
    Set if the regulator is enabled when the system is initially
    started.  If the regulator is not enabled by the hardware or
    bootloader then it will be enabled when the constraints are
    applied.

apply_uV
    Apply the voltage constraint when initialising.

ramp_disable
    Disable ramp delay when initialising or when setting voltage.

soft_start
    Enable soft start so that voltage ramps slowly.

pull_down
    Enable pull down when regulator is disabled.

over_current_protection
    Auto disable on over current event.

.. _`regulation_constraints.description`:

Description
-----------

This struct describes regulator and board/machine specific constraints.

.. _`regulator_consumer_supply`:

struct regulator_consumer_supply
================================

.. c:type:: struct regulator_consumer_supply

    supply -> device mapping

.. _`regulator_consumer_supply.definition`:

Definition
----------

.. code-block:: c

    struct regulator_consumer_supply {
        const char *dev_name;
        const char *supply;
    }

.. _`regulator_consumer_supply.members`:

Members
-------

dev_name
    Result of \ :c:func:`dev_name`\  for the consumer.

supply
    Name for the supply.

.. _`regulator_consumer_supply.description`:

Description
-----------

This maps a supply name to a device. Use of dev_name allows support for
buses which make struct device available late such as I2C.

.. _`regulator_init_data`:

struct regulator_init_data
==========================

.. c:type:: struct regulator_init_data

    regulator platform initialisation data.

.. _`regulator_init_data.definition`:

Definition
----------

.. code-block:: c

    struct regulator_init_data {
        const char *supply_regulator;
        struct regulation_constraints constraints;
        int num_consumer_supplies;
        struct regulator_consumer_supply *consumer_supplies;
        int (*regulator_init)(void *driver_data);
        void *driver_data;
    }

.. _`regulator_init_data.members`:

Members
-------

supply_regulator
    Parent regulator.  Specified using the regulator name
    as it appears in the name field in sysfs, which can
    be explicitly set using the constraints field 'name'.

constraints
    Constraints.  These must be specified for the regulator to
    be usable.

num_consumer_supplies
    Number of consumer device supplies.

consumer_supplies
    Consumer device supply configuration.

regulator_init
    Callback invoked when the regulator has been registered.

driver_data
    Data passed to regulator_init.

.. _`regulator_init_data.description`:

Description
-----------

Initialisation constraints, our supply and consumers supplies.

.. This file was automatic generated / don't edit.

