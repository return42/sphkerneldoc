.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_pdu.c

.. _`llc_pdu_set_pf_bit`:

llc_pdu_set_pf_bit
==================

.. c:function:: void llc_pdu_set_pf_bit(struct sk_buff *skb, u8 bit_value)

    sets poll/final bit in LLC header

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param bit_value:
        poll/final bit (0 or 1).
    :type bit_value: u8

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

    :param skb:
        input skb that p/f bit must be extracted from it
    :type skb: struct sk_buff \*

    :param pf_bit:
        poll/final bit (0 or 1)
    :type pf_bit: u8 \*

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

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

.. _`llc_pdu_init_as_disc_cmd.description`:

Description
-----------

Builds a pdu frame as a DISC command.

.. _`llc_pdu_init_as_i_cmd`:

llc_pdu_init_as_i_cmd
=====================

.. c:function:: void llc_pdu_init_as_i_cmd(struct sk_buff *skb, u8 p_bit, u8 ns, u8 nr)

    builds I pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

    :param ns:
        The sequence number of the data PDU
    :type ns: u8

    :param nr:
        The seq. number of the expected I PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_i_cmd.description`:

Description
-----------

Builds a pdu frame as an I command.

.. _`llc_pdu_init_as_rej_cmd`:

llc_pdu_init_as_rej_cmd
=======================

.. c:function:: void llc_pdu_init_as_rej_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    builds REJ PDU

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

    :param nr:
        The seq. number of the expected I PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rej_cmd.description`:

Description
-----------

Builds a pdu frame as a REJ command.

.. _`llc_pdu_init_as_rnr_cmd`:

llc_pdu_init_as_rnr_cmd
=======================

.. c:function:: void llc_pdu_init_as_rnr_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    builds RNR pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

    :param nr:
        The seq. number of the expected I PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rnr_cmd.description`:

Description
-----------

Builds a pdu frame as an RNR command.

.. _`llc_pdu_init_as_rr_cmd`:

llc_pdu_init_as_rr_cmd
======================

.. c:function:: void llc_pdu_init_as_rr_cmd(struct sk_buff *skb, u8 p_bit, u8 nr)

    Builds RR pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

    :param nr:
        The seq. number of the expected I PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rr_cmd.description`:

Description
-----------

Builds a pdu frame as an RR command.

.. _`llc_pdu_init_as_sabme_cmd`:

llc_pdu_init_as_sabme_cmd
=========================

.. c:function:: void llc_pdu_init_as_sabme_cmd(struct sk_buff *skb, u8 p_bit)

    builds SABME pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param p_bit:
        The P bit to set in the PDU
    :type p_bit: u8

.. _`llc_pdu_init_as_sabme_cmd.description`:

Description
-----------

Builds a pdu frame as an SABME command.

.. _`llc_pdu_init_as_dm_rsp`:

llc_pdu_init_as_dm_rsp
======================

.. c:function:: void llc_pdu_init_as_dm_rsp(struct sk_buff *skb, u8 f_bit)

    builds DM response pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

.. _`llc_pdu_init_as_dm_rsp.description`:

Description
-----------

Builds a pdu frame as a DM response.

.. _`llc_pdu_init_as_frmr_rsp`:

llc_pdu_init_as_frmr_rsp
========================

.. c:function:: void llc_pdu_init_as_frmr_rsp(struct sk_buff *skb, struct llc_pdu_sn *prev_pdu, u8 f_bit, u8 vs, u8 vr, u8 vzyxw)

    builds FRMR response PDU

    :param skb:
        Address of the frame to build
    :type skb: struct sk_buff \*

    :param prev_pdu:
        The rejected PDU frame
    :type prev_pdu: struct llc_pdu_sn \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

    :param vs:
        tx state vari value for the data link conn at the rejecting LLC
    :type vs: u8

    :param vr:
        rx state var value for the data link conn at the rejecting LLC
    :type vr: u8

    :param vzyxw:
        completely described in the IEEE Std 802.2 document (Pg 55)
    :type vzyxw: u8

.. _`llc_pdu_init_as_frmr_rsp.description`:

Description
-----------

Builds a pdu frame as a FRMR response.

.. _`llc_pdu_init_as_rr_rsp`:

llc_pdu_init_as_rr_rsp
======================

.. c:function:: void llc_pdu_init_as_rr_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds RR response pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

    :param nr:
        The seq. number of the expected data PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rr_rsp.description`:

Description
-----------

Builds a pdu frame as an RR response.

.. _`llc_pdu_init_as_rej_rsp`:

llc_pdu_init_as_rej_rsp
=======================

.. c:function:: void llc_pdu_init_as_rej_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds REJ response pdu

    :param skb:
        Address of the skb to build
    :type skb: struct sk_buff \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

    :param nr:
        The seq. number of the expected data PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rej_rsp.description`:

Description
-----------

Builds a pdu frame as a REJ response.

.. _`llc_pdu_init_as_rnr_rsp`:

llc_pdu_init_as_rnr_rsp
=======================

.. c:function:: void llc_pdu_init_as_rnr_rsp(struct sk_buff *skb, u8 f_bit, u8 nr)

    builds RNR response pdu

    :param skb:
        Address of the frame to build
    :type skb: struct sk_buff \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

    :param nr:
        The seq. number of the expected data PDU from the remote
    :type nr: u8

.. _`llc_pdu_init_as_rnr_rsp.description`:

Description
-----------

Builds a pdu frame as an RNR response.

.. _`llc_pdu_init_as_ua_rsp`:

llc_pdu_init_as_ua_rsp
======================

.. c:function:: void llc_pdu_init_as_ua_rsp(struct sk_buff *skb, u8 f_bit)

    builds UA response pdu

    :param skb:
        Address of the frame to build
    :type skb: struct sk_buff \*

    :param f_bit:
        The F bit to set in the PDU
    :type f_bit: u8

.. _`llc_pdu_init_as_ua_rsp.description`:

Description
-----------

Builds a pdu frame as a UA response.

.. _`llc_pdu_decode_pdu_type`:

llc_pdu_decode_pdu_type
=======================

.. c:function:: void llc_pdu_decode_pdu_type(struct sk_buff *skb, u8 *type)

    designates PDU type

    :param skb:
        input skb that type of it must be designated.
    :type skb: struct sk_buff \*

    :param type:
        type of PDU (output argument).
    :type type: u8 \*

.. _`llc_pdu_decode_pdu_type.description`:

Description
-----------

This function designates type of PDU (I, S or U).

.. _`llc_pdu_get_pf_bit`:

llc_pdu_get_pf_bit
==================

.. c:function:: u8 llc_pdu_get_pf_bit(struct llc_pdu_sn *pdu)

    extracts p/f bit of input PDU

    :param pdu:
        pointer to LLC header.
    :type pdu: struct llc_pdu_sn \*

.. _`llc_pdu_get_pf_bit.description`:

Description
-----------

This function extracts p/f bit of input PDU. at first examines type of
PDU and then extracts p/f bit. Returns the p/f bit.

.. This file was automatic generated / don't edit.

