.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/fastmap.c

.. _`init_seen`:

init_seen
=========

.. c:function:: unsigned long *init_seen(struct ubi_device *ubi)

    allocate memory for used for debugging.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`free_seen`:

free_seen
=========

.. c:function:: void free_seen(unsigned long *seen)

    free the seen logic integer array.

    :param seen:
        integer array of \ ``ubi->peb_count``\  size
    :type seen: unsigned long \*

.. _`set_seen`:

set_seen
========

.. c:function:: void set_seen(struct ubi_device *ubi, int pnum, unsigned long *seen)

    mark a PEB as seen.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        The PEB to be makred as seen
    :type pnum: int

    :param seen:
        integer array of \ ``ubi->peb_count``\  size
    :type seen: unsigned long \*

.. _`self_check_seen`:

self_check_seen
===============

.. c:function:: int self_check_seen(struct ubi_device *ubi, unsigned long *seen)

    check whether all PEB have been seen by fastmap.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param seen:
        integer array of \ ``ubi->peb_count``\  size
    :type seen: unsigned long \*

.. _`ubi_calc_fm_size`:

ubi_calc_fm_size
================

.. c:function:: size_t ubi_calc_fm_size(struct ubi_device *ubi)

    calculates the fastmap size in bytes for an UBI device.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`new_fm_vbuf`:

new_fm_vbuf
===========

.. c:function:: struct ubi_vid_io_buf *new_fm_vbuf(struct ubi_device *ubi, int vol_id)

    allocate a new volume header for fastmap usage.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        the VID of the new header
    :type vol_id: int

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

    :param ai:
        UBI attach info object
    :type ai: struct ubi_attach_info \*

    :param list:
        the target list
    :type list: struct list_head \*

    :param pnum:
        PEB number of the new attach erase block
    :type pnum: int

    :param ec:
        erease counter of the new LEB
    :type ec: int

    :param scrub:
        scrub this PEB after attaching
    :type scrub: int

.. _`add_aeb.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`add_vol`:

add_vol
=======

.. c:function:: struct ubi_ainf_volume *add_vol(struct ubi_attach_info *ai, int vol_id, int used_ebs, int data_pad, u8 vol_type, int last_eb_bytes)

    create and add a new volume to ubi_attach_info.

    :param ai:
        ubi_attach_info object
    :type ai: struct ubi_attach_info \*

    :param vol_id:
        VID of the new volume
    :type vol_id: int

    :param used_ebs:
        number of used EBS
    :type used_ebs: int

    :param data_pad:
        data padding value of the new volume
    :type data_pad: int

    :param vol_type:
        volume type
    :type vol_type: u8

    :param last_eb_bytes:
        number of bytes in the last LEB
    :type last_eb_bytes: int

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

    :param ai:
        ubi_attach_info object
    :type ai: struct ubi_attach_info \*

    :param aeb:
        the to be assigned SEB
    :type aeb: struct ubi_ainf_peb \*

    :param av:
        target scan volume
    :type av: struct ubi_ainf_volume \*

.. _`update_vol`:

update_vol
==========

.. c:function:: int update_vol(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_ainf_volume *av, struct ubi_vid_hdr *new_vh, struct ubi_ainf_peb *new_aeb)

    inserts or updates a LEB which was found a pool.

    :param ubi:
        the UBI device object
    :type ubi: struct ubi_device \*

    :param ai:
        attach info object
    :type ai: struct ubi_attach_info \*

    :param av:
        the volume this LEB belongs to
    :type av: struct ubi_ainf_volume \*

    :param new_vh:
        the volume header derived from new_aeb
    :type new_vh: struct ubi_vid_hdr \*

    :param new_aeb:
        the AEB to be examined
    :type new_aeb: struct ubi_ainf_peb \*

.. _`update_vol.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`process_pool_aeb`:

process_pool_aeb
================

.. c:function:: int process_pool_aeb(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_vid_hdr *new_vh, struct ubi_ainf_peb *new_aeb)

    we found a non-empty PEB in a pool.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param ai:
        attach info object
    :type ai: struct ubi_attach_info \*

    :param new_vh:
        the volume header derived from new_aeb
    :type new_vh: struct ubi_vid_hdr \*

    :param new_aeb:
        the AEB to be examined
    :type new_aeb: struct ubi_ainf_peb \*

.. _`process_pool_aeb.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`unmap_peb`:

unmap_peb
=========

.. c:function:: void unmap_peb(struct ubi_attach_info *ai, int pnum)

    unmap a PEB. If fastmap detects a free PEB in the pool it has to check whether this PEB has been unmapped after writing the fastmap.

    :param ai:
        UBI attach info object
    :type ai: struct ubi_attach_info \*

    :param pnum:
        The PEB to be unmapped
    :type pnum: int

.. _`scan_pool`:

scan_pool
=========

.. c:function:: int scan_pool(struct ubi_device *ubi, struct ubi_attach_info *ai, __be32 *pebs, int pool_size, unsigned long long *max_sqnum, struct list_head *free)

    scans a pool for changed (no longer empty PEBs).

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param ai:
        attach info object
    :type ai: struct ubi_attach_info \*

    :param pebs:
        an array of all PEB numbers in the to be scanned pool
    :type pebs: __be32 \*

    :param pool_size:
        size of the pool (number of entries in \ ``pebs``\ )
    :type pool_size: int

    :param max_sqnum:
        pointer to the maximal sequence number
    :type max_sqnum: unsigned long long \*

    :param free:
        list of PEBs which are most likely free (and go into \ ``ai->free``\ )
    :type free: struct list_head \*

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

    :param ai:
        The UBI attach info object
    :type ai: struct ubi_attach_info \*

.. _`ubi_attach_fastmap`:

ubi_attach_fastmap
==================

.. c:function:: int ubi_attach_fastmap(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_fastmap_layout *fm)

    creates ubi_attach_info from a fastmap.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param ai:
        UBI attach info object
    :type ai: struct ubi_attach_info \*

    :param fm:
        the fastmap to be attached
    :type fm: struct ubi_fastmap_layout \*

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

    :param ai:
        UBI attach info to be filled
    :type ai: struct ubi_attach_info \*

.. _`ubi_scan_fastmap`:

ubi_scan_fastmap
================

.. c:function:: int ubi_scan_fastmap(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_attach_info *scan_ai)

    scan the fastmap.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param ai:
        UBI attach info to be filled
    :type ai: struct ubi_attach_info \*

    :param scan_ai:
        UBI attach info from the first 64 PEBs,
        used to find the most recent Fastmap data structure
    :type scan_ai: struct ubi_attach_info \*

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

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param new_fm:
        the to be written fastmap
    :type new_fm: struct ubi_fastmap_layout \*

.. _`ubi_write_fastmap.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. _`erase_block`:

erase_block
===========

.. c:function:: int erase_block(struct ubi_device *ubi, int pnum)

    Manually erase a PEB.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param pnum:
        PEB to be erased
    :type pnum: int

.. _`erase_block.description`:

Description
-----------

Returns the new EC value on success, < 0 indicates an internal error.

.. _`invalidate_fastmap`:

invalidate_fastmap
==================

.. c:function:: int invalidate_fastmap(struct ubi_device *ubi)

    destroys a fastmap.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

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

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

    :param fm:
        fastmap layout object
    :type fm: struct ubi_fastmap_layout \*

.. _`ubi_update_fastmap`:

ubi_update_fastmap
==================

.. c:function:: int ubi_update_fastmap(struct ubi_device *ubi)

    will be called by UBI if a volume changes or a fastmap pool becomes full.

    :param ubi:
        UBI device object
    :type ubi: struct ubi_device \*

.. _`ubi_update_fastmap.description`:

Description
-----------

Returns 0 on success, < 0 indicates an internal error.

.. This file was automatic generated / don't edit.

