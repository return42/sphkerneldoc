.. -*- coding: utf-8; mode: rst -*-

============
llc_output.c
============


.. _`llc_mac_hdr_init`:

llc_mac_hdr_init
================

.. c:function:: int llc_mac_hdr_init (struct sk_buff *skb, const unsigned char *sa, const unsigned char *da)

    fills MAC header fields

    :param struct sk_buff \*skb:
        Address of the frame to initialize its MAC header

    :param const unsigned char \*sa:
        The MAC source address

    :param const unsigned char \*da:
        The MAC destination address



.. _`llc_mac_hdr_init.description`:

Description
-----------

Fills MAC header fields, depending on MAC type. Returns 0, If MAC type
is a valid type and initialization completes correctly 1, otherwise.



.. _`llc_build_and_send_ui_pkt`:

llc_build_and_send_ui_pkt
=========================

.. c:function:: int llc_build_and_send_ui_pkt (struct llc_sap *sap, struct sk_buff *skb, unsigned char *dmac, unsigned char dsap)

    unitdata request interface for upper layers

    :param struct llc_sap \*sap:
        sap to use

    :param struct sk_buff \*skb:
        packet to send

    :param unsigned char \*dmac:
        destination mac address

    :param unsigned char dsap:
        destination sap



.. _`llc_build_and_send_ui_pkt.description`:

Description
-----------

Upper layers calls this function when upper layer wants to send data
using connection-less mode communication (UI pdu).

Accept data frame from network layer to be sent using connection-
less mode communication; timeout/retries handled by network layer;
package primitive as an event and send to SAP event handler

