.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/wusb.c

.. _`whc_set_ptk`:

whc_set_ptk
===========

.. c:function:: int whc_set_ptk(struct wusbhc *wusbhc, u8 port_idx, u32 tkid, const void *ptk, size_t key_size)

    set the PTK to use for a device.

    :param wusbhc:
        *undescribed*
    :type wusbhc: struct wusbhc \*

    :param port_idx:
        *undescribed*
    :type port_idx: u8

    :param tkid:
        *undescribed*
    :type tkid: u32

    :param ptk:
        *undescribed*
    :type ptk: const void \*

    :param key_size:
        *undescribed*
    :type key_size: size_t

.. _`whc_set_ptk.description`:

Description
-----------

The index into the key table for this PTK is the same as the
device's port index.

.. _`whc_set_gtk`:

whc_set_gtk
===========

.. c:function:: int whc_set_gtk(struct wusbhc *wusbhc, u32 tkid, const void *gtk, size_t key_size)

    set the GTK for subsequent broadcast packets

    :param wusbhc:
        *undescribed*
    :type wusbhc: struct wusbhc \*

    :param tkid:
        *undescribed*
    :type tkid: u32

    :param gtk:
        *undescribed*
    :type gtk: const void \*

    :param key_size:
        *undescribed*
    :type key_size: size_t

.. _`whc_set_gtk.description`:

Description
-----------

The GTK is stored in the last entry in the key table (the previous
N_DEVICES entries are for the per-device PTKs).

.. This file was automatic generated / don't edit.

