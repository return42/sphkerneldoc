.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_pdu.c

.. _`llc_pdu_set_pf_bit`:

llc_pdu_set_pf_bit
==================

.. c:function:: void llc_pdu_set_pf_bit(struct sk_buff *skb, u8 bit_value)

    sets poll/final bit in LLC header

    :param struct sk_buff \*skb:
        *undescribed*

    :param u8 bit_value:
        poll/final bit (0 or 1).

.. _`llc_pdu_set_pf_bit.description`:

Description
-----------

This function sets poll/final bit in LLC header (based on type of PDU).
in I or S pdus, p/f bit is right bit of fourth byte in header. in U
pdus p/f bit is fifth bit of third byte.

.. _`llc_pdu_decode_pf_bit`:

llc_pdu_decode_pf_bit
=====================

.. c:function:: void llc_pdu_decode_pf_bit(struct sk_buff *skb, u8 *pf_bit)

    extracs poll/final bit from LLC header

    :param struct sk_buff \*skb:
        input skb that p/f bit must be extracted from it

    :param u8 \*pf_bit:
        poll/final bit (0 or 1)

.. _`llc_pdu_decode_pf_bit.description`:

Description
-----------

This function extracts poll/final bit from LLC header (based on type of
PDU). In I or S pdus, p/f bit is right bit of fourth byte in header. In
U pdus p/f bit is fifth bit of third byte.

.. _`llc_pdu_init_as_disc_cmd`:

llc_pdu_init_as_disc_cmd
========================

.. c:function:: void llc_pdu_init_as_disc_cmd(struct sk_buff *skb, u8 p_bit)

    Builds DISC PDU

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

.. _`llc_pdu_init_as_disc_cmd.description`:

Description
-----------

Builds a pdu frame as a DISC command.

.. _`llc_pdu_init_as_i_cmd`:

llc_pdu_init_as_i_cmd
=====================

.. c:function:: void llc_pdu_init_as_i_cmd(struct sk_buff *skb, u8 p_bit, u8 ns, u8 nr)

    builds I pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

    :param u8 ns:
        The sequence number of the data PDU

    :param u8 nr:
        The seq. number of the expected I PDU from the remote

.. _`llc_pdu_init_as_i_cmd.description`:

Description
-----------

Builds a pdu frame as an I command.

.. _`llc_pdu_init_as_rej_cmd`:

llc_pdu_init_as_rej_cmd
=======================

.. c:function:: void llc_pdu_init_as_rej_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    builds REJ PDU

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected I PDU from the remote

.. _`llc_pdu_init_as_rej_cmd.description`:

Description
-----------

Builds a pdu frame as a REJ command.

.. _`llc_pdu_init_as_rnr_cmd`:

llc_pdu_init_as_rnr_cmd
=======================

.. c:function:: void llc_pdu_init_as_rnr_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    builds RNR pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected I PDU from the remote

.. _`llc_pdu_init_as_rnr_cmd.description`:

Description
-----------

Builds a pdu frame as an RNR command.

.. _`llc_pdu_init_as_rr_cmd`:

llc_pdu_init_as_rr_cmd
======================

.. c:function:: void llc_pdu_init_as_rr_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    Builds RR pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected I PDU from the remote

.. _`llc_pdu_init_as_rr_cmd.description`:

Description
-----------

Builds a pdu frame as an RR command.

.. _`llc_pdu_init_as_sabme_cmd`:

llc_pdu_init_as_sabme_cmd
=========================

.. c:function:: void llc_pdu_init_as_sabme_cmd(struct sk_buff *skb, u8 p_bit)

    builds SABME pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 p_bit:
        The P bit to set in the PDU

.. _`llc_pdu_init_as_sabme_cmd.description`:

Description
-----------

Builds a pdu frame as an SABME command.

.. _`llc_pdu_init_as_dm_rsp`:

llc_pdu_init_as_dm_rsp
======================

.. c:function:: void llc_pdu_init_as_dm_rsp(struct sk_buff *skb, u8 f_bit)

    builds DM response pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 f_bit:
        The F bit to set in the PDU

.. _`llc_pdu_init_as_dm_rsp.description`:

Description
-----------

Builds a pdu frame as a DM response.

.. _`llc_pdu_init_as_frmr_rsp`:

llc_pdu_init_as_frmr_rsp
========================

.. c:function:: void llc_pdu_init_as_frmr_rsp(struct sk_buff *skb, struct llc_pdu_sn *prev_pdu, u8 f_bit, u8 vs, u8 vr, u8 vzyxw)

    builds FRMR response PDU

    :param struct sk_buff \*skb:
        Address of the frame to build

    :param struct llc_pdu_sn \*prev_pdu:
        The rejected PDU frame

    :param u8 f_bit:
        The F bit to set in the PDU

    :param u8 vs:
        tx state vari value for the data link conn at the rejecting LLC

    :param u8 vr:
        rx state var value for the data link conn at the rejecting LLC

    :param u8 vzyxw:
        completely described in the IEEE Std 802.2 document (Pg 55)

.. _`llc_pdu_init_as_frmr_rsp.description`:

Description
-----------

Builds a pdu frame as a FRMR response.

.. _`llc_pdu_init_as_rr_rsp`:

llc_pdu_init_as_rr_rsp
======================

.. c:function:: void llc_pdu_init_as_rr_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds RR response pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 f_bit:
        The F bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected data PDU from the remote

.. _`llc_pdu_init_as_rr_rsp.description`:

Description
-----------

Builds a pdu frame as an RR response.

.. _`llc_pdu_init_as_rej_rsp`:

llc_pdu_init_as_rej_rsp
=======================

.. c:function:: void llc_pdu_init_as_rej_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds REJ response pdu

    :param struct sk_buff \*skb:
        Address of the skb to build

    :param u8 f_bit:
        The F bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected data PDU from the remote

.. _`llc_pdu_init_as_rej_rsp.description`:

Description
-----------

Builds a pdu frame as a REJ response.

.. _`llc_pdu_init_as_rnr_rsp`:

llc_pdu_init_as_rnr_rsp
=======================

.. c:function:: void llc_pdu_init_as_rnr_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds RNR response pdu

    :param struct sk_buff \*skb:
        Address of the frame to build

    :param u8 f_bit:
        The F bit to set in the PDU

    :param u8 nr:
        The seq. number of the expected data PDU from the remote

.. _`llc_pdu_init_as_rnr_rsp.description`:

Description
-----------

Builds a pdu frame as an RNR response.

.. _`llc_pdu_init_as_ua_rsp`:

llc_pdu_init_as_ua_rsp
======================

.. c:function:: void llc_pdu_init_as_ua_rsp(struct sk_buff *skb, u8 f_bit)

    builds UA response pdu

    :param struct sk_buff \*skb:
        Address of the frame to build

    :param u8 f_bit:
        The F bit to set in the PDU

.. _`llc_pdu_init_as_ua_rsp.description`:

Description
-----------

Builds a pdu frame as a UA response.

.. _`llc_pdu_decode_pdu_type`:

llc_pdu_decode_pdu_type
=======================

.. c:function:: void llc_pdu_decode_pdu_type(struct sk_buff *skb, u8 *type)

    designates PDU type

    :param struct sk_buff \*skb:
        input skb that type of it must be designated.

    :param u8 \*type:
        type of PDU (output argument).

.. _`llc_pdu_decode_pdu_type.description`:

Description
-----------

This function designates type of PDU (I, S or U).

.. _`llc_pdu_get_pf_bit`:

llc_pdu_get_pf_bit
==================

.. c:function:: u8 llc_pdu_get_pf_bit(struct llc_pdu_sn *pdu)

    extracts p/f bit of input PDU

    :param struct llc_pdu_sn \*pdu:
        pointer to LLC header.

.. _`llc_pdu_get_pf_bit.description`:

Description
-----------

This function extracts p/f bit of input PDU. at first examines type of
PDU and then extracts p/f bit. Returns the p/f bit.

.. This file was automatic generated / don't edit.

