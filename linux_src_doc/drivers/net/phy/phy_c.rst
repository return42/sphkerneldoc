.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phy.c

.. _`phy_print_status`:

phy_print_status
================

.. c:function:: void phy_print_status(struct phy_device *phydev)

    Convenience function to print out the current phy status

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_clear_interrupt`:

phy_clear_interrupt
===================

.. c:function:: int phy_clear_interrupt(struct phy_device *phydev)

    Ack the phy device's interrupt

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_clear_interrupt.description`:

Description
-----------

If the \ ``phydev``\  driver has an ack_interrupt function, call it to
ack and clear the phy device's interrupt.

Returns 0 on success or < 0 on error.

.. _`phy_config_interrupt`:

phy_config_interrupt
====================

.. c:function:: int phy_config_interrupt(struct phy_device *phydev, u32 interrupts)

    configure the PHY device for the requested interrupts

    :param struct phy_device \*phydev:
        the phy_device struct

    :param u32 interrupts:
        interrupt flags to configure for this \ ``phydev``\ 

.. _`phy_config_interrupt.description`:

Description
-----------

Returns 0 on success or < 0 on error.

.. _`phy_restart_aneg`:

phy_restart_aneg
================

.. c:function:: int phy_restart_aneg(struct phy_device *phydev)

    restart auto-negotiation

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_restart_aneg.description`:

Description
-----------

Restart the autonegotiation on \ ``phydev``\ .  Returns >= 0 on success or
negative errno on error.

.. _`phy_aneg_done`:

phy_aneg_done
=============

.. c:function:: int phy_aneg_done(struct phy_device *phydev)

    return auto-negotiation status

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_aneg_done.description`:

Description
-----------

Return the auto-negotiation status from this \ ``phydev``\ 
Returns > 0 on success or < 0 on error. 0 means that auto-negotiation
is still pending.

.. _`phy_find_valid`:

phy_find_valid
==============

.. c:function:: const struct phy_setting *phy_find_valid(int speed, int duplex, u32 supported)

    find a PHY setting that matches the requested parameters

    :param int speed:
        desired speed

    :param int duplex:
        desired duplex

    :param u32 supported:
        mask of supported link modes

.. _`phy_find_valid.description`:

Description
-----------

Locate a supported phy setting that is, in priority order:
- an exact match for the specified speed and duplex mode
- a match for the specified speed, or slower speed
- the slowest supported speed
Returns the matched phy_setting entry, or \ ``NULL``\  if no supported phy
settings were found.

.. _`phy_supported_speeds`:

phy_supported_speeds
====================

.. c:function:: unsigned int phy_supported_speeds(struct phy_device *phy, unsigned int *speeds, unsigned int size)

    return all speeds currently supported by a phy device

    :param struct phy_device \*phy:
        The phy device to return supported speeds of.

    :param unsigned int \*speeds:
        buffer to store supported speeds in.

    :param unsigned int size:
        size of speeds buffer.

.. _`phy_supported_speeds.description`:

Description
-----------

Returns the number of supported speeds, and fills the speeds
buffer with the supported speeds. If speeds buffer is too small to contain
all currently supported speeds, will return as many speeds as can fit.

.. _`phy_check_valid`:

phy_check_valid
===============

.. c:function:: bool phy_check_valid(int speed, int duplex, u32 features)

    check if there is a valid PHY setting which matches speed, duplex, and feature mask

    :param int speed:
        speed to match

    :param int duplex:
        duplex to match

    :param u32 features:
        A mask of the valid settings

.. _`phy_check_valid.description`:

Description
-----------

Returns true if there is a valid setting, false otherwise.

.. _`phy_sanitize_settings`:

phy_sanitize_settings
=====================

.. c:function:: void phy_sanitize_settings(struct phy_device *phydev)

    make sure the PHY is set to supported speed and duplex

    :param struct phy_device \*phydev:
        the target phy_device struct

.. _`phy_sanitize_settings.description`:

Description
-----------

Make sure the PHY is set to supported speeds and
  duplexes.  Drop down by one in this order:  1000/FULL,
  1000/HALF, 100/FULL, 100/HALF, 10/FULL, 10/HALF.

.. _`phy_ethtool_sset`:

phy_ethtool_sset
================

.. c:function:: int phy_ethtool_sset(struct phy_device *phydev, struct ethtool_cmd *cmd)

    generic ethtool sset function, handles all the details

    :param struct phy_device \*phydev:
        target phy_device struct

    :param struct ethtool_cmd \*cmd:
        ethtool_cmd

.. _`phy_ethtool_sset.a-few-notes-about-parameter-checking`:

A few notes about parameter checking
------------------------------------


- We don't set port or transceiver, so we don't care what they
  were set to.
- \ :c:func:`phy_start_aneg`\  will make sure forced settings are sane, and
  choose the next best ones from the ones selected, so we don't
  care if ethtool tries to give us bad values.

.. _`phy_mii_ioctl`:

phy_mii_ioctl
=============

.. c:function:: int phy_mii_ioctl(struct phy_device *phydev, struct ifreq *ifr, int cmd)

    generic PHY MII ioctl interface

    :param struct phy_device \*phydev:
        the phy_device struct

    :param struct ifreq \*ifr:
        &struct ifreq for socket ioctl's

    :param int cmd:
        ioctl cmd to execute

.. _`phy_mii_ioctl.description`:

Description
-----------

Note that this function is currently incompatible with the
PHYCONTROL layer.  It changes registers without regard to
current state.  Use at own risk.

.. _`phy_start_aneg_priv`:

phy_start_aneg_priv
===================

.. c:function:: int phy_start_aneg_priv(struct phy_device *phydev, bool sync)

    start auto-negotiation for this PHY device

    :param struct phy_device \*phydev:
        the phy_device struct

    :param bool sync:
        indicate whether we should wait for the workqueue cancelation

.. _`phy_start_aneg_priv.description`:

Description
-----------

Sanitizes the settings (if we're not autonegotiating
  them), and then calls the driver's config_aneg function.
  If the PHYCONTROL Layer is operating, we change the state to
  reflect the beginning of Auto-negotiation or forcing.

.. _`phy_start_aneg`:

phy_start_aneg
==============

.. c:function:: int phy_start_aneg(struct phy_device *phydev)

    start auto-negotiation for this PHY device

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_start_aneg.description`:

Description
-----------

Sanitizes the settings (if we're not autonegotiating
  them), and then calls the driver's config_aneg function.
  If the PHYCONTROL Layer is operating, we change the state to
  reflect the beginning of Auto-negotiation or forcing.

.. _`phy_start_machine`:

phy_start_machine
=================

.. c:function:: void phy_start_machine(struct phy_device *phydev)

    start PHY state machine tracking

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_start_machine.description`:

Description
-----------

The PHY infrastructure can run a state machine
  which tracks whether the PHY is starting up, negotiating,
  etc.  This function starts the delayed workqueue which tracks
  the state of the PHY. If you want to maintain your own state machine,
  do not call this function.

.. _`phy_trigger_machine`:

phy_trigger_machine
===================

.. c:function:: void phy_trigger_machine(struct phy_device *phydev, bool sync)

    trigger the state machine to run

    :param struct phy_device \*phydev:
        the phy_device struct

    :param bool sync:
        indicate whether we should wait for the workqueue cancelation

.. _`phy_trigger_machine.description`:

Description
-----------

There has been a change in state which requires that the
  state machine runs.

.. _`phy_stop_machine`:

phy_stop_machine
================

.. c:function:: void phy_stop_machine(struct phy_device *phydev)

    stop the PHY state machine tracking

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_stop_machine.description`:

Description
-----------

Stops the state machine delayed workqueue, sets the
  state to UP (unless it wasn't up yet). This function must be
  called BEFORE phy_detach.

.. _`phy_error`:

phy_error
=========

.. c:function:: void phy_error(struct phy_device *phydev)

    enter HALTED state for this PHY device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_error.description`:

Description
-----------

Moves the PHY to the HALTED state in response to a read
or write error, and tells the controller the link is down.
Must not be called from interrupt context, or while the
phydev->lock is held.

.. _`phy_interrupt`:

phy_interrupt
=============

.. c:function:: irqreturn_t phy_interrupt(int irq, void *phy_dat)

    PHY interrupt handler

    :param int irq:
        interrupt line

    :param void \*phy_dat:
        phy_device pointer

.. _`phy_interrupt.description`:

Description
-----------

When a PHY interrupt occurs, the handler disables
interrupts, and uses phy_change to handle the interrupt.

.. _`phy_enable_interrupts`:

phy_enable_interrupts
=====================

.. c:function:: int phy_enable_interrupts(struct phy_device *phydev)

    Enable the interrupts from the PHY side

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_disable_interrupts`:

phy_disable_interrupts
======================

.. c:function:: int phy_disable_interrupts(struct phy_device *phydev)

    Disable the PHY interrupts from the PHY side

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_start_interrupts`:

phy_start_interrupts
====================

.. c:function:: int phy_start_interrupts(struct phy_device *phydev)

    request and enable interrupts for a PHY device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_start_interrupts.description`:

Description
-----------

Request the interrupt for the given PHY.
  If this fails, then we set irq to PHY_POLL.
  Otherwise, we enable the interrupts in the PHY.
  This should only be called with a valid IRQ number.
  Returns 0 on success or < 0 on error.

.. _`phy_stop_interrupts`:

phy_stop_interrupts
===================

.. c:function:: int phy_stop_interrupts(struct phy_device *phydev)

    disable interrupts from a PHY device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_change`:

phy_change
==========

.. c:function:: void phy_change(struct phy_device *phydev)

    Called by the phy_interrupt to handle PHY changes

    :param struct phy_device \*phydev:
        phy_device struct that interrupted

.. _`phy_change_work`:

phy_change_work
===============

.. c:function:: void phy_change_work(struct work_struct *work)

    Scheduled by the phy_mac_interrupt to handle PHY changes

    :param struct work_struct \*work:
        work_struct that describes the work to be done

.. _`phy_stop`:

phy_stop
========

.. c:function:: void phy_stop(struct phy_device *phydev)

    Bring down the PHY link, and stop checking the status

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_start`:

phy_start
=========

.. c:function:: void phy_start(struct phy_device *phydev)

    start or restart a PHY device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_start.description`:

Description
-----------

Indicates the attached device's readiness to
  handle PHY-related work.  Used during startup to start the
  PHY, and after a call to \ :c:func:`phy_stop`\  to resume operation.
  Also used to indicate the MDIO bus has cleared an error
  condition.

.. _`phy_state_machine`:

phy_state_machine
=================

.. c:function:: void phy_state_machine(struct work_struct *work)

    Handle the state machine

    :param struct work_struct \*work:
        work_struct that describes the work to be done

.. _`phy_mac_interrupt`:

phy_mac_interrupt
=================

.. c:function:: void phy_mac_interrupt(struct phy_device *phydev)

    MAC says the link has changed

    :param struct phy_device \*phydev:
        phy_device struct with changed link

.. _`phy_mac_interrupt.description`:

Description
-----------

The MAC layer is able to indicate there has been a change in the PHY link
status. Trigger the state machine and work a work queue.

.. _`phy_init_eee`:

phy_init_eee
============

.. c:function:: int phy_init_eee(struct phy_device *phydev, bool clk_stop_enable)

    init and check the EEE feature

    :param struct phy_device \*phydev:
        target phy_device struct

    :param bool clk_stop_enable:
        PHY may stop the clock during LPI

.. _`phy_init_eee.description`:

Description
-----------

it checks if the Energy-Efficient Ethernet (EEE)
is supported by looking at the MMD registers 3.20 and 7.60/61
and it programs the MMD register 3.0 setting the "Clock stop enable"
bit if required.

.. _`phy_get_eee_err`:

phy_get_eee_err
===============

.. c:function:: int phy_get_eee_err(struct phy_device *phydev)

    report the EEE wake error count

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_get_eee_err.description`:

Description
-----------

it is to report the number of time where the PHY
failed to complete its normal wake sequence.

.. _`phy_ethtool_get_eee`:

phy_ethtool_get_eee
===================

.. c:function:: int phy_ethtool_get_eee(struct phy_device *phydev, struct ethtool_eee *data)

    get EEE supported and status

    :param struct phy_device \*phydev:
        target phy_device struct

    :param struct ethtool_eee \*data:
        ethtool_eee data

.. _`phy_ethtool_get_eee.description`:

Description
-----------

it reportes the Supported/Advertisement/LP Advertisement
capabilities.

.. _`phy_ethtool_set_eee`:

phy_ethtool_set_eee
===================

.. c:function:: int phy_ethtool_set_eee(struct phy_device *phydev, struct ethtool_eee *data)

    set EEE supported and status

    :param struct phy_device \*phydev:
        target phy_device struct

    :param struct ethtool_eee \*data:
        ethtool_eee data

.. _`phy_ethtool_set_eee.description`:

Description
-----------

it is to program the Advertisement EEE register.

.. This file was automatic generated / don't edit.

