.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3vf/hclgevf_main.c

.. _`hclgevf_get_channels`:

hclgevf_get_channels
====================

.. c:function:: void hclgevf_get_channels(struct hnae3_handle *handle, struct ethtool_channels *ch)

    Get the current channels enabled and max supported.

    :param handle:
        hardware information for network interface
    :type handle: struct hnae3_handle \*

    :param ch:
        ethtool channels structure
    :type ch: struct ethtool_channels \*

.. _`hclgevf_get_channels.description`:

Description
-----------

We don't support separate tx and rx queues as channels. The other count
represents how many queues are being used for control. max_combined counts
how many queue pairs we can support. They may not be mapped 1 to 1 with
q_vectors since we support a lot more queue pairs than q_vectors.

.. This file was automatic generated / don't edit.

