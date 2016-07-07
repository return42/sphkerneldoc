.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/dvb-usb/dib0700_devices.c

.. _`novatd_frontend_attach`:

novatd_frontend_attach
======================

.. c:function:: int novatd_frontend_attach(struct dvb_usb_adapter *adap)

    Nova-TD specific attach

    :param struct dvb_usb_adapter \*adap:
        *undescribed*

.. _`novatd_frontend_attach.description`:

Description
-----------

Nova-TD has GPIO0, 1 and 2 for LEDs. So do not fiddle with them except for
information purposes.

.. This file was automatic generated / don't edit.

