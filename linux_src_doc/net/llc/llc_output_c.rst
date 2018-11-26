.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_output.c

.. _`llc_mac_hdr_init`:

llc_mac_hdr_init
================

.. c:function:: int llc_mac_hdr_init(struct sk_buff *skb, const unsigned char *sa, const unsigned char *da)

    fills MAC header fields

    :param skb:
        Address of the frame to initialize its MAC header
    :type skb: struct sk_buff \*

    :param sa:
        The MAC source address
    :type sa: const unsigned char \*

    :param da:
        The MAC destination address
    :type da: const unsigned char \*

.. _`llc_mac_hdr_init.description`:

Description
-----------

Fills MAC header fields, depending on MAC type. Returns 0, If MAC type
is a valid type and initialization completes correctly 1, otherwise.

.. _`llc_build_and_send_ui_pkt`:

llc_build_and_send_ui_pkt
=========================

.. c:function:: int llc_build_and_send_ui_pkt(struct llc_sap *sap, struct sk_buff *skb, unsigned char *dmac, unsigned char dsap)

    unitdata request interface for upper layers

    :param sap:
        sap to use
    :type sap: struct llc_sap \*

    :param skb:
        packet to send
    :type skb: struct sk_buff \*

    :param dmac:
        destination mac address
    :type dmac: unsigned char \*

    :param dsap:
        destination sap
    :type dsap: unsigned char

.. _`llc_build_and_send_ui_pkt.description`:

Description
-----------

Upper layers calls this function when upper layer wants to send data
using connection-less mode communication (UI pdu).

Accept data frame from network layer to be sent using connection-
less mode communication; timeout/retries handled by network layer;
package primitive as an event and send to SAP event handler

.. This file was automatic generated / don't edit.

