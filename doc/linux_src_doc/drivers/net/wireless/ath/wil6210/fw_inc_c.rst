.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/fw_inc.c

.. _`wil_fw_verify`:

wil_fw_verify
=============

.. c:function:: int wil_fw_verify(struct wil6210_priv *wil, const u8 *data, size_t size)

    verify firmware file validity

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param const u8 \*data:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`wil_fw_verify.description`:

Description
-----------

perform various checks for the firmware file header.
records are not validated.

Return file size or negative error

.. _`wil_fw_load`:

wil_fw_load
===========

.. c:function:: int wil_fw_load(struct wil6210_priv *wil, const void *data, size_t size)

    load FW into device

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param const void \*data:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`wil_fw_load.description`:

Description
-----------

Load the FW and uCode code and data to the corresponding device
memory regions

Return error code

.. _`wil_request_firmware`:

wil_request_firmware
====================

.. c:function:: int wil_request_firmware(struct wil6210_priv *wil, const char *name)

    Request firmware and load to device

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`wil_request_firmware.description`:

Description
-----------

Request firmware image from the file and load it to device

Return error code

.. This file was automatic generated / don't edit.

