.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/firmware.c

.. _`lbs_get_firmware_async`:

lbs_get_firmware_async
======================

.. c:function:: int lbs_get_firmware_async(struct lbs_private *priv, struct device *device, u32 card_model, const struct lbs_fw_table *fw_table, lbs_fw_cb callback)

    Retrieves firmware asynchronously. Can load either a helper firmware and a main firmware (2-stage), or just the helper.

    :param priv:
        Pointer to lbs_private instance
    :type priv: struct lbs_private \*

    :param device:
        *undescribed*
    :type device: struct device \*

    :param card_model:
        Bus-specific card model ID used to filter firmware table
        elements
    :type card_model: u32

    :param fw_table:
        Table of firmware file names and device model numbers
        terminated by an entry with a NULL helper name
    :type fw_table: const struct lbs_fw_table \*

    :param callback:
        User callback to invoke when firmware load succeeds or fails.
    :type callback: lbs_fw_cb

.. _`lbs_get_firmware`:

lbs_get_firmware
================

.. c:function:: int lbs_get_firmware(struct device *dev, u32 card_model, const struct lbs_fw_table *fw_table, const struct firmware **helper, const struct firmware **mainfw)

    Retrieves two-stage firmware

    :param dev:
        A pointer to \ :c:type:`struct device <device>`\  structure
    :type dev: struct device \*

    :param card_model:
        Bus-specific card model ID used to filter firmware table
        elements
    :type card_model: u32

    :param fw_table:
        Table of firmware file names and device model numbers
        terminated by an entry with a NULL helper name
    :type fw_table: const struct lbs_fw_table \*

    :param helper:
        On success, the helper firmware; caller must free
    :type helper: const struct firmware \*\*

    :param mainfw:
        On success, the main firmware; caller must free
    :type mainfw: const struct firmware \*\*

.. _`lbs_get_firmware.deprecated`:

Deprecated
----------

use \ :c:func:`lbs_get_firmware_async`\  instead.

.. _`lbs_get_firmware.return`:

Return
------

0 on success, non-zero on failure

.. This file was automatic generated / don't edit.

