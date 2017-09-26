.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/ls_ucode.h

.. _`ls_ucode_img_desc`:

struct ls_ucode_img_desc
========================

.. c:type:: struct ls_ucode_img_desc

    descriptor of firmware image

.. _`ls_ucode_img_desc.definition`:

Definition
----------

.. code-block:: c

    struct ls_ucode_img_desc {
        u32 descriptor_size;
        u32 image_size;
        u32 tools_version;
        u32 app_version;
        char date[64];
        u32 bootloader_start_offset;
        u32 bootloader_size;
        u32 bootloader_imem_offset;
        u32 bootloader_entry_point;
        u32 app_start_offset;
        u32 app_size;
        u32 app_imem_offset;
        u32 app_imem_entry;
        u32 app_dmem_offset;
        u32 app_resident_code_offset;
        u32 app_resident_code_size;
        u32 app_resident_data_offset;
        u32 app_resident_data_size;
        u32 nb_overlays;
        struct {
            u32 start;
            u32 size;
        } load_ovl[64];
        u32 compressed;
    }

.. _`ls_ucode_img_desc.members`:

Members
-------

descriptor_size
    size of this descriptor

image_size
    size of the whole image

tools_version
    *undescribed*

app_version
    *undescribed*

date
    *undescribed*

bootloader_start_offset
    start offset of the bootloader in ucode image

bootloader_size
    size of the bootloader

bootloader_imem_offset
    start off set of the bootloader in IMEM

bootloader_entry_point
    entry point of the bootloader in IMEM

app_start_offset
    start offset of the LS firmware

app_size
    size of the LS firmware's code and data

app_imem_offset
    offset of the app in IMEM

app_imem_entry
    entry point of the app in IMEM

app_dmem_offset
    offset of the data in DMEM

app_resident_code_offset
    offset of app code from app_start_offset

app_resident_code_size
    size of the code

app_resident_data_offset
    offset of data from app_start_offset

app_resident_data_size
    size of data

nb_overlays
    *undescribed*

load_ovl
    *undescribed*

compressed
    *undescribed*

.. _`ls_ucode_img_desc.description`:

Description
-----------

A firmware image contains the code, data, and bootloader of a given LS
falcon in a single blob. This structure describes where everything is.

This can be generated from a (bootloader, code, data) set if they have
been loaded separately, or come directly from a file.

.. _`ls_ucode_img`:

struct ls_ucode_img
===================

.. c:type:: struct ls_ucode_img

    temporary storage for loaded LS firmwares

.. _`ls_ucode_img.definition`:

Definition
----------

.. code-block:: c

    struct ls_ucode_img {
        struct list_head node;
        enum nvkm_secboot_falcon falcon_id;
        struct ls_ucode_img_desc ucode_desc;
        u8 *ucode_data;
        u32 ucode_size;
        u32 ucode_off;
        u8 *sig;
        u32 sig_size;
    }

.. _`ls_ucode_img.members`:

Members
-------

node
    to link within lsf_ucode_mgr

falcon_id
    ID of the falcon this LS firmware is for

ucode_desc
    loaded or generated map of ucode_data

ucode_data
    firmware payload (code and data)

ucode_size
    size in bytes of data in ucode_data

ucode_off
    offset of the ucode in ucode_data

sig
    size:           size of the signature in bytes

sig_size
    *undescribed*

.. _`ls_ucode_img.description`:

Description
-----------

Preparing the WPR LS blob requires information about all the LS firmwares
(size, etc) to be known. This structure contains all the data of one LS
firmware.

.. _`fw_bin_header`:

struct fw_bin_header
====================

.. c:type:: struct fw_bin_header

    header of firmware files

.. _`fw_bin_header.definition`:

Definition
----------

.. code-block:: c

    struct fw_bin_header {
        u32 bin_magic;
        u32 bin_ver;
        u32 bin_size;
        u32 header_offset;
        u32 data_offset;
        u32 data_size;
    }

.. _`fw_bin_header.members`:

Members
-------

bin_magic
    always 0x3b1d14f0

bin_ver
    version of the bin format

bin_size
    entire image size including this header

header_offset
    offset of the firmware/bootloader header in the file

data_offset
    offset of the firmware/bootloader payload in the file

data_size
    size of the payload

.. _`fw_bin_header.description`:

Description
-----------

This header is located at the beginning of the HS firmware and HS bootloader
files, to describe where the headers and data can be found.

.. _`fw_bl_desc`:

struct fw_bl_desc
=================

.. c:type:: struct fw_bl_desc

    firmware bootloader descriptor

.. _`fw_bl_desc.definition`:

Definition
----------

.. code-block:: c

    struct fw_bl_desc {
        u32 start_tag;
        u32 dmem_load_off;
        u32 code_off;
        u32 code_size;
        u32 data_off;
        u32 data_size;
    }

.. _`fw_bl_desc.members`:

Members
-------

start_tag
    starting tag of bootloader

dmem_load_off
    *undescribed*

code_off
    offset of code section

code_size
    size of code section

data_off
    offset of data section

data_size
    size of data section

.. _`fw_bl_desc.description`:

Description
-----------

This structure is embedded in bootloader firmware files at to describe the
IMEM and DMEM layout expected by the bootloader.

.. This file was automatic generated / don't edit.

