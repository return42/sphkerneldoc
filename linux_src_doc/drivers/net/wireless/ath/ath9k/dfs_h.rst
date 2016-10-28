.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/dfs.h

.. _`ath9k_dfs_process_phyerr`:

ath9k_dfs_process_phyerr
========================

.. c:function:: void ath9k_dfs_process_phyerr(struct ath_softc *sc, void *data, struct ath_rx_status *rs, u64 mactime)

    process radar PHY error

    :param struct ath_softc \*sc:
        ath_softc

    :param void \*data:
        RX payload data

    :param struct ath_rx_status \*rs:
        RX status after processing descriptor

    :param u64 mactime:
        receive time

.. _`ath9k_dfs_process_phyerr.description`:

Description
-----------

This function is called whenever the HW DFS module detects a radar
pulse and reports it as a PHY error.

The radar information provided as raw payload data is validated and
filtered for false pulses. Events passing all tests are forwarded to
the DFS detector for pattern detection.

.. This file was automatic generated / don't edit.

