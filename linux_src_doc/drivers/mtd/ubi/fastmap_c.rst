.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/fastmap.c

.. _`init_seen`:

init_seen
=========

.. c:function:: unsigned long *init_seen(struct ubi_device *ubi)

    allocate memory for used for debugging.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`free_seen`:

free_seen
=========

.. c:function:: void free_seen(unsigned long *seen)

    free the seen logic integer array.

    :param unsigned long \*seen:
        integer array of \ ``ubi``\ ->peb_count size

.. _`set_seen`:

set_seen
========

.. c:function:: void set_seen(struct ubi_device *ubi, int pnum, unsigned long *seen)

    mark a PEB as seen.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int pnum:
        The PEB to be makred as seen

    :param unsigned long \*seen:
        integer array of \ ``ubi``\ ->peb_count size

.. _`self_check_seen`:

self_check_seen
===============

.. c:function:: int self_check_seen(struct ubi_device *ubi, unsigned long *seen)

    check whether all PEB have been seen by fastmap.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param unsigned long \*seen:
        integer array of \ ``ubi``\ ->peb_count size

.. _`ubi_calc_fm_size`:

ubi_calc_fm_size
================

.. c:function:: size_t ubi_calc_fm_size(struct ubi_device *ubi)

    calculates the fastmap size in bytes for an UBI device.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`new_fm_vbuf`:

new_fm_vbuf
===========

.. c:function:: struct ubi_vid_io_buf *new_fm_vbuf(struct ubi_device *ubi, int vol_id)

    allocate a new volume header for fastmap usage.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        the VID of the new header

.. _`new_fm_vbuf.description`:

Description
-----------

Returns a new struct ubi_vid_hdr on success.
NULL indicates out of memory.

.. _`add_aeb`:

add_aeb
=======

.. c:function:: int add_aeb(struct ubi_attach_info *ai, struct list_head *list, int pnum, int ec, int scrub)

    create and add a attach erase block to a given list.

    :param struct ubi_attach_info \*ai:
        UBI attach info object

    :param struct list_head \*list:
        the target list

    :param int pnum:
        PEB number of the new attach erase block

    :param int ec:
        erease counter of the new LEB

    :param int scrub:
        scrub this PEB after attaching

.. _`add_aeb.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`add_vol`:

add_vol
=======

.. c:function:: struct ubi_ainf_volume *add_vol(struct ubi_attach_info *ai, int vol_id, int used_ebs, int data_pad, u8 vol_type, int last_eb_bytes)

    create and add a new volume to ubi_attach_info.

    :param struct ubi_attach_info \*ai:
        ubi_attach_info object

    :param int vol_id:
        VID of the new volume

    :param int used_ebs:
        number of used EBS

    :param int data_pad:
        data padding value of the new volume

    :param u8 vol_type:
        volume type

    :param int last_eb_bytes:
        number of bytes in the last LEB

.. _`add_vol.description`:

Description
-----------

Returns the new struct ubi_ainf_volume on success.
NULL indicates an error.

.. _`assign_aeb_to_av`:

assign_aeb_to_av
================

.. c:function:: void assign_aeb_to_av(struct ubi_attach_info *ai, struct ubi_ainf_peb *aeb, struct ubi_ainf_volume *av)

    assigns a SEB to a given ainf_volume and removes it from it's original list.

    :param struct ubi_attach_info \*ai:
        ubi_attach_info object

    :param struct ubi_ainf_peb \*aeb:
        the to be assigned SEB

    :param struct ubi_ainf_volume \*av:
        target scan volume

.. _`update_vol`:

update_vol
==========

.. c:function:: int update_vol(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_ainf_volume *av, struct ubi_vid_hdr *new_vh, struct ubi_ainf_peb *new_aeb)

    inserts or updates a LEB which was found a pool.

    :param struct ubi_device \*ubi:
        the UBI device object

    :param struct ubi_attach_info \*ai:
        attach info object

    :param struct ubi_ainf_volume \*av:
        the volume this LEB belongs to

    :param struct ubi_vid_hdr \*new_vh:
        the volume header derived from new_aeb

    :param struct ubi_ainf_peb \*new_aeb:
        the AEB to be examined

.. _`update_vol.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`process_pool_aeb`:

process_pool_aeb
================

.. c:function:: int process_pool_aeb(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_vid_hdr *new_vh, struct ubi_ainf_peb *new_aeb)

    we found a non-empty PEB in a pool.

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_attach_info \*ai:
        attach info object

    :param struct ubi_vid_hdr \*new_vh:
        the volume header derived from new_aeb

    :param struct ubi_ainf_peb \*new_aeb:
        the AEB to be examined

.. _`process_pool_aeb.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`unmap_peb`:

unmap_peb
=========

.. c:function:: void unmap_peb(struct ubi_attach_info *ai, int pnum)

    unmap a PEB. If fastmap detects a free PEB in the pool it has to check whether this PEB has been unmapped after writing the fastmap.

    :param struct ubi_attach_info \*ai:
        UBI attach info object

    :param int pnum:
        The PEB to be unmapped

.. _`scan_pool`:

scan_pool
=========

.. c:function:: int scan_pool(struct ubi_device *ubi, struct ubi_attach_info *ai, __be32 *pebs, int pool_size, unsigned long long *max_sqnum, struct list_head *free)

    scans a pool for changed (no longer empty PEBs).

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_attach_info \*ai:
        attach info object

    :param __be32 \*pebs:
        an array of all PEB numbers in the to be scanned pool

    :param int pool_size:
        size of the pool (number of entries in \ ``pebs``\ )

    :param unsigned long long \*max_sqnum:
        pointer to the maximal sequence number

    :param struct list_head \*free:
        list of PEBs which are most likely free (and go into \ ``ai``\ ->free)

.. _`scan_pool.description`:

Description
-----------

Returns 0 on success, if the pool is unusable UBI_BAD_FASTMAP is returned.
< 0 indicates an internal error.

.. _`count_fastmap_pebs`:

count_fastmap_pebs
==================

.. c:function:: int count_fastmap_pebs(struct ubi_attach_info *ai)

    Counts the PEBs found by fastmap.

    :param struct ubi_attach_info \*ai:
        The UBI attach info object

.. _`ubi_attach_fastmap`:

ubi_attach_fastmap
==================

.. c:function:: int ubi_attach_fastmap(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_fastmap_layout *fm)

    creates ubi_attach_info from a fastmap.

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_attach_info \*ai:
        UBI attach info object

    :param struct ubi_fastmap_layout \*fm:
        the fastmap to be attached

.. _`ubi_attach_fastmap.description`:

Description
-----------

Returns 0 on success, UBI_BAD_FASTMAP if the found fastmap was unusable.
< 0 indicates an internal error.

.. _`find_fm_anchor`:

find_fm_anchor
==============

.. c:function:: int find_fm_anchor(struct ubi_attach_info *ai)

    find the most recent Fastmap superblock (anchor)

    :param struct ubi_attach_info \*ai:
        UBI attach info to be filled

.. _`ubi_scan_fastmap`:

ubi_scan_fastmap
================

.. c:function:: int ubi_scan_fastmap(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_attach_info *scan_ai)

    scan the fastmap.

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_attach_info \*ai:
        UBI attach info to be filled

    :param struct ubi_attach_info \*scan_ai:
        UBI attach info from the first 64 PEBs,
        used to find the most recent Fastmap data structure

.. _`ubi_scan_fastmap.description`:

Description
-----------

Returns 0 on success, UBI_NO_FASTMAP if no fastmap was found,
UBI_BAD_FASTMAP if one was found but is not usable.
< 0 indicates an internal error.

.. _`ubi_write_fastmap`:

ubi_write_fastmap
=================

.. c:function:: int ubi_write_fastmap(struct ubi_device *ubi, struct ubi_fastmap_layout *new_fm)

    writes a fastmap.

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_fastmap_layout \*new_fm:
        the to be written fastmap

.. _`ubi_write_fastmap.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`erase_block`:

erase_block
===========

.. c:function:: int erase_block(struct ubi_device *ubi, int pnum)

    Manually erase a PEB.

    :param struct ubi_device \*ubi:
        UBI device object

    :param int pnum:
        PEB to be erased

.. _`erase_block.description`:

Description
-----------

Returns the new EC value on success, < 0 indicates an internal error.

.. _`invalidate_fastmap`:

invalidate_fastmap
==================

.. c:function:: int invalidate_fastmap(struct ubi_device *ubi)

    destroys a fastmap.

    :param struct ubi_device \*ubi:
        UBI device object

.. _`invalidate_fastmap.description`:

Description
-----------

This function ensures that upon next UBI attach a full scan
is issued. We need this if UBI is about to write a new fastmap
but is unable to do so. In this case we have two options:
a) Make sure that the current fastmap will not be usued upon
attach time and contine or b) fall back to RO mode to have the
current fastmap in a valid state.
Returns 0 on success, < 0 indicates an internal error.

.. _`return_fm_pebs`:

return_fm_pebs
==============

.. c:function:: void return_fm_pebs(struct ubi_device *ubi, struct ubi_fastmap_layout *fm)

    returns all PEBs used by a fastmap back to the WL sub-system.

    :param struct ubi_device \*ubi:
        UBI device object

    :param struct ubi_fastmap_layout \*fm:
        fastmap layout object

.. _`ubi_update_fastmap`:

ubi_update_fastmap
==================

.. c:function:: int ubi_update_fastmap(struct ubi_device *ubi)

    will be called by UBI if a volume changes or a fastmap pool becomes full.

    :param struct ubi_device \*ubi:
        UBI device object

.. _`ubi_update_fastmap.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. This file was automatic generated / don't edit.

