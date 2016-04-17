.. -*- coding: utf-8; mode: rst -*-

==============
ptp_classify.h
==============


.. _`ptp_classify_raw`:

ptp_classify_raw
================

.. c:function:: unsigned int ptp_classify_raw (const struct sk_buff *skb)

    classify a PTP packet

    :param const struct sk_buff \*skb:
        buffer



.. _`ptp_classify_raw.description`:

Description
-----------

Runs a minimal BPF dissector to classify a network packet to
determine the PTP class. In case the skb does not contain any
PTP protocol data, PTP_CLASS_NONE will be returned, otherwise
PTP_CLASS_V1_IPV{4,6}, PTP_CLASS_V2_IPV{4,6} or
PTP_CLASS_V2_{L2,VLAN}, depending on the packet content.

