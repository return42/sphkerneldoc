.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ti-st/st_core.c

.. _`st_reg_complete`:

st_reg_complete
===============

.. c:function:: void st_reg_complete(struct st_data_s *st_gdata, char err)

    to call registration complete callbacks of all protocol stack drivers This function is being called with spin lock held, protocol drivers are only expected to complete their waits and do nothing more than that.

    :param struct st_data_s \*st_gdata:
        *undescribed*

    :param char err:
        *undescribed*

.. _`st_wakeup_ack`:

st_wakeup_ack
=============

.. c:function:: void st_wakeup_ack(struct st_data_s *st_gdata, unsigned char cmd)

    internal function for action when wake-up ack received

    :param struct st_data_s \*st_gdata:
        *undescribed*

    :param unsigned char cmd:
        *undescribed*

.. _`st_int_recv`:

st_int_recv
===========

.. c:function:: void st_int_recv(void *disc_data, const unsigned char *data, long count)

    ST's internal receive function. Decodes received RAW data and forwards to corresponding client drivers (Bluetooth,FM,GPS..etc). This can receive various types of packets, HCI-Events, ACL, SCO, 4 types of HCI-LL PM packets CH-8 packets from FM, CH-9 packets from GPS cores.

    :param void \*disc_data:
        *undescribed*

    :param const unsigned char \*data:
        *undescribed*

    :param long count:
        *undescribed*

.. _`st_int_dequeue`:

st_int_dequeue
==============

.. c:function:: struct sk_buff *st_int_dequeue(struct st_data_s *st_gdata)

    internal de-Q function. If the previous data set was not written completely, return that skb which has the pending data. In normal cases, return top of txq.

    :param struct st_data_s \*st_gdata:
        *undescribed*

.. _`st_int_enqueue`:

st_int_enqueue
==============

.. c:function:: void st_int_enqueue(struct st_data_s *st_gdata, struct sk_buff *skb)

    internal Q-ing function. Will either Q the skb to txq or the tx_waitq depending on the ST LL state. If the chip is asleep, then Q it onto waitq and wakeup the chip. txq and waitq needs protection since the other contexts may be sending data, waking up chip.

    :param struct st_data_s \*st_gdata:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. This file was automatic generated / don't edit.

