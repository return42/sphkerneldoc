.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/ani.c

.. _`ath5k_ani_set_noise_immunity_level`:

ath5k_ani_set_noise_immunity_level
==================================

.. c:function:: void ath5k_ani_set_noise_immunity_level(struct ath5k_hw *ah, int level)

    Set noise immunity level

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param int level:
        level between 0 and \ ``ATH5K_ANI_MAX_NOISE_IMM_LVL``\ 

.. _`ath5k_ani_set_spur_immunity_level`:

ath5k_ani_set_spur_immunity_level
=================================

.. c:function:: void ath5k_ani_set_spur_immunity_level(struct ath5k_hw *ah, int level)

    Set spur immunity level

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param int level:
        level between 0 and \ ``max_spur_level``\  (the maximum level is dependent
        on the chip revision).

.. _`ath5k_ani_set_firstep_level`:

ath5k_ani_set_firstep_level
===========================

.. c:function:: void ath5k_ani_set_firstep_level(struct ath5k_hw *ah, int level)

    Set "firstep" level

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param int level:
        level between 0 and \ ``ATH5K_ANI_MAX_FIRSTEP_LVL``\ 

.. _`ath5k_ani_set_ofdm_weak_signal_detection`:

ath5k_ani_set_ofdm_weak_signal_detection
========================================

.. c:function:: void ath5k_ani_set_ofdm_weak_signal_detection(struct ath5k_hw *ah, bool on)

    Set OFDM weak signal detection

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param bool on:
        turn on or off

.. _`ath5k_ani_set_cck_weak_signal_detection`:

ath5k_ani_set_cck_weak_signal_detection
=======================================

.. c:function:: void ath5k_ani_set_cck_weak_signal_detection(struct ath5k_hw *ah, bool on)

    Set CCK weak signal detection

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param bool on:
        turn on or off

.. _`ath5k_ani_raise_immunity`:

ath5k_ani_raise_immunity
========================

.. c:function:: void ath5k_ani_raise_immunity(struct ath5k_hw *ah, struct ath5k_ani_state *as, bool ofdm_trigger)

    Increase noise immunity

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ath5k_ani_state \*as:
        The \ :c:type:`struct ath5k_ani_state <ath5k_ani_state>`\ 

    :param bool ofdm_trigger:
        If this is true we are called because of too many OFDM errors,
        the algorithm will tune more parameters then.

.. _`ath5k_ani_raise_immunity.description`:

Description
-----------

Try to raise noise immunity (=decrease sensitivity) in several steps
depending on the average RSSI of the beacons we received.

.. _`ath5k_ani_lower_immunity`:

ath5k_ani_lower_immunity
========================

.. c:function:: void ath5k_ani_lower_immunity(struct ath5k_hw *ah, struct ath5k_ani_state *as)

    Decrease noise immunity

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ath5k_ani_state \*as:
        The \ :c:type:`struct ath5k_ani_state <ath5k_ani_state>`\ 

.. _`ath5k_ani_lower_immunity.description`:

Description
-----------

Try to lower noise immunity (=increase sensitivity) in several steps
depending on the average RSSI of the beacons we received.

.. _`ath5k_hw_ani_get_listen_time`:

ath5k_hw_ani_get_listen_time
============================

.. c:function:: int ath5k_hw_ani_get_listen_time(struct ath5k_hw *ah, struct ath5k_ani_state *as)

    Update counters and return listening time

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ath5k_ani_state \*as:
        The \ :c:type:`struct ath5k_ani_state <ath5k_ani_state>`\ 

.. _`ath5k_hw_ani_get_listen_time.description`:

Description
-----------

Return an approximation of the time spent "listening" in milliseconds (ms)
since the last call of this function.
Save a snapshot of the counter values for debugging/statistics.

.. _`ath5k_ani_save_and_clear_phy_errors`:

ath5k_ani_save_and_clear_phy_errors
===================================

.. c:function:: int ath5k_ani_save_and_clear_phy_errors(struct ath5k_hw *ah, struct ath5k_ani_state *as)

    Clear and save PHY error counters

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ath5k_ani_state \*as:
        The \ :c:type:`struct ath5k_ani_state <ath5k_ani_state>`\ 

.. _`ath5k_ani_save_and_clear_phy_errors.description`:

Description
-----------

Clear the PHY error counters as soon as possible, since this might be called
from a MIB interrupt and we want to make sure we don't get interrupted again.
Add the count of CCK and OFDM errors to our internal state, so it can be used
by the algorithm later.

Will be called from interrupt and tasklet context.
Returns 0 if both counters are zero.

.. _`ath5k_ani_period_restart`:

ath5k_ani_period_restart
========================

.. c:function:: void ath5k_ani_period_restart(struct ath5k_ani_state *as)

    Restart ANI period

    :param struct ath5k_ani_state \*as:
        The \ :c:type:`struct ath5k_ani_state <ath5k_ani_state>`\ 

.. _`ath5k_ani_period_restart.description`:

Description
-----------

Just reset counters, so they are clear for the next "ani period".

.. _`ath5k_ani_calibration`:

ath5k_ani_calibration
=====================

.. c:function:: void ath5k_ani_calibration(struct ath5k_hw *ah)

    The main ANI calibration function

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_ani_calibration.description`:

Description
-----------

We count OFDM and CCK errors relative to the time where we did not send or
receive ("listen" time) and raise or lower immunity accordingly.
This is called regularly (every second) from the calibration timer, but also
when an error threshold has been reached.

In order to synchronize access from different contexts, this should be
called only indirectly by scheduling the ANI tasklet!

.. _`ath5k_ani_mib_intr`:

ath5k_ani_mib_intr
==================

.. c:function:: void ath5k_ani_mib_intr(struct ath5k_hw *ah)

    Interrupt handler for ANI MIB counters

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_ani_mib_intr.description`:

Description
-----------

Just read & reset the registers quickly, so they don't generate more
interrupts, save the counters and schedule the tasklet to decide whether
to raise immunity or not.

We just need to handle PHY error counters, \ :c:func:`ath5k_hw_update_mib_counters`\ 
should take care of all "normal" MIB interrupts.

.. _`ath5k_ani_phy_error_report`:

ath5k_ani_phy_error_report
==========================

.. c:function:: void ath5k_ani_phy_error_report(struct ath5k_hw *ah, enum ath5k_phy_error_code phyerr)

    Used by older HW to report PHY errors

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum ath5k_phy_error_code phyerr:
        One of enum ath5k_phy_error_code

.. _`ath5k_ani_phy_error_report.description`:

Description
-----------

This is used by hardware without PHY error counters to report PHY errors
on a frame-by-frame basis, instead of the interrupt.

.. _`ath5k_enable_phy_err_counters`:

ath5k_enable_phy_err_counters
=============================

.. c:function:: void ath5k_enable_phy_err_counters(struct ath5k_hw *ah)

    Enable PHY error counters

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_enable_phy_err_counters.description`:

Description
-----------

Enable PHY error counters for OFDM and CCK timing errors.

.. _`ath5k_disable_phy_err_counters`:

ath5k_disable_phy_err_counters
==============================

.. c:function:: void ath5k_disable_phy_err_counters(struct ath5k_hw *ah)

    Disable PHY error counters

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_disable_phy_err_counters.description`:

Description
-----------

Disable PHY error counters for OFDM and CCK timing errors.

.. _`ath5k_ani_init`:

ath5k_ani_init
==============

.. c:function:: void ath5k_ani_init(struct ath5k_hw *ah, enum ath5k_ani_mode mode)

    Initialize ANI

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum ath5k_ani_mode mode:
        One of enum ath5k_ani_mode

.. _`ath5k_ani_init.description`:

Description
-----------

Initialize ANI according to mode.

.. _`ath5k_ani_print_counters`:

ath5k_ani_print_counters
========================

.. c:function:: void ath5k_ani_print_counters(struct ath5k_hw *ah)

    Print ANI counters

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_ani_print_counters.description`:

Description
-----------

Used for debugging ANI

.. This file was automatic generated / don't edit.

