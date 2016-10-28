.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/orinoco/orinoco_usb.c

.. _`ezusb_req_queue_run`:

ezusb_req_queue_run
===================

.. c:function:: void ezusb_req_queue_run(struct ezusb_priv *upriv)

    :param struct ezusb_priv \*upriv:
        *undescribed*

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

    :param struct ezusb_packet \*req:
        *undescribed*

    :param u16 length:
        *undescribed*

    :param u16 rid:
        *undescribed*

    :param const void \*data:
        *undescribed*

    :param u16 frame_type:
        *undescribed*

    :param u8 reply_count:
        *undescribed*

.. _`ezusb_fill_req.description`:

Description
-----------

if data == NULL and length > 0 the data is assumed to be already in
the target buffer and only the header is filled.

.. This file was automatic generated / don't edit.

