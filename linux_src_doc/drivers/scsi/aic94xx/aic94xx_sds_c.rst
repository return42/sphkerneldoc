.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_sds.c

.. _`asd_read_ocm_seg`:

asd_read_ocm_seg
================

.. c:function:: int asd_read_ocm_seg(struct asd_ha_struct *asd_ha, void *buffer, u32 offs, int size)

    read an on chip memory (OCM) segment

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param void \*buffer:
        where to write the read data

    :param u32 offs:
        offset into OCM where to read from

    :param int size:
        how many bytes to read

.. _`asd_read_ocm_seg.description`:

Description
-----------

Return the number of bytes not read. Return 0 on success.

.. _`asd_write_ocm_seg`:

asd_write_ocm_seg
=================

.. c:function:: void asd_write_ocm_seg(struct asd_ha_struct *asd_ha, void *buffer, u32 offs, int size)

    write an on chip memory (OCM) segment

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param void \*buffer:
        where to read the write data

    :param u32 offs:
        offset into OCM to write to

    :param int size:
        how many bytes to write

.. _`asd_write_ocm_seg.description`:

Description
-----------

Return the number of bytes not written. Return 0 on success.

.. _`asd_read_ocm`:

asd_read_ocm
============

.. c:function:: int asd_read_ocm(struct asd_ha_struct *asd_ha)

    read on chip memory (OCM)

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

.. _`asd_find_flash_dir`:

asd_find_flash_dir
==================

.. c:function:: int asd_find_flash_dir(struct asd_ha_struct *asd_ha, struct asd_flash_dir *flash_dir)

    finds and reads the flash directory

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param struct asd_flash_dir \*flash_dir:
        pointer to flash directory structure

.. _`asd_find_flash_dir.description`:

Description
-----------

If found, the flash directory segment will be copied to
\ ``flash_dir``\ .  Return 1 if found, 0 if not.

.. _`asd_find_ll_by_id`:

asd_find_ll_by_id
=================

.. c:function:: void *asd_find_ll_by_id(void * const start, const u8 id0, const u8 id1)

    find a linked list entry by its id

    :param void \* const start:
        void pointer to the first element in the linked list

    :param const u8 id0:
        the first byte of the id  (offs 0)

    :param const u8 id1:
        the second byte of the id (offs 1)

.. _`asd_find_ll_by_id.description`:

Description
-----------

@start has to be the \_base\_ element start, since the
linked list entries's offset is from this pointer.
Some linked list entries use only the first id, in which case
you can pass 0xFF for the second.

.. _`asd_ms_get_phy_params`:

asd_ms_get_phy_params
=====================

.. c:function:: int asd_ms_get_phy_params(struct asd_ha_struct *asd_ha, struct asd_manuf_sec *manuf_sec)

    get phy parameters from the manufacturing sector

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param struct asd_manuf_sec \*manuf_sec:
        pointer to the manufacturing sector

.. _`asd_ms_get_phy_params.description`:

Description
-----------

The manufacturing sector contans also the linked list of sub-segments,
since when it was read, its size was taken from the flash directory,
not from the structure size.

HIDDEN phys do not count in the total count.  REPORTED phys cannot
be enabled but are reported and counted towards the total.
ENABLED phys are enabled by default and count towards the total.
The absolute total phy number is ASD_MAX_PHYS.  hw_prof->num_phys
merely specifies the number of phys the host adapter decided to
report.  E.g., it is possible for phys 0, 1 and 2 to be HIDDEN,
phys 3, 4 and 5 to be REPORTED and phys 6 and 7 to be ENABLED.
In this case ASD_MAX_PHYS is 8, hw_prof->num_phys is 5, and only 2
are actually enabled (enabled by default, max number of phys
enableable in this case).

.. _`asd_process_ms`:

asd_process_ms
==============

.. c:function:: int asd_process_ms(struct asd_ha_struct *asd_ha, struct asd_flash_dir *flash_dir)

    find and extract information from the manufacturing sector

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param struct asd_flash_dir \*flash_dir:
        pointer to the flash directory

.. _`asd_process_ctrl_a_user`:

asd_process_ctrl_a_user
=======================

.. c:function:: int asd_process_ctrl_a_user(struct asd_ha_struct *asd_ha, struct asd_flash_dir *flash_dir)

    process CTRL-A user settings

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param struct asd_flash_dir \*flash_dir:
        pointer to the flash directory

.. _`asd_read_flash`:

asd_read_flash
==============

.. c:function:: int asd_read_flash(struct asd_ha_struct *asd_ha)

    read flash memory

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

.. _`asd_verify_flash_seg`:

asd_verify_flash_seg
====================

.. c:function:: int asd_verify_flash_seg(struct asd_ha_struct *asd_ha, const void *src, u32 dest_offset, u32 bytes_to_verify)

    verify data with flash memory

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param const void \*src:
        pointer to the source data to be verified

    :param u32 dest_offset:
        offset from flash memory

    :param u32 bytes_to_verify:
        total bytes to verify

.. _`asd_write_flash_seg`:

asd_write_flash_seg
===================

.. c:function:: int asd_write_flash_seg(struct asd_ha_struct *asd_ha, const void *src, u32 dest_offset, u32 bytes_to_write)

    write data into flash memory

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param const void \*src:
        pointer to the source data to be written

    :param u32 dest_offset:
        offset from flash memory

    :param u32 bytes_to_write:
        total bytes to write

.. _`asd_erase_nv_sector`:

asd_erase_nv_sector
===================

.. c:function:: int asd_erase_nv_sector(struct asd_ha_struct *asd_ha, u32 flash_addr, u32 size)

    Erase the flash memory sectors.

    :param struct asd_ha_struct \*asd_ha:
        pointer to the host adapter structure

    :param u32 flash_addr:
        pointer to offset from flash memory

    :param u32 size:
        total bytes to erase.

.. This file was automatic generated / don't edit.

