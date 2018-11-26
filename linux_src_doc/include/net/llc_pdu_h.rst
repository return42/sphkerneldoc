.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/llc_pdu.h

.. _`llc_pdu_header_init`:

llc_pdu_header_init
===================

.. c:function:: void llc_pdu_header_init(struct sk_buff *skb, u8 type, u8 ssap, u8 dsap, u8 cr)

    initializes pdu header

    :param skb:
        input skb that header must be set into it.
    :type skb: struct sk_buff \*

    :param type:
        type of PDU (U, I or S).
    :type type: u8

    :param ssap:
        source sap.
    :type ssap: u8

    :param dsap:
        destination sap.
    :type dsap: u8

    :param cr:
        command/response bit (0 or 1).
    :type cr: u8

.. _`llc_pdu_header_init.description`:

Description
-----------

This function sets DSAP, SSAP and command/Response bit in LLC header.

.. _`llc_pdu_decode_sa`:

llc_pdu_decode_sa
=================

.. c:function:: void llc_pdu_decode_sa(struct sk_buff *skb, u8 *sa)

    extracs source address (MAC) of input frame

    :param skb:
        input skb that source address must be extracted from it.
    :type skb: struct sk_buff \*

    :param sa:
        pointer to source address (6 byte array).
    :type sa: u8 \*

.. _`llc_pdu_decode_sa.description`:

Description
-----------

This function extracts source address(MAC) of input frame.

.. _`llc_pdu_decode_da`:

llc_pdu_decode_da
=================

.. c:function:: void llc_pdu_decode_da(struct sk_buff *skb, u8 *da)

    extracts dest address of input frame

    :param skb:
        input skb that destination address must be extracted from it
    :type skb: struct sk_buff \*

    :param da:
        *undescribed*
    :type da: u8 \*

.. _`llc_pdu_decode_da.description`:

Description
-----------

This function extracts destination address(MAC) of input frame.

.. _`llc_pdu_decode_ssap`:

llc_pdu_decode_ssap
===================

.. c:function:: void llc_pdu_decode_ssap(struct sk_buff *skb, u8 *ssap)

    extracts source SAP of input frame

    :param skb:
        input skb that source SAP must be extracted from it.
    :type skb: struct sk_buff \*

    :param ssap:
        source SAP (output argument).
    :type ssap: u8 \*

.. _`llc_pdu_decode_ssap.description`:

Description
-----------

This function extracts source SAP of input frame. Right bit of SSAP is
command/response bit.

.. _`llc_pdu_decode_dsap`:

llc_pdu_decode_dsap
===================

.. c:function:: void llc_pdu_decode_dsap(struct sk_buff *skb, u8 *dsap)

    extracts dest SAP of input frame

    :param skb:
        input skb that destination SAP must be extracted from it.
    :type skb: struct sk_buff \*

    :param dsap:
        destination SAP (output argument).
    :type dsap: u8 \*

.. _`llc_pdu_decode_dsap.description`:

Description
-----------

This function extracts destination SAP of input frame. right bit of
DSAP designates individual/group SAP.

.. _`llc_pdu_init_as_ui_cmd`:

llc_pdu_init_as_ui_cmd
======================

.. c:function:: void llc_pdu_init_as_ui_cmd(struct sk_buff *skb)

    sets LLC header as UI PDU

    :param skb:
        input skb that header must be set into it.
    :type skb: struct sk_buff \*

.. _`llc_pdu_init_as_ui_cmd.description`:

Description
-----------

This function sets third byte of LLC header as a UI PDU.

.. _`llc_pdu_init_as_test_cmd`:

llc_pdu_init_as_test_cmd
========================

.. c:function:: void llc_pdu_init_as_test_cmd(struct sk_buff *skb)

    sets PDU as TEST \ ``skb``\  - Address of the skb to build

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`llc_pdu_init_as_test_cmd.description`:

Description
-----------

Sets a PDU as TEST

.. _`llc_pdu_init_as_test_rsp`:

llc_pdu_init_as_test_rsp
========================

.. c:function:: void llc_pdu_init_as_test_rsp(struct sk_buff *skb, struct sk_buff *ev_skb)

    build TEST response PDU

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param ev_skb:
        The received TEST command PDU frame
    :type ev_skb: struct sk_buff \*

.. _`llc_pdu_init_as_test_rsp.description`:

Description
-----------

Builds a pdu frame as a TEST response.

.. _`llc_pdu_init_as_xid_cmd`:

llc_pdu_init_as_xid_cmd
=======================

.. c:function:: void llc_pdu_init_as_xid_cmd(struct sk_buff *skb, u8 svcs_supported, u8 rx_window)

    sets bytes 3, 4 & 5 of LLC header as XID

    :param skb:
        input skb that header must be set into it.
    :type skb: struct sk_buff \*

    :param svcs_supported:
        *undescribed*
    :type svcs_supported: u8

    :param rx_window:
        *undescribed*
    :type rx_window: u8

.. _`llc_pdu_init_as_xid_cmd.description`:

Description
-----------

This function sets third,fourth,fifth and sixth bytes of LLC header as
a XID PDU.

.. _`llc_pdu_init_as_xid_rsp`:

llc_pdu_init_as_xid_rsp
=======================

.. c:function:: void llc_pdu_init_as_xid_rsp(struct sk_buff *skb, u8 svcs_supported, u8 rx_window)

    builds XID response PDU

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param svcs_supported:
        The class of the LLC (I or II)
    :type svcs_supported: u8

    :param rx_window:
        The size of the receive window of the LLC
    :type rx_window: u8

.. _`llc_pdu_init_as_xid_rsp.description`:

Description
-----------

Builds a pdu frame as an XID response.

.. This file was automatic generated / don't edit.

