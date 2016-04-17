.. -*- coding: utf-8; mode: rst -*-

=============
scsi_common.c
=============


.. _`scsi_device_type`:

scsi_device_type
================

.. c:function:: const char *scsi_device_type (unsigned type)

    Return 17 char string indicating device type.

    :param unsigned type:
        type number to look up



.. _`scsilun_to_int`:

scsilun_to_int
==============

.. c:function:: u64 scsilun_to_int (struct scsi_lun *scsilun)

    convert a scsi_lun to an int

    :param struct scsi_lun \*scsilun:
        struct scsi_lun to be converted.



.. _`scsilun_to_int.description`:

Description
-----------

Convert ``scsilun`` from a struct scsi_lun to a four byte host byte-ordered
integer, and return the result. The caller must check for
truncation before using this function.



.. _`scsilun_to_int.notes`:

Notes
-----

For a description of the LUN format, post SCSI-3 see the SCSI
Architecture Model, for SCSI-3 see the SCSI Controller Commands.



.. _`scsilun_to_int.given-a-struct-scsi_lun-of`:

Given a struct scsi_lun of
--------------------------

d2 04 0b 03 00 00 00 00, this function



.. _`scsilun_to_int.returns-the-integer`:

returns the integer
-------------------

0x0b03d204

This encoding will return a standard integer LUN for LUNs smaller
than 256, which typically use a single level LUN structure with
addressing method 0.



.. _`int_to_scsilun`:

int_to_scsilun
==============

.. c:function:: void int_to_scsilun (u64 lun, struct scsi_lun *scsilun)

    reverts an int into a scsi_lun

    :param u64 lun:
        integer to be reverted

    :param struct scsi_lun \*scsilun:
        struct scsi_lun to be set.



.. _`int_to_scsilun.description`:

Description
-----------

Reverts the functionality of the scsilun_to_int, which packed
an 8-byte lun value into an int. This routine unpacks the int
back into the lun value.



.. _`int_to_scsilun.given-an-integer`:

Given an integer 
-----------------

0x0b03d204,  this function returns a



.. _`int_to_scsilun.struct-scsi_lun-of`:

struct scsi_lun of
------------------

d2 04 0b 03 00 00 00 00



.. _`scsi_normalize_sense`:

scsi_normalize_sense
====================

.. c:function:: bool scsi_normalize_sense (const u8 *sense_buffer, int sb_len, struct scsi_sense_hdr *sshdr)

    normalize main elements from either fixed or descriptor sense data format into a common format.

    :param const u8 \*sense_buffer:
        byte array containing sense data returned by device

    :param int sb_len:
        number of valid bytes in sense_buffer

    :param struct scsi_sense_hdr \*sshdr:
        pointer to instance of structure that common
        elements are written to.



.. _`scsi_normalize_sense.notes`:

Notes
-----

The "main elements" from sense data are: response_code, sense_key,
asc, ascq and additional_length (only for descriptor format).

Typically this function can be called after a device has
responded to a SCSI command with the CHECK_CONDITION status.



.. _`scsi_normalize_sense.return-value`:

Return value
------------

true if valid sense data information found, else false;



.. _`scsi_sense_desc_find`:

scsi_sense_desc_find
====================

.. c:function:: const u8 *scsi_sense_desc_find (const u8 *sense_buffer, int sb_len, int desc_type)

    search for a given descriptor type in descriptor sense data format.

    :param const u8 \*sense_buffer:
        byte array of descriptor format sense data

    :param int sb_len:
        number of valid bytes in sense_buffer

    :param int desc_type:
        value of descriptor type to find
        (e.g. 0 -> information)



.. _`scsi_sense_desc_find.notes`:

Notes
-----

only valid when sense data is in descriptor format



.. _`scsi_sense_desc_find.return-value`:

Return value
------------

pointer to start of (first) descriptor if found else NULL



.. _`scsi_build_sense_buffer`:

scsi_build_sense_buffer
=======================

.. c:function:: void scsi_build_sense_buffer (int desc, u8 *buf, u8 key, u8 asc, u8 ascq)

    build sense data in a buffer

    :param int desc:
        Sense format (non zero == descriptor format,

                     0 == fixed format)

    :param u8 \*buf:
        Where to build sense data

    :param u8 key:
        Sense key

    :param u8 asc:
        Additional sense code

    :param u8 ascq:
        Additional sense code qualifier



.. _`scsi_set_sense_information`:

scsi_set_sense_information
==========================

.. c:function:: int scsi_set_sense_information (u8 *buf, int buf_len, u64 info)

    set the information field in a formatted sense data buffer

    :param u8 \*buf:
        Where to build sense data

    :param int buf_len:
        buffer length

    :param u64 info:
        64-bit information value to be set



.. _`scsi_set_sense_information.return-value`:

Return value
------------

0 on success or EINVAL for invalid sense buffer length

