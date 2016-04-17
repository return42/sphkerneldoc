.. -*- coding: utf-8; mode: rst -*-

================
qeth_core_main.c
================


.. _`qeth_send_control_data`:

qeth_send_control_data
======================

.. c:function:: int qeth_send_control_data (struct qeth_card *card, int len, struct qeth_cmd_buffer *iob, int (*reply_cb) (struct qeth_card *cb_card, struct qeth_reply *cb_reply, unsigned long cb_cmd, void *reply_param)

    send control command to the card

    :param struct qeth_card \*card:
        qeth_card structure pointer

    :param int len:
        size of the command buffer

    :param struct qeth_cmd_buffer \*iob:
        qeth_cmd_buffer pointer

    :param int (\*reply_cb) (struct qeth_card \*cb_card, struct qeth_reply \*cb_reply, unsigned long cb_cmd):
        callback function pointer

    :param void \*reply_param:
        private pointer passed to the callback



.. _`qeth_send_control_data.description`:

Description
-----------

Returns the value of the `return_code' field of the response
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

.. c:function:: int qeth_send_ipa_cmd (struct qeth_card *card, struct qeth_cmd_buffer *iob, int (*reply_cb) (struct qeth_card *, struct qeth_reply*, unsigned long, void *reply_param)

    send an IPA command

    :param struct qeth_card \*card:

        *undescribed*

    :param struct qeth_cmd_buffer \*iob:

        *undescribed*

    :param int (\*reply_cb) (struct qeth_card \*, struct qeth_reply\*, unsigned long):

        *undescribed*

    :param void \*reply_param:

        *undescribed*



.. _`qeth_send_ipa_cmd.description`:

Description
-----------


See :c:func:`qeth_send_control_data` for explanation of the arguments.



.. _`qeth_get_priority_queue`:

qeth_get_priority_queue
=======================

.. c:function:: int qeth_get_priority_queue (struct qeth_card *card, struct sk_buff *skb, int ipv, int cast_type)

    :param struct qeth_card \*card:

        *undescribed*

    :param struct sk_buff \*skb:

        *undescribed*

    :param int ipv:

        *undescribed*

    :param int cast_type:

        *undescribed*

