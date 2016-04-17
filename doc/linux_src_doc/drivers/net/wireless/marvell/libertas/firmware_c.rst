.. -*- coding: utf-8; mode: rst -*-

==========
firmware.c
==========


.. _`lbs_get_firmware_async`:

lbs_get_firmware_async
======================

.. c:function:: int lbs_get_firmware_async (struct lbs_private *priv, struct device *device, u32 card_model, const struct lbs_fw_table *fw_table, lbs_fw_cb callback)

    Retrieves firmware asynchronously. Can load either a helper firmware and a main firmware (2-stage), or just the helper.

    :param struct lbs_private \*priv:
        Pointer to lbs_private instance

    :param struct device \*device:

        *undescribed*

    :param u32 card_model:
        Bus-specific card model ID used to filter firmware table
        elements

    :param const struct lbs_fw_table \*fw_table:
        Table of firmware file names and device model numbers
        terminated by an entry with a NULL helper name

    :param lbs_fw_cb callback:
        User callback to invoke when firmware load succeeds or fails.



.. _`lbs_get_firmware`:

lbs_get_firmware
================

.. c:function:: int lbs_get_firmware (struct device *dev, u32 card_model, const struct lbs_fw_table *fw_table, const struct firmware **helper, const struct firmware **mainfw)

    Retrieves two-stage firmware

    :param struct device \*dev:
        A pointer to :c:type:`struct device <device>` structure

    :param u32 card_model:
        Bus-specific card model ID used to filter firmware table
        elements

    :param const struct lbs_fw_table \*fw_table:
        Table of firmware file names and device model numbers
        terminated by an entry with a NULL helper name

    :param const struct firmware \*\*helper:
        On success, the helper firmware; caller must free

    :param const struct firmware \*\*mainfw:
        On success, the main firmware; caller must free



.. _`lbs_get_firmware.deprecated`:

Deprecated
----------

use :c:func:`lbs_get_firmware_async` instead.



.. _`lbs_get_firmware.returns`:

returns
-------

0 on success, non-zero on failure

