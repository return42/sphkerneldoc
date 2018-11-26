.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/c67x00/c67x00-hcd.c

.. _`c67x00_hcd_irq`:

c67x00_hcd_irq
==============

.. c:function:: void c67x00_hcd_irq(struct c67x00_sie *sie, u16 int_status, u16 msg)

    :param sie:
        *undescribed*
    :type sie: struct c67x00_sie \*

    :param int_status:
        *undescribed*
    :type int_status: u16

    :param msg:
        *undescribed*
    :type msg: u16

.. _`c67x00_hcd_irq.description`:

Description
-----------

This function is called from the interrupt handler in c67x00-drv.c

.. _`c67x00_hcd_start`:

c67x00_hcd_start
================

.. c:function:: int c67x00_hcd_start(struct usb_hcd *hcd)

    Host controller start hook

    :param hcd:
        *undescribed*
    :type hcd: struct usb_hcd \*

.. _`c67x00_hcd_stop`:

c67x00_hcd_stop
===============

.. c:function:: void c67x00_hcd_stop(struct usb_hcd *hcd)

    Host controller stop hook

    :param hcd:
        *undescribed*
    :type hcd: struct usb_hcd \*

.. This file was automatic generated / don't edit.

