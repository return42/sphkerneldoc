.. -*- coding: utf-8; mode: rst -*-

========
smsusb.c
========



.. _xref_smsusb_onresponse:

smsusb_onresponse
=================

.. c:function:: void smsusb_onresponse (struct urb * urb)

    top half (interrupt context) adds completing sms urb to the global surbs list and activtes the worker thread the surb IMPORTANT - blocking functions must not be called from here !!! @param urb pointer to a completing urb object

    :param struct urb * urb:

        _undescribed_


