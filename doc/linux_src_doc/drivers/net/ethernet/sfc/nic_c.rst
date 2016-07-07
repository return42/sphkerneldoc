.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/nic.c

.. _`efx_nic_describe_stats`:

efx_nic_describe_stats
======================

.. c:function:: size_t efx_nic_describe_stats(const struct efx_hw_stat_desc *desc, size_t count, const unsigned long *mask, u8 *names)

    Describe supported statistics for ethtool

    :param const struct efx_hw_stat_desc \*desc:
        Array of \ :c:type:`struct efx_hw_stat_desc <efx_hw_stat_desc>`\  describing the statistics

    :param size_t count:
        Length of the \ ``desc``\  array

    :param const unsigned long \*mask:
        Bitmask of which elements of \ ``desc``\  are enabled

    :param u8 \*names:
        Buffer to copy names to, or \ ``NULL``\ .  The names are copied
        starting at intervals of \ ``ETH_GSTRING_LEN``\  bytes.

.. _`efx_nic_describe_stats.description`:

Description
-----------

Returns the number of visible statistics, i.e. the number of set
bits in the first \ ``count``\  bits of \ ``mask``\  for which a name is defined.

.. _`efx_nic_update_stats`:

efx_nic_update_stats
====================

.. c:function:: void efx_nic_update_stats(const struct efx_hw_stat_desc *desc, size_t count, const unsigned long *mask, u64 *stats, const void *dma_buf, bool accumulate)

    Convert statistics DMA buffer to array of u64

    :param const struct efx_hw_stat_desc \*desc:
        Array of \ :c:type:`struct efx_hw_stat_desc <efx_hw_stat_desc>`\  describing the DMA buffer
        layout.  DMA widths of 0, 16, 32 and 64 are supported; where
        the width is specified as 0 the corresponding element of
        \ ``stats``\  is not updated.

    :param size_t count:
        Length of the \ ``desc``\  array

    :param const unsigned long \*mask:
        Bitmask of which elements of \ ``desc``\  are enabled

    :param u64 \*stats:
        Buffer to update with the converted statistics.  The length
        of this array must be at least \ ``count``\ .

    :param const void \*dma_buf:
        DMA buffer containing hardware statistics

    :param bool accumulate:
        If set, the converted values will be added rather than
        directly stored to the corresponding elements of \ ``stats``\ 

.. This file was automatic generated / don't edit.

