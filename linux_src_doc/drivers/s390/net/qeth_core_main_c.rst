.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_core_main.c

.. _`qeth_send_control_data`:

qeth_send_control_data
======================

.. c:function:: int qeth_send_control_data(struct qeth_card *card, int len, struct qeth_cmd_buffer *iob, int (*reply_cb)(struct qeth_card *cb_card, struct qeth_reply *cb_reply, unsigned long cb_cmd), void *reply_param)

    send control command to the card

    :param struct qeth_card \*card:
        qeth_card structure pointer

    :param int len:
        size of the command buffer

    :param struct qeth_cmd_buffer \*iob:
        qeth_cmd_buffer pointer

    :param int (\*reply_cb)(struct qeth_card \*cb_card, struct qeth_reply \*cb_reply, unsigned long cb_cmd):
        callback function pointer

    :param void \*reply_param:
        private pointer passed to the callback

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

    :param struct qeth_card \*card:
        *undescribed*

    :param struct qeth_cmd_buffer \*iob:
        *undescribed*

    :param int (\*reply_cb)(struct qeth_card \*, struct qeth_reply\*, unsigned long):
        *undescribed*

    :param void \*reply_param:
        *undescribed*

.. _`qeth_send_ipa_cmd.description`:

Description
-----------

See \ :c:func:`qeth_send_control_data`\  for explanation of the arguments.

.. _`qeth_prep_flush_pack_buffer`:

qeth_prep_flush_pack_buffer
===========================

.. c:function:: int qeth_prep_flush_pack_buffer(struct qeth_qdio_out_q *queue)

    Prepares flushing of a packing buffer.

    :param struct qeth_qdio_out_q \*queue:
        queue to check for packing buffer

.. _`qeth_prep_flush_pack_buffer.description`:

Description
-----------

Returns number of buffers that were prepared for flush.

.. _`qeth_get_priority_queue`:

qeth_get_priority_queue
=======================

.. c:function:: int qeth_get_priority_queue(struct qeth_card *card, struct sk_buff *skb, int ipv, int cast_type)

    Function assumes that we have 4 outbound queues.

    :param struct qeth_card \*card:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param int ipv:
        *undescribed*

    :param int cast_type:
        *undescribed*

.. _`qeth_get_elements_for_frags`:

qeth_get_elements_for_frags
===========================

.. c:function:: int qeth_get_elements_for_frags(struct sk_buff *skb)

    find number of SBALEs for skb frags.

    :param struct sk_buff \*skb:
        SKB address

.. _`qeth_get_elements_for_frags.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to cover
fragmented part of the SKB. Returns zero for linear SKB.

.. _`qeth_get_elements_no`:

qeth_get_elements_no
====================

.. c:function:: int qeth_get_elements_no(struct qeth_card *card, struct sk_buff *skb, int extra_elems, int data_offset)

    find number of SBALEs for skb data, inc. frags.

    :param struct qeth_card \*card:
        qeth card structure, to check max. elems.

    :param struct sk_buff \*skb:
        SKB address

    :param int extra_elems:
        extra elems needed, to check against max.

    :param int data_offset:
        range starts at skb->data + data_offset

.. _`qeth_get_elements_no.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to cover
skb data, including linear part and fragments. Checks if the result plus
extra_elems fits under the limit for the card. Returns 0 if it does not.

.. _`qeth_get_elements_no.note`:

Note
----

extra_elems is not included in the returned result.

.. _`qeth_push_hdr`:

qeth_push_hdr
=============

.. c:function:: int qeth_push_hdr(struct sk_buff *skb, struct qeth_hdr **hdr, unsigned int len)

    push a qeth_hdr onto an skb.

    :param struct sk_buff \*skb:
        skb that the qeth_hdr should be pushed onto.

    :param struct qeth_hdr \*\*hdr:
        double pointer to a qeth_hdr. When returning with >= 0,
        it contains a valid pointer to a qeth_hdr.

    :param unsigned int len:
        length of the hdr that needs to be pushed on.

.. _`qeth_push_hdr.description`:

Description
-----------

Returns the pushed length. If the header can't be pushed on
(eg. because it would cross a page boundary), it is allocated from
the cache instead and 0 is returned.
Error to create the hdr is indicated by returning with < 0.

.. _`qeth_fill_buffer`:

qeth_fill_buffer
================

.. c:function:: int qeth_fill_buffer(struct qeth_qdio_out_q *queue, struct qeth_qdio_out_buffer *buf, struct sk_buff *skb, struct qeth_hdr *hdr, unsigned int offset, unsigned int hd_len)

    map skb into an output buffer

    :param struct qeth_qdio_out_q \*queue:
        QDIO queue to submit the buffer on

    :param struct qeth_qdio_out_buffer \*buf:
        buffer to transport the skb

    :param struct sk_buff \*skb:
        skb to map into the buffer

    :param struct qeth_hdr \*hdr:
        qeth_hdr for this skb. Either at skb->data, or allocated
        from qeth_core_header_cache.

    :param unsigned int offset:
        when mapping the skb, start at skb->data + offset

    :param unsigned int hd_len:
        if > 0, build a dedicated header element of this size

.. _`qeth_vm_request_mac`:

qeth_vm_request_mac
===================

.. c:function:: int qeth_vm_request_mac(struct qeth_card *card)

    Request a hypervisor-managed MAC address

    :param struct qeth_card \*card:
        pointer to a qeth_card

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

    :param struct net_device \*dev:
        a net_device

.. This file was automatic generated / don't edit.

