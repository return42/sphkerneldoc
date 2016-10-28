.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/6lowpan.h

.. _`lowpan_fetch_skb`:

lowpan_fetch_skb
================

.. c:function:: bool lowpan_fetch_skb(struct sk_buff *skb, void *data, unsigned int len)

    getting inline data from 6LoWPAN header

    :param struct sk_buff \*skb:
        the buffer where the inline data should be pulled from.

    :param void \*data:
        destination buffer for the inline data.

    :param unsigned int len:
        amount of data which should be pulled in bytes.

.. _`lowpan_fetch_skb.description`:

Description
-----------

This function will pull data from sk buffer and put it into data to
remove the 6LoWPAN inline data. This function returns true if the
sk buffer is too small to pull the amount of data which is specified
by len.

.. _`lowpan_header_decompress`:

lowpan_header_decompress
========================

.. c:function:: int lowpan_header_decompress(struct sk_buff *skb, const struct net_device *dev, const void *daddr, const void *saddr)

    replace 6LoWPAN header with IPv6 header

    :param struct sk_buff \*skb:
        the buffer which should be manipulate.

    :param const struct net_device \*dev:
        the lowpan net device pointer.

    :param const void \*daddr:
        destination lladdr of mac header which is used for compression
        methods.

    :param const void \*saddr:
        source lladdr of mac header which is used for compression
        methods.

.. _`lowpan_header_decompress.description`:

Description
-----------

This function replaces the IPHC 6LoWPAN header which should be pointed at
skb->data and skb_network_header, with the IPv6 header.
It would be nice that the caller have the necessary headroom of IPv6 header
and greatest Transport layer header, this would reduce the overhead for
reallocate headroom.

.. _`lowpan_header_compress`:

lowpan_header_compress
======================

.. c:function:: int lowpan_header_compress(struct sk_buff *skb, const struct net_device *dev, const void *daddr, const void *saddr)

    replace IPv6 header with 6LoWPAN header

    :param struct sk_buff \*skb:
        the buffer which should be manipulate.

    :param const struct net_device \*dev:
        the lowpan net device pointer.

    :param const void \*daddr:
        destination lladdr of mac header which is used for compression
        methods.

    :param const void \*saddr:
        source lladdr of mac header which is used for compression
        methods.

.. _`lowpan_header_compress.description`:

Description
-----------

This function replaces the IPv6 header which should be pointed at
skb->data and skb_network_header, with the IPHC 6LoWPAN header.
The caller need to be sure that the sk buffer is not shared and at have
at least a headroom which is smaller or equal LOWPAN_IPHC_MAX_HEADER_LEN,
which is the IPHC "more bytes than IPv6 header" at worst case.

.. This file was automatic generated / don't edit.

