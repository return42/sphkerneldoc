.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath.h

.. _`ath_ops`:

struct ath_ops
==============

.. c:type:: struct ath_ops

    Register read/write operations

.. _`ath_ops.definition`:

Definition
----------

.. code-block:: c

    struct ath_ops {
        unsigned int (*read)(void *, u32 reg_offset);
        void (*multi_read)(void *, u32 *addr, u32 *val, u16 count);
        void (*write)(void *, u32 val, u32 reg_offset);
        void (*enable_write_buffer)(void *);
        void (*write_flush)(void *);
        u32 (*rmw)(void *, u32 reg_offset, u32 set, u32 clr);
        void (*enable_rmw_buffer)(void *);
        void (*rmw_flush)(void *);
    }

.. _`ath_ops.members`:

Members
-------

read
    Register read

multi_read
    Multiple register read

write
    Register write

enable_write_buffer
    Enable multiple register writes

write_flush
    flush buffered register writes and disable buffering

rmw
    *undescribed*

enable_rmw_buffer
    *undescribed*

rmw_flush
    *undescribed*

.. _`ath_debug`:

enum ATH_DEBUG
==============

.. c:type:: enum ATH_DEBUG

    atheros wireless debug level

.. _`ath_debug.definition`:

Definition
----------

.. code-block:: c

    enum ATH_DEBUG {
        ATH_DBG_RESET,
        ATH_DBG_QUEUE,
        ATH_DBG_EEPROM,
        ATH_DBG_CALIBRATE,
        ATH_DBG_INTERRUPT,
        ATH_DBG_REGULATORY,
        ATH_DBG_ANI,
        ATH_DBG_XMIT,
        ATH_DBG_BEACON,
        ATH_DBG_CONFIG,
        ATH_DBG_FATAL,
        ATH_DBG_PS,
        ATH_DBG_BTCOEX,
        ATH_DBG_WMI,
        ATH_DBG_BSTUCK,
        ATH_DBG_MCI,
        ATH_DBG_DFS,
        ATH_DBG_WOW,
        ATH_DBG_CHAN_CTX,
        ATH_DBG_DYNACK,
        ATH_DBG_SPECTRAL_SCAN,
        ATH_DBG_ANY
    };

.. _`ath_debug.constants`:

Constants
---------

ATH_DBG_RESET
    reset processing

ATH_DBG_QUEUE
    hardware queue management

ATH_DBG_EEPROM
    eeprom processing

ATH_DBG_CALIBRATE
    periodic calibration

ATH_DBG_INTERRUPT
    interrupt processing

ATH_DBG_REGULATORY
    regulatory processing

ATH_DBG_ANI
    adaptive noise immunitive processing

ATH_DBG_XMIT
    basic xmit operation

ATH_DBG_BEACON
    beacon handling

ATH_DBG_CONFIG
    configuration of the hardware

ATH_DBG_FATAL
    fatal errors, this is the default, DBG_DEFAULT

ATH_DBG_PS
    power save processing

ATH_DBG_BTCOEX
    bluetooth coexistance

ATH_DBG_WMI
    *undescribed*

ATH_DBG_BSTUCK
    stuck beacons

ATH_DBG_MCI
    Message Coexistence Interface, a private protocol
    used exclusively for WLAN-BT coexistence starting from
    AR9462.

ATH_DBG_DFS
    radar datection

ATH_DBG_WOW
    Wake on Wireless

ATH_DBG_CHAN_CTX
    *undescribed*

ATH_DBG_DYNACK
    dynack handling

ATH_DBG_SPECTRAL_SCAN
    FFT spectral scan

ATH_DBG_ANY
    enable all debugging

.. _`ath_debug.description`:

Description
-----------

The debug level is used to control the amount and type of debugging output
we want to see. Each driver has its own method for enabling debugging and
modifying debug level states -- but this is typically done through a
module parameter 'debug' along with a respective 'debug' debugfs file
entry.

.. This file was automatic generated / don't edit.

