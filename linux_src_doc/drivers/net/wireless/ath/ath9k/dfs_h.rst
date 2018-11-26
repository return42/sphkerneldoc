.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/dfs.h

.. _`ath9k_dfs_process_phyerr`:

ath9k_dfs_process_phyerr
========================

.. c:function:: void ath9k_dfs_process_phyerr(struct ath_softc *sc, void *data, struct ath_rx_status *rs, u64 mactime)

    process radar PHY error

    :param sc:
        ath_softc
    :type sc: struct ath_softc \*

    :param data:
        RX payload data
    :type data: void \*

    :param rs:
        RX status after processing descriptor
    :type rs: struct ath_rx_status \*

    :param mactime:
        receive time
    :type mactime: u64

.. _`ath9k_dfs_process_phyerr.description`:

Description
-----------

This function is called whenever the HW DFS module detects a radar
pulse and reports it as a PHY error.

The radar information provided as raw payload data is validated and
filtered for false pulses. Events passing all tests are forwarded to
the DFS detector for pattern detection.

.. This file was automatic generated / don't edit.

