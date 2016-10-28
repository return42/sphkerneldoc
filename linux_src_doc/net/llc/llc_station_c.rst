.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_station.c

.. _`llc_station_rcv`:

llc_station_rcv
===============

.. c:function:: void llc_station_rcv(struct sk_buff *skb)

    send received pdu to the station state machine

    :param struct sk_buff \*skb:
        received frame.

.. _`llc_station_rcv.description`:

Description
-----------

Sends data unit to station state machine.

.. This file was automatic generated / don't edit.

