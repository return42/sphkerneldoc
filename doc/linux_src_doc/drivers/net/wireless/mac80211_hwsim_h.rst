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

.. This file was automatic generated / don't edit.

