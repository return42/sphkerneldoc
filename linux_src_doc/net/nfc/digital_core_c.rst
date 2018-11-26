.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/digital_core.c

.. _`digital_start_poll`:

digital_start_poll
==================

.. c:function:: int digital_start_poll(struct nfc_dev *nfc_dev, __u32 im_protocols, __u32 tm_protocols)

    :param nfc_dev:
        *undescribed*
    :type nfc_dev: struct nfc_dev \*

    :param im_protocols:
        *undescribed*
    :type im_protocols: __u32

    :param tm_protocols:
        *undescribed*
    :type tm_protocols: __u32

.. _`digital_start_poll.description`:

Description
-----------

For every supported protocol, the corresponding polling function is added
to the table of polling technologies (ddev->poll_techs[]) using
\ :c:func:`digital_add_poll_tech`\ .
When a polling function fails (by timeout or protocol error) the next one is
schedule by \ :c:func:`digital_poll_next_tech`\  on the poll workqueue (ddev->poll_work).

.. This file was automatic generated / don't edit.

