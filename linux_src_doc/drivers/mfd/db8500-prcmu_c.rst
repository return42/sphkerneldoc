.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/db8500-prcmu.c

.. _`prcmu_set_rc_a2p`:

prcmu_set_rc_a2p
================

.. c:function:: int prcmu_set_rc_a2p(enum romcode_write val)

    This function is used to run few power state sequences

    :param val:
        Value to be set, i.e. transition requested
    :type val: enum romcode_write

.. _`prcmu_set_rc_a2p.return`:

Return
------

0 on success, -EINVAL on invalid argument

This function is used to run the following power state sequences -
any state to ApReset,  ApDeepSleep to ApExecute, ApExecute to ApDeepSleep

.. _`prcmu_get_rc_p2a`:

prcmu_get_rc_p2a
================

.. c:function:: enum romcode_read prcmu_get_rc_p2a( void)

    This function is used to get power state sequences

    :param void:
        no arguments
    :type void: 

.. _`prcmu_get_rc_p2a.return`:

Return
------

the power transition that has last happened

This function can return the following transitions-
any state to ApReset,  ApDeepSleep to ApExecute, ApExecute to ApDeepSleep

.. _`prcmu_get_xp70_current_state`:

prcmu_get_xp70_current_state
============================

.. c:function:: enum ap_pwrst prcmu_get_xp70_current_state( void)

    Return the current XP70 power mode

    :param void:
        no arguments
    :type void: 

.. _`prcmu_get_xp70_current_state.return`:

Return
------

Returns the current AP(ARM) power mode: init,
apBoot, apExecute, apDeepSleep, apSleep, apIdle, apReset

.. _`prcmu_config_clkout`:

prcmu_config_clkout
===================

.. c:function:: int prcmu_config_clkout(u8 clkout, u8 source, u8 div)

    Configure one of the programmable clock outputs.

    :param clkout:
        The CLKOUT number (0 or 1).
    :type clkout: u8

    :param source:
        The clock to be used (one of the PRCMU_CLKSRC\_\*).
    :type source: u8

    :param div:
        The divider to be applied.
    :type div: u8

.. _`prcmu_config_clkout.description`:

Description
-----------

Configures one of the programmable clock outputs (CLKOUTs).
\ ``div``\  should be in the range [1,63] to request a configuration, or 0 to
inform that the configuration is no longer requested.

.. _`db8500_prcmu_set_arm_opp`:

db8500_prcmu_set_arm_opp
========================

.. c:function:: int db8500_prcmu_set_arm_opp(u8 opp)

    set the appropriate ARM OPP

    :param opp:
        The new ARM operating point to which transition is to be made
    :type opp: u8

.. _`db8500_prcmu_set_arm_opp.return`:

Return
------

0 on success, non-zero on failure

This function sets the the operating point of the ARM.

.. _`db8500_prcmu_get_arm_opp`:

db8500_prcmu_get_arm_opp
========================

.. c:function:: int db8500_prcmu_get_arm_opp( void)

    get the current ARM OPP

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_get_arm_opp.return`:

Return
------

the current ARM OPP

.. _`db8500_prcmu_get_ddr_opp`:

db8500_prcmu_get_ddr_opp
========================

.. c:function:: int db8500_prcmu_get_ddr_opp( void)

    get the current DDR OPP

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_get_ddr_opp.return`:

Return
------

the current DDR OPP

.. _`db8500_prcmu_set_ape_opp`:

db8500_prcmu_set_ape_opp
========================

.. c:function:: int db8500_prcmu_set_ape_opp(u8 opp)

    set the appropriate APE OPP

    :param opp:
        The new APE operating point to which transition is to be made
    :type opp: u8

.. _`db8500_prcmu_set_ape_opp.return`:

Return
------

0 on success, non-zero on failure

This function sets the operating point of the APE.

.. _`db8500_prcmu_get_ape_opp`:

db8500_prcmu_get_ape_opp
========================

.. c:function:: int db8500_prcmu_get_ape_opp( void)

    get the current APE OPP

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_get_ape_opp.return`:

Return
------

the current APE OPP

.. _`db8500_prcmu_request_ape_opp_100_voltage`:

db8500_prcmu_request_ape_opp_100_voltage
========================================

.. c:function:: int db8500_prcmu_request_ape_opp_100_voltage(bool enable)

    Request APE OPP 100% voltage

    :param enable:
        true to request the higher voltage, false to drop a request.
    :type enable: bool

.. _`db8500_prcmu_request_ape_opp_100_voltage.description`:

Description
-----------

Calls to this function to enable and disable requests must be balanced.

.. _`prcmu_release_usb_wakeup_state`:

prcmu_release_usb_wakeup_state
==============================

.. c:function:: int prcmu_release_usb_wakeup_state( void)

    release the state required by a USB wakeup

    :param void:
        no arguments
    :type void: 

.. _`prcmu_release_usb_wakeup_state.description`:

Description
-----------

This function releases the power state requirements of a USB wakeup.

.. _`db8500_prcmu_set_epod`:

db8500_prcmu_set_epod
=====================

.. c:function:: int db8500_prcmu_set_epod(u16 epod_id, u8 epod_state)

    set the state of a EPOD (power domain)

    :param epod_id:
        The EPOD to set
    :type epod_id: u16

    :param epod_state:
        The new EPOD state
    :type epod_state: u8

.. _`db8500_prcmu_set_epod.description`:

Description
-----------

This function sets the state of a EPOD (power domain). It may not be called
from interrupt context.

.. _`prcmu_configure_auto_pm`:

prcmu_configure_auto_pm
=======================

.. c:function:: void prcmu_configure_auto_pm(struct prcmu_auto_pm_config *sleep, struct prcmu_auto_pm_config *idle)

    Configure autonomous power management.

    :param sleep:
        Configuration for ApSleep.
    :type sleep: struct prcmu_auto_pm_config \*

    :param idle:
        Configuration for ApIdle.
    :type idle: struct prcmu_auto_pm_config \*

.. _`db8500_prcmu_request_clock`:

db8500_prcmu_request_clock
==========================

.. c:function:: int db8500_prcmu_request_clock(u8 clock, bool enable)

    Request for a clock to be enabled or disabled.

    :param clock:
        The clock for which the request is made.
    :type clock: u8

    :param enable:
        Whether the clock should be enabled (true) or disabled (false).
    :type enable: bool

.. _`db8500_prcmu_request_clock.description`:

Description
-----------

This function should only be used by the clock implementation.
Do not use it from any other place!

.. _`prcmu_abb_read`:

prcmu_abb_read
==============

.. c:function:: int prcmu_abb_read(u8 slave, u8 reg, u8 *value, u8 size)

    Read register value(s) from the ABB.

    :param slave:
        The I2C slave address.
    :type slave: u8

    :param reg:
        The (start) register address.
    :type reg: u8

    :param value:
        The read out value(s).
    :type value: u8 \*

    :param size:
        The number of registers to read.
    :type size: u8

.. _`prcmu_abb_read.description`:

Description
-----------

Reads register value(s) from the ABB.
\ ``size``\  has to be 1 for the current firmware version.

.. _`prcmu_abb_write_masked`:

prcmu_abb_write_masked
======================

.. c:function:: int prcmu_abb_write_masked(u8 slave, u8 reg, u8 *value, u8 *mask, u8 size)

    Write masked register value(s) to the ABB.

    :param slave:
        The I2C slave address.
    :type slave: u8

    :param reg:
        The (start) register address.
    :type reg: u8

    :param value:
        The value(s) to write.
    :type value: u8 \*

    :param mask:
        The mask(s) to use.
    :type mask: u8 \*

    :param size:
        The number of registers to write.
    :type size: u8

.. _`prcmu_abb_write_masked.description`:

Description
-----------

Writes masked register value(s) to the ABB.
For each \ ``value``\ , only the bits set to 1 in the corresponding \ ``mask``\ 
will be written. The other bits are not changed.
\ ``size``\  has to be 1 for the current firmware version.

.. _`prcmu_abb_write`:

prcmu_abb_write
===============

.. c:function:: int prcmu_abb_write(u8 slave, u8 reg, u8 *value, u8 size)

    Write register value(s) to the ABB.

    :param slave:
        The I2C slave address.
    :type slave: u8

    :param reg:
        The (start) register address.
    :type reg: u8

    :param value:
        The value(s) to write.
    :type value: u8 \*

    :param size:
        The number of registers to write.
    :type size: u8

.. _`prcmu_abb_write.description`:

Description
-----------

Writes register value(s) to the ABB.
\ ``size``\  has to be 1 for the current firmware version.

.. _`prcmu_ac_wake_req`:

prcmu_ac_wake_req
=================

.. c:function:: int prcmu_ac_wake_req( void)

    should be called whenever ARM wants to wakeup Modem

    :param void:
        no arguments
    :type void: 

.. _`prcmu_ac_sleep_req`:

prcmu_ac_sleep_req
==================

.. c:function:: void prcmu_ac_sleep_req( void)

    called when ARM no longer needs to talk to modem

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_system_reset`:

db8500_prcmu_system_reset
=========================

.. c:function:: void db8500_prcmu_system_reset(u16 reset_code)

    System reset

    :param reset_code:
        *undescribed*
    :type reset_code: u16

.. _`db8500_prcmu_system_reset.description`:

Description
-----------

Saves the reset reason code and then sets the APE_SOFTRST register which
fires interrupt to fw

.. _`db8500_prcmu_get_reset_code`:

db8500_prcmu_get_reset_code
===========================

.. c:function:: u16 db8500_prcmu_get_reset_code( void)

    Retrieve SW reset reason code

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_get_reset_code.description`:

Description
-----------

Retrieves the reset reason code stored by \ :c:func:`prcmu_system_reset`\  before
last restart.

.. _`db8500_prcmu_modem_reset`:

db8500_prcmu_modem_reset
========================

.. c:function:: void db8500_prcmu_modem_reset( void)

    ask the PRCMU to reset modem

    :param void:
        no arguments
    :type void: 

.. _`db8500_prcmu_probe`:

db8500_prcmu_probe
==================

.. c:function:: int db8500_prcmu_probe(struct platform_device *pdev)

    arch init call for the Linux PRCMU fw init logic

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. This file was automatic generated / don't edit.

