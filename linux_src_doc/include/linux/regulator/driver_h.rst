.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regulator/driver.h

.. _`regulator_linear_range`:

struct regulator_linear_range
=============================

.. c:type:: struct regulator_linear_range

    specify linear voltage ranges

.. _`regulator_linear_range.definition`:

Definition
----------

.. code-block:: c

    struct regulator_linear_range {
        unsigned int min_uV;
        unsigned int min_sel;
        unsigned int max_sel;
        unsigned int uV_step;
    }

.. _`regulator_linear_range.members`:

Members
-------

min_uV
    Lowest voltage in range

min_sel
    Lowest selector for range

max_sel
    Highest selector for range

uV_step
    Step size

.. _`regulator_linear_range.description`:

Description
-----------

Specify a range of voltages for \ :c:func:`regulator_map_linear_range`\  and
\ :c:func:`regulator_list_linear_range`\ .

.. _`regulator_ops`:

struct regulator_ops
====================

.. c:type:: struct regulator_ops

    regulator operations.

.. _`regulator_ops.definition`:

Definition
----------

.. code-block:: c

    struct regulator_ops {
        int (*list_voltage) (struct regulator_dev *, unsigned selector);
        int (*set_voltage) (struct regulator_dev *, int min_uV, int max_uV, unsigned *selector);
        int (*map_voltage)(struct regulator_dev *, int min_uV, int max_uV);
        int (*set_voltage_sel) (struct regulator_dev *, unsigned selector);
        int (*get_voltage) (struct regulator_dev *);
        int (*get_voltage_sel) (struct regulator_dev *);
        int (*set_current_limit) (struct regulator_dev *, int min_uA, int max_uA);
        int (*get_current_limit) (struct regulator_dev *);
        int (*set_input_current_limit) (struct regulator_dev *, int lim_uA);
        int (*set_over_current_protection) (struct regulator_dev *);
        int (*set_active_discharge) (struct regulator_dev *, bool enable);
        int (*enable) (struct regulator_dev *);
        int (*disable) (struct regulator_dev *);
        int (*is_enabled) (struct regulator_dev *);
        int (*set_mode) (struct regulator_dev *, unsigned int mode);
        unsigned int (*get_mode) (struct regulator_dev *);
        int (*get_error_flags)(struct regulator_dev *, unsigned int *flags);
        int (*enable_time) (struct regulator_dev *);
        int (*set_ramp_delay) (struct regulator_dev *, int ramp_delay);
        int (*set_voltage_time) (struct regulator_dev *, int old_uV, int new_uV);
        int (*set_voltage_time_sel) (struct regulator_dev *,unsigned int old_selector, unsigned int new_selector);
        int (*set_soft_start) (struct regulator_dev *);
        int (*get_status)(struct regulator_dev *);
        unsigned int (*get_optimum_mode) (struct regulator_dev *, int input_uV, int output_uV, int load_uA);
        int (*set_load)(struct regulator_dev *, int load_uA);
        int (*set_bypass)(struct regulator_dev *dev, bool enable);
        int (*get_bypass)(struct regulator_dev *dev, bool *enable);
        int (*set_suspend_voltage) (struct regulator_dev *, int uV);
        int (*set_suspend_enable) (struct regulator_dev *);
        int (*set_suspend_disable) (struct regulator_dev *);
        int (*set_suspend_mode) (struct regulator_dev *, unsigned int mode);
        int (*resume)(struct regulator_dev *rdev);
        int (*set_pull_down) (struct regulator_dev *);
    }

.. _`regulator_ops.members`:

Members
-------

list_voltage
    Return one of the supported voltages, in microvolts; zero
    if the selector indicates a voltage that is unusable on this system;
    or negative errno.  Selectors range from zero to one less than
    regulator_desc.n_voltages.  Voltages may be reported in any order.

set_voltage
    Set the voltage for the regulator within the range specified.
    The driver should select the voltage closest to min_uV.

map_voltage
    Convert a voltage into a selector

set_voltage_sel
    Set the voltage for the regulator using the specified
    selector.

get_voltage
    Return the currently configured voltage for the regulator;
    return -ENOTRECOVERABLE if regulator can't be read at
    bootup and hasn't been set yet.

get_voltage_sel
    Return the currently configured voltage selector for the
    regulator; return -ENOTRECOVERABLE if regulator can't
    be read at bootup and hasn't been set yet.

set_current_limit
    Configure a limit for a current-limited regulator.
    The driver should select the current closest to max_uA.

get_current_limit
    Get the configured limit for a current-limited regulator.

set_input_current_limit
    Configure an input limit.

set_over_current_protection
    Support capability of automatically shutting
    down when detecting an over current event.

set_active_discharge
    Set active discharge enable/disable of regulators.

enable
    Configure the regulator as enabled.

disable
    Configure the regulator as disabled.

is_enabled
    Return 1 if the regulator is enabled, 0 if not.
    May also return negative errno.

set_mode
    Set the configured operating mode for the regulator.

get_mode
    Get the configured operating mode for the regulator.

get_error_flags
    Get the current error(s) for the regulator.

enable_time
    Time taken for the regulator voltage output voltage to
    stabilise after being enabled, in microseconds.

set_ramp_delay
    Set the ramp delay for the regulator. The driver should
    select ramp delay equal to or less than(closest) ramp_delay.

set_voltage_time
    Time taken for the regulator voltage output voltage
    to stabilise after being set to a new value, in microseconds.
    The function receives the from and to voltage as input, it
    should return the worst case.

set_voltage_time_sel
    Time taken for the regulator voltage output voltage
    to stabilise after being set to a new value, in microseconds.
    The function receives the from and to voltage selector as
    input, it should return the worst case.

set_soft_start
    Enable soft start for the regulator.

get_status
    Return actual (not as-configured) status of regulator, as a
    REGULATOR_STATUS value (or negative errno)

get_optimum_mode
    Get the most efficient operating mode for the regulator
    when running with the specified parameters.

set_load
    Set the load for the regulator.

set_bypass
    Set the regulator in bypass mode.

get_bypass
    Get the regulator bypass mode state.

set_suspend_voltage
    Set the voltage for the regulator when the system
    is suspended.

set_suspend_enable
    Mark the regulator as enabled when the system is
    suspended.

set_suspend_disable
    Mark the regulator as disabled when the system is
    suspended.

set_suspend_mode
    Set the operating mode for the regulator when the
    system is suspended.

resume
    *undescribed*

set_pull_down
    Configure the regulator to pull down when the regulator
    is disabled.

.. _`regulator_ops.description`:

Description
-----------

This struct describes regulator operations which can be implemented by
regulator chip drivers.

.. _`regulator_desc`:

struct regulator_desc
=====================

.. c:type:: struct regulator_desc

    Static regulator descriptor

.. _`regulator_desc.definition`:

Definition
----------

.. code-block:: c

    struct regulator_desc {
        const char *name;
        const char *supply_name;
        const char *of_match;
        const char *regulators_node;
        int (*of_parse_cb)(struct device_node *,const struct regulator_desc *, struct regulator_config *);
        int id;
        unsigned int continuous_voltage_range:1;
        unsigned n_voltages;
        const struct regulator_ops *ops;
        int irq;
        enum regulator_type type;
        struct module *owner;
        unsigned int min_uV;
        unsigned int uV_step;
        unsigned int linear_min_sel;
        int fixed_uV;
        unsigned int ramp_delay;
        int min_dropout_uV;
        const struct regulator_linear_range *linear_ranges;
        const unsigned int *linear_range_selectors;
        int n_linear_ranges;
        const unsigned int *volt_table;
        unsigned int vsel_range_reg;
        unsigned int vsel_range_mask;
        unsigned int vsel_reg;
        unsigned int vsel_mask;
        unsigned int csel_reg;
        unsigned int csel_mask;
        unsigned int apply_reg;
        unsigned int apply_bit;
        unsigned int enable_reg;
        unsigned int enable_mask;
        unsigned int enable_val;
        unsigned int disable_val;
        bool enable_is_inverted;
        unsigned int bypass_reg;
        unsigned int bypass_mask;
        unsigned int bypass_val_on;
        unsigned int bypass_val_off;
        unsigned int active_discharge_on;
        unsigned int active_discharge_off;
        unsigned int active_discharge_mask;
        unsigned int active_discharge_reg;
        unsigned int soft_start_reg;
        unsigned int soft_start_mask;
        unsigned int soft_start_val_on;
        unsigned int pull_down_reg;
        unsigned int pull_down_mask;
        unsigned int pull_down_val_on;
        unsigned int enable_time;
        unsigned int off_on_delay;
        unsigned int (*of_map_mode)(unsigned int mode);
    }

.. _`regulator_desc.members`:

Members
-------

name
    Identifying name for the regulator.

supply_name
    Identifying the regulator supply

of_match
    Name used to identify regulator in DT.

regulators_node
    Name of node containing regulator definitions in DT.

of_parse_cb
    Optional callback called only if of_match is present.
    Will be called for each regulator parsed from DT, during
    init_data parsing.
    The regulator_config passed as argument to the callback will
    be a copy of config passed to regulator_register, valid only
    for this particular call. Callback may freely change the
    config but it cannot store it for later usage.
    Callback should return 0 on success or negative ERRNO
    indicating failure.

id
    Numerical identifier for the regulator.

continuous_voltage_range
    Indicates if the regulator can set any
    voltage within constrains range.

n_voltages
    Number of selectors available for ops.list_voltage().

ops
    Regulator operations table.

irq
    Interrupt number for the regulator.

type
    Indicates if the regulator is a voltage or current regulator.

owner
    Module providing the regulator, used for refcounting.

min_uV
    Voltage given by the lowest selector (if linear mapping)

uV_step
    Voltage increase with each selector (if linear mapping)

linear_min_sel
    Minimal selector for starting linear mapping

fixed_uV
    Fixed voltage of rails.

ramp_delay
    Time to settle down after voltage change (unit: uV/us)

min_dropout_uV
    The minimum dropout voltage this regulator can handle

linear_ranges
    A constant table of possible voltage ranges.

linear_range_selectors
    A constant table of voltage range selectors.
    If pickable ranges are used each range must
    have corresponding selector here.

n_linear_ranges
    Number of entries in the \ ``linear_ranges``\  (and in
    linear_range_selectors if used) table(s).

volt_table
    Voltage mapping table (if table based mapping)

vsel_range_reg
    Register for range selector when using pickable ranges
    and regulator_regmap_X_voltage_X_pickable functions.

vsel_range_mask
    Mask for register bitfield used for range selector

vsel_reg
    Register for selector when using regulator_regmap_X_voltage_

vsel_mask
    Mask for register bitfield used for selector

csel_reg
    Register for TPS65218 LS3 current regulator

csel_mask
    Mask for TPS65218 LS3 current regulator

apply_reg
    Register for initiate voltage change on the output when
    using regulator_set_voltage_sel_regmap

apply_bit
    Register bitfield used for initiate voltage change on the
    output when using regulator_set_voltage_sel_regmap

enable_reg
    Register for control when using regmap enable/disable ops

enable_mask
    Mask for control when using regmap enable/disable ops

enable_val
    Enabling value for control when using regmap enable/disable ops

disable_val
    Disabling value for control when using regmap enable/disable ops

enable_is_inverted
    A flag to indicate set enable_mask bits to disable
    when using regulator_enable_regmap and friends APIs.

bypass_reg
    Register for control when using regmap set_bypass

bypass_mask
    Mask for control when using regmap set_bypass

bypass_val_on
    Enabling value for control when using regmap set_bypass

bypass_val_off
    Disabling value for control when using regmap set_bypass

active_discharge_on
    Disabling value for control when using regmap
    set_active_discharge

active_discharge_off
    Enabling value for control when using regmap
    set_active_discharge

active_discharge_mask
    Mask for control when using regmap
    set_active_discharge

active_discharge_reg
    Register for control when using regmap
    set_active_discharge

soft_start_reg
    Register for control when using regmap set_soft_start

soft_start_mask
    Mask for control when using regmap set_soft_start

soft_start_val_on
    Enabling value for control when using regmap
    set_soft_start

pull_down_reg
    Register for control when using regmap set_pull_down

pull_down_mask
    Mask for control when using regmap set_pull_down

pull_down_val_on
    Enabling value for control when using regmap
    set_pull_down

enable_time
    Time taken for initial enable of regulator (in uS).

off_on_delay
    guard time (in uS), before re-enabling a regulator

of_map_mode
    Maps a hardware mode defined in a DeviceTree to a standard mode

.. _`regulator_desc.description`:

Description
-----------

Each regulator registered with the core is described with a
structure of this type and a struct regulator_config.  This
structure contains the non-varying parts of the regulator
description.

.. _`regulator_config`:

struct regulator_config
=======================

.. c:type:: struct regulator_config

    Dynamic regulator descriptor

.. _`regulator_config.definition`:

Definition
----------

.. code-block:: c

    struct regulator_config {
        struct device *dev;
        const struct regulator_init_data *init_data;
        void *driver_data;
        struct device_node *of_node;
        struct regmap *regmap;
        bool ena_gpio_initialized;
        int ena_gpio;
        struct gpio_desc *ena_gpiod;
        unsigned int ena_gpio_invert:1;
        unsigned int ena_gpio_flags;
    }

.. _`regulator_config.members`:

Members
-------

dev
    struct device for the regulator

init_data
    platform provided init data, passed through by driver

driver_data
    private regulator data

of_node
    OpenFirmware node to parse for device tree bindings (may be
    NULL).

regmap
    regmap to use for core regmap helpers if \ :c:func:`dev_get_regmap`\  is
    insufficient.

ena_gpio_initialized
    GPIO controlling regulator enable was properly
    initialized, meaning that >= 0 is a valid gpio
    identifier and < 0 is a non existent gpio.

ena_gpio
    GPIO controlling regulator enable.

ena_gpiod
    GPIO descriptor controlling regulator enable.

ena_gpio_invert
    Sense for GPIO enable control.

ena_gpio_flags
    Flags to use when calling \ :c:func:`gpio_request_one`\ 

.. _`regulator_config.description`:

Description
-----------

Each regulator registered with the core is described with a
structure of this type and a struct regulator_desc.  This structure
contains the runtime variable parts of the regulator description.

.. This file was automatic generated / don't edit.

