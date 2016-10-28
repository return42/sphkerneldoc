.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_pkt.c

.. _`rsi_send_data_pkt`:

rsi_send_data_pkt
=================

.. c:function:: int rsi_send_data_pkt(struct rsi_common *common, struct sk_buff *skb)

    :param struct rsi_common \*common:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`rsi_send_data_pkt.description`:

Description
-----------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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

