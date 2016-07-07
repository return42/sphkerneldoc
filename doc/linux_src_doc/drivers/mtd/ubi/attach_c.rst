.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/attach.c

.. _`add_to_list`:

add_to_list
===========

.. c:function:: int add_to_list(struct ubi_attach_info *ai, int pnum, int vol_id, int lnum, int ec, int to_head, struct list_head *list)

    add physical eraseblock to a list.

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int pnum:
        physical eraseblock number to add

    :param int vol_id:
        the last used volume id for the PEB

    :param int lnum:
        the last used LEB number for the PEB

    :param int ec:
        erase counter of the physical eraseblock

    :param int to_head:
        if not zero, add to the head of the list

    :param struct list_head \*list:
        the list to add to

.. _`add_to_list.description`:

Description
-----------

This function allocates a 'struct ubi_ainf_peb' object for physical
eraseblock \ ``pnum``\  and adds it to the "free", "erase", or "alien" lists.
It stores the \ ``lnum``\  and \ ``vol_id``\  alongside, which can both be
\ ``UBI_UNKNOWN``\  if they are not available, not readable, or not assigned.
If \ ``to_head``\  is not zero, PEB will be added to the head of the list, which
basically means it will be processed first later. E.g., we add corrupted
PEBs (corrupted due to power cuts) to the head of the erase list to make
sure we erase them first and get rid of corruptions ASAP. This function
returns zero in case of success and a negative error code in case of
failure.

.. _`add_corrupted`:

add_corrupted
=============

.. c:function:: int add_corrupted(struct ubi_attach_info *ai, int pnum, int ec)

    add a corrupted physical eraseblock.

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int pnum:
        physical eraseblock number to add

    :param int ec:
        erase counter of the physical eraseblock

.. _`add_corrupted.description`:

Description
-----------

This function allocates a 'struct ubi_ainf_peb' object for a corrupted
physical eraseblock \ ``pnum``\  and adds it to the 'corr' list.  The corruption
was presumably not caused by a power cut. Returns zero in case of success
and a negative error code in case of failure.

.. _`validate_vid_hdr`:

validate_vid_hdr
================

.. c:function:: int validate_vid_hdr(const struct ubi_device *ubi, const struct ubi_vid_hdr *vid_hdr, const struct ubi_ainf_volume *av, int pnum)

    check volume identifier header.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param const struct ubi_vid_hdr \*vid_hdr:
        the volume identifier header to check

    :param const struct ubi_ainf_volume \*av:
        information about the volume this logical eraseblock belongs to

    :param int pnum:
        physical eraseblock number the VID header came from

.. _`validate_vid_hdr.description`:

Description
-----------

This function checks that data stored in \ ``vid_hdr``\  is consistent. Returns
non-zero if an inconsistency was found and zero if not.

Note, UBI does sanity check of everything it reads from the flash media.
Most of the checks are done in the I/O sub-system. Here we check that the
information in the VID header is consistent to the information in other VID
headers of the same volume.

.. _`add_volume`:

add_volume
==========

.. c:function:: struct ubi_ainf_volume *add_volume(struct ubi_attach_info *ai, int vol_id, int pnum, const struct ubi_vid_hdr *vid_hdr)

    add volume to the attaching information.

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int vol_id:
        ID of the volume to add

    :param int pnum:
        physical eraseblock number

    :param const struct ubi_vid_hdr \*vid_hdr:
        volume identifier header

.. _`add_volume.description`:

Description
-----------

If the volume corresponding to the \ ``vid_hdr``\  logical eraseblock is already
present in the attaching information, this function does nothing. Otherwise
it adds corresponding volume to the attaching information. Returns a pointer
to the allocated "av" object in case of success and a negative error code in
case of failure.

.. _`ubi_compare_lebs`:

ubi_compare_lebs
================

.. c:function:: int ubi_compare_lebs(struct ubi_device *ubi, const struct ubi_ainf_peb *aeb, int pnum, const struct ubi_vid_hdr *vid_hdr)

    find out which logical eraseblock is newer.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param const struct ubi_ainf_peb \*aeb:
        first logical eraseblock to compare

    :param int pnum:
        physical eraseblock number of the second logical eraseblock to
        compare

    :param const struct ubi_vid_hdr \*vid_hdr:
        volume identifier header of the second logical eraseblock

.. _`ubi_compare_lebs.description`:

Description
-----------

This function compares 2 copies of a LEB and informs which one is newer. In
case of success this function returns a positive value, in case of failure, a
negative error code is returned. The success return codes use the following

.. _`ubi_compare_lebs.o-bit-0-is-cleared`:

o bit 0 is cleared
------------------

the first PEB (described by \ ``aeb``\ ) is newer than the
second PEB (described by \ ``pnum``\  and \ ``vid_hdr``\ );

.. _`ubi_compare_lebs.o-bit-0-is-set`:

o bit 0 is set
--------------

the second PEB is newer;

.. _`ubi_compare_lebs.o-bit-1-is-cleared`:

o bit 1 is cleared
------------------

no bit-flips were detected in the newer LEB;

.. _`ubi_compare_lebs.o-bit-1-is-set`:

o bit 1 is set
--------------

bit-flips were detected in the newer LEB;

.. _`ubi_compare_lebs.o-bit-2-is-cleared`:

o bit 2 is cleared
------------------

the older LEB is not corrupted;

.. _`ubi_compare_lebs.o-bit-2-is-set`:

o bit 2 is set
--------------

the older LEB is corrupted.

.. _`ubi_add_to_av`:

ubi_add_to_av
=============

.. c:function:: int ubi_add_to_av(struct ubi_device *ubi, struct ubi_attach_info *ai, int pnum, int ec, const struct ubi_vid_hdr *vid_hdr, int bitflips)

    add used physical eraseblock to the attaching information.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int pnum:
        the physical eraseblock number

    :param int ec:
        erase counter

    :param const struct ubi_vid_hdr \*vid_hdr:
        the volume identifier header

    :param int bitflips:
        if bit-flips were detected when this physical eraseblock was read

.. _`ubi_add_to_av.description`:

Description
-----------

This function adds information about a used physical eraseblock to the
'used' tree of the corresponding volume. The function is rather complex
because it has to handle cases when this is not the first physical
eraseblock belonging to the same logical eraseblock, and the newer one has
to be picked, while the older one has to be dropped. This function returns
zero in case of success and a negative error code in case of failure.

.. _`ubi_find_av`:

ubi_find_av
===========

.. c:function:: struct ubi_ainf_volume *ubi_find_av(const struct ubi_attach_info *ai, int vol_id)

    find volume in the attaching information.

    :param const struct ubi_attach_info \*ai:
        attaching information

    :param int vol_id:
        the requested volume ID

.. _`ubi_find_av.description`:

Description
-----------

This function returns a pointer to the volume description or \ ``NULL``\  if there
are no data about this volume in the attaching information.

.. _`ubi_remove_av`:

ubi_remove_av
=============

.. c:function:: void ubi_remove_av(struct ubi_attach_info *ai, struct ubi_ainf_volume *av)

    delete attaching information about a volume.

    :param struct ubi_attach_info \*ai:
        attaching information

    :param struct ubi_ainf_volume \*av:
        the volume attaching information to delete

.. _`early_erase_peb`:

early_erase_peb
===============

.. c:function:: int early_erase_peb(struct ubi_device *ubi, const struct ubi_attach_info *ai, int pnum, int ec)

    erase a physical eraseblock.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param const struct ubi_attach_info \*ai:
        attaching information

    :param int pnum:
        physical eraseblock number to erase;

    :param int ec:
        erase counter value to write (\ ``UBI_UNKNOWN``\  if it is unknown)

.. _`early_erase_peb.description`:

Description
-----------

This function erases physical eraseblock 'pnum', and writes the erase
counter header to it. This function should only be used on UBI device
initialization stages, when the EBA sub-system had not been yet initialized.
This function returns zero in case of success and a negative error code in
case of failure.

.. _`ubi_early_get_peb`:

ubi_early_get_peb
=================

.. c:function:: struct ubi_ainf_peb *ubi_early_get_peb(struct ubi_device *ubi, struct ubi_attach_info *ai)

    get a free physical eraseblock.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

.. _`ubi_early_get_peb.description`:

Description
-----------

This function returns a free physical eraseblock. It is supposed to be
called on the UBI initialization stages when the wear-leveling sub-system is
not initialized yet. This function picks a physical eraseblocks from one of
the lists, writes the EC header if it is needed, and removes it from the
list.

This function returns a pointer to the "aeb" of the found free PEB in case
of success and an error code in case of failure.

.. _`check_corruption`:

check_corruption
================

.. c:function:: int check_corruption(struct ubi_device *ubi, struct ubi_vid_hdr *vid_hdr, int pnum)

    check the data area of PEB.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_vid_hdr \*vid_hdr:
        the (corrupted) VID header of this PEB

    :param int pnum:
        the physical eraseblock number to check

.. _`check_corruption.description`:

Description
-----------

This is a helper function which is used to distinguish between VID header
corruptions caused by power cuts and other reasons. If the PEB contains only
0xFF bytes in the data area, the VID header is most probably corrupted
because of a power cut (\ ``0``\  is returned in this case). Otherwise, it was
probably corrupted for some other reasons (\ ``1``\  is returned in this case). A
negative error code is returned if a read error occurred.

If the corruption reason was a power cut, UBI can safely erase this PEB.
Otherwise, it should preserve it to avoid possibly destroying important
information.

.. _`scan_peb`:

scan_peb
========

.. c:function:: int scan_peb(struct ubi_device *ubi, struct ubi_attach_info *ai, int pnum, int *vid, unsigned long long *sqnum)

    scan and process UBI headers of a PEB.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int pnum:
        the physical eraseblock number

    :param int \*vid:
        The volume ID of the found volume will be stored in this pointer

    :param unsigned long long \*sqnum:
        The sqnum of the found volume will be stored in this pointer

.. _`scan_peb.description`:

Description
-----------

This function reads UBI headers of PEB \ ``pnum``\ , checks them, and adds
information about this PEB to the corresponding list or RB-tree in the
"attaching info" structure. Returns zero if the physical eraseblock was
successfully handled and a negative error code in case of failure.

.. _`late_analysis`:

late_analysis
=============

.. c:function:: int late_analysis(struct ubi_device *ubi, struct ubi_attach_info *ai)

    analyze the overall situation with PEB.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

.. _`late_analysis.description`:

Description
-----------

This is a helper function which takes a look what PEBs we have after we
gather information about all of them ("ai" is compete). It decides whether
the flash is empty and should be formatted of whether there are too many
corrupted PEBs and we should not attach this MTD device. Returns zero if we
should proceed with attaching the MTD device, and \ ``-EINVAL``\  if we should not.

.. _`destroy_av`:

destroy_av
==========

.. c:function:: void destroy_av(struct ubi_attach_info *ai, struct ubi_ainf_volume *av)

    free volume attaching information.

    :param struct ubi_attach_info \*ai:
        attaching information

    :param struct ubi_ainf_volume \*av:
        volume attaching information

.. _`destroy_av.description`:

Description
-----------

This function destroys the volume attaching information.

.. _`destroy_ai`:

destroy_ai
==========

.. c:function:: void destroy_ai(struct ubi_attach_info *ai)

    destroy attaching information.

    :param struct ubi_attach_info \*ai:
        attaching information

.. _`scan_all`:

scan_all
========

.. c:function:: int scan_all(struct ubi_device *ubi, struct ubi_attach_info *ai, int start)

    scan entire MTD device.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attach info object

    :param int start:
        start scanning at this PEB

.. _`scan_all.description`:

Description
-----------

This function does full scanning of an MTD device and returns complete
information about it in form of a "struct ubi_attach_info" object. In case
of failure, an error code is returned.

.. _`scan_fast`:

scan_fast
=========

.. c:function:: int scan_fast(struct ubi_device *ubi, struct ubi_attach_info **ai)

    try to find a fastmap and attach from it.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*\*ai:
        attach info object

.. _`scan_fast.description`:

Description
-----------

Returns 0 on success, negative return values indicate an internal
error.
UBI_NO_FASTMAP denotes that no fastmap was found.
UBI_BAD_FASTMAP denotes that the found fastmap was invalid.

.. _`ubi_attach`:

ubi_attach
==========

.. c:function:: int ubi_attach(struct ubi_device *ubi, int force_scan)

    attach an MTD device.

    :param struct ubi_device \*ubi:
        UBI device descriptor

    :param int force_scan:
        if set to non-zero attach by scanning

.. _`ubi_attach.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`self_check_ai`:

self_check_ai
=============

.. c:function:: int self_check_ai(struct ubi_device *ubi, struct ubi_attach_info *ai)

    check the attaching information.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

.. _`self_check_ai.description`:

Description
-----------

This function returns zero if the attaching information is all right, and a
negative error code if not or if an error occurred.

.. This file was automatic generated / don't edit.

