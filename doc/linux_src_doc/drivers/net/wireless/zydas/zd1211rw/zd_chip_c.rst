.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/zydas/zd1211rw/zd_chip.c

.. _`zd_rx_rate`:

zd_rx_rate
==========

.. c:function:: u8 zd_rx_rate(const void *rx_frame, const struct rx_status *status)

    report zd-rate \ ``rx_frame``\  - received frame \ ``rx_status``\  - rx_status as given by the device

    :param const void \*rx_frame:
        *undescribed*

    :param const struct rx_status \*status:
        *undescribed*

.. _`zd_rx_rate.description`:

Description
-----------

This function converts the rate as encoded in the received packet to the
zd-rate, we are using on other places in the driver.

.. This file was automatic generated / don't edit.

