.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/debug.c

.. _`ubi_dump_flash`:

ubi_dump_flash
==============

.. c:function:: void ubi_dump_flash(struct ubi_device *ubi, int pnum, int offset, int len)

    dump a region of flash.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pnum:
        the physical eraseblock number to dump
    :type pnum: int

    :param offset:
        the starting offset within the physical eraseblock to dump
    :type offset: int

    :param len:
        the length of the region to dump
    :type len: int

.. _`ubi_dump_ec_hdr`:

ubi_dump_ec_hdr
===============

.. c:function:: void ubi_dump_ec_hdr(const struct ubi_ec_hdr *ec_hdr)

    dump an erase counter header.

    :param ec_hdr:
        the erase counter header to dump
    :type ec_hdr: const struct ubi_ec_hdr \*

.. _`ubi_dump_vid_hdr`:

ubi_dump_vid_hdr
================

.. c:function:: void ubi_dump_vid_hdr(const struct ubi_vid_hdr *vid_hdr)

    dump a volume identifier header.

    :param vid_hdr:
        the volume identifier header to dump
    :type vid_hdr: const struct ubi_vid_hdr \*

.. _`ubi_dump_vol_info`:

ubi_dump_vol_info
=================

.. c:function:: void ubi_dump_vol_info(const struct ubi_volume *vol)

    dump volume information.

    :param vol:
        UBI volume description object
    :type vol: const struct ubi_volume \*

.. _`ubi_dump_vtbl_record`:

ubi_dump_vtbl_record
====================

.. c:function:: void ubi_dump_vtbl_record(const struct ubi_vtbl_record *r, int idx)

    dump a \ :c:type:`struct ubi_vtbl_record <ubi_vtbl_record>`\  object.

    :param r:
        the object to dump
    :type r: const struct ubi_vtbl_record \*

    :param idx:
        volume table index
    :type idx: int

.. _`ubi_dump_av`:

ubi_dump_av
===========

.. c:function:: void ubi_dump_av(const struct ubi_ainf_volume *av)

    dump a \ :c:type:`struct ubi_ainf_volume <ubi_ainf_volume>`\  object.

    :param av:
        the object to dump
    :type av: const struct ubi_ainf_volume \*

.. _`ubi_dump_aeb`:

ubi_dump_aeb
============

.. c:function:: void ubi_dump_aeb(const struct ubi_ainf_peb *aeb, int type)

    dump a \ :c:type:`struct ubi_ainf_peb <ubi_ainf_peb>`\  object.

    :param aeb:
        the object to dump
    :type aeb: const struct ubi_ainf_peb \*

    :param type:
        object type: 0 - not corrupted, 1 - corrupted
    :type type: int

.. _`ubi_dump_mkvol_req`:

ubi_dump_mkvol_req
==================

.. c:function:: void ubi_dump_mkvol_req(const struct ubi_mkvol_req *req)

    dump a \ :c:type:`struct ubi_mkvol_req <ubi_mkvol_req>`\  object.

    :param req:
        the object to dump
    :type req: const struct ubi_mkvol_req \*

.. _`ubi_debugfs_init`:

ubi_debugfs_init
================

.. c:function:: int ubi_debugfs_init( void)

    create UBI debugfs directory.

    :param void:
        no arguments
    :type void: 

.. _`ubi_debugfs_init.description`:

Description
-----------

Create UBI debugfs directory. Returns zero in case of success and a negative
error code in case of failure.

.. _`ubi_debugfs_exit`:

ubi_debugfs_exit
================

.. c:function:: void ubi_debugfs_exit( void)

    remove UBI debugfs directory.

    :param void:
        no arguments
    :type void: 

.. _`ubi_debugfs_init_dev`:

ubi_debugfs_init_dev
====================

.. c:function:: int ubi_debugfs_init_dev(struct ubi_device *ubi)

    initialize debugfs for an UBI device.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_debugfs_init_dev.description`:

Description
-----------

This function creates all debugfs files for UBI device \ ``ubi``\ . Returns zero in
case of success and a negative error code in case of failure.

.. _`ubi_debugfs_exit_dev`:

ubi_debugfs_exit_dev
====================

.. c:function:: void ubi_debugfs_exit_dev(struct ubi_device *ubi)

    free all debugfs files corresponding to device \ ``ubi``\ 

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_dbg_power_cut`:

ubi_dbg_power_cut
=================

.. c:function:: int ubi_dbg_power_cut(struct ubi_device *ubi, int caller)

    emulate a power cut if it is time to do so

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param caller:
        Flags set to indicate from where the function is being called
    :type caller: int

.. _`ubi_dbg_power_cut.description`:

Description
-----------

Returns non-zero if a power cut was emulated, zero if not.

.. This file was automatic generated / don't edit.

