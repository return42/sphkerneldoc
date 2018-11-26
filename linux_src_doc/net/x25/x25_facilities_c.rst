.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/x25/x25_facilities.c

.. _`x25_parse_facilities`:

x25_parse_facilities
====================

.. c:function:: int x25_parse_facilities(struct sk_buff *skb, struct x25_facilities *facilities, struct x25_dte_facilities *dte_facs, unsigned long *vc_fac_mask)

    Parse facilities from skb into the facilities structs

    :param skb:
        sk_buff to parse
    :type skb: struct sk_buff \*

    :param facilities:
        Regular facilities, updated as facilities are found
    :type facilities: struct x25_facilities \*

    :param dte_facs:
        ITU DTE facilities, updated as DTE facilities are found
    :type dte_facs: struct x25_dte_facilities \*

    :param vc_fac_mask:
        mask is updated with all facilities found
    :type vc_fac_mask: unsigned long \*

.. _`x25_parse_facilities.return-codes`:

Return codes
------------

-1 - Parsing error, caller should drop call and clean up
0 - Parse OK, this skb has no facilities
>0 - Parse OK, returns the length of the facilities header

.. This file was automatic generated / don't edit.

