.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-desc:

=====================
struct regulator_desc
=====================

*man struct regulator_desc(9)*

*4.6.0-rc5*

Static regulator descriptor


Synopsis
========

.. code-block:: c

    struct regulator_desc {
      const char * name;
      const char * supply_name;
      const char * of_match;
      const char * regulators_node;
      int (* of_parse_cb) (struct device_node *,const struct regulator_desc *,struct regulator_config *);
      int id;
      bool continuous_voltage_range;
      unsigned n_voltages;
      const struct regulator_ops * ops;
      int irq;
      enum regulator_type type;
      struct module * owner;
      unsigned int min_uV;
      unsigned int uV_step;
      unsigned int linear_min_sel;
      int fixed_uV;
      unsigned int ramp_delay;
      int min_dropout_uV;
      const struct regulator_linear_range * linear_ranges;
      int n_linear_ranges;
      const unsigned int * volt_table;
      unsigned int vsel_reg;
      unsigned int vsel_mask;
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
      unsigned int enable_time;
      unsigned int off_on_delay;
      unsigned int (* of_map_mode) (unsigned int mode);
    };


Members
=======

name
    Identifying name for the regulator.

supply_name
    Identifying the regulator supply

of_match
    Name used to identify regulator in DT.

regulators_node
    Name of node containing regulator definitions in DT.

of_parse_cb
    Optional callback called only if of_match is present. Will be
    called for each regulator parsed from DT, during init_data parsing.
    The regulator_config passed as argument to the callback will be a
    copy of config passed to regulator_register, valid only for this
    particular call. Callback may freely change the config but it cannot
    store it for later usage. Callback should return 0 on success or
    negative ERRNO indicating failure.

id
    Numerical identifier for the regulator.

continuous_voltage_range
    Indicates if the regulator can set any voltage within constrains
    range.

n_voltages
    Number of selectors available for ops.\ ``list_voltage``.

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

n_linear_ranges
    Number of entries in the ``linear_ranges`` table.

volt_table
    Voltage mapping table (if table based mapping)

vsel_reg
    Register for selector when using regulator_regmap_X_voltage_

vsel_mask
    Mask for register bitfield used for selector

apply_reg
    Register for initiate voltage change on the output when using
    regulator_set_voltage_sel_regmap

apply_bit
    Register bitfield used for initiate voltage change on the output
    when using regulator_set_voltage_sel_regmap

enable_reg
    Register for control when using regmap enable/disable ops

enable_mask
    Mask for control when using regmap enable/disable ops

enable_val
    Enabling value for control when using regmap enable/disable ops

disable_val
    Disabling value for control when using regmap enable/disable ops

enable_is_inverted
    A flag to indicate set enable_mask bits to disable when using
    regulator_enable_regmap and friends APIs.

bypass_reg
    Register for control when using regmap set_bypass

bypass_mask
    Mask for control when using regmap set_bypass

bypass_val_on
    Enabling value for control when using regmap set_bypass

bypass_val_off
    Disabling value for control when using regmap set_bypass

active_discharge_on
    Disabling value for control when using regmap set_active_discharge

active_discharge_off
    Enabling value for control when using regmap set_active_discharge

active_discharge_mask
    Mask for control when using regmap set_active_discharge

active_discharge_reg
    Register for control when using regmap set_active_discharge

enable_time
    Time taken for initial enable of regulator (in uS).

off_on_delay
    guard time (in uS), before re-enabling a regulator

of_map_mode
    Maps a hardware mode defined in a DeviceTree to a standard mode


Description
===========

Each regulator registered with the core is described with a structure of
this type and a struct regulator_config. This structure contains the
non-varying parts of the regulator description.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
