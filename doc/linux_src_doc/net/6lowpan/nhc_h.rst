.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/6lowpan/nhc.h

.. _`lowpan_nhc`:

struct lowpan_nhc
=================

.. c:type:: struct lowpan_nhc

    hold 6lowpan next hdr compression ifnformation

.. _`lowpan_nhc.definition`:

Definition
----------

.. code-block:: c

    struct lowpan_nhc {
        struct rb_node node;
        const char *name;
        const u8 nexthdr;
        const size_t nexthdrlen;
        u8 *id;
        u8 *idmask;
        const size_t idlen;
        void (* idsetup) (struct lowpan_nhc *nhc);
        int (* uncompress) (struct sk_buff *skb, size_t needed);
        int (* compress) (struct sk_buff *skb, u8 **hc_ptr);
    }

.. _`lowpan_nhc.members`:

Members
-------

node
    holder for the rbtree.

name
    name of the specific next header compression

nexthdr
    next header value of the protocol which should be compressed.

nexthdrlen
    ipv6 nexthdr len for the reserved space.

id
    array for nhc id. Note this need to be in network byteorder.

idmask
    *undescribed*

idlen
    *undescribed*

idsetup
    *undescribed*

uncompress
    callback to do the header uncompression.

compress
    callback to do the header compression.

.. _`lowpan_nhc_by_nexthdr`:

lowpan_nhc_by_nexthdr
=====================

.. c:function:: struct lowpan_nhc *lowpan_nhc_by_nexthdr(u8 nexthdr)

    return the 6lowpan nhc by ipv6 nexthdr.

    :param u8 nexthdr:
        ipv6 nexthdr value.

.. _`lowpan_nhc_check_compression`:

lowpan_nhc_check_compression
============================

.. c:function:: int lowpan_nhc_check_compression(struct sk_buff *skb, const struct ipv6hdr *hdr, u8 **hc_ptr)

    checks if we support compression format. If we support the nhc by nexthdr field, the function will return 0. If we don't support the nhc by nexthdr this function will return -ENOENT.

    :param struct sk_buff \*skb:
        skb of 6LoWPAN header to read nhc and replace header.

    :param const struct ipv6hdr \*hdr:
        ipv6hdr to check the nexthdr value

    :param u8 \*\*hc_ptr:
        pointer for 6LoWPAN header which should increment at the end of
        replaced header.

.. _`lowpan_nhc_do_compression`:

lowpan_nhc_do_compression
=========================

.. c:function:: int lowpan_nhc_do_compression(struct sk_buff *skb, const struct ipv6hdr *hdr, u8 **hc_ptr)

    calling compress callback for nhc

    :param struct sk_buff \*skb:
        skb of 6LoWPAN header to read nhc and replace header.

    :param const struct ipv6hdr \*hdr:
        ipv6hdr to set the nexthdr value

    :param u8 \*\*hc_ptr:
        pointer for 6LoWPAN header which should increment at the end of
        replaced header.

.. _`lowpan_nhc_do_uncompression`:

lowpan_nhc_do_uncompression
===========================

.. c:function:: int lowpan_nhc_do_uncompression(struct sk_buff *skb, const struct net_device *dev, struct ipv6hdr *hdr)

    calling uncompress callback for nhc

    :param struct sk_buff \*skb:
        skb of 6LoWPAN header, skb->data should be pointed to nhc id value.

    :param const struct net_device \*dev:
        netdevice for print logging information.

    :param struct ipv6hdr \*hdr:
        ipv6hdr for setting nexthdr value.

.. _`lowpan_nhc_add`:

lowpan_nhc_add
==============

.. c:function:: int lowpan_nhc_add(struct lowpan_nhc *nhc)

    register a next header compression to framework

    :param struct lowpan_nhc \*nhc:
        nhc which should be add.

.. _`lowpan_nhc_del`:

lowpan_nhc_del
==============

.. c:function:: void lowpan_nhc_del(struct lowpan_nhc *nhc)

    delete a next header compression from framework

    :param struct lowpan_nhc \*nhc:
        nhc which should be delete.

.. _`lowpan_nhc_init`:

lowpan_nhc_init
===============

.. c:function:: void lowpan_nhc_init( void)

    adding all default nhcs

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

