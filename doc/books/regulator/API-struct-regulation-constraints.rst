.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulation-constraints:

=============================
struct regulation_constraints
=============================

*man struct regulation_constraints(9)*

*4.6.0-rc5*

regulator operating constraints.


Synopsis
========

.. code-block:: c

    struct regulation_constraints {
      const char * name;
      int min_uV;
      int max_uV;
      int uV_offset;
      int min_uA;
      int max_uA;
      int ilim_uA;
      int system_load;
      unsigned int valid_modes_mask;
      unsigned int valid_ops_mask;
      int input_uV;
      struct regulator_state state_disk;
      struct regulator_state state_mem;
      struct regulator_state state_standby;
      suspend_state_t initial_state;
      unsigned int initial_mode;
      unsigned int ramp_delay;
      unsigned int enable_time;
      unsigned int active_discharge;
      unsigned always_on:1;
      unsigned boot_on:1;
      unsigned apply_uV:1;
      unsigned ramp_disable:1;
      unsigned soft_start:1;
      unsigned pull_down:1;
    };


Members
=======

name
    Descriptive name for the constraints, used for display purposes.

min_uV
    Smallest voltage consumers may set.

max_uV
    Largest voltage consumers may set.

uV_offset
    Offset applied to voltages from consumer to compensate for voltage
    drops.

min_uA
    Smallest current consumers may set.

max_uA
    Largest current consumers may set.

ilim_uA
    Maximum input current.

system_load
    Load that isn't captured by any consumer requests.

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
    State for regulator when system is suspended in standby mode.

initial_state
    Suspend state to set by default.

initial_mode
    Mode to set at startup.

ramp_delay
    Time to settle down after voltage change (unit: uV/us)

enable_time
    Turn-on time of the rails (unit: microseconds)

active_discharge
    Enable/disable active discharge. The enum
    regulator_active_discharge values are used for initialisation.

always_on
    Set if the regulator should never be disabled.

boot_on
    Set if the regulator is enabled when the system is initially
    started. If the regulator is not enabled by the hardware or
    bootloader then it will be enabled when the constraints are applied.

apply_uV
    Apply the voltage constraint when initialising.

ramp_disable
    Disable ramp delay when initialising or when setting voltage.

soft_start
    Enable soft start so that voltage ramps slowly.

pull_down
    Enable pull down when regulator is disabled.


Description
===========

This struct describes regulator and board/machine specific constraints.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
