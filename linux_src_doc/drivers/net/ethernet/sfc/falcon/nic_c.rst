.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/nic.c

.. _`ef4_nic_describe_stats`:

ef4_nic_describe_stats
======================

.. c:function:: size_t ef4_nic_describe_stats(const struct ef4_hw_stat_desc *desc, size_t count, const unsigned long *mask, u8 *names)

    Describe supported statistics for ethtool

    :param desc:
        Array of \ :c:type:`struct ef4_hw_stat_desc <ef4_hw_stat_desc>`\  describing the statistics
    :type desc: const struct ef4_hw_stat_desc \*

    :param count:
        Length of the \ ``desc``\  array
    :type count: size_t

    :param mask:
        Bitmask of which elements of \ ``desc``\  are enabled
    :type mask: const unsigned long \*

    :param names:
        Buffer to copy names to, or \ ``NULL``\ .  The names are copied
        starting at intervals of \ ``ETH_GSTRING_LEN``\  bytes.
    :type names: u8 \*

.. _`ef4_nic_describe_stats.description`:

Description
-----------

Returns the number of visible statistics, i.e. the number of set
bits in the first \ ``count``\  bits of \ ``mask``\  for which a name is defined.

.. _`ef4_nic_update_stats`:

ef4_nic_update_stats
====================

.. c:function:: void ef4_nic_update_stats(const struct ef4_hw_stat_desc *desc, size_t count, const unsigned long *mask, u64 *stats, const void *dma_buf, bool accumulate)

    Convert statistics DMA buffer to array of u64

    :param desc:
        Array of \ :c:type:`struct ef4_hw_stat_desc <ef4_hw_stat_desc>`\  describing the DMA buffer
        layout.  DMA widths of 0, 16, 32 and 64 are supported; where
        the width is specified as 0 the corresponding element of
        \ ``stats``\  is not updated.
    :type desc: const struct ef4_hw_stat_desc \*

    :param count:
        Length of the \ ``desc``\  array
    :type count: size_t

    :param mask:
        Bitmask of which elements of \ ``desc``\  are enabled
    :type mask: const unsigned long \*

    :param stats:
        Buffer to update with the converted statistics.  The length
        of this array must be at least \ ``count``\ .
    :type stats: u64 \*

    :param dma_buf:
        DMA buffer containing hardware statistics
    :type dma_buf: const void \*

    :param accumulate:
        If set, the converted values will be added rather than
        directly stored to the corresponding elements of \ ``stats``\ 
    :type accumulate: bool

.. This file was automatic generated / don't edit.

