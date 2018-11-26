.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/fw_inc.c

.. _`wil_fw_verify`:

wil_fw_verify
=============

.. c:function:: int wil_fw_verify(struct wil6210_priv *wil, const u8 *data, size_t size)

    verify firmware file validity

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param data:
        *undescribed*
    :type data: const u8 \*

    :param size:
        *undescribed*
    :type size: size_t

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

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param data:
        *undescribed*
    :type data: const void \*

    :param size:
        *undescribed*
    :type size: size_t

    :param load:
        *undescribed*
    :type load: bool

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

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param name:
        *undescribed*
    :type name: const char \*

    :param load:
        *undescribed*
    :type load: bool

.. _`wil_request_firmware.description`:

Description
-----------

Request firmware image from the file
If load is true, load firmware to device, otherwise
only parse and extract capabilities

Return error code

.. _`wil_brd_process`:

wil_brd_process
===============

.. c:function:: int wil_brd_process(struct wil6210_priv *wil, const void *data, size_t size)

    process section from BRD file

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param data:
        *undescribed*
    :type data: const void \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`wil_brd_process.description`:

Description
-----------

Return error code

.. _`wil_request_board`:

wil_request_board
=================

.. c:function:: int wil_request_board(struct wil6210_priv *wil, const char *name)

    Request board file

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param name:
        *undescribed*
    :type name: const char \*

.. _`wil_request_board.description`:

Description
-----------

Request board image from the file
board file address and max size are read from FW file
during initialization.
brd file shall include one header and one data section.

Return error code

.. _`wil_fw_verify_file_exists`:

wil_fw_verify_file_exists
=========================

.. c:function:: bool wil_fw_verify_file_exists(struct wil6210_priv *wil, const char *name)

    checks if firmware file exist

    :param wil:
        driver context
    :type wil: struct wil6210_priv \*

    :param name:
        firmware file name
    :type name: const char \*

.. _`wil_fw_verify_file_exists.description`:

Description
-----------

return value - boolean, true for success, false for failure

.. This file was automatic generated / don't edit.

