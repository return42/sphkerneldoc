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

.. _`wil_fw_process`:

wil_fw_process
==============

.. c:function:: int wil_fw_process(struct wil6210_priv *wil, const void *data, size_t size, bool load)

    process section from FW file

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param const void \*data:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param bool load:
        *undescribed*

.. _`wil_fw_process.if-load-is-true`:

if load is true
---------------

Load the FW and uCode code and data to the
corresponding device memory regions,
otherwise only parse and look for capabilities

Return error code

.. _`wil_request_firmware`:

wil_request_firmware
====================

.. c:function:: int wil_request_firmware(struct wil6210_priv *wil, const char *name, bool load)

    Request firmware

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param bool load:
        *undescribed*

.. _`wil_request_firmware.description`:

Description
-----------

Request firmware image from the file
If load is true, load firmware to device, otherwise
only parse and extract capabilities

Return error code

.. This file was automatic generated / don't edit.

