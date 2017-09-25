.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/desc.h

.. _`ath5k_hw_rx_ctl`:

struct ath5k_hw_rx_ctl
======================

.. c:type:: struct ath5k_hw_rx_ctl

    Common hardware RX control descriptor

.. _`ath5k_hw_rx_ctl.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_rx_ctl {
        u32 rx_control_0;
        u32 rx_control_1;
    }

.. _`ath5k_hw_rx_ctl.members`:

Members
-------

rx_control_0
    RX control word 0

rx_control_1
    RX control word 1

.. _`ath5k_hw_rx_status`:

struct ath5k_hw_rx_status
=========================

.. c:type:: struct ath5k_hw_rx_status

    Common hardware RX status descriptor

.. _`ath5k_hw_rx_status.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_rx_status {
        u32 rx_status_0;
        u32 rx_status_1;
    }

.. _`ath5k_hw_rx_status.members`:

Members
-------

rx_status_0
    RX status word 0

rx_status_1
    RX status word 1

.. _`ath5k_hw_rx_status.description`:

Description
-----------

5210, 5211 and 5212 differ only in the fields and flags defined below

.. _`ath5k_phy_error_code`:

enum ath5k_phy_error_code
=========================

.. c:type:: enum ath5k_phy_error_code

    PHY Error codes

.. _`ath5k_phy_error_code.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_phy_error_code {
        AR5K_RX_PHY_ERROR_UNDERRUN,
        AR5K_RX_PHY_ERROR_TIMING,
        AR5K_RX_PHY_ERROR_PARITY,
        AR5K_RX_PHY_ERROR_RATE,
        AR5K_RX_PHY_ERROR_LENGTH,
        AR5K_RX_PHY_ERROR_RADAR,
        AR5K_RX_PHY_ERROR_SERVICE,
        AR5K_RX_PHY_ERROR_TOR,
        AR5K_RX_PHY_ERROR_OFDM_TIMING,
        AR5K_RX_PHY_ERROR_OFDM_SIGNAL_PARITY,
        AR5K_RX_PHY_ERROR_OFDM_RATE_ILLEGAL,
        AR5K_RX_PHY_ERROR_OFDM_LENGTH_ILLEGAL,
        AR5K_RX_PHY_ERROR_OFDM_POWER_DROP,
        AR5K_RX_PHY_ERROR_OFDM_SERVICE,
        AR5K_RX_PHY_ERROR_OFDM_RESTART,
        AR5K_RX_PHY_ERROR_CCK_TIMING,
        AR5K_RX_PHY_ERROR_CCK_HEADER_CRC,
        AR5K_RX_PHY_ERROR_CCK_RATE_ILLEGAL,
        AR5K_RX_PHY_ERROR_CCK_SERVICE,
        AR5K_RX_PHY_ERROR_CCK_RESTART
    };

.. _`ath5k_phy_error_code.constants`:

Constants
---------

AR5K_RX_PHY_ERROR_UNDERRUN
    Transmit underrun, [5210] No error

AR5K_RX_PHY_ERROR_TIMING
    Timing error

AR5K_RX_PHY_ERROR_PARITY
    Illegal parity

AR5K_RX_PHY_ERROR_RATE
    Illegal rate

AR5K_RX_PHY_ERROR_LENGTH
    Illegal length

AR5K_RX_PHY_ERROR_RADAR
    Radar detect, [5210] 64 QAM rate

AR5K_RX_PHY_ERROR_SERVICE
    Illegal service

AR5K_RX_PHY_ERROR_TOR
    Transmit override receive

AR5K_RX_PHY_ERROR_OFDM_TIMING
    OFDM Timing error [5212+]

AR5K_RX_PHY_ERROR_OFDM_SIGNAL_PARITY
    OFDM Signal parity error [5212+]

AR5K_RX_PHY_ERROR_OFDM_RATE_ILLEGAL
    OFDM Illegal rate [5212+]

AR5K_RX_PHY_ERROR_OFDM_LENGTH_ILLEGAL
    OFDM Illegal length [5212+]

AR5K_RX_PHY_ERROR_OFDM_POWER_DROP
    OFDM Power drop [5212+]

AR5K_RX_PHY_ERROR_OFDM_SERVICE
    OFDM Service (?) [5212+]

AR5K_RX_PHY_ERROR_OFDM_RESTART
    OFDM Restart (?) [5212+]

AR5K_RX_PHY_ERROR_CCK_TIMING
    CCK Timing error [5212+]

AR5K_RX_PHY_ERROR_CCK_HEADER_CRC
    Header CRC error [5212+]

AR5K_RX_PHY_ERROR_CCK_RATE_ILLEGAL
    Illegal rate [5212+]

AR5K_RX_PHY_ERROR_CCK_SERVICE
    CCK Service (?) [5212+]

AR5K_RX_PHY_ERROR_CCK_RESTART
    CCK Restart (?) [5212+]

.. _`ath5k_hw_2w_tx_ctl`:

struct ath5k_hw_2w_tx_ctl
=========================

.. c:type:: struct ath5k_hw_2w_tx_ctl

    5210/5211 hardware 2-word TX control descriptor

.. _`ath5k_hw_2w_tx_ctl.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_2w_tx_ctl {
        u32 tx_control_0;
        u32 tx_control_1;
    }

.. _`ath5k_hw_2w_tx_ctl.members`:

Members
-------

tx_control_0
    TX control word 0

tx_control_1
    TX control word 1

.. _`ath5k_hw_4w_tx_ctl`:

struct ath5k_hw_4w_tx_ctl
=========================

.. c:type:: struct ath5k_hw_4w_tx_ctl

    5212 hardware 4-word TX control descriptor

.. _`ath5k_hw_4w_tx_ctl.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_4w_tx_ctl {
        u32 tx_control_0;
        u32 tx_control_1;
        u32 tx_control_2;
        u32 tx_control_3;
    }

.. _`ath5k_hw_4w_tx_ctl.members`:

Members
-------

tx_control_0
    TX control word 0

tx_control_1
    TX control word 1

tx_control_2
    TX control word 2

tx_control_3
    TX control word 3

.. _`ath5k_hw_tx_status`:

struct ath5k_hw_tx_status
=========================

.. c:type:: struct ath5k_hw_tx_status

    Common TX status descriptor

.. _`ath5k_hw_tx_status.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_tx_status {
        u32 tx_status_0;
        u32 tx_status_1;
    }

.. _`ath5k_hw_tx_status.members`:

Members
-------

tx_status_0
    TX status word 0

tx_status_1
    TX status word 1

.. _`ath5k_hw_5210_tx_desc`:

struct ath5k_hw_5210_tx_desc
============================

.. c:type:: struct ath5k_hw_5210_tx_desc

    5210/5211 hardware TX descriptor

.. _`ath5k_hw_5210_tx_desc.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_5210_tx_desc {
        struct ath5k_hw_2w_tx_ctl tx_ctl;
        struct ath5k_hw_tx_status tx_stat;
    }

.. _`ath5k_hw_5210_tx_desc.members`:

Members
-------

tx_ctl
    The \ :c:type:`struct ath5k_hw_2w_tx_ctl <ath5k_hw_2w_tx_ctl>`\ 

tx_stat
    The \ :c:type:`struct ath5k_hw_tx_status <ath5k_hw_tx_status>`\ 

.. _`ath5k_hw_5212_tx_desc`:

struct ath5k_hw_5212_tx_desc
============================

.. c:type:: struct ath5k_hw_5212_tx_desc

    5212 hardware TX descriptor

.. _`ath5k_hw_5212_tx_desc.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_5212_tx_desc {
        struct ath5k_hw_4w_tx_ctl tx_ctl;
        struct ath5k_hw_tx_status tx_stat;
    }

.. _`ath5k_hw_5212_tx_desc.members`:

Members
-------

tx_ctl
    The \ :c:type:`struct ath5k_hw_4w_tx_ctl <ath5k_hw_4w_tx_ctl>`\ 

tx_stat
    The \ :c:type:`struct ath5k_hw_tx_status <ath5k_hw_tx_status>`\ 

.. _`ath5k_hw_all_rx_desc`:

struct ath5k_hw_all_rx_desc
===========================

.. c:type:: struct ath5k_hw_all_rx_desc

    Common hardware RX descriptor

.. _`ath5k_hw_all_rx_desc.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_hw_all_rx_desc {
        struct ath5k_hw_rx_ctl rx_ctl;
        struct ath5k_hw_rx_status rx_stat;
    }

.. _`ath5k_hw_all_rx_desc.members`:

Members
-------

rx_ctl
    The \ :c:type:`struct ath5k_hw_rx_ctl <ath5k_hw_rx_ctl>`\ 

rx_stat
    The \ :c:type:`struct ath5k_hw_rx_status <ath5k_hw_rx_status>`\ 

.. _`ath5k_desc`:

struct ath5k_desc
=================

.. c:type:: struct ath5k_desc

    Atheros hardware DMA descriptor

.. _`ath5k_desc.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_desc {
        u32 ds_link;
        u32 ds_data;
        union {
            struct ath5k_hw_5210_tx_desc ds_tx5210;
            struct ath5k_hw_5212_tx_desc ds_tx5212;
            struct ath5k_hw_all_rx_desc ds_rx;
        } ud;
    }

.. _`ath5k_desc.members`:

Members
-------

ds_link
    Physical address of the next descriptor

ds_data
    Physical address of data buffer (skb)

ds_tx5210
    *undescribed*

ds_tx5212
    *undescribed*

ds_rx
    *undescribed*

d
    *undescribed*

.. _`ath5k_desc.description`:

Description
-----------

This is read and written to by the hardware

.. This file was automatic generated / don't edit.

