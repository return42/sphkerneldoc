.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fman/mac.c

.. _`fman_set_mac_active_pause`:

fman_set_mac_active_pause
=========================

.. c:function:: int fman_set_mac_active_pause(struct mac_device *mac_dev, bool rx, bool tx)

    :param struct mac_device \*mac_dev:
        A pointer to the MAC device

    :param bool rx:
        Pause frame setting for RX

    :param bool tx:
        Pause frame setting for TX

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

    :param struct mac_device \*mac_dev:
        A pointer to the MAC device

    :param bool \*rx_pause:
        *undescribed*

    :param bool \*tx_pause:
        *undescribed*

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

