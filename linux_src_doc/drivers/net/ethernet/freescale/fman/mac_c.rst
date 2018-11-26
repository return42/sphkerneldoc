.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fman/mac.c

.. _`fman_set_mac_active_pause`:

fman_set_mac_active_pause
=========================

.. c:function:: int fman_set_mac_active_pause(struct mac_device *mac_dev, bool rx, bool tx)

    :param mac_dev:
        A pointer to the MAC device
    :type mac_dev: struct mac_device \*

    :param rx:
        Pause frame setting for RX
    :type rx: bool

    :param tx:
        Pause frame setting for TX
    :type tx: bool

.. _`fman_set_mac_active_pause.description`:

Description
-----------

Set the MAC RX/TX PAUSE frames settings

Avoid redundant calls to FMD, if the MAC driver already contains the desired
active PAUSE settings. Otherwise, the new active settings should be reflected
in FMan.

.. _`fman_set_mac_active_pause.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_get_pause_cfg`:

fman_get_pause_cfg
==================

.. c:function:: void fman_get_pause_cfg(struct mac_device *mac_dev, bool *rx_pause, bool *tx_pause)

    :param mac_dev:
        A pointer to the MAC device
    :type mac_dev: struct mac_device \*

    :param rx_pause:
        *undescribed*
    :type rx_pause: bool \*

    :param tx_pause:
        *undescribed*
    :type tx_pause: bool \*

.. _`fman_get_pause_cfg.description`:

Description
-----------

Determine the MAC RX/TX PAUSE frames settings based on PHY
autonegotiation or values set by eththool.

.. _`fman_get_pause_cfg.return`:

Return
------

Pointer to FMan device.

.. This file was automatic generated / don't edit.

