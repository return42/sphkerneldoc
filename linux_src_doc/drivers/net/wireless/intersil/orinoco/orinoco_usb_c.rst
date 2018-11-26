.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/orinoco/orinoco_usb.c

.. _`ezusb_req_queue_run`:

ezusb_req_queue_run
===================

.. c:function:: void ezusb_req_queue_run(struct ezusb_priv *upriv)

    :param upriv:
        *undescribed*
    :type upriv: struct ezusb_priv \*

.. _`ezusb_req_queue_run.note`:

Note
----

Only one active CTX at any one time, because there's no
other (reliable) way to match the response URB to the correct
CTX.

.. _`ezusb_fill_req`:

ezusb_fill_req
==============

.. c:function:: int ezusb_fill_req(struct ezusb_packet *req, u16 length, u16 rid, const void *data, u16 frame_type, u8 reply_count)

    :param req:
        *undescribed*
    :type req: struct ezusb_packet \*

    :param length:
        *undescribed*
    :type length: u16

    :param rid:
        *undescribed*
    :type rid: u16

    :param data:
        *undescribed*
    :type data: const void \*

    :param frame_type:
        *undescribed*
    :type frame_type: u16

    :param reply_count:
        *undescribed*
    :type reply_count: u8

.. _`ezusb_fill_req.description`:

Description
-----------

if data == NULL and length > 0 the data is assumed to be already in
the target buffer and only the header is filled.

.. This file was automatic generated / don't edit.

