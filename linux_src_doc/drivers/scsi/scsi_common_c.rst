.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_common.c

.. _`scsi_device_type`:

scsi_device_type
================

.. c:function:: const char *scsi_device_type(unsigned type)

    Return 17-char string indicating device type.

    :param type:
        type number to look up
    :type type: unsigned

.. _`scsilun_to_int`:

scsilun_to_int
==============

.. c:function:: u64 scsilun_to_int(struct scsi_lun *scsilun)

    convert a scsi_lun to an int

    :param scsilun:
        struct scsi_lun to be converted.
    :type scsilun: struct scsi_lun \*

.. _`scsilun_to_int.description`:

Description
-----------

    Convert \ ``scsilun``\  from a struct scsi_lun to a four-byte host byte-ordered
    integer, and return the result. The caller must check for
    truncation before using this function.

.. _`scsilun_to_int.notes`:

Notes
-----

    For a description of the LUN format, post SCSI-3 see the SCSI
    Architecture Model, for SCSI-3 see the SCSI Controller Commands.

    Given a struct scsi_lun of: d2 04 0b 03 00 00 00 00, this function
    returns the integer: 0x0b03d204

    This encoding will return a standard integer LUN for LUNs smaller
    than 256, which typically use a single level LUN structure with
    addressing method 0.

.. _`int_to_scsilun`:

int_to_scsilun
==============

.. c:function:: void int_to_scsilun(u64 lun, struct scsi_lun *scsilun)

    reverts an int into a scsi_lun

    :param lun:
        integer to be reverted
    :type lun: u64

    :param scsilun:
        struct scsi_lun to be set.
    :type scsilun: struct scsi_lun \*

.. _`int_to_scsilun.description`:

Description
-----------

    Reverts the functionality of the scsilun_to_int, which packed
    an 8-byte lun value into an int. This routine unpacks the int
    back into the lun value.

.. _`int_to_scsilun.notes`:

Notes
-----

    Given an integer : 0x0b03d204, this function returns a
    struct scsi_lun of: d2 04 0b 03 00 00 00 00

.. _`scsi_normalize_sense`:

scsi_normalize_sense
====================

.. c:function:: bool scsi_normalize_sense(const u8 *sense_buffer, int sb_len, struct scsi_sense_hdr *sshdr)

    normalize main elements from either fixed or descriptor sense data format into a common format.

    :param sense_buffer:
        byte array containing sense data returned by device
    :type sense_buffer: const u8 \*

    :param sb_len:
        number of valid bytes in sense_buffer
    :type sb_len: int

    :param sshdr:
        pointer to instance of structure that common
        elements are written to.
    :type sshdr: struct scsi_sense_hdr \*

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

.. c:function:: const u8 *scsi_sense_desc_find(const u8 *sense_buffer, int sb_len, int desc_type)

    search for a given descriptor type in descriptor sense data format.

    :param sense_buffer:
        byte array of descriptor format sense data
    :type sense_buffer: const u8 \*

    :param sb_len:
        number of valid bytes in sense_buffer
    :type sb_len: int

    :param desc_type:
        value of descriptor type to find
        (e.g. 0 -> information)
    :type desc_type: int

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

.. c:function:: void scsi_build_sense_buffer(int desc, u8 *buf, u8 key, u8 asc, u8 ascq)

    build sense data in a buffer

    :param desc:
        Sense format (non-zero == descriptor format,
        0 == fixed format)
    :type desc: int

    :param buf:
        Where to build sense data
    :type buf: u8 \*

    :param key:
        Sense key
    :type key: u8

    :param asc:
        Additional sense code
    :type asc: u8

    :param ascq:
        Additional sense code qualifier
    :type ascq: u8

.. _`scsi_set_sense_information`:

scsi_set_sense_information
==========================

.. c:function:: int scsi_set_sense_information(u8 *buf, int buf_len, u64 info)

    set the information field in a formatted sense data buffer

    :param buf:
        Where to build sense data
    :type buf: u8 \*

    :param buf_len:
        buffer length
    :type buf_len: int

    :param info:
        64-bit information value to be set
    :type info: u64

.. _`scsi_set_sense_information.return-value`:

Return value
------------

     0 on success or -EINVAL for invalid sense buffer length

.. _`scsi_set_sense_field_pointer`:

scsi_set_sense_field_pointer
============================

.. c:function:: int scsi_set_sense_field_pointer(u8 *buf, int buf_len, u16 fp, u8 bp, bool cd)

    set the field pointer sense key specific information in a formatted sense data buffer

    :param buf:
        Where to build sense data
    :type buf: u8 \*

    :param buf_len:
        buffer length
    :type buf_len: int

    :param fp:
        field pointer to be set
    :type fp: u16

    :param bp:
        bit pointer to be set
    :type bp: u8

    :param cd:
        command/data bit
    :type cd: bool

.. _`scsi_set_sense_field_pointer.return-value`:

Return value
------------

     0 on success or -EINVAL for invalid sense buffer length

.. This file was automatic generated / don't edit.

