.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_ethtool.c

.. _`bnx2x_read_pages_regs`:

bnx2x_read_pages_regs
=====================

.. c:function:: void bnx2x_read_pages_regs(struct bnx2x *bp, u32 *p, u32 preset)

    read "paged" registers

    :param bp:
        *undescribed*
    :type bp: struct bnx2x \*

    :param p:
        *undescribed*
    :type p: u32 \*

    :param preset:
        *undescribed*
    :type preset: u32

.. _`bnx2x_read_pages_regs.description`:

Description
-----------

\ ``bp``\           device handle
\ ``p``\            output buffer

Reads "paged" memories: memories that may only be read by first writing to a
specific address ("write address") and then reading from a specific address
("read address"). There may be more than one write address per "page" and
more than one read address per write address.

.. _`bnx2x_get_channels`:

bnx2x_get_channels
==================

.. c:function:: void bnx2x_get_channels(struct net_device *dev, struct ethtool_channels *channels)

    gets the number of RSS queues.

    :param dev:
        net device
    :type dev: struct net_device \*

    :param channels:
        returns the number of max / current queues
    :type channels: struct ethtool_channels \*

.. _`bnx2x_change_num_queues`:

bnx2x_change_num_queues
=======================

.. c:function:: void bnx2x_change_num_queues(struct bnx2x *bp, int num_rss)

    change the number of RSS queues.

    :param bp:
        bnx2x private structure
    :type bp: struct bnx2x \*

    :param num_rss:
        *undescribed*
    :type num_rss: int

.. _`bnx2x_change_num_queues.description`:

Description
-----------

Re-configure interrupt mode to get the new number of MSI-X
vectors and re-add NAPI objects.

.. _`bnx2x_set_channels`:

bnx2x_set_channels
==================

.. c:function:: int bnx2x_set_channels(struct net_device *dev, struct ethtool_channels *channels)

    sets the number of RSS queues.

    :param dev:
        net device
    :type dev: struct net_device \*

    :param channels:
        includes the number of queues requested
    :type channels: struct ethtool_channels \*

.. This file was automatic generated / don't edit.

