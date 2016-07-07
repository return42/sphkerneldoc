.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/realtek/rtl818x/rtl818x.h

.. _`rtl818x_tx_desc_flags`:

enum rtl818x_tx_desc_flags
==========================

.. c:type:: enum rtl818x_tx_desc_flags

    Tx/Rx flags are common between RTL818X chips

.. _`rtl818x_tx_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum rtl818x_tx_desc_flags {
        RTL818X_TX_DESC_FLAG_NO_ENC,
        RTL818X_TX_DESC_FLAG_TX_OK,
        RTL818X_TX_DESC_FLAG_SPLCP,
        RTL818X_TX_DESC_FLAG_RX_UNDER,
        RTL818X_TX_DESC_FLAG_MOREFRAG,
        RTL818X_TX_DESC_FLAG_CTS,
        RTL818X_TX_DESC_FLAG_RTS,
        RTL818X_TX_DESC_FLAG_LS,
        RTL818X_TX_DESC_FLAG_FS,
        RTL818X_TX_DESC_FLAG_DMA,
        RTL818X_TX_DESC_FLAG_OWN
    };

.. _`rtl818x_tx_desc_flags.constants`:

Constants
---------

RTL818X_TX_DESC_FLAG_NO_ENC
    Disable hardware based encryption.

RTL818X_TX_DESC_FLAG_TX_OK
    TX frame was ACKed.

RTL818X_TX_DESC_FLAG_SPLCP
    Use short preamble.

RTL818X_TX_DESC_FLAG_RX_UNDER
    *undescribed*

RTL818X_TX_DESC_FLAG_MOREFRAG
    More fragments follow.

RTL818X_TX_DESC_FLAG_CTS
    Use CTS-to-self protection.

RTL818X_TX_DESC_FLAG_RTS
    Use RTS/CTS protection.

RTL818X_TX_DESC_FLAG_LS
    Last segment of the frame.

RTL818X_TX_DESC_FLAG_FS
    First segment of the frame.

RTL818X_TX_DESC_FLAG_DMA
    *undescribed*

RTL818X_TX_DESC_FLAG_OWN
    *undescribed*

.. This file was automatic generated / don't edit.

