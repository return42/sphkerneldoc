.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/eba.c

.. _`ubi_eba_entry`:

struct ubi_eba_entry
====================

.. c:type:: struct ubi_eba_entry

    structure encoding a single LEB -> PEB association

.. _`ubi_eba_entry.definition`:

Definition
----------

.. code-block:: c

    struct ubi_eba_entry {
        int pnum;
    }

.. _`ubi_eba_entry.members`:

Members
-------

pnum
    the physical eraseblock number attached to the LEB

.. _`ubi_eba_entry.description`:

Description
-----------

This structure is encoding a LEB -> PEB association. Note that the LEB
number is not stored here, because it is the index used to access the
entries table.

.. _`ubi_eba_table`:

struct ubi_eba_table
====================

.. c:type:: struct ubi_eba_table

    LEB -> PEB association information

.. _`ubi_eba_table.definition`:

Definition
----------

.. code-block:: c

    struct ubi_eba_table {
        struct ubi_eba_entry *entries;
    }

.. _`ubi_eba_table.members`:

Members
-------

entries
    the LEB to PEB mapping (one entry per LEB).

.. _`ubi_eba_table.description`:

Description
-----------

This structure is private to the EBA logic and should be kept here.
It is encoding the LEB to PEB association table, and is subject to
changes.

.. _`ubi_next_sqnum`:

ubi_next_sqnum
==============

.. c:function:: unsigned long long ubi_next_sqnum(struct ubi_device *ubi)

    get next sequence number.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_next_sqnum.description`:

Description
-----------

This function returns next sequence number to use, which is just the current
global sequence counter value. It also increases the global sequence
counter.

.. _`ubi_get_compat`:

ubi_get_compat
==============

.. c:function:: int ubi_get_compat(const struct ubi_device *ubi, int vol_id)

    get compatibility flags of a volume.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

.. _`ubi_get_compat.description`:

Description
-----------

This function returns compatibility flags for an internal volume. User
volumes have no compatibility flags, so \ ``0``\  is returned.

.. _`ubi_eba_get_ldesc`:

ubi_eba_get_ldesc
=================

.. c:function:: void ubi_eba_get_ldesc(struct ubi_volume *vol, int lnum, struct ubi_eba_leb_desc *ldesc)

    get information about a LEB

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param ldesc:
        the LEB descriptor to fill
    :type ldesc: struct ubi_eba_leb_desc \*

.. _`ubi_eba_get_ldesc.description`:

Description
-----------

Used to query information about a specific LEB.
It is currently only returning the physical position of the LEB, but will be
extended to provide more information.

.. _`ubi_eba_create_table`:

ubi_eba_create_table
====================

.. c:function:: struct ubi_eba_table *ubi_eba_create_table(struct ubi_volume *vol, int nentries)

    allocate a new EBA table and initialize it with all LEBs unmapped

    :param vol:
        volume containing the EBA table to copy
    :type vol: struct ubi_volume \*

    :param nentries:
        number of entries in the table
    :type nentries: int

.. _`ubi_eba_create_table.description`:

Description
-----------

Allocate a new EBA table and initialize it with all LEBs unmapped.
Returns a valid pointer if it succeed, an \ :c:func:`ERR_PTR`\  otherwise.

.. _`ubi_eba_destroy_table`:

ubi_eba_destroy_table
=====================

.. c:function:: void ubi_eba_destroy_table(struct ubi_eba_table *tbl)

    destroy an EBA table

    :param tbl:
        the table to destroy
    :type tbl: struct ubi_eba_table \*

.. _`ubi_eba_destroy_table.description`:

Description
-----------

Destroy an EBA table.

.. _`ubi_eba_copy_table`:

ubi_eba_copy_table
==================

.. c:function:: void ubi_eba_copy_table(struct ubi_volume *vol, struct ubi_eba_table *dst, int nentries)

    copy the EBA table attached to vol into another table

    :param vol:
        volume containing the EBA table to copy
    :type vol: struct ubi_volume \*

    :param dst:
        destination
    :type dst: struct ubi_eba_table \*

    :param nentries:
        number of entries to copy
    :type nentries: int

.. _`ubi_eba_copy_table.description`:

Description
-----------

Copy the EBA table stored in vol into the one pointed by dst.

.. _`ubi_eba_replace_table`:

ubi_eba_replace_table
=====================

.. c:function:: void ubi_eba_replace_table(struct ubi_volume *vol, struct ubi_eba_table *tbl)

    assign a new EBA table to a volume

    :param vol:
        volume containing the EBA table to copy
    :type vol: struct ubi_volume \*

    :param tbl:
        new EBA table
    :type tbl: struct ubi_eba_table \*

.. _`ubi_eba_replace_table.description`:

Description
-----------

Assign a new EBA table to the volume and release the old one.

.. _`ltree_lookup`:

ltree_lookup
============

.. c:function:: struct ubi_ltree_entry *ltree_lookup(struct ubi_device *ubi, int vol_id, int lnum)

    look up the lock tree.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`ltree_lookup.description`:

Description
-----------

This function returns a pointer to the corresponding \ :c:type:`struct ubi_ltree_entry <ubi_ltree_entry>`\ 
object if the logical eraseblock is locked and \ ``NULL``\  if it is not.
\ ``ubi->ltree_lock``\  has to be locked.

.. _`ltree_add_entry`:

ltree_add_entry
===============

.. c:function:: struct ubi_ltree_entry *ltree_add_entry(struct ubi_device *ubi, int vol_id, int lnum)

    add new entry to the lock tree.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`ltree_add_entry.description`:

Description
-----------

This function adds new entry for logical eraseblock (@vol_id, \ ``lnum``\ ) to the
lock tree. If such entry is already there, its usage counter is increased.
Returns pointer to the lock tree entry or \ ``-ENOMEM``\  if memory allocation
failed.

.. _`leb_read_lock`:

leb_read_lock
=============

.. c:function:: int leb_read_lock(struct ubi_device *ubi, int vol_id, int lnum)

    lock logical eraseblock for reading.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`leb_read_lock.description`:

Description
-----------

This function locks a logical eraseblock for reading. Returns zero in case
of success and a negative error code in case of failure.

.. _`leb_read_unlock`:

leb_read_unlock
===============

.. c:function:: void leb_read_unlock(struct ubi_device *ubi, int vol_id, int lnum)

    unlock logical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`leb_write_lock`:

leb_write_lock
==============

.. c:function:: int leb_write_lock(struct ubi_device *ubi, int vol_id, int lnum)

    lock logical eraseblock for writing.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`leb_write_lock.description`:

Description
-----------

This function locks a logical eraseblock for writing. Returns zero in case
of success and a negative error code in case of failure.

.. _`leb_write_trylock`:

leb_write_trylock
=================

.. c:function:: int leb_write_trylock(struct ubi_device *ubi, int vol_id, int lnum)

    try to lock logical eraseblock for writing.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`leb_write_trylock.description`:

Description
-----------

This function locks a logical eraseblock for writing if there is no
contention and does nothing if there is contention. Returns \ ``0``\  in case of
success, \ ``1``\  in case of contention, and and a negative error code in case of
failure.

.. _`leb_write_unlock`:

leb_write_unlock
================

.. c:function:: void leb_write_unlock(struct ubi_device *ubi, int vol_id, int lnum)

    unlock logical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`ubi_eba_is_mapped`:

ubi_eba_is_mapped
=================

.. c:function:: bool ubi_eba_is_mapped(struct ubi_volume *vol, int lnum)

    check if a LEB is mapped.

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`ubi_eba_is_mapped.description`:

Description
-----------

This function returns true if the LEB is mapped, false otherwise.

.. _`ubi_eba_unmap_leb`:

ubi_eba_unmap_leb
=================

.. c:function:: int ubi_eba_unmap_leb(struct ubi_device *ubi, struct ubi_volume *vol, int lnum)

    un-map logical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

.. _`ubi_eba_unmap_leb.description`:

Description
-----------

This function un-maps logical eraseblock \ ``lnum``\  and schedules corresponding
physical eraseblock for erasure. Returns zero in case of success and a
negative error code in case of failure.

.. _`check_mapping`:

check_mapping
=============

.. c:function:: int check_mapping(struct ubi_device *ubi, struct ubi_volume *vol, int lnum, int *pnum)

    check and fixup a mapping

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param pnum:
        physical eraseblock number
    :type pnum: int \*

.. _`check_mapping.description`:

Description
-----------

Checks whether a given mapping is valid. Fastmap cannot track LEB unmap
operations, if such an operation is interrupted the mapping still looks
good, but upon first read an ECC is reported to the upper layer.
Normaly during the full-scan at attach time this is fixed, for Fastmap
we have to deal with it while reading.
If the PEB behind a LEB shows this symthom we change the mapping to
\ ``UBI_LEB_UNMAPPED``\  and schedule the PEB for erasure.

Returns 0 on success, negative error code in case of failure.

.. _`ubi_eba_read_leb`:

ubi_eba_read_leb
================

.. c:function:: int ubi_eba_read_leb(struct ubi_device *ubi, struct ubi_volume *vol, int lnum, void *buf, int offset, int len, int check)

    read data.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        buffer to store the read data
    :type buf: void \*

    :param offset:
        offset from where to read
    :type offset: int

    :param len:
        how many bytes to read
    :type len: int

    :param check:
        data CRC check flag
    :type check: int

.. _`ubi_eba_read_leb.description`:

Description
-----------

If the logical eraseblock \ ``lnum``\  is unmapped, \ ``buf``\  is filled with 0xFF
bytes. The \ ``check``\  flag only makes sense for static volumes and forces
eraseblock data CRC checking.

In case of success this function returns zero. In case of a static volume,
if data CRC mismatches - \ ``-EBADMSG``\  is returned. \ ``-EBADMSG``\  may also be
returned for any volume type if an ECC error was detected by the MTD device
driver. Other negative error cored may be returned in case of other errors.

.. _`ubi_eba_read_leb_sg`:

ubi_eba_read_leb_sg
===================

.. c:function:: int ubi_eba_read_leb_sg(struct ubi_device *ubi, struct ubi_volume *vol, struct ubi_sgl *sgl, int lnum, int offset, int len, int check)

    read data into a scatter gather list.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param sgl:
        UBI scatter gather list to store the read data
    :type sgl: struct ubi_sgl \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offset:
        offset from where to read
    :type offset: int

    :param len:
        how many bytes to read
    :type len: int

    :param check:
        data CRC check flag
    :type check: int

.. _`ubi_eba_read_leb_sg.description`:

Description
-----------

This function works exactly like \ :c:func:`ubi_eba_read_leb`\ . But instead of
storing the read data into a buffer it writes to an UBI scatter gather
list.

.. _`try_recover_peb`:

try_recover_peb
===============

.. c:function:: int try_recover_peb(struct ubi_volume *vol, int pnum, int lnum, const void *buf, int offset, int len, struct ubi_vid_io_buf *vidb, bool *retry)

    try to recover from write failure.

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param pnum:
        the physical eraseblock to recover
    :type pnum: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        data which was not written because of the write failure
    :type buf: const void \*

    :param offset:
        offset of the failed write
    :type offset: int

    :param len:
        how many bytes should have been written
    :type len: int

    :param vidb:
        VID buffer
    :type vidb: struct ubi_vid_io_buf \*

    :param retry:
        whether the caller should retry in case of failure
    :type retry: bool \*

.. _`try_recover_peb.description`:

Description
-----------

This function is called in case of a write failure and moves all good data
from the potentially bad physical eraseblock to a good physical eraseblock.
This function also writes the data which was not written due to the failure.
Returns 0 in case of success, and a negative error code in case of failure.
In case of failure, the \ ``retry``\  parameter is set to false if this is a fatal
error (retrying won't help), and true otherwise.

.. _`recover_peb`:

recover_peb
===========

.. c:function:: int recover_peb(struct ubi_device *ubi, int pnum, int vol_id, int lnum, const void *buf, int offset, int len)

    recover from write failure.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock to recover
    :type pnum: int

    :param vol_id:
        volume ID
    :type vol_id: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        data which was not written because of the write failure
    :type buf: const void \*

    :param offset:
        offset of the failed write
    :type offset: int

    :param len:
        how many bytes should have been written
    :type len: int

.. _`recover_peb.description`:

Description
-----------

This function is called in case of a write failure and moves all good data
from the potentially bad physical eraseblock to a good physical eraseblock.
This function also writes the data which was not written due to the failure.
Returns 0 in case of success, and a negative error code in case of failure.
This function tries \ ``UBI_IO_RETRIES``\  before giving up.

.. _`try_write_vid_and_data`:

try_write_vid_and_data
======================

.. c:function:: int try_write_vid_and_data(struct ubi_volume *vol, int lnum, struct ubi_vid_io_buf *vidb, const void *buf, int offset, int len)

    try to write VID header and data to a new PEB.

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param vidb:
        the VID buffer to write
    :type vidb: struct ubi_vid_io_buf \*

    :param buf:
        buffer containing the data
    :type buf: const void \*

    :param offset:
        where to start writing data
    :type offset: int

    :param len:
        how many bytes should be written
    :type len: int

.. _`try_write_vid_and_data.description`:

Description
-----------

This function tries to write VID header and data belonging to logical
eraseblock \ ``lnum``\  of volume \ ``vol``\  to a new physical eraseblock. Returns zero
in case of success and a negative error code in case of failure.
In case of error, it is possible that something was still written to the
flash media, but may be some garbage.

.. _`ubi_eba_write_leb`:

ubi_eba_write_leb
=================

.. c:function:: int ubi_eba_write_leb(struct ubi_device *ubi, struct ubi_volume *vol, int lnum, const void *buf, int offset, int len)

    write data to dynamic volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        the data to write
    :type buf: const void \*

    :param offset:
        offset within the logical eraseblock where to write
    :type offset: int

    :param len:
        how many bytes to write
    :type len: int

.. _`ubi_eba_write_leb.description`:

Description
-----------

This function writes data to logical eraseblock \ ``lnum``\  of a dynamic volume
\ ``vol``\ . Returns zero in case of success and a negative error code in case
of failure. In case of error, it is possible that something was still
written to the flash media, but may be some garbage.
This function retries \ ``UBI_IO_RETRIES``\  times before giving up.

.. _`ubi_eba_write_leb_st`:

ubi_eba_write_leb_st
====================

.. c:function:: int ubi_eba_write_leb_st(struct ubi_device *ubi, struct ubi_volume *vol, int lnum, const void *buf, int len, int used_ebs)

    write data to static volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        data to write
    :type buf: const void \*

    :param len:
        how many bytes to write
    :type len: int

    :param used_ebs:
        how many logical eraseblocks will this volume contain
    :type used_ebs: int

.. _`ubi_eba_write_leb_st.description`:

Description
-----------

This function writes data to logical eraseblock \ ``lnum``\  of static volume
\ ``vol``\ . The \ ``used_ebs``\  argument should contain total number of logical
eraseblock in this static volume.

When writing to the last logical eraseblock, the \ ``len``\  argument doesn't have
to be aligned to the minimal I/O unit size. Instead, it has to be equivalent
to the real data size, although the \ ``buf``\  buffer has to contain the
alignment. In all other cases, \ ``len``\  has to be aligned.

It is prohibited to write more than once to logical eraseblocks of static
volumes. This function returns zero in case of success and a negative error
code in case of failure.

.. _`is_error_sane`:

is_error_sane
=============

.. c:function:: int is_error_sane(int err)

    check whether a read error is sane.

    :param err:
        code of the error happened during reading
    :type err: int

.. _`is_error_sane.description`:

Description
-----------

This is a helper function for 'ubi_eba_copy_leb()' which is called when we
cannot read data from the target PEB (an error \ ``err``\  happened). If the error
code is sane, then we treat this error as non-fatal. Otherwise the error is
fatal and UBI will be switched to R/O mode later.

The idea is that we try not to switch to R/O mode if the read error is
something which suggests there was a real read problem. E.g., \ ``-EIO``\ . Or a
memory allocation failed (-%ENOMEM). Otherwise, it is safer to switch to R/O
mode, simply because we do not know what happened at the MTD level, and we
cannot handle this. E.g., the underlying driver may have become crazy, and
it is safer to switch to R/O mode to preserve the data.

And bear in mind, this is about reading from the target PEB, i.e. the PEB
which we have just written.

.. _`ubi_eba_copy_leb`:

ubi_eba_copy_leb
================

.. c:function:: int ubi_eba_copy_leb(struct ubi_device *ubi, int from, int to, struct ubi_vid_io_buf *vidb)

    copy logical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param from:
        physical eraseblock number from where to copy
    :type from: int

    :param to:
        physical eraseblock number where to copy
    :type to: int

    :param vidb:
        *undescribed*
    :type vidb: struct ubi_vid_io_buf \*

.. _`ubi_eba_copy_leb.description`:

Description
-----------

This function copies logical eraseblock from physical eraseblock \ ``from``\  to
physical eraseblock \ ``to``\ . The \ ``vid_hdr``\  buffer may be changed by this
function. Returns:
o \ ``0``\  in case of success;
o \ ``MOVE_CANCEL_RACE``\ , \ ``MOVE_TARGET_WR_ERR``\ , \ ``MOVE_TARGET_BITFLIPS``\ , etc;
o a negative error code in case of failure.

.. _`print_rsvd_warning`:

print_rsvd_warning
==================

.. c:function:: void print_rsvd_warning(struct ubi_device *ubi, struct ubi_attach_info *ai)

    warn about not having enough reserved PEBs.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        *undescribed*
    :type ai: struct ubi_attach_info \*

.. _`print_rsvd_warning.description`:

Description
-----------

This is a helper function for 'ubi_eba_init()' which is called when UBI
cannot reserve enough PEBs for bad block handling. This function makes a
decision whether we have to print a warning or not. The algorithm is as

.. _`print_rsvd_warning.follows`:

follows
-------

o if this is a new UBI image, then just print the warning
o if this is an UBI image which has already been used for some time, print
a warning only if we can reserve less than 10% of the expected amount of
the reserved PEB.

The idea is that when UBI is used, PEBs become bad, and the reserved pool
of PEBs becomes smaller, which is normal and we do not want to scare users
with a warning every time they attach the MTD device. This was an issue
reported by real users.

.. _`self_check_eba`:

self_check_eba
==============

.. c:function:: int self_check_eba(struct ubi_device *ubi, struct ubi_attach_info *ai_fastmap, struct ubi_attach_info *ai_scan)

    run a self check on the EBA table constructed by fastmap.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai_fastmap:
        UBI attach info object created by fastmap
    :type ai_fastmap: struct ubi_attach_info \*

    :param ai_scan:
        UBI attach info object created by scanning
    :type ai_scan: struct ubi_attach_info \*

.. _`self_check_eba.description`:

Description
-----------

Returns < 0 in case of an internal error, 0 otherwise.
If a bad EBA table entry was found it will be printed out and
\ :c:func:`ubi_assert`\  triggers.

.. _`ubi_eba_init`:

ubi_eba_init
============

.. c:function:: int ubi_eba_init(struct ubi_device *ubi, struct ubi_attach_info *ai)

    initialize the EBA sub-system using attaching information.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

.. _`ubi_eba_init.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. This file was automatic generated / don't edit.

