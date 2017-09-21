.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_hal.c

.. _`rsi_send_mgmt_pkt`:

rsi_send_mgmt_pkt
=================

.. c:function:: int rsi_send_mgmt_pkt(struct rsi_common *common, struct sk_buff *skb)

    This functions sends the received management packet from driver to device.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param struct sk_buff \*skb:
        Pointer to the socket buffer structure.

.. _`rsi_send_mgmt_pkt.return`:

Return
------

status: 0 on success, -1 on failure.

.. This file was automatic generated / don't edit.

