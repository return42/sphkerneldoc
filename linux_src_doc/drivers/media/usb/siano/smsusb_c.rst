.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/siano/smsusb.c

.. _`do_submit_urb`:

do_submit_urb
=============

.. c:function:: void do_submit_urb(struct work_struct *work)

    bottom half (proccess context) submits the URB prepared on \ :c:func:`smsusb_onresponse`\ 

    :param struct work_struct \*work:
        *undescribed*

.. _`smsusb_onresponse`:

smsusb_onresponse
=================

.. c:function:: void smsusb_onresponse(struct urb *urb)

    top half (interrupt context) adds completing sms urb to the global surbs list and activtes the worker thread the surb IMPORTANT - blocking functions must not be called from here !!! \ ``param``\  urb pointer to a completing urb object

    :param struct urb \*urb:
        *undescribed*

.. This file was automatic generated / don't edit.

