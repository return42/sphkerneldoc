.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/reset.c

.. _`reset-function-and-helpers`:

Reset function and helpers
==========================

Here we implement the main reset routine, used to bring the card
to a working state and ready to receive. We also handle routines
that don't fit on other places such as clock, sleep and power control

.. _`ath5k_hw_register_timeout`:

ath5k_hw_register_timeout
=========================

.. c:function:: int ath5k_hw_register_timeout(struct ath5k_hw *ah, u32 reg, u32 flag, u32 val, bool is_set)

    Poll a register for a flag/field change

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param reg:
        The register to read
    :type reg: u32

    :param flag:
        The flag/field to check on the register
    :type flag: u32

    :param val:
        The field value we expect (if we check a field)
    :type val: u32

    :param is_set:
        Instead of checking if the flag got cleared, check if it got set
    :type is_set: bool

.. _`ath5k_hw_register_timeout.description`:

Description
-----------

Some registers contain flags that indicate that an operation is
running. We use this function to poll these registers and check
if these flags get cleared. We also use it to poll a register
field (containing multiple flags) until it gets a specific value.

Returns -EAGAIN if we exceeded AR5K_TUNE_REGISTER_TIMEOUT \* 15us or 0

.. _`ath5k_hw_htoclock`:

ath5k_hw_htoclock
=================

.. c:function:: unsigned int ath5k_hw_htoclock(struct ath5k_hw *ah, unsigned int usec)

    Translate usec to hw clock units

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param usec:
        value in microseconds
    :type usec: unsigned int

.. _`ath5k_hw_htoclock.description`:

Description
-----------

Translate usecs to hw clock units based on the current
hw clock rate.

Returns number of clock units

.. _`ath5k_hw_clocktoh`:

ath5k_hw_clocktoh
=================

.. c:function:: unsigned int ath5k_hw_clocktoh(struct ath5k_hw *ah, unsigned int clock)

    Translate hw clock units to usec

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param clock:
        value in hw clock units
    :type clock: unsigned int

.. _`ath5k_hw_clocktoh.description`:

Description
-----------

Translate hw clock units to usecs based on the current
hw clock rate.

Returns number of usecs

.. _`ath5k_hw_init_core_clock`:

ath5k_hw_init_core_clock
========================

.. c:function:: void ath5k_hw_init_core_clock(struct ath5k_hw *ah)

    Initialize core clock

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_init_core_clock.description`:

Description
-----------

Initialize core clock parameters (usec, usec32, latencies etc),
based on current bwmode and chipset properties.

.. _`ath5k_hw_set_sleep_clock`:

ath5k_hw_set_sleep_clock
========================

.. c:function:: void ath5k_hw_set_sleep_clock(struct ath5k_hw *ah, bool enable)

    Setup sleep clock operation

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param enable:
        Enable sleep clock operation (false to disable)
    :type enable: bool

.. _`ath5k_hw_set_sleep_clock.description`:

Description
-----------

If there is an external 32KHz crystal available, use it
as ref. clock instead of 32/40MHz clock and baseband clocks
to save power during sleep or restore normal 32/40MHz
operation.

.. _`ath5k_hw_set_sleep_clock.note`:

NOTE
----

When operating on 32KHz certain PHY registers (27 - 31,
123 - 127) require delay on access.

.. _`ath5k_hw_nic_reset`:

ath5k_hw_nic_reset
==================

.. c:function:: int ath5k_hw_nic_reset(struct ath5k_hw *ah, u32 val)

    Reset the various chipset units

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param val:
        Mask to indicate what units to reset
    :type val: u32

.. _`ath5k_hw_nic_reset.description`:

Description
-----------

To reset the various chipset units we need to write
the mask to AR5K_RESET_CTL and poll the register until
all flags are cleared.

Returns 0 if we are O.K. or -EAGAIN (from athk5_hw_register_timeout)

.. _`ath5k_hw_wisoc_reset`:

ath5k_hw_wisoc_reset
====================

.. c:function:: int ath5k_hw_wisoc_reset(struct ath5k_hw *ah, u32 flags)

    Reset AHB chipset

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param flags:
        Mask to indicate what units to reset
    :type flags: u32

.. _`ath5k_hw_wisoc_reset.description`:

Description
-----------

Same as ath5k_hw_nic_reset but for AHB based devices

Returns 0 if we are O.K. or -EAGAIN (from athk5_hw_register_timeout)

.. _`ath5k_hw_set_power_mode`:

ath5k_hw_set_power_mode
=======================

.. c:function:: int ath5k_hw_set_power_mode(struct ath5k_hw *ah, enum ath5k_power_mode mode, bool set_chip, u16 sleep_duration)

    Set power mode

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param mode:
        One of enum ath5k_power_mode
    :type mode: enum ath5k_power_mode

    :param set_chip:
        Set to true to write sleep control register
    :type set_chip: bool

    :param sleep_duration:
        How much time the device is allowed to sleep
        when sleep logic is enabled (in 128 microsecond increments).
    :type sleep_duration: u16

.. _`ath5k_hw_set_power_mode.description`:

Description
-----------

This function is used to configure sleep policy and allowed
sleep modes. For more information check out the sleep control
register on reg.h and STA_ID1.

Returns 0 on success, -EIO if chip didn't wake up or -EINVAL if an invalid
mode is requested.

.. _`ath5k_hw_on_hold`:

ath5k_hw_on_hold
================

.. c:function:: int ath5k_hw_on_hold(struct ath5k_hw *ah)

    Put device on hold

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_on_hold.description`:

Description
-----------

Put MAC and Baseband on warm reset and keep that state
(don't clean sleep control register). After this MAC
and Baseband are disabled and a full reset is needed
to come back. This way we save as much power as possible
without putting the card on full sleep.

Returns 0 on success or -EIO on error

.. _`ath5k_hw_nic_wakeup`:

ath5k_hw_nic_wakeup
===================

.. c:function:: int ath5k_hw_nic_wakeup(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Force card out of sleep

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_nic_wakeup.description`:

Description
-----------

Bring up MAC + PHY Chips and program PLL

.. _`ath5k_hw_nic_wakeup.note`:

NOTE
----

Channel is NULL for the initial wakeup.

Returns 0 on success, -EIO on hw failure or -EINVAL for false channel infos

.. _`ath5k_hw_tweak_initval_settings`:

ath5k_hw_tweak_initval_settings
===============================

.. c:function:: void ath5k_hw_tweak_initval_settings(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Tweak initial settings

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_tweak_initval_settings.description`:

Description
-----------

Some settings are not handled on initvals, e.g. bwmode
settings, some phy settings, workarounds etc that in general
don't fit anywhere else or are too small to introduce a separate
function for each one. So we have this function to handle
them all during reset and complete card's initialization.

.. _`ath5k_hw_commit_eeprom_settings`:

ath5k_hw_commit_eeprom_settings
===============================

.. c:function:: void ath5k_hw_commit_eeprom_settings(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Commit settings from EEPROM

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_commit_eeprom_settings.description`:

Description
-----------

Use settings stored on EEPROM to properly initialize the card
based on various infos and per-mode calibration data.

.. _`ath5k_hw_reset`:

ath5k_hw_reset
==============

.. c:function:: int ath5k_hw_reset(struct ath5k_hw *ah, enum nl80211_iftype op_mode, struct ieee80211_channel *channel, bool fast, bool skip_pcu)

    The main reset function

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param op_mode:
        One of enum nl80211_iftype
    :type op_mode: enum nl80211_iftype

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param fast:
        Enable fast channel switching
    :type fast: bool

    :param skip_pcu:
        Skip pcu initialization
    :type skip_pcu: bool

.. _`ath5k_hw_reset.description`:

Description
-----------

This is the function we call each time we want to (re)initialize the
card and pass new settings to hw. We also call it when hw runs into
trouble to make it come back to a working state.

Returns 0 on success, -EINVAL on false op_mode or channel infos, or -EIO
on failure.

.. This file was automatic generated / don't edit.

