.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/digital_core.c

.. _`digital_start_poll`:

digital_start_poll
==================

.. c:function:: int digital_start_poll(struct nfc_dev *nfc_dev, __u32 im_protocols, __u32 tm_protocols)

    :param struct nfc_dev \*nfc_dev:
        *undescribed*

    :param __u32 im_protocols:
        *undescribed*

    :param __u32 tm_protocols:
        *undescribed*

.. _`digital_start_poll.description`:

Description
-----------

For every supported protocol, the corresponding polling function is added
to the table of polling technologies (ddev->poll_techs[]) using
\ :c:func:`digital_add_poll_tech`\ .
When a polling function fails (by timeout or protocol error) the next one is
schedule by \ :c:func:`digital_poll_next_tech`\  on the poll workqueue (ddev->poll_work).

.. This file was automatic generated / don't edit.

