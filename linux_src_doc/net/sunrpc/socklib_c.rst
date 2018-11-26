.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/socklib.c

.. _`xdr_skb_read_bits`:

xdr_skb_read_bits
=================

.. c:function:: size_t xdr_skb_read_bits(struct xdr_skb_reader *desc, void *to, size_t len)

    copy some data bits from skb to internal buffer

    :param desc:
        sk_buff copy helper
    :type desc: struct xdr_skb_reader \*

    :param to:
        copy destination
    :type to: void \*

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`xdr_skb_read_bits.description`:

Description
-----------

Possibly called several times to iterate over an sk_buff and copy
data out of it.

.. _`xdr_skb_read_and_csum_bits`:

xdr_skb_read_and_csum_bits
==========================

.. c:function:: size_t xdr_skb_read_and_csum_bits(struct xdr_skb_reader *desc, void *to, size_t len)

    copy and checksum from skb to buffer

    :param desc:
        sk_buff copy helper
    :type desc: struct xdr_skb_reader \*

    :param to:
        copy destination
    :type to: void \*

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`xdr_skb_read_and_csum_bits.description`:

Description
-----------

Same as skb_read_bits, but calculate a checksum at the same time.

.. _`xdr_partial_copy_from_skb`:

xdr_partial_copy_from_skb
=========================

.. c:function:: ssize_t xdr_partial_copy_from_skb(struct xdr_buf *xdr, unsigned int base, struct xdr_skb_reader *desc, xdr_skb_read_actor copy_actor)

    copy data out of an skb

    :param xdr:
        target XDR buffer
    :type xdr: struct xdr_buf \*

    :param base:
        starting offset
    :type base: unsigned int

    :param desc:
        sk_buff copy helper
    :type desc: struct xdr_skb_reader \*

    :param copy_actor:
        virtual method for copying data
    :type copy_actor: xdr_skb_read_actor

.. _`csum_partial_copy_to_xdr`:

csum_partial_copy_to_xdr
========================

.. c:function:: int csum_partial_copy_to_xdr(struct xdr_buf *xdr, struct sk_buff *skb)

    checksum and copy data

    :param xdr:
        target XDR buffer
    :type xdr: struct xdr_buf \*

    :param skb:
        source skb
    :type skb: struct sk_buff \*

.. _`csum_partial_copy_to_xdr.description`:

Description
-----------

We have set things up such that we perform the checksum of the UDP
packet in parallel with the copies into the RPC client iovec.  -DaveM

.. This file was automatic generated / don't edit.

