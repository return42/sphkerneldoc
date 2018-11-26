.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ibm/ibmvnic.c

.. _`build_hdr_data`:

build_hdr_data
==============

.. c:function:: int build_hdr_data(u8 hdr_field, struct sk_buff *skb, int *hdr_len, u8 *hdr_data)

    creates L2/L3/L4 header data buffer \ ``hdr_field``\  - bitfield determining needed headers \ ``skb``\  - socket buffer \ ``hdr_len``\  - array of header lengths \ ``tot_len``\  - total length of data

    :param hdr_field:
        *undescribed*
    :type hdr_field: u8

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param hdr_len:
        *undescribed*
    :type hdr_len: int \*

    :param hdr_data:
        *undescribed*
    :type hdr_data: u8 \*

.. _`build_hdr_data.description`:

Description
-----------

Reads hdr_field to determine which headers are needed by firmware.
Builds a buffer containing these headers.  Saves individual header
lengths and total buffer length to be used to build descriptors.

.. _`create_hdr_descs`:

create_hdr_descs
================

.. c:function:: int create_hdr_descs(u8 hdr_field, u8 *hdr_data, int len, int *hdr_len, union sub_crq *scrq_arr)

    create header and header extension descriptors \ ``hdr_field``\  - bitfield determining needed headers \ ``data``\  - buffer containing header data \ ``len``\  - length of data buffer \ ``hdr_len``\  - array of individual header lengths \ ``scrq_arr``\  - descriptor array

    :param hdr_field:
        *undescribed*
    :type hdr_field: u8

    :param hdr_data:
        *undescribed*
    :type hdr_data: u8 \*

    :param len:
        *undescribed*
    :type len: int

    :param hdr_len:
        *undescribed*
    :type hdr_len: int \*

    :param scrq_arr:
        *undescribed*
    :type scrq_arr: union sub_crq \*

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

    :param txbuff:
        *undescribed*
    :type txbuff: struct ibmvnic_tx_buff \*

    :param num_entries:
        *undescribed*
    :type num_entries: int \*

    :param hdr_field:
        *undescribed*
    :type hdr_field: u8

.. _`build_hdr_descs_arr.description`:

Description
-----------

This function will build a TX descriptor array with applicable
L2/L3/L4 packet header descriptors to be sent by send_subcrq_indirect.

.. _`do_reset`:

do_reset
========

.. c:function:: int do_reset(struct ibmvnic_adapter *adapter, struct ibmvnic_rwi *rwi, u32 reset_state)

    non-zero if we hit a fatal error and must halt.

    :param adapter:
        *undescribed*
    :type adapter: struct ibmvnic_adapter \*

    :param rwi:
        *undescribed*
    :type rwi: struct ibmvnic_rwi \*

    :param reset_state:
        *undescribed*
    :type reset_state: u32

.. This file was automatic generated / don't edit.

