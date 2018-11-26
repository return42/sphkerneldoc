.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/vc.c

.. _`omap_vc_channel_cfg`:

struct omap_vc_channel_cfg
==========================

.. c:type:: struct omap_vc_channel_cfg

    describe the cfg_channel bitfield

.. _`omap_vc_channel_cfg.definition`:

Definition
----------

.. code-block:: c

    struct omap_vc_channel_cfg {
        u8 sa;
        u8 rav;
        u8 rac;
        u8 racen;
        u8 cmd;
    }

.. _`omap_vc_channel_cfg.members`:

Members
-------

sa
    bit for slave address

rav
    bit for voltage configuration register

rac
    bit for command configuration register

racen
    enable bit for RAC

cmd
    bit for command value set selection

.. _`omap_vc_channel_cfg.description`:

Description
-----------

Channel configuration bits, common for OMAP3+

.. _`omap_vc_channel_cfg.omap3-register`:

OMAP3 register
--------------

PRM_VC_CH_CONF

.. _`omap_vc_channel_cfg.omap4-register`:

OMAP4 register
--------------

PRM_VC_CFG_CHANNEL

.. _`omap_vc_channel_cfg.omap5-register`:

OMAP5 register
--------------

PRM_VC_SMPS_<voltdm>_CONFIG

.. _`omap_vc_config_channel`:

omap_vc_config_channel
======================

.. c:function:: int omap_vc_config_channel(struct voltagedomain *voltdm)

    configure VC channel to PMIC mappings

    :param voltdm:
        pointer to voltagdomain defining the desired VC channel
    :type voltdm: struct voltagedomain \*

.. _`omap_vc_config_channel.description`:

Description
-----------

Configures the VC channel to PMIC mappings for the following
PMIC settings
- i2c slave address (SA)
- voltage configuration address (RAV)
- command configuration address (RAC) and enable bit (RACEN)
- command values for ON, ONLP, RET and OFF (CMD)

This function currently only allows flexible configuration of the
non-default channel.  Starting with OMAP4, there are more than 2
channels, with one defined as the default (on OMAP4, it's MPU.)
Only the non-default channel can be configured.

.. _`omap3_set_i2c_timings`:

omap3_set_i2c_timings
=====================

.. c:function:: void omap3_set_i2c_timings(struct voltagedomain *voltdm)

    sets i2c sleep timings for a channel

    :param voltdm:
        channel to configure
    :type voltdm: struct voltagedomain \*

.. _`omap3_set_i2c_timings.description`:

Description
-----------

Calculates and sets up voltage controller to use I2C based
voltage scaling for sleep modes. This can be used for either off mode
or retention. Off mode has additionally an option to use sys_off_mode
pad, which uses a global signal to program the whole power IC to
off-mode.

Note that pmic is not controlling the voltage scaling during
retention signaled over I2C4, so we can keep voltsetup2 as 0.
And the oscillator is not shut off over I2C4, so no need to
set clksetup.

.. _`omap3_set_off_timings`:

omap3_set_off_timings
=====================

.. c:function:: void omap3_set_off_timings(struct voltagedomain *voltdm)

    sets off-mode timings for a channel

    :param voltdm:
        channel to configure
    :type voltdm: struct voltagedomain \*

.. _`omap3_set_off_timings.description`:

Description
-----------

Calculates and sets up off-mode timings for a channel. Off-mode
can use either I2C based voltage scaling, or alternatively
sys_off_mode pad can be used to send a global command to power IC.n,
sys_off_mode has the additional benefit that voltages can be
scaled to zero volt level with TWL4030 / TWL5030, I2C can only
scale to 600mV.

Note that omap is not controlling the voltage scaling during
off idle signaled by sys_off_mode, so we can keep voltsetup1
as 0.

.. _`omap4_calc_volt_ramp`:

omap4_calc_volt_ramp
====================

.. c:function:: u32 omap4_calc_volt_ramp(struct voltagedomain *voltdm, u32 voltage_diff)

    calculates voltage ramping delays on omap4

    :param voltdm:
        channel to calculate values for
    :type voltdm: struct voltagedomain \*

    :param voltage_diff:
        voltage difference in microvolts
    :type voltage_diff: u32

.. _`omap4_calc_volt_ramp.description`:

Description
-----------

Calculates voltage ramp prescaler + counter values for a voltage
difference on omap4. Returns a field value suitable for writing to

.. _`omap4_calc_volt_ramp.voltsetup-register-for-a-channel-in-following-format`:

VOLTSETUP register for a channel in following format
----------------------------------------------------

bits[8:9] prescaler ... bits[0:5] counter. See OMAP4 TRM for reference.

.. _`omap4_usec_to_val_scrm`:

omap4_usec_to_val_scrm
======================

.. c:function:: u32 omap4_usec_to_val_scrm(u32 usec, int shift, u32 mask)

    convert microsecond value to SCRM module bitfield

    :param usec:
        microseconds
    :type usec: u32

    :param shift:
        number of bits to shift left
    :type shift: int

    :param mask:
        bitfield mask
    :type mask: u32

.. _`omap4_usec_to_val_scrm.description`:

Description
-----------

Converts microsecond value to OMAP4 SCRM bitfield. Bitfield is
shifted to requested position, and checked agains the mask value.
If larger, forced to the max value of the field (i.e. the mask itself.)
Returns the SCRM bitfield value.

.. _`omap4_set_timings`:

omap4_set_timings
=================

.. c:function:: void omap4_set_timings(struct voltagedomain *voltdm, bool off_mode)

    set voltage ramp timings for a channel

    :param voltdm:
        channel to configure
    :type voltdm: struct voltagedomain \*

    :param off_mode:
        whether off-mode values are used
    :type off_mode: bool

.. _`omap4_set_timings.description`:

Description
-----------

Calculates and sets the voltage ramp up / down values for a channel.

.. _`omap4_vc_i2c_timing_init`:

omap4_vc_i2c_timing_init
========================

.. c:function:: void omap4_vc_i2c_timing_init(struct voltagedomain *voltdm)

    sets up board I2C timing parameters

    :param voltdm:
        voltagedomain pointer to get data from
    :type voltdm: struct voltagedomain \*

.. _`omap4_vc_i2c_timing_init.description`:

Description
-----------

Use PMIC + board supplied settings for calculating the total I2C
channel capacitance and set the timing parameters based on this.
Pre-calculated values are provided in data tables, as it is not
too straightforward to calculate these runtime.

.. _`omap_vc_i2c_init`:

omap_vc_i2c_init
================

.. c:function:: void omap_vc_i2c_init(struct voltagedomain *voltdm)

    initialize I2C interface to PMIC

    :param voltdm:
        voltage domain containing VC data
    :type voltdm: struct voltagedomain \*

.. _`omap_vc_i2c_init.description`:

Description
-----------

Use PMIC supplied settings for I2C high-speed mode and
master code (if set) and program the VC I2C configuration
register.

The VC I2C configuration is common to all VC channels,
so this function only configures I2C for the first VC
channel registers.  All other VC channels will use the
same configuration.

.. _`omap_vc_calc_vsel`:

omap_vc_calc_vsel
=================

.. c:function:: u8 omap_vc_calc_vsel(struct voltagedomain *voltdm, u32 uvolt)

    calculate vsel value for a channel

    :param voltdm:
        channel to calculate value for
    :type voltdm: struct voltagedomain \*

    :param uvolt:
        microvolt value to convert to vsel
    :type uvolt: u32

.. _`omap_vc_calc_vsel.description`:

Description
-----------

Converts a microvolt value to vsel value for the used PMIC.
This checks whether the microvolt value is out of bounds, and
adjusts the value accordingly. If unsupported value detected,
warning is thrown.

.. _`omap_pm_setup_sr_i2c_pcb_length`:

omap_pm_setup_sr_i2c_pcb_length
===============================

.. c:function:: void omap_pm_setup_sr_i2c_pcb_length(u32 mm)

    set length of SR I2C traces on PCB

    :param mm:
        length of the PCB trace in millimetres
    :type mm: u32

.. _`omap_pm_setup_sr_i2c_pcb_length.description`:

Description
-----------

Sets the PCB trace length for the I2C channel. By default uses 63mm.
This is needed for properly calculating the capacitance value for
the PCB trace, and for setting the SR I2C channel timing parameters.

.. This file was automatic generated / don't edit.

