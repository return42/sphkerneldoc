
.. _API-struct-regulator-ops:

====================
struct regulator_ops
====================

*man struct regulator_ops(9)*

*4.6.0-rc1*

regulator operations.


Synopsis
========

.. code-block:: c

    struct regulator_ops {
      int (* list_voltage) (struct regulator_dev *, unsigned selector);
      int (* set_voltage) (struct regulator_dev *, int min_uV, int max_uV,unsigned *selector);
      int (* map_voltage) (struct regulator_dev *, int min_uV, int max_uV);
      int (* set_voltage_sel) (struct regulator_dev *, unsigned selector);
      int (* get_voltage) (struct regulator_dev *);
      int (* get_voltage_sel) (struct regulator_dev *);
      int (* set_current_limit) (struct regulator_dev *,int min_uA, int max_uA);
      int (* get_current_limit) (struct regulator_dev *);
      int (* set_input_current_limit) (struct regulator_dev *, int lim_uA);
      int (* set_active_discharge) (struct regulator_dev *, bool enable);
      int (* enable) (struct regulator_dev *);
      int (* disable) (struct regulator_dev *);
      int (* is_enabled) (struct regulator_dev *);
      int (* set_mode) (struct regulator_dev *, unsigned int mode);
      unsigned int (* get_mode) (struct regulator_dev *);
      int (* enable_time) (struct regulator_dev *);
      int (* set_ramp_delay) (struct regulator_dev *, int ramp_delay);
      int (* set_voltage_time_sel) (struct regulator_dev *,unsigned int old_selector,unsigned int new_selector);
      int (* set_soft_start) (struct regulator_dev *);
      int (* get_status) (struct regulator_dev *);
      unsigned int (* get_optimum_mode) (struct regulator_dev *, int input_uV,int output_uV, int load_uA);
      int (* set_load) (struct regulator_dev *, int load_uA);
      int (* set_bypass) (struct regulator_dev *dev, bool enable);
      int (* get_bypass) (struct regulator_dev *dev, bool *enable);
      int (* set_suspend_voltage) (struct regulator_dev *, int uV);
      int (* set_suspend_enable) (struct regulator_dev *);
      int (* set_suspend_disable) (struct regulator_dev *);
      int (* set_suspend_mode) (struct regulator_dev *, unsigned int mode);
      int (* set_pull_down) (struct regulator_dev *);
    };


Members
=======

list_voltage
    Return one of the supported voltages, in microvolts; zero if the selector indicates a voltage that is unusable on this system; or negative errno. Selectors range from zero to
    one less than regulator_desc.n_voltages. Voltages may be reported in any order.

set_voltage
    Set the voltage for the regulator within the range specified. The driver should select the voltage closest to min_uV.

map_voltage
    Convert a voltage into a selector

set_voltage_sel
    Set the voltage for the regulator using the specified selector.

get_voltage
    Return the currently configured voltage for the regulator.

get_voltage_sel
    Return the currently configured voltage selector for the regulator.

set_current_limit
    Configure a limit for a current-limited regulator. The driver should select the current closest to max_uA.

get_current_limit
    Get the configured limit for a current-limited regulator.

set_input_current_limit
    Configure an input limit.

set_active_discharge
    Set active discharge enable/disable of regulators.

enable
    Configure the regulator as enabled.

disable
    Configure the regulator as disabled.

is_enabled
    Return 1 if the regulator is enabled, 0 if not. May also return negative errno.

set_mode
    Set the configured operating mode for the regulator.

get_mode
    Get the configured operating mode for the regulator.

enable_time
    Time taken for the regulator voltage output voltage to stabilise after being enabled, in microseconds.

set_ramp_delay
    Set the ramp delay for the regulator. The driver should select ramp delay equal to or less than(closest) ramp_delay.

set_voltage_time_sel
    Time taken for the regulator voltage output voltage to stabilise after being set to a new value, in microseconds. The function provides the from and to voltage selector, the
    function should return the worst case.

set_soft_start
    Enable soft start for the regulator.

get_status
    Return actual (not as-configured) status of regulator, as a REGULATOR_STATUS value (or negative errno)

get_optimum_mode
    Get the most efficient operating mode for the regulator when running with the specified parameters.

set_load
    Set the load for the regulator.

set_bypass
    Set the regulator in bypass mode.

get_bypass
    Get the regulator bypass mode state.

set_suspend_voltage
    Set the voltage for the regulator when the system is suspended.

set_suspend_enable
    Mark the regulator as enabled when the system is suspended.

set_suspend_disable
    Mark the regulator as disabled when the system is suspended.

set_suspend_mode
    Set the operating mode for the regulator when the system is suspended.

set_pull_down
    Configure the regulator to pull down when the regulator is disabled.


Description
===========

This struct describes regulator operations which can be implemented by regulator chip drivers.
