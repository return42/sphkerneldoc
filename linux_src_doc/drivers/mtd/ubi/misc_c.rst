.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/misc.c

.. _`ubi_calc_data_len`:

ubi_calc_data_len
=================

.. c:function:: int ubi_calc_data_len(const struct ubi_device *ubi, const void *buf, int length)

    calculate how much real data is stored in a buffer.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param buf:
        a buffer with the contents of the physical eraseblock
    :type buf: const void \*

    :param length:
        the buffer length
    :type length: int

.. _`ubi_calc_data_len.description`:

Description
-----------

This function calculates how much "real data" is stored in \ ``buf``\  and returnes
the length. Continuous 0xFF bytes at the end of the buffer are not
considered as "real data".

.. _`ubi_check_volume`:

ubi_check_volume
================

.. c:function:: int ubi_check_volume(struct ubi_device *ubi, int vol_id)

    check the contents of a static volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        ID of the volume to check
    :type vol_id: int

.. _`ubi_check_volume.description`:

Description
-----------

This function checks if static volume \ ``vol_id``\  is corrupted by fully reading
it and checking data CRC. This function returns \ ``0``\  if the volume is not
corrupted, \ ``1``\  if it is corrupted and a negative error code in case of
failure. Dynamic volumes are not checked and zero is returned immediately.

.. _`ubi_update_reserved`:

ubi_update_reserved
===================

.. c:function:: void ubi_update_reserved(struct ubi_device *ubi)

    update bad eraseblock handling accounting data.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_update_reserved.description`:

Description
-----------

This function calculates the gap between current number of PEBs reserved for
bad eraseblock handling and the required level of PEBs that must be
reserved, and if necessary, reserves more PEBs to fill that gap, according
to availability. Should be called with ubi->volumes_lock held.

.. _`ubi_calculate_reserved`:

ubi_calculate_reserved
======================

.. c:function:: void ubi_calculate_reserved(struct ubi_device *ubi)

    calculate how many PEBs must be reserved for bad eraseblock handling.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_check_pattern`:

ubi_check_pattern
=================

.. c:function:: int ubi_check_pattern(const void *buf, uint8_t patt, int size)

    check if buffer contains only a certain byte pattern.

    :param buf:
        buffer to check
    :type buf: const void \*

    :param patt:
        the pattern to check
    :type patt: uint8_t

    :param size:
        buffer size in bytes
    :type size: int

.. _`ubi_check_pattern.description`:

Description
-----------

This function returns \ ``1``\  in there are only \ ``patt``\  bytes in \ ``buf``\ , and \ ``0``\  if
something else was also found.

.. This file was automatic generated / don't edit.

