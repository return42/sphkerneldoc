.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/misc.c

.. _`ubi_calc_data_len`:

ubi_calc_data_len
=================

.. c:function:: int ubi_calc_data_len(const struct ubi_device *ubi, const void *buf, int length)

    calculate how much real data is stored in a buffer.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param const void \*buf:
        a buffer with the contents of the physical eraseblock

    :param int length:
        the buffer length

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        ID of the volume to check

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

    :param struct ubi_device \*ubi:
        UBI device description object

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

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`ubi_check_pattern`:

ubi_check_pattern
=================

.. c:function:: int ubi_check_pattern(const void *buf, uint8_t patt, int size)

    check if buffer contains only a certain byte pattern.

    :param const void \*buf:
        buffer to check

    :param uint8_t patt:
        the pattern to check

    :param int size:
        buffer size in bytes

.. _`ubi_check_pattern.description`:

Description
-----------

This function returns \ ``1``\  in there are only \ ``patt``\  bytes in \ ``buf``\ , and \ ``0``\  if
something else was also found.

.. This file was automatic generated / don't edit.

