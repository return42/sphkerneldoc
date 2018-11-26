.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/io.c

.. _`ubi_io_read`:

ubi_io_read
===========

.. c:function:: int ubi_io_read(const struct ubi_device *ubi, void *buf, int pnum, int offset, int len)

    read data from a physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param buf:
        buffer where to store the read data
    :type buf: void \*

    :param pnum:
        physical eraseblock number to read from
    :type pnum: int

    :param offset:
        offset within the physical eraseblock from where to read
    :type offset: int

    :param len:
        how many bytes to read
    :type len: int

.. _`ubi_io_read.description`:

Description
-----------

This function reads data from offset \ ``offset``\  of physical eraseblock \ ``pnum``\ 
and stores the read data in the \ ``buf``\  buffer. The following return codes are

.. _`ubi_io_read.possible`:

possible
--------


o \ ``0``\  if all the requested data were successfully read;
o \ ``UBI_IO_BITFLIPS``\  if all the requested data were successfully read, but
correctable bit-flips were detected; this is harmless but may indicate
that this eraseblock may become bad soon (but do not have to);
o \ ``-EBADMSG``\  if the MTD subsystem reported about data integrity problems, for
example it can be an ECC error in case of NAND; this most probably means
that the data is corrupted;
o \ ``-EIO``\  if some I/O error occurred;
o other negative error codes in case of other errors.

.. _`ubi_io_write`:

ubi_io_write
============

.. c:function:: int ubi_io_write(struct ubi_device *ubi, const void *buf, int pnum, int offset, int len)

    write data to a physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param buf:
        buffer with the data to write
    :type buf: const void \*

    :param pnum:
        physical eraseblock number to write to
    :type pnum: int

    :param offset:
        offset within the physical eraseblock where to write
    :type offset: int

    :param len:
        how many bytes to write
    :type len: int

.. _`ubi_io_write.description`:

Description
-----------

This function writes \ ``len``\  bytes of data from buffer \ ``buf``\  to offset \ ``offset``\ 
of physical eraseblock \ ``pnum``\ . If all the data were successfully written,
zero is returned. If an error occurred, this function returns a negative
error code. If \ ``-EIO``\  is returned, the physical eraseblock most probably went
bad.

Note, in case of an error, it is possible that something was still written
to the flash media, but may be some garbage.

.. _`do_sync_erase`:

do_sync_erase
=============

.. c:function:: int do_sync_erase(struct ubi_device *ubi, int pnum)

    synchronously erase a physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock number to erase
    :type pnum: int

.. _`do_sync_erase.description`:

Description
-----------

This function synchronously erases physical eraseblock \ ``pnum``\  and returns
zero in case of success and a negative error code in case of failure. If
\ ``-EIO``\  is returned, the physical eraseblock most probably went bad.

.. _`torture_peb`:

torture_peb
===========

.. c:function:: int torture_peb(struct ubi_device *ubi, int pnum)

    test a supposedly bad physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock number to test
    :type pnum: int

.. _`torture_peb.description`:

Description
-----------

This function returns \ ``-EIO``\  if the physical eraseblock did not pass the
test, a positive number of erase operations done if the test was
successfully passed, and other negative error codes in case of other errors.

.. _`nor_erase_prepare`:

nor_erase_prepare
=================

.. c:function:: int nor_erase_prepare(struct ubi_device *ubi, int pnum)

    prepare a NOR flash PEB for erasure.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        physical eraseblock number to prepare
    :type pnum: int

.. _`nor_erase_prepare.description`:

Description
-----------

NOR flash, or at least some of them, have peculiar embedded PEB erasure

.. _`nor_erase_prepare.algorithm`:

algorithm
---------

the PEB is first filled with zeroes, then it is erased. And
filling with zeroes starts from the end of the PEB. This was observed with
Spansion S29GL512N NOR flash.

This means that in case of a power cut we may end up with intact data at the
beginning of the PEB, and all zeroes at the end of PEB. In other words, the
EC and VID headers are OK, but a large chunk of data at the end of PEB is
zeroed. This makes UBI mistakenly treat this PEB as used and associate it
with an LEB, which leads to subsequent failures (e.g., UBIFS fails).

This function is called before erasing NOR PEBs and it zeroes out EC and VID
magic numbers in order to invalidate them and prevent the failures. Returns
zero in case of success and a negative error code in case of failure.

.. _`ubi_io_sync_erase`:

ubi_io_sync_erase
=================

.. c:function:: int ubi_io_sync_erase(struct ubi_device *ubi, int pnum, int torture)

    synchronously erase a physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        physical eraseblock number to erase
    :type pnum: int

    :param torture:
        if this physical eraseblock has to be tortured
    :type torture: int

.. _`ubi_io_sync_erase.description`:

Description
-----------

This function synchronously erases physical eraseblock \ ``pnum``\ . If \ ``torture``\ 
flag is not zero, the physical eraseblock is checked by means of writing
different patterns to it and reading them back. If the torturing is enabled,
the physical eraseblock is erased more than once.

This function returns the number of erasures made in case of success, \ ``-EIO``\ 
if the erasure failed or the torturing test failed, and other negative error
codes in case of other errors. Note, \ ``-EIO``\  means that the physical
eraseblock is bad.

.. _`ubi_io_is_bad`:

ubi_io_is_bad
=============

.. c:function:: int ubi_io_is_bad(const struct ubi_device *ubi, int pnum)

    check if a physical eraseblock is bad.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        the physical eraseblock number to check
    :type pnum: int

.. _`ubi_io_is_bad.description`:

Description
-----------

This function returns a positive number if the physical eraseblock is bad,
zero if not, and a negative error code if an error occurred.

.. _`ubi_io_mark_bad`:

ubi_io_mark_bad
===============

.. c:function:: int ubi_io_mark_bad(const struct ubi_device *ubi, int pnum)

    mark a physical eraseblock as bad.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        the physical eraseblock number to mark
    :type pnum: int

.. _`ubi_io_mark_bad.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`validate_ec_hdr`:

validate_ec_hdr
===============

.. c:function:: int validate_ec_hdr(const struct ubi_device *ubi, const struct ubi_ec_hdr *ec_hdr)

    validate an erase counter header.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param ec_hdr:
        the erase counter header to check
    :type ec_hdr: const struct ubi_ec_hdr \*

.. _`validate_ec_hdr.description`:

Description
-----------

This function returns zero if the erase counter header is OK, and \ ``1``\  if
not.

.. _`ubi_io_read_ec_hdr`:

ubi_io_read_ec_hdr
==================

.. c:function:: int ubi_io_read_ec_hdr(struct ubi_device *ubi, int pnum, struct ubi_ec_hdr *ec_hdr, int verbose)

    read and check an erase counter header.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        physical eraseblock to read from
    :type pnum: int

    :param ec_hdr:
        a \ :c:type:`struct ubi_ec_hdr <ubi_ec_hdr>`\  object where to store the read erase counter
        header
    :type ec_hdr: struct ubi_ec_hdr \*

    :param verbose:
        be verbose if the header is corrupted or was not found
    :type verbose: int

.. _`ubi_io_read_ec_hdr.description`:

Description
-----------

This function reads erase counter header from physical eraseblock \ ``pnum``\  and
stores it in \ ``ec_hdr``\ . This function also checks CRC checksum of the read
erase counter header. The following codes may be returned:

o \ ``0``\  if the CRC checksum is correct and the header was successfully read;
o \ ``UBI_IO_BITFLIPS``\  if the CRC is correct, but bit-flips were detected
and corrected by the flash driver; this is harmless but may indicate that
this eraseblock may become bad soon (but may be not);
o \ ``UBI_IO_BAD_HDR``\  if the erase counter header is corrupted (a CRC error);
o \ ``UBI_IO_BAD_HDR_EBADMSG``\  is the same as \ ``UBI_IO_BAD_HDR``\ , but there also was
a data integrity error (uncorrectable ECC error in case of NAND);
o \ ``UBI_IO_FF``\  if only 0xFF bytes were read (the PEB is supposedly empty)
o a negative error code in case of failure.

.. _`ubi_io_write_ec_hdr`:

ubi_io_write_ec_hdr
===================

.. c:function:: int ubi_io_write_ec_hdr(struct ubi_device *ubi, int pnum, struct ubi_ec_hdr *ec_hdr)

    write an erase counter header.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        physical eraseblock to write to
    :type pnum: int

    :param ec_hdr:
        the erase counter header to write
    :type ec_hdr: struct ubi_ec_hdr \*

.. _`ubi_io_write_ec_hdr.description`:

Description
-----------

This function writes erase counter header described by \ ``ec_hdr``\  to physical
eraseblock \ ``pnum``\ . It also fills most fields of \ ``ec_hdr``\  before writing, so
the caller do not have to fill them. Callers must only fill the \ ``ec_hdr->ec``\ 
field.

This function returns zero in case of success and a negative error code in
case of failure. If \ ``-EIO``\  is returned, the physical eraseblock most probably
went bad.

.. _`validate_vid_hdr`:

validate_vid_hdr
================

.. c:function:: int validate_vid_hdr(const struct ubi_device *ubi, const struct ubi_vid_hdr *vid_hdr)

    validate a volume identifier header.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param vid_hdr:
        the volume identifier header to check
    :type vid_hdr: const struct ubi_vid_hdr \*

.. _`validate_vid_hdr.description`:

Description
-----------

This function checks that data stored in the volume identifier header
\ ``vid_hdr``\ . Returns zero if the VID header is OK and \ ``1``\  if not.

.. _`ubi_io_read_vid_hdr`:

ubi_io_read_vid_hdr
===================

.. c:function:: int ubi_io_read_vid_hdr(struct ubi_device *ubi, int pnum, struct ubi_vid_io_buf *vidb, int verbose)

    read and check a volume identifier header.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        physical eraseblock number to read from
    :type pnum: int

    :param vidb:
        the volume identifier buffer to store data in
    :type vidb: struct ubi_vid_io_buf \*

    :param verbose:
        be verbose if the header is corrupted or wasn't found
    :type verbose: int

.. _`ubi_io_read_vid_hdr.description`:

Description
-----------

This function reads the volume identifier header from physical eraseblock
\ ``pnum``\  and stores it in \ ``vidb``\ . It also checks CRC checksum of the read
volume identifier header. The error codes are the same as in
'ubi_io_read_ec_hdr()'.

Note, the implementation of this function is also very similar to
'ubi_io_read_ec_hdr()', so refer commentaries in 'ubi_io_read_ec_hdr()'.

.. _`ubi_io_write_vid_hdr`:

ubi_io_write_vid_hdr
====================

.. c:function:: int ubi_io_write_vid_hdr(struct ubi_device *ubi, int pnum, struct ubi_vid_io_buf *vidb)

    write a volume identifier header.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock number to write to
    :type pnum: int

    :param vidb:
        the volume identifier buffer to write
    :type vidb: struct ubi_vid_io_buf \*

.. _`ubi_io_write_vid_hdr.description`:

Description
-----------

This function writes the volume identifier header described by \ ``vid_hdr``\  to
physical eraseblock \ ``pnum``\ . This function automatically fills the
\ ``vidb->hdr->magic``\  and the \ ``vidb->hdr->version``\  fields, as well as calculates
header CRC checksum and stores it at vidb->hdr->hdr_crc.

This function returns zero in case of success and a negative error code in
case of failure. If \ ``-EIO``\  is returned, the physical eraseblock probably went
bad.

.. _`self_check_not_bad`:

self_check_not_bad
==================

.. c:function:: int self_check_not_bad(const struct ubi_device *ubi, int pnum)

    ensure that a physical eraseblock is not bad.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        physical eraseblock number to check
    :type pnum: int

.. _`self_check_not_bad.description`:

Description
-----------

This function returns zero if the physical eraseblock is good, \ ``-EINVAL``\  if
it is bad and a negative error code if an error occurred.

.. _`self_check_ec_hdr`:

self_check_ec_hdr
=================

.. c:function:: int self_check_ec_hdr(const struct ubi_device *ubi, int pnum, const struct ubi_ec_hdr *ec_hdr)

    check if an erase counter header is all right.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        physical eraseblock number the erase counter header belongs to
    :type pnum: int

    :param ec_hdr:
        the erase counter header to check
    :type ec_hdr: const struct ubi_ec_hdr \*

.. _`self_check_ec_hdr.description`:

Description
-----------

This function returns zero if the erase counter header contains valid
values, and \ ``-EINVAL``\  if not.

.. _`self_check_peb_ec_hdr`:

self_check_peb_ec_hdr
=====================

.. c:function:: int self_check_peb_ec_hdr(const struct ubi_device *ubi, int pnum)

    check erase counter header.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        the physical eraseblock number to check
    :type pnum: int

.. _`self_check_peb_ec_hdr.description`:

Description
-----------

This function returns zero if the erase counter header is all right and and
a negative error code if not or if an error occurred.

.. _`self_check_vid_hdr`:

self_check_vid_hdr
==================

.. c:function:: int self_check_vid_hdr(const struct ubi_device *ubi, int pnum, const struct ubi_vid_hdr *vid_hdr)

    check that a volume identifier header is all right.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        physical eraseblock number the volume identifier header belongs to
    :type pnum: int

    :param vid_hdr:
        the volume identifier header to check
    :type vid_hdr: const struct ubi_vid_hdr \*

.. _`self_check_vid_hdr.description`:

Description
-----------

This function returns zero if the volume identifier header is all right, and
\ ``-EINVAL``\  if not.

.. _`self_check_peb_vid_hdr`:

self_check_peb_vid_hdr
======================

.. c:function:: int self_check_peb_vid_hdr(const struct ubi_device *ubi, int pnum)

    check volume identifier header.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param pnum:
        the physical eraseblock number to check
    :type pnum: int

.. _`self_check_peb_vid_hdr.description`:

Description
-----------

This function returns zero if the volume identifier header is all right,
and a negative error code if not or if an error occurred.

.. _`self_check_write`:

self_check_write
================

.. c:function:: int self_check_write(struct ubi_device *ubi, const void *buf, int pnum, int offset, int len)

    make sure write succeeded.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param buf:
        buffer with data which were written
    :type buf: const void \*

    :param pnum:
        physical eraseblock number the data were written to
    :type pnum: int

    :param offset:
        offset within the physical eraseblock the data were written to
    :type offset: int

    :param len:
        how many bytes were written
    :type len: int

.. _`self_check_write.description`:

Description
-----------

This functions reads data which were recently written and compares it with
the original data buffer - the data have to match. Returns zero if the data
match and a negative error code if not or in case of failure.

.. _`ubi_self_check_all_ff`:

ubi_self_check_all_ff
=====================

.. c:function:: int ubi_self_check_all_ff(struct ubi_device *ubi, int pnum, int offset, int len)

    check that a region of flash is empty.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock number to check
    :type pnum: int

    :param offset:
        the starting offset within the physical eraseblock to check
    :type offset: int

    :param len:
        the length of the region to check
    :type len: int

.. _`ubi_self_check_all_ff.description`:

Description
-----------

This function returns zero if only 0xFF bytes are present at offset
\ ``offset``\  of the physical eraseblock \ ``pnum``\ , and a negative error code if not
or if an error occurred.

.. This file was automatic generated / don't edit.

