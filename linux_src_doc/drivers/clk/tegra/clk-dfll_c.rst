.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk-dfll.c

.. _`dfll_ctrl_mode`:

enum dfll_ctrl_mode
===================

.. c:type:: enum dfll_ctrl_mode

    DFLL hardware operating mode

.. _`dfll_ctrl_mode.definition`:

Definition
----------

.. code-block:: c

    enum dfll_ctrl_mode {
        DFLL_UNINITIALIZED,
        DFLL_DISABLED,
        DFLL_OPEN_LOOP,
        DFLL_CLOSED_LOOP
    };

.. _`dfll_ctrl_mode.constants`:

Constants
---------

DFLL_UNINITIALIZED
    (uninitialized state - not in hardware bitfield)

DFLL_DISABLED
    DFLL not generating an output clock

DFLL_OPEN_LOOP
    DVCO running, but DFLL not adjusting voltage

DFLL_CLOSED_LOOP
    DVCO running, and DFLL adjusting voltage to match
    the requested rate

.. _`dfll_ctrl_mode.description`:

Description
-----------

The integer corresponding to the last two states, minus one, is
written to the DFLL hardware to change operating modes.

.. _`dfll_tune_range`:

enum dfll_tune_range
====================

.. c:type:: enum dfll_tune_range

    voltage range that the driver believes it's in

.. _`dfll_tune_range.definition`:

Definition
----------

.. code-block:: c

    enum dfll_tune_range {
        DFLL_TUNE_UNINITIALIZED,
        DFLL_TUNE_LOW
    };

.. _`dfll_tune_range.constants`:

Constants
---------

DFLL_TUNE_UNINITIALIZED
    DFLL tuning not yet programmed

DFLL_TUNE_LOW
    DFLL in the low-voltage range (or open-loop mode)

.. _`dfll_tune_range.description`:

Description
-----------

Some DFLL tuning parameters may need to change depending on the
DVCO's voltage; these states represent the ranges that the driver
supports. These are software states; these values are never
written into registers.

.. _`dfll_rate_req`:

struct dfll_rate_req
====================

.. c:type:: struct dfll_rate_req

    target DFLL rate request data

.. _`dfll_rate_req.definition`:

Definition
----------

.. code-block:: c

    struct dfll_rate_req {
        unsigned long rate;
        unsigned long dvco_target_rate;
        int lut_index;
        u8 mult_bits;
        u8 scale_bits;
    }

.. _`dfll_rate_req.members`:

Members
-------

rate
    target frequency, after the postscaling

dvco_target_rate
    target frequency, after the postscaling

lut_index
    LUT index at which voltage the dvco_target_rate will be reached

mult_bits
    value to program to the MULT bits of the DFLL_FREQ_REQ register

scale_bits
    value to program to the SCALE bits of the DFLL_FREQ_REQ register

.. _`dfll_is_running`:

dfll_is_running
===============

.. c:function:: bool dfll_is_running(struct tegra_dfll *td)

    is the DFLL currently generating a clock?

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_is_running.description`:

Description
-----------

If the DFLL is currently generating an output clock signal, return
true; otherwise return false.

.. _`tegra_dfll_runtime_resume`:

tegra_dfll_runtime_resume
=========================

.. c:function:: int tegra_dfll_runtime_resume(struct device *dev)

    enable all clocks needed by the DFLL

    :param struct device \*dev:
        DFLL device \*

.. _`tegra_dfll_runtime_resume.description`:

Description
-----------

Enable all clocks needed by the DFLL. Assumes that \ :c:func:`clk_prepare`\ 
has already been called on all the clocks.

XXX Should also handle context restore when returning from off.

.. _`tegra_dfll_runtime_suspend`:

tegra_dfll_runtime_suspend
==========================

.. c:function:: int tegra_dfll_runtime_suspend(struct device *dev)

    disable all clocks needed by the DFLL

    :param struct device \*dev:
        DFLL device \*

.. _`tegra_dfll_runtime_suspend.description`:

Description
-----------

Disable all clocks needed by the DFLL. Assumes that other code
will later call \ :c:func:`clk_unprepare`\ .

.. _`dfll_tune_low`:

dfll_tune_low
=============

.. c:function:: void dfll_tune_low(struct tegra_dfll *td)

    tune to DFLL and CPU settings valid for any voltage

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_tune_low.description`:

Description
-----------

Tune the DFLL oscillator parameters and the CPU clock shaper for
the low-voltage range. These settings are valid for any voltage,
but may not be optimal.

.. _`dfll_scale_dvco_rate`:

dfll_scale_dvco_rate
====================

.. c:function:: unsigned long dfll_scale_dvco_rate(int scale_bits, unsigned long dvco_rate)

    calculate scaled rate from the DVCO rate

    :param int scale_bits:
        clock scaler value (bits in the DFLL_FREQ_REQ_SCALE field)

    :param unsigned long dvco_rate:
        the DVCO rate

.. _`dfll_scale_dvco_rate.description`:

Description
-----------

Apply the same scaling formula that the DFLL hardware uses to scale
the DVCO rate.

.. _`dfll_set_mode`:

dfll_set_mode
=============

.. c:function:: void dfll_set_mode(struct tegra_dfll *td, enum dfll_ctrl_mode mode)

    change the DFLL control mode

    :param struct tegra_dfll \*td:
        DFLL instance

    :param enum dfll_ctrl_mode mode:
        DFLL control mode (see enum dfll_ctrl_mode)

.. _`dfll_set_mode.description`:

Description
-----------

Change the DFLL's operating mode between disabled, open-loop mode,
and closed-loop mode, or vice versa.

.. _`dfll_i2c_set_output_enabled`:

dfll_i2c_set_output_enabled
===========================

.. c:function:: int dfll_i2c_set_output_enabled(struct tegra_dfll *td, bool enable)

    enable/disable I2C PMIC voltage requests

    :param struct tegra_dfll \*td:
        DFLL instance

    :param bool enable:
        whether to enable or disable the I2C voltage requests

.. _`dfll_i2c_set_output_enabled.description`:

Description
-----------

Set the master enable control for I2C control value updates. If disabled,
then I2C control messages are inhibited, regardless of the DFLL mode.

.. _`dfll_load_i2c_lut`:

dfll_load_i2c_lut
=================

.. c:function:: void dfll_load_i2c_lut(struct tegra_dfll *td)

    load the voltage lookup table

    :param struct tegra_dfll \*td:
        struct tegra_dfll \*

.. _`dfll_load_i2c_lut.description`:

Description
-----------

Load the voltage-to-PMIC register value lookup table into the DFLL
IP block memory. Look-up tables can be loaded at any time.

.. _`dfll_init_i2c_if`:

dfll_init_i2c_if
================

.. c:function:: void dfll_init_i2c_if(struct tegra_dfll *td)

    set up the DFLL's DFLL-I2C interface

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_init_i2c_if.description`:

Description
-----------

During DFLL driver initialization, program the DFLL-I2C interface
with the PMU slave address, vdd register offset, and transfer mode.
This data is used by the DFLL to automatically construct I2C
voltage-set commands, which are then passed to the DFLL's internal
I2C controller.

.. _`dfll_init_out_if`:

dfll_init_out_if
================

.. c:function:: void dfll_init_out_if(struct tegra_dfll *td)

    prepare DFLL-to-PMIC interface

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_init_out_if.description`:

Description
-----------

During DFLL driver initialization or resume from context loss,
disable the I2C command output to the PMIC, set safe voltage and
output limits, and disable and clear limit interrupts.

.. _`find_lut_index_for_rate`:

find_lut_index_for_rate
=======================

.. c:function:: int find_lut_index_for_rate(struct tegra_dfll *td, unsigned long rate)

    determine I2C LUT index for given DFLL rate

    :param struct tegra_dfll \*td:
        DFLL instance

    :param unsigned long rate:
        clock rate

.. _`find_lut_index_for_rate.description`:

Description
-----------

Determines the index of a I2C LUT entry for a voltage that approximately
produces the given DFLL clock rate. This is used when forcing a value
to the integrator during rate changes. Returns -ENOENT if a suitable
LUT index is not found.

.. _`dfll_calculate_rate_request`:

dfll_calculate_rate_request
===========================

.. c:function:: int dfll_calculate_rate_request(struct tegra_dfll *td, struct dfll_rate_req *req, unsigned long rate)

    calculate DFLL parameters for a given rate

    :param struct tegra_dfll \*td:
        DFLL instance

    :param struct dfll_rate_req \*req:
        DFLL-rate-request structure

    :param unsigned long rate:
        the desired DFLL rate

.. _`dfll_calculate_rate_request.description`:

Description
-----------

Populate the DFLL-rate-request record \ ``req``\  fields with the scale_bits
and mult_bits fields, based on the target input rate. Returns 0 upon
success, or -EINVAL if the requested rate in req->rate is too high
or low for the DFLL to generate.

.. _`dfll_set_frequency_request`:

dfll_set_frequency_request
==========================

.. c:function:: void dfll_set_frequency_request(struct tegra_dfll *td, struct dfll_rate_req *req)

    start the frequency change operation

    :param struct tegra_dfll \*td:
        DFLL instance

    :param struct dfll_rate_req \*req:
        rate request structure

.. _`dfll_set_frequency_request.description`:

Description
-----------

Tell the DFLL to try to change its output frequency to the
frequency represented by \ ``req``\ . DFLL must be in closed-loop mode.

.. _`dfll_request_rate`:

dfll_request_rate
=================

.. c:function:: int dfll_request_rate(struct tegra_dfll *td, unsigned long rate)

    set the next rate for the DFLL to tune to

    :param struct tegra_dfll \*td:
        DFLL instance

    :param unsigned long rate:
        clock rate to target

.. _`dfll_request_rate.description`:

Description
-----------

Convert the requested clock rate \ ``rate``\  into the DFLL control logic
settings. In closed-loop mode, update new settings immediately to
adjust DFLL output rate accordingly. Otherwise, just save them
until the next switch to closed loop. Returns 0 upon success,
-EPERM if the DFLL driver has not yet been initialized, or -EINVAL
if \ ``rate``\  is outside the DFLL's tunable range.

.. _`dfll_disable`:

dfll_disable
============

.. c:function:: int dfll_disable(struct tegra_dfll *td)

    switch from open-loop mode to disabled mode

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_disable.description`:

Description
-----------

Switch from OPEN_LOOP state to DISABLED state. Returns 0 upon success
or -EPERM if the DFLL is not currently in open-loop mode.

.. _`dfll_enable`:

dfll_enable
===========

.. c:function:: int dfll_enable(struct tegra_dfll *td)

    switch a disabled DFLL to open-loop mode

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_enable.description`:

Description
-----------

Switch from DISABLED state to OPEN_LOOP state. Returns 0 upon success
or -EPERM if the DFLL is not currently disabled.

.. _`dfll_set_open_loop_config`:

dfll_set_open_loop_config
=========================

.. c:function:: void dfll_set_open_loop_config(struct tegra_dfll *td)

    prepare to switch to open-loop mode

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_set_open_loop_config.description`:

Description
-----------

Prepare to switch the DFLL to open-loop mode. This switches the
DFLL to the low-voltage tuning range, ensures that I2C output
forcing is disabled, and disables the output clock rate scaler.
The DFLL's low-voltage tuning range parameters must be
characterized to keep the downstream device stable at any DVCO
input voltage. No return value.

.. _`dfll_lock`:

dfll_lock
=========

.. c:function:: int dfll_lock(struct tegra_dfll *td)

    switch from open-loop to closed-loop mode

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_lock.description`:

Description
-----------

Switch from OPEN_LOOP state to CLOSED_LOOP state. Returns 0 upon success,
-EINVAL if the DFLL's target rate hasn't been set yet, or -EPERM if the
DFLL is not currently in open-loop mode.

.. _`dfll_unlock`:

dfll_unlock
===========

.. c:function:: int dfll_unlock(struct tegra_dfll *td)

    switch from closed-loop to open-loop mode

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_unlock.description`:

Description
-----------

Switch from CLOSED_LOOP state to OPEN_LOOP state. Returns 0 upon success,
or -EPERM if the DFLL is not currently in open-loop mode.

.. _`dfll_register_clk`:

dfll_register_clk
=================

.. c:function:: int dfll_register_clk(struct tegra_dfll *td)

    register the DFLL output clock with the clock framework

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_register_clk.description`:

Description
-----------

Register the DFLL's output clock with the Linux clock framework and register
the DFLL driver as an OF clock provider. Returns 0 upon success or -EINVAL
or -ENOMEM upon failure.

.. _`dfll_unregister_clk`:

dfll_unregister_clk
===================

.. c:function:: void dfll_unregister_clk(struct tegra_dfll *td)

    unregister the DFLL output clock

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_unregister_clk.description`:

Description
-----------

Unregister the DFLL's output clock from the Linux clock framework
and from clkdev. No return value.

.. _`dfll_calc_monitored_rate`:

dfll_calc_monitored_rate
========================

.. c:function:: u64 dfll_calc_monitored_rate(u32 monitor_data, unsigned long ref_rate)

    convert DFLL_MONITOR_DATA_VAL rate into real freq

    :param u32 monitor_data:
        value read from the DFLL_MONITOR_DATA_VAL bitfield

    :param unsigned long ref_rate:
        DFLL reference clock rate

.. _`dfll_calc_monitored_rate.description`:

Description
-----------

Convert \ ``monitor_data``\  from DFLL_MONITOR_DATA_VAL units into cycles
per second. Returns the converted value.

.. _`dfll_read_monitor_rate`:

dfll_read_monitor_rate
======================

.. c:function:: u64 dfll_read_monitor_rate(struct tegra_dfll *td)

    return the DFLL's output rate from internal monitor

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_read_monitor_rate.description`:

Description
-----------

If the DFLL is enabled, return the last rate reported by the DFLL's
internal monitoring hardware. This works in both open-loop and
closed-loop mode, and takes the output scaler setting into account.
Assumes that the monitor was programmed to monitor frequency before
the sample period started. If the driver believes that the DFLL is
currently uninitialized or disabled, it will return 0, since
otherwise the DFLL monitor data register will return the last
measured rate from when the DFLL was active.

.. _`dfll_set_default_params`:

dfll_set_default_params
=======================

.. c:function:: void dfll_set_default_params(struct tegra_dfll *td)

    program non-output related DFLL parameters

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_set_default_params.description`:

Description
-----------

During DFLL driver initialization or resume from context loss,
program parameters for the closed loop integrator, DVCO tuning,
voltage droop control and monitor control.

.. _`dfll_init_clks`:

dfll_init_clks
==============

.. c:function:: int dfll_init_clks(struct tegra_dfll *td)

    clk_get() the DFLL source clocks

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_init_clks.description`:

Description
-----------

Call \ :c:func:`clk_get`\  on the DFLL source clocks and save the pointers for later
use. Returns 0 upon success or error (see devm_clk_get) if one or more
of the clocks couldn't be looked up.

.. _`dfll_init`:

dfll_init
=========

.. c:function:: int dfll_init(struct tegra_dfll *td)

    Prepare the DFLL IP block for use

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_init.description`:

Description
-----------

Do everything necessary to prepare the DFLL IP block for use. The
DFLL will be left in DISABLED state. Called by \ :c:func:`dfll_probe`\ .
Returns 0 upon success, or passes along the error from whatever
function returned it.

.. _`dfll_build_i2c_lut`:

dfll_build_i2c_lut
==================

.. c:function:: int dfll_build_i2c_lut(struct tegra_dfll *td)

    build the I2C voltage register lookup table

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_build_i2c_lut.description`:

Description
-----------

The DFLL hardware has 33 bytes of look-up table RAM that must be filled with
PMIC voltage register values that span the entire DFLL operating range.
This function builds the look-up table based on the OPP table provided by
the soc-specific platform driver (td->soc->opp_dev) and the PMIC
register-to-voltage mapping queried from the regulator framework.

On success, fills in td->i2c_lut and returns 0, or -err on failure.

.. _`read_dt_param`:

read_dt_param
=============

.. c:function:: bool read_dt_param(struct tegra_dfll *td, const char *param, u32 *dest)

    helper function for reading required parameters from the DT

    :param struct tegra_dfll \*td:
        DFLL instance

    :param const char \*param:
        DT property name

    :param u32 \*dest:
        output pointer for the value read

.. _`read_dt_param.description`:

Description
-----------

Read a required numeric parameter from the DFLL device node, or complain
if the property doesn't exist. Returns a boolean indicating success for
easy chaining of multiple calls to this function.

.. _`dfll_fetch_i2c_params`:

dfll_fetch_i2c_params
=====================

.. c:function:: int dfll_fetch_i2c_params(struct tegra_dfll *td)

    query PMIC I2C params from DT & regulator subsystem

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_fetch_i2c_params.description`:

Description
-----------

Read all the parameters required for operation in I2C mode. The parameters
can originate from the device tree or the regulator subsystem.
Returns 0 on success or -err on failure.

.. _`dfll_fetch_common_params`:

dfll_fetch_common_params
========================

.. c:function:: int dfll_fetch_common_params(struct tegra_dfll *td)

    read DFLL parameters from the device tree

    :param struct tegra_dfll \*td:
        DFLL instance

.. _`dfll_fetch_common_params.description`:

Description
-----------

Read all the DT parameters that are common to both I2C and PWM operation.
Returns 0 on success or -EINVAL on any failure.

.. _`tegra_dfll_register`:

tegra_dfll_register
===================

.. c:function:: int tegra_dfll_register(struct platform_device *pdev, struct tegra_dfll_soc_data *soc)

    probe a Tegra DFLL device

    :param struct platform_device \*pdev:
        DFLL platform_device \*

    :param struct tegra_dfll_soc_data \*soc:
        Per-SoC integration and characterization data for this DFLL instance

.. _`tegra_dfll_register.description`:

Description
-----------

Probe and initialize a DFLL device instance. Intended to be called
by a SoC-specific shim driver that passes in per-SoC integration
and configuration data via \ ``soc``\ . Returns 0 on success or -err on failure.

.. _`tegra_dfll_unregister`:

tegra_dfll_unregister
=====================

.. c:function:: int tegra_dfll_unregister(struct platform_device *pdev)

    release all of the DFLL driver resources for a device

    :param struct platform_device \*pdev:
        DFLL platform_device \*

.. _`tegra_dfll_unregister.description`:

Description
-----------

Unbind this driver from the DFLL hardware device represented by
\ ``pdev``\ . The DFLL must be disabled for this to succeed. Returns 0
upon success or -EBUSY if the DFLL is still active.

.. This file was automatic generated / don't edit.

