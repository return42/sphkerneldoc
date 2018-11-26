.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_core_main.c

.. _`qeth_send_control_data`:

qeth_send_control_data
======================

.. c:function:: int qeth_send_control_data(struct qeth_card *card, int len, struct qeth_cmd_buffer *iob, int (*reply_cb)(struct qeth_card *cb_card, struct qeth_reply *cb_reply, unsigned long cb_cmd), void *reply_param)

    send control command to the card

    :param card:
        qeth_card structure pointer
    :type card: struct qeth_card \*

    :param len:
        size of the command buffer
    :type len: int

    :param iob:
        qeth_cmd_buffer pointer
    :type iob: struct qeth_cmd_buffer \*

    :param int (\*reply_cb)(struct qeth_card \*cb_card, struct qeth_reply \*cb_reply, unsigned long cb_cmd):
        callback function pointer

    :param reply_param:
        private pointer passed to the callback
    :type reply_param: void \*

.. _`qeth_send_control_data.description`:

Description
-----------

Returns the value of the \`return_code' field of the response
block returned from the hardware, or other error indication.
Value of zero indicates successful execution of the command.

Callback function gets called one or more times, with cb_cmd
pointing to the response returned by the hardware. Callback
function must return non-zero if more reply blocks are expected,
and zero if the last or only reply block is received. Callback
function can get the value of the reply_param pointer from the
field 'param' of the structure qeth_reply.

.. _`qeth_send_ipa_cmd`:

qeth_send_ipa_cmd
=================

.. c:function:: int qeth_send_ipa_cmd(struct qeth_card *card, struct qeth_cmd_buffer *iob, int (*reply_cb)(struct qeth_card *, struct qeth_reply*, unsigned long), void *reply_param)

    send an IPA command

    :param card:
        *undescribed*
    :type card: struct qeth_card \*

    :param iob:
        *undescribed*
    :type iob: struct qeth_cmd_buffer \*

    :param int (\*reply_cb)(struct qeth_card \*, struct qeth_reply\*, unsigned long):
        *undescribed*

    :param reply_param:
        *undescribed*
    :type reply_param: void \*

.. _`qeth_send_ipa_cmd.description`:

Description
-----------

See \ :c:func:`qeth_send_control_data`\  for explanation of the arguments.

.. _`qeth_prep_flush_pack_buffer`:

qeth_prep_flush_pack_buffer
===========================

.. c:function:: int qeth_prep_flush_pack_buffer(struct qeth_qdio_out_q *queue)

    Prepares flushing of a packing buffer.

    :param queue:
        queue to check for packing buffer
    :type queue: struct qeth_qdio_out_q \*

.. _`qeth_prep_flush_pack_buffer.description`:

Description
-----------

Returns number of buffers that were prepared for flush.

.. _`qeth_get_priority_queue`:

qeth_get_priority_queue
=======================

.. c:function:: int qeth_get_priority_queue(struct qeth_card *card, struct sk_buff *skb, int ipv)

    Function assumes that we have 4 outbound queues.

    :param card:
        *undescribed*
    :type card: struct qeth_card \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param ipv:
        *undescribed*
    :type ipv: int

.. _`qeth_get_elements_for_frags`:

qeth_get_elements_for_frags
===========================

.. c:function:: int qeth_get_elements_for_frags(struct sk_buff *skb)

    find number of SBALEs for skb frags.

    :param skb:
        SKB address
    :type skb: struct sk_buff \*

.. _`qeth_get_elements_for_frags.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to cover
fragmented part of the SKB. Returns zero for linear SKB.

.. _`qeth_count_elements`:

qeth_count_elements
===================

.. c:function:: unsigned int qeth_count_elements(struct sk_buff *skb, unsigned int data_offset)

    Counts the number of QDIO buffer elements needed to transmit an skb.

    :param skb:
        the skb to operate on.
    :type skb: struct sk_buff \*

    :param data_offset:
        skip this part of the skb's linear data
    :type data_offset: unsigned int

.. _`qeth_count_elements.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to map the
skb's data (both its linear part and paged fragments).

.. _`qeth_add_hw_header`:

qeth_add_hw_header
==================

.. c:function:: int qeth_add_hw_header(struct qeth_card *card, struct sk_buff *skb, struct qeth_hdr **hdr, unsigned int hdr_len, unsigned int proto_len, unsigned int *elements)

    add a HW header to an skb.

    :param card:
        *undescribed*
    :type card: struct qeth_card \*

    :param skb:
        skb that the HW header should be added to.
    :type skb: struct sk_buff \*

    :param hdr:
        double pointer to a qeth_hdr. When returning with >= 0,
        it contains a valid pointer to a qeth_hdr.
    :type hdr: struct qeth_hdr \*\*

    :param hdr_len:
        length of the HW header.
    :type hdr_len: unsigned int

    :param proto_len:
        length of protocol headers that need to be in same page as the
        HW header.
    :type proto_len: unsigned int

    :param elements:
        *undescribed*
    :type elements: unsigned int \*

.. _`qeth_add_hw_header.description`:

Description
-----------

Returns the pushed length. If the header can't be pushed on
(eg. because it would cross a page boundary), it is allocated from
the cache instead and 0 is returned.
The number of needed buffer elements is returned in \ ``elements``\ .
Error to create the hdr is indicated by returning with < 0.

.. _`qeth_fill_buffer`:

qeth_fill_buffer
================

.. c:function:: int qeth_fill_buffer(struct qeth_qdio_out_q *queue, struct qeth_qdio_out_buffer *buf, struct sk_buff *skb, struct qeth_hdr *hdr, unsigned int offset, unsigned int hd_len)

    map skb into an output buffer

    :param queue:
        QDIO queue to submit the buffer on
    :type queue: struct qeth_qdio_out_q \*

    :param buf:
        buffer to transport the skb
    :type buf: struct qeth_qdio_out_buffer \*

    :param skb:
        skb to map into the buffer
    :type skb: struct sk_buff \*

    :param hdr:
        qeth_hdr for this skb. Either at skb->data, or allocated
        from qeth_core_header_cache.
    :type hdr: struct qeth_hdr \*

    :param offset:
        when mapping the skb, start at skb->data + offset
    :type offset: unsigned int

    :param hd_len:
        if > 0, build a dedicated header element of this size
    :type hd_len: unsigned int

.. _`qeth_vm_request_mac`:

qeth_vm_request_mac
===================

.. c:function:: int qeth_vm_request_mac(struct qeth_card *card)

    Request a hypervisor-managed MAC address

    :param card:
        pointer to a qeth_card
    :type card: struct qeth_card \*

.. _`qeth_vm_request_mac.description`:

Description
-----------

Returns
0, if a MAC address has been set for the card's netdevice
a return code, for various error conditions

.. _`qeth_enable_hw_features`:

qeth_enable_hw_features
=======================

.. c:function:: void qeth_enable_hw_features(struct net_device *dev)

    (Re-)Enable HW functions for device features

    :param dev:
        a net_device
    :type dev: struct net_device \*

.. This file was automatic generated / don't edit.

