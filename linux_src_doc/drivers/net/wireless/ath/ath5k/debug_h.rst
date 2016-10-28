.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/debug.h

.. _`ath5k_debug_level`:

enum ath5k_debug_level
======================

.. c:type:: enum ath5k_debug_level

    ath5k debug level

.. _`ath5k_debug_level.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_debug_level {
        ATH5K_DEBUG_RESET,
        ATH5K_DEBUG_INTR,
        ATH5K_DEBUG_MODE,
        ATH5K_DEBUG_XMIT,
        ATH5K_DEBUG_BEACON,
        ATH5K_DEBUG_CALIBRATE,
        ATH5K_DEBUG_TXPOWER,
        ATH5K_DEBUG_LED,
        ATH5K_DEBUG_DUMPBANDS,
        ATH5K_DEBUG_DMA,
        ATH5K_DEBUG_ANI,
        ATH5K_DEBUG_DESC,
        ATH5K_DEBUG_ANY
    };

.. _`ath5k_debug_level.constants`:

Constants
---------

ATH5K_DEBUG_RESET
    reset processing

ATH5K_DEBUG_INTR
    interrupt handling

ATH5K_DEBUG_MODE
    mode init/setup

ATH5K_DEBUG_XMIT
    basic xmit operation

ATH5K_DEBUG_BEACON
    beacon handling

ATH5K_DEBUG_CALIBRATE
    periodic calibration

ATH5K_DEBUG_TXPOWER
    transmit power setting

ATH5K_DEBUG_LED
    led management

ATH5K_DEBUG_DUMPBANDS
    dump bands

ATH5K_DEBUG_DMA
    debug dma start/stop

ATH5K_DEBUG_ANI
    *undescribed*

ATH5K_DEBUG_DESC
    descriptor setup

ATH5K_DEBUG_ANY
    show at any debug level

.. _`ath5k_debug_level.description`:

Description
-----------

The debug level is used to control the amount and type of debugging output
we want to see. The debug level is given in calls to ATH5K_DBG to specify
where the message should appear, and the user can control the debugging
messages he wants to see, either by the module parameter 'debug' on module
load, or dynamically by using debugfs 'ath5k/phyX/debug'. these levels can
be combined together by bitwise OR.

.. This file was automatic generated / don't edit.

