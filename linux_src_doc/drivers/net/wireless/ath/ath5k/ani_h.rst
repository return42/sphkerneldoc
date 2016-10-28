.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/ani.h

.. _`ath5k_ani_mode`:

enum ath5k_ani_mode
===================

.. c:type:: enum ath5k_ani_mode

    mode for ANI / noise sensitivity

.. _`ath5k_ani_mode.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_ani_mode {
        ATH5K_ANI_MODE_OFF,
        ATH5K_ANI_MODE_MANUAL_LOW,
        ATH5K_ANI_MODE_MANUAL_HIGH,
        ATH5K_ANI_MODE_AUTO
    };

.. _`ath5k_ani_mode.constants`:

Constants
---------

ATH5K_ANI_MODE_OFF
    Turn ANI off. This can be useful to just stop the ANI
    algorithm after it has been on auto mode.

ATH5K_ANI_MODE_MANUAL_LOW
    Manually set all immunity parameters to low,
    maximizing sensitivity. ANI will not run.

ATH5K_ANI_MODE_MANUAL_HIGH
    Manually set all immunity parameters to high,
    minimizing sensitivity. ANI will not run.

ATH5K_ANI_MODE_AUTO
    Automatically control immunity parameters based on the
    amount of OFDM and CCK frame errors (default).

.. _`ath5k_ani_state`:

struct ath5k_ani_state
======================

.. c:type:: struct ath5k_ani_state

    ANI state and associated counters

.. _`ath5k_ani_state.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_ani_state {
        enum ath5k_ani_mode ani_mode;
        int noise_imm_level;
        int spur_level;
        int firstep_level;
        bool ofdm_weak_sig;
        bool cck_weak_sig;
        int max_spur_level;
        unsigned int listen_time;
        unsigned int ofdm_errors;
        unsigned int cck_errors;
        struct ath_cycle_counters last_cc;
        unsigned int last_listen;
        unsigned int last_ofdm_errors;
        unsigned int last_cck_errors;
        unsigned int sum_ofdm_errors;
        unsigned int sum_cck_errors;
    }

.. _`ath5k_ani_state.members`:

Members
-------

ani_mode
    One of enum ath5k_ani_mode

noise_imm_level
    Noise immunity level

spur_level
    Spur immunity level

firstep_level
    FIRstep level

ofdm_weak_sig
    OFDM weak signal detection state (on/off)

cck_weak_sig
    CCK weak signal detection state (on/off)

max_spur_level
    Max spur immunity level (chip specific)

listen_time
    Listen time

ofdm_errors
    OFDM timing error count

cck_errors
    CCK timing error count

last_cc
    The \ :c:type:`struct ath_cycle_counters <ath_cycle_counters>`\  (for stats)

last_listen
    Listen time from previous run (for stats)

last_ofdm_errors
    OFDM timing error count from previous run (for tats)

last_cck_errors
    CCK timing error count from previous run (for stats)

sum_ofdm_errors
    Sum of OFDM timing errors (for stats)

sum_cck_errors
    Sum of all CCK timing errors (for stats)

.. This file was automatic generated / don't edit.

