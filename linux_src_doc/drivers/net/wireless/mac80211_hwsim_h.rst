.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/mac80211_hwsim.h

.. _`hwsim_tx_control_flags`:

enum hwsim_tx_control_flags
===========================

.. c:type:: enum hwsim_tx_control_flags

    flags to describe transmission info/status

.. _`hwsim_tx_control_flags.definition`:

Definition
----------

.. code-block:: c

    enum hwsim_tx_control_flags {
        HWSIM_TX_CTL_REQ_TX_STATUS,
        HWSIM_TX_CTL_NO_ACK,
        HWSIM_TX_STAT_ACK
    };

.. _`hwsim_tx_control_flags.constants`:

Constants
---------

HWSIM_TX_CTL_REQ_TX_STATUS
    require TX status callback for this frame.

HWSIM_TX_CTL_NO_ACK
    tell the wmediumd not to wait for an ack

HWSIM_TX_STAT_ACK
    Frame was acknowledged

.. _`hwsim_tx_control_flags.description`:

Description
-----------

These flags are used to give the wmediumd extra information in order to
modify its behavior for each frame

.. _`frame-transmission-registration-support`:

Frame transmission/registration support
=======================================

Frame transmission and registration support exists to allow userspace
entities such as wmediumd to receive and process all broadcasted
frames from a mac80211_hwsim radio device.

This allow user space applications to decide if the frame should be
dropped or not and implement a wireless medium simulator at user space.

Registration is done by sending a register message to the driver and
will be automatically unregistered if the user application doesn't
responds to sent frames.
Once registered the user application has to take responsibility of
broadcasting the frames to all listening mac80211_hwsim radio
interfaces.

For more technical details, see the corresponding command descriptions
below.

.. _`hwsim_tx_rate`:

struct hwsim_tx_rate
====================

.. c:type:: struct hwsim_tx_rate

    rate selection/status

.. _`hwsim_tx_rate.definition`:

Definition
----------

.. code-block:: c

    struct hwsim_tx_rate {
        s8 idx;
        u8 count;
    }

.. _`hwsim_tx_rate.members`:

Members
-------

idx
    rate index to attempt to send with

count
    number of tries in this rate before going to the next rate

.. _`hwsim_tx_rate.description`:

Description
-----------

A value of -1 for \ ``idx``\  indicates an invalid rate and, if used
in an array of retry rates, that no more rates should be tried.

When used for transmit status reporting, the driver should
always report the rate and number of retries used.

.. _`hwsim_tx_rate_flags`:

enum hwsim_tx_rate_flags
========================

.. c:type:: enum hwsim_tx_rate_flags

    per-rate flags set by the rate control algorithm. Inspired by structure mac80211_rate_control_flags. New flags may be appended, but old flags not deleted, to keep compatibility for userspace.

.. _`hwsim_tx_rate_flags.definition`:

Definition
----------

.. code-block:: c

    enum hwsim_tx_rate_flags {
        MAC80211_HWSIM_TX_RC_USE_RTS_CTS,
        MAC80211_HWSIM_TX_RC_USE_CTS_PROTECT,
        MAC80211_HWSIM_TX_RC_USE_SHORT_PREAMBLE,
        MAC80211_HWSIM_TX_RC_MCS,
        MAC80211_HWSIM_TX_RC_GREEN_FIELD,
        MAC80211_HWSIM_TX_RC_40_MHZ_WIDTH,
        MAC80211_HWSIM_TX_RC_DUP_DATA,
        MAC80211_HWSIM_TX_RC_SHORT_GI,
        MAC80211_HWSIM_TX_RC_VHT_MCS,
        MAC80211_HWSIM_TX_RC_80_MHZ_WIDTH,
        MAC80211_HWSIM_TX_RC_160_MHZ_WIDTH
    };

.. _`hwsim_tx_rate_flags.constants`:

Constants
---------

MAC80211_HWSIM_TX_RC_USE_RTS_CTS
    Use RTS/CTS exchange for this rate.

MAC80211_HWSIM_TX_RC_USE_CTS_PROTECT
    CTS-to-self protection is required.
    This is set if the current BSS requires ERP protection.

MAC80211_HWSIM_TX_RC_USE_SHORT_PREAMBLE
    Use short preamble.

MAC80211_HWSIM_TX_RC_MCS
    HT rate.

MAC80211_HWSIM_TX_RC_GREEN_FIELD
    Indicates whether this rate should be used
    in Greenfield mode.

MAC80211_HWSIM_TX_RC_40_MHZ_WIDTH
    Indicates if the Channel Width should be
    40 MHz.

MAC80211_HWSIM_TX_RC_DUP_DATA
    The frame should be transmitted on both of
    the adjacent 20 MHz channels, if the current channel type is
    NL80211_CHAN_HT40MINUS or NL80211_CHAN_HT40PLUS.

MAC80211_HWSIM_TX_RC_SHORT_GI
    Short Guard interval should be used for this
    rate.

MAC80211_HWSIM_TX_RC_VHT_MCS
    VHT MCS rate, in this case the idx field is
    split into a higher 4 bits (Nss) and lower 4 bits (MCS number)

MAC80211_HWSIM_TX_RC_80_MHZ_WIDTH
    Indicates 80 MHz transmission

MAC80211_HWSIM_TX_RC_160_MHZ_WIDTH
    Indicates 160 MHz transmission
    (80+80 isn't supported yet)

.. _`hwsim_tx_rate_flags.description`:

Description
-----------

These flags are set by the Rate control algorithm for each rate during tx,
in the \ ``flags``\  member of struct ieee80211_tx_rate.

.. _`hwsim_tx_rate_flag`:

struct hwsim_tx_rate_flag
=========================

.. c:type:: struct hwsim_tx_rate_flag

    rate selection/status

.. _`hwsim_tx_rate_flag.definition`:

Definition
----------

.. code-block:: c

    struct hwsim_tx_rate_flag {
        s8 idx;
        u16 flags;
    }

.. _`hwsim_tx_rate_flag.members`:

Members
-------

idx
    rate index to attempt to send with

flags
    *undescribed*

.. _`hwsim_tx_rate_flag.description`:

Description
-----------

A value of -1 for \ ``idx``\  indicates an invalid rate and, if used
in an array of retry rates, that no more rates should be tried.

When used for transmit status reporting, the driver should
always report the rate and number of retries used.

.. This file was automatic generated / don't edit.

