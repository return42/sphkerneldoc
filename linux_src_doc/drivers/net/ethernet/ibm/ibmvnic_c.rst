.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ibm/ibmvnic.c

.. _`build_hdr_data`:

build_hdr_data
==============

.. c:function:: int build_hdr_data(u8 hdr_field, struct sk_buff *skb, int *hdr_len, u8 *hdr_data)

    creates L2/L3/L4 header data buffer \ ``hdr_field``\  - bitfield determining needed headers \ ``skb``\  - socket buffer \ ``hdr_len``\  - array of header lengths \ ``tot_len``\  - total length of data

    :param u8 hdr_field:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param int \*hdr_len:
        *undescribed*

    :param u8 \*hdr_data:
        *undescribed*

.. _`build_hdr_data.description`:

Description
-----------

Reads hdr_field to determine which headers are needed by firmware.
Builds a buffer containing these headers.  Saves individual header
lengths and total buffer length to be used to build descriptors.

.. _`create_hdr_descs`:

create_hdr_descs
================

.. c:function:: void create_hdr_descs(u8 hdr_field, u8 *hdr_data, int len, int *hdr_len, union sub_crq *scrq_arr)

    create header and header extension descriptors \ ``hdr_field``\  - bitfield determining needed headers \ ``data``\  - buffer containing header data \ ``len``\  - length of data buffer \ ``hdr_len``\  - array of individual header lengths \ ``scrq_arr``\  - descriptor array

    :param u8 hdr_field:
        *undescribed*

    :param u8 \*hdr_data:
        *undescribed*

    :param int len:
        *undescribed*

    :param int \*hdr_len:
        *undescribed*

    :param union sub_crq \*scrq_arr:
        *undescribed*

.. _`create_hdr_descs.description`:

Description
-----------

Creates header and, if needed, header extension descriptors and
places them in a descriptor array, scrq_arr

.. _`build_hdr_descs_arr`:

build_hdr_descs_arr
===================

.. c:function:: void build_hdr_descs_arr(struct ibmvnic_tx_buff *txbuff, int *num_entries, u8 hdr_field)

    build a header descriptor array \ ``skb``\  - socket buffer \ ``num_entries``\  - number of descriptors to be sent \ ``subcrq``\  - first TX descriptor \ ``hdr_field``\  - bit field determining which headers will be sent

    :param struct ibmvnic_tx_buff \*txbuff:
        *undescribed*

    :param int \*num_entries:
        *undescribed*

    :param u8 hdr_field:
        *undescribed*

.. _`build_hdr_descs_arr.description`:

Description
-----------

This function will build a TX descriptor array with applicable
L2/L3/L4 packet header descriptors to be sent by send_subcrq_indirect.

.. This file was automatic generated / don't edit.

