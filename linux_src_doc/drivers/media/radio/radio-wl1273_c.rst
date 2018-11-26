.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/radio/radio-wl1273.c

.. _`wl1273_fm_upload_firmware_patch`:

wl1273_fm_upload_firmware_patch
===============================

.. c:function:: int wl1273_fm_upload_firmware_patch(struct wl1273_device *radio)

    Upload the firmware.

    :param radio:
        A pointer to the device struct.
    :type radio: struct wl1273_device \*

.. _`wl1273_fm_upload_firmware_patch.description`:

Description
-----------

The firmware file consists of arrays of bytes where the first byte
gives the array length. The first byte in the file gives the
number of these arrays.

.. _`wl1273_fm_get_tx_ctune`:

wl1273_fm_get_tx_ctune
======================

.. c:function:: unsigned int wl1273_fm_get_tx_ctune(struct wl1273_device *radio)

    Get the TX tuning capacitor value.

    :param radio:
        A pointer to the device struct.
    :type radio: struct wl1273_device \*

.. _`wl1273_fm_set_preemphasis`:

wl1273_fm_set_preemphasis
=========================

.. c:function:: int wl1273_fm_set_preemphasis(struct wl1273_device *radio, unsigned int preemphasis)

    Set the TX pre-emphasis value.

    :param radio:
        A pointer to the device struct.
    :type radio: struct wl1273_device \*

    :param preemphasis:
        The new pre-amphasis value.
    :type preemphasis: unsigned int

.. _`wl1273_fm_set_preemphasis.description`:

Description
-----------

Possible pre-emphasis values are: V4L2_PREEMPHASIS_DISABLED,
V4L2_PREEMPHASIS_50_uS and V4L2_PREEMPHASIS_75_uS.

.. _`wl1273_fm_set_tx_power`:

wl1273_fm_set_tx_power
======================

.. c:function:: int wl1273_fm_set_tx_power(struct wl1273_device *radio, u16 power)

    Set the transmission power value.

    :param radio:
        A pointer to the device struct.
    :type radio: struct wl1273_device \*

    :param power:
        The new power value.
    :type power: u16

.. This file was automatic generated / don't edit.

