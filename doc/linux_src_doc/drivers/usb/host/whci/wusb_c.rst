.. -*- coding: utf-8; mode: rst -*-

======
wusb.c
======


.. _`whc_set_ptk`:

whc_set_ptk
===========

.. c:function:: int whc_set_ptk (struct wusbhc *wusbhc, u8 port_idx, u32 tkid, const void *ptk, size_t key_size)

    set the PTK to use for a device.

    :param struct wusbhc \*wusbhc:

        *undescribed*

    :param u8 port_idx:

        *undescribed*

    :param u32 tkid:

        *undescribed*

    :param const void \*ptk:

        *undescribed*

    :param size_t key_size:

        *undescribed*



.. _`whc_set_ptk.description`:

Description
-----------


The index into the key table for this PTK is the same as the
device's port index.



.. _`whc_set_gtk`:

whc_set_gtk
===========

.. c:function:: int whc_set_gtk (struct wusbhc *wusbhc, u32 tkid, const void *gtk, size_t key_size)

    set the GTK for subsequent broadcast packets

    :param struct wusbhc \*wusbhc:

        *undescribed*

    :param u32 tkid:

        *undescribed*

    :param const void \*gtk:

        *undescribed*

    :param size_t key_size:

        *undescribed*



.. _`whc_set_gtk.description`:

Description
-----------


The GTK is stored in the last entry in the key table (the previous
N_DEVICES entries are for the per-device PTKs).

