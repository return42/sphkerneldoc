.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/debug.h

.. _`ubi_dbg_is_bgt_disabled`:

ubi_dbg_is_bgt_disabled
=======================

.. c:function:: int ubi_dbg_is_bgt_disabled(const struct ubi_device *ubi)

    if the background thread is disabled.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

.. _`ubi_dbg_is_bgt_disabled.description`:

Description
-----------

Returns non-zero if the UBI background thread is disabled for testing
purposes.

.. _`ubi_dbg_is_bitflip`:

ubi_dbg_is_bitflip
==================

.. c:function:: int ubi_dbg_is_bitflip(const struct ubi_device *ubi)

    if it is time to emulate a bit-flip.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

.. _`ubi_dbg_is_bitflip.description`:

Description
-----------

Returns non-zero if a bit-flip should be emulated, otherwise returns zero.

.. _`ubi_dbg_is_write_failure`:

ubi_dbg_is_write_failure
========================

.. c:function:: int ubi_dbg_is_write_failure(const struct ubi_device *ubi)

    if it is time to emulate a write failure.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

.. _`ubi_dbg_is_write_failure.description`:

Description
-----------

Returns non-zero if a write failure should be emulated, otherwise returns
zero.

.. _`ubi_dbg_is_erase_failure`:

ubi_dbg_is_erase_failure
========================

.. c:function:: int ubi_dbg_is_erase_failure(const struct ubi_device *ubi)

    if its time to emulate an erase failure.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

.. _`ubi_dbg_is_erase_failure.description`:

Description
-----------

Returns non-zero if an erase failure should be emulated, otherwise returns
zero.

.. This file was automatic generated / don't edit.

