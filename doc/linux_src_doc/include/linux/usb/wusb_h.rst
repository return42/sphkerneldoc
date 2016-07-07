.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/wusb.h

.. _`wuie_elt_max`:

WUIE_ELT_MAX
============

.. c:function::  WUIE_ELT_MAX()

.. _`wuie_elt_max.description`:

Description
-----------

WUSB1.0[7.5 before table 7-38] says that in WUSB IEs that
are "arrays" have to limited to 4 elements. So we define it
like that to ease up and submit only the neeed size.

.. _`wusb_key_index`:

wusb_key_index
==============

.. c:function:: u8 wusb_key_index(int index, int type, int originator)

    the host or the device.

    :param int index:
        *undescribed*

    :param int type:
        *undescribed*

    :param int originator:
        *undescribed*

.. This file was automatic generated / don't edit.

