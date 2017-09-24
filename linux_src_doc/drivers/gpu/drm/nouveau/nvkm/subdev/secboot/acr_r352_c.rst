.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/acr_r352.c

.. _`acr_r352_flcn_bl_desc`:

struct acr_r352_flcn_bl_desc
============================

.. c:type:: struct acr_r352_flcn_bl_desc

    DMEM bootloader descriptor

.. _`acr_r352_flcn_bl_desc.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_flcn_bl_desc {
        u32 reserved;
        u32 signature;
        u32 ctx_dma;
        u32 code_dma_base;
        u32 non_sec_code_off;
        u32 non_sec_code_size;
        u32 sec_code_off;
        u32 sec_code_size;
        u32 code_entry_point;
        u32 data_dma_base;
        u32 data_size;
        u32 code_dma_base1;
        u32 data_dma_base1;
    }

.. _`acr_r352_flcn_bl_desc.members`:

Members
-------

reserved
    *undescribed*

signature
    16B signature for secure code. 0s if no secure code

ctx_dma
    DMA context to be used by BL while loading code/data

code_dma_base
    256B-aligned Physical FB Address where code is located
    (falcon's \ ``$xcbase``\  register)

non_sec_code_off
    offset from code_dma_base where the non-secure code is
    located. The offset must be multiple of 256 to help perf

non_sec_code_size
    the size of the nonSecure code part.

sec_code_off
    offset from code_dma_base where the secure code is
    located. The offset must be multiple of 256 to help perf

sec_code_size
    offset from code_dma_base where the secure code is
    located. The offset must be multiple of 256 to help perf

code_entry_point
    code entry point which will be invoked by BL after
    code is loaded.

data_dma_base
    256B aligned Physical FB Address where data is located.
    (falcon's \ ``$xdbase``\  register)

data_size
    size of data block. Should be multiple of 256B

code_dma_base1
    *undescribed*

data_dma_base1
    *undescribed*

.. _`acr_r352_flcn_bl_desc.description`:

Description
-----------

Structure used by the bootloader to load the rest of the code. This has
to be filled by host and copied into DMEM at offset provided in the
hsflcn_bl_desc.bl_desc_dmem_load_off.

.. _`acr_r352_generate_flcn_bl_desc`:

acr_r352_generate_flcn_bl_desc
==============================

.. c:function:: void acr_r352_generate_flcn_bl_desc(const struct nvkm_acr *acr, const struct ls_ucode_img *img, u64 wpr_addr, void *_desc)

    generate generic BL descriptor for LS image

    :param const struct nvkm_acr \*acr:
        *undescribed*

    :param const struct ls_ucode_img \*img:
        *undescribed*

    :param u64 wpr_addr:
        *undescribed*

    :param void \*_desc:
        *undescribed*

.. _`hsflcn_acr_desc`:

struct hsflcn_acr_desc
======================

.. c:type:: struct hsflcn_acr_desc

    data section of the HS firmware

.. _`hsflcn_acr_desc.definition`:

Definition
----------

.. code-block:: c

    struct hsflcn_acr_desc {
        union ucode_reserved_space;
        u32 wpr_region_id;
        u32 wpr_offset;
        u32 mmu_mem_range;
    #define FLCN_ACR_MAX_REGIONS 2
        struct regions;
        u32 ucode_blob_size;
        u64 ucode_blob_base;
        struct vpr_desc;
    }

.. _`hsflcn_acr_desc.members`:

Members
-------

ucode_reserved_space
    *undescribed*

wpr_region_id
    region ID holding the WPR header and its details

wpr_offset
    offset from the WPR region holding the wpr header

mmu_mem_range
    *undescribed*

regions
    region descriptors

ucode_blob_size
    *undescribed*

ucode_blob_base
    *undescribed*

vpr_desc
    *undescribed*

.. _`hsflcn_acr_desc.description`:

Description
-----------

This header is to be copied at the beginning of DMEM by the HS bootloader.

.. _`acr_r352_lsf_lsb_header`:

struct acr_r352_lsf_lsb_header
==============================

.. c:type:: struct acr_r352_lsf_lsb_header

    LS firmware header

.. _`acr_r352_lsf_lsb_header.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_lsf_lsb_header {
        struct signature;
        u32 ucode_off;
        u32 ucode_size;
        u32 data_size;
        u32 bl_code_size;
        u32 bl_imem_off;
        u32 bl_data_off;
        u32 bl_data_size;
        u32 app_code_off;
        u32 app_code_size;
        u32 app_data_off;
        u32 app_data_size;
        u32 flags;
    }

.. _`acr_r352_lsf_lsb_header.members`:

Members
-------

signature
    signature to verify the firmware against

ucode_off
    offset of the ucode blob in the WPR region. The ucode
    blob contains the bootloader, code and data of the
    LS falcon

ucode_size
    size of the ucode blob, including bootloader

data_size
    size of the ucode blob data

bl_code_size
    size of the bootloader code

bl_imem_off
    offset in imem of the bootloader

bl_data_off
    offset of the bootloader data in WPR region

bl_data_size
    size of the bootloader data

app_code_off
    offset of the app code relative to ucode_off

app_code_size
    size of the app code

app_data_off
    offset of the app data relative to ucode_off

app_data_size
    size of the app data

flags
    flags for the secure bootloader

.. _`acr_r352_lsf_lsb_header.description`:

Description
-----------

This structure is written into the WPR region for each managed falcon. Each
instance is referenced by the lsb_offset member of the corresponding
lsf_wpr_header.

.. _`acr_r352_lsf_wpr_header`:

struct acr_r352_lsf_wpr_header
==============================

.. c:type:: struct acr_r352_lsf_wpr_header

    LS blob WPR Header

.. _`acr_r352_lsf_wpr_header.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_lsf_wpr_header {
        u32 falcon_id;
        u32 lsb_offset;
        u32 bootstrap_owner;
        u32 lazy_bootstrap;
        u32 status;
    #define LSF_IMAGE_STATUS_NONE 0
    #define LSF_IMAGE_STATUS_COPY 1
    #define LSF_IMAGE_STATUS_VALIDATION_CODE_FAILED 2
    #define LSF_IMAGE_STATUS_VALIDATION_DATA_FAILED 3
    #define LSF_IMAGE_STATUS_VALIDATION_DONE 4
    #define LSF_IMAGE_STATUS_VALIDATION_SKIPPED 5
    #define LSF_IMAGE_STATUS_BOOTSTRAP_READY 6
    }

.. _`acr_r352_lsf_wpr_header.members`:

Members
-------

falcon_id
    LS falcon ID

lsb_offset
    offset of the lsb_lsf_header in the WPR region

bootstrap_owner
    secure falcon reponsible for bootstrapping the LS falcon

lazy_bootstrap
    skip bootstrapping by ACR

status
    bootstrapping status

.. _`acr_r352_lsf_wpr_header.description`:

Description
-----------

An array of these is written at the beginning of the WPR region, one for
each managed falcon. The array is terminated by an instance which falcon_id
is LSF_FALCON_ID_INVALID.

.. _`ls_ucode_img_r352`:

struct ls_ucode_img_r352
========================

.. c:type:: struct ls_ucode_img_r352

    ucode image augmented with r352 headers

.. _`ls_ucode_img_r352.definition`:

Definition
----------

.. code-block:: c

    struct ls_ucode_img_r352 {
        struct ls_ucode_img base;
        struct acr_r352_lsf_wpr_header wpr_header;
        struct acr_r352_lsf_lsb_header lsb_header;
    }

.. _`ls_ucode_img_r352.members`:

Members
-------

base
    *undescribed*

wpr_header
    *undescribed*

lsb_header
    *undescribed*

.. _`acr_r352_ls_ucode_img_load`:

acr_r352_ls_ucode_img_load
==========================

.. c:function:: struct ls_ucode_img *acr_r352_ls_ucode_img_load(const struct acr_r352 *acr, const struct nvkm_secboot *sb, enum nvkm_secboot_falcon falcon_id)

    create a lsf_ucode_img and load it

    :param const struct acr_r352 \*acr:
        *undescribed*

    :param const struct nvkm_secboot \*sb:
        *undescribed*

    :param enum nvkm_secboot_falcon falcon_id:
        *undescribed*

.. _`acr_r352_ls_img_fill_headers`:

acr_r352_ls_img_fill_headers
============================

.. c:function:: u32 acr_r352_ls_img_fill_headers(struct acr_r352 *acr, struct ls_ucode_img_r352 *img, u32 offset)

    fill the WPR and LSB headers of an image

    :param struct acr_r352 \*acr:
        ACR to use

    :param struct ls_ucode_img_r352 \*img:
        image to generate for

    :param u32 offset:
        offset in the WPR region where this image starts

.. _`acr_r352_ls_img_fill_headers.description`:

Description
-----------

Allocate space in the WPR area from offset and write the WPR and LSB headers
accordingly.

.. _`acr_r352_ls_img_fill_headers.return`:

Return
------

offset at the end of this image.

.. _`acr_r352_ls_fill_headers`:

acr_r352_ls_fill_headers
========================

.. c:function:: int acr_r352_ls_fill_headers(struct acr_r352 *acr, struct list_head *imgs)

    fill WPR and LSB headers of all managed images

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct list_head \*imgs:
        *undescribed*

.. _`acr_r352_ls_write_wpr`:

acr_r352_ls_write_wpr
=====================

.. c:function:: int acr_r352_ls_write_wpr(struct acr_r352 *acr, struct list_head *imgs, struct nvkm_gpuobj *wpr_blob, u64 wpr_addr)

    write the WPR blob contents

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct list_head \*imgs:
        *undescribed*

    :param struct nvkm_gpuobj \*wpr_blob:
        *undescribed*

    :param u64 wpr_addr:
        *undescribed*

.. _`acr_r352_prepare_ls_blob`:

acr_r352_prepare_ls_blob
========================

.. c:function:: int acr_r352_prepare_ls_blob(struct acr_r352 *acr, struct nvkm_secboot *sb)

    prepare the LS blob

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct nvkm_secboot \*sb:
        *undescribed*

.. _`acr_r352_prepare_ls_blob.description`:

Description
-----------

For each securely managed falcon, load the FW, signatures and bootloaders and
prepare a ucode blob. Then, compute the offsets in the WPR region for each
blob, and finally write the headers and ucode blobs into a GPU object that
will be copied into the WPR region by the HS firmware.

.. _`acr_r352_prepare_hs_blob`:

acr_r352_prepare_hs_blob
========================

.. c:function:: int acr_r352_prepare_hs_blob(struct acr_r352 *acr, struct nvkm_secboot *sb, const char *fw, struct nvkm_gpuobj **blob, struct hsf_load_header *load_header, bool patch)

    load and prepare a HS blob and BL descriptor

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct nvkm_secboot \*sb:
        *undescribed*

    :param const char \*fw:
        *undescribed*

    :param struct nvkm_gpuobj \*\*blob:
        *undescribed*

    :param struct hsf_load_header \*load_header:
        *undescribed*

    :param bool patch:
        *undescribed*

.. _`acr_r352_prepare_hs_blob.description`:

Description
-----------

@sb secure boot instance to prepare for
\ ``fw``\  name of the HS firmware to load
\ ``blob``\  pointer to gpuobj that will be allocated to receive the HS FW payload
\ ``bl_desc``\  pointer to the BL descriptor to write for this firmware
\ ``patch``\  whether we should patch the HS descriptor (only for HS loaders)

.. _`acr_r352_load_blobs`:

acr_r352_load_blobs
===================

.. c:function:: int acr_r352_load_blobs(struct acr_r352 *acr, struct nvkm_secboot *sb)

    load blobs common to all ACR V1 versions.

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct nvkm_secboot \*sb:
        *undescribed*

.. _`acr_r352_load_blobs.description`:

Description
-----------

This includes the LS blob, HS ucode loading blob, and HS bootloader.

The HS ucode unload blob is only used on dGPU if the WPR region is variable.

.. _`acr_r352_load`:

acr_r352_load
=============

.. c:function:: int acr_r352_load(struct nvkm_acr *_acr, struct nvkm_falcon *falcon, struct nvkm_gpuobj *blob, u64 offset)

    prepare HS falcon to run the specified blob, mapped.

    :param struct nvkm_acr \*_acr:
        *undescribed*

    :param struct nvkm_falcon \*falcon:
        *undescribed*

    :param struct nvkm_gpuobj \*blob:
        *undescribed*

    :param u64 offset:
        *undescribed*

.. _`acr_r352_load.description`:

Description
-----------

Returns the start address to use, or a negative error value.

.. _`acr_r352_wpr_is_set`:

acr_r352_wpr_is_set
===================

.. c:function:: bool acr_r352_wpr_is_set(const struct acr_r352 *acr, const struct nvkm_secboot *sb)

    matches where it should be.

    :param const struct acr_r352 \*acr:
        *undescribed*

    :param const struct nvkm_secboot \*sb:
        *undescribed*

.. _`acr_r352_reset_nopmu`:

acr_r352_reset_nopmu
====================

.. c:function:: int acr_r352_reset_nopmu(struct acr_r352 *acr, struct nvkm_secboot *sb, unsigned long falcon_mask)

    dummy reset method when no PMU firmware is loaded

    :param struct acr_r352 \*acr:
        *undescribed*

    :param struct nvkm_secboot \*sb:
        *undescribed*

    :param unsigned long falcon_mask:
        *undescribed*

.. _`acr_r352_reset_nopmu.description`:

Description
-----------

Reset is done by re-executing secure boot from scratch, with lazy bootstrap
disabled. This has the effect of making all managed falcons ready-to-run.

.. _`acr_r352_pmu_bl_desc`:

struct acr_r352_pmu_bl_desc
===========================

.. c:type:: struct acr_r352_pmu_bl_desc

    PMU DMEM bootloader descriptor

.. _`acr_r352_pmu_bl_desc.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_pmu_bl_desc {
        u32 dma_idx;
        u32 code_dma_base;
        u32 code_size_total;
        u32 code_size_to_load;
        u32 code_entry_point;
        u32 data_dma_base;
        u32 data_size;
        u32 overlay_dma_base;
        u32 argc;
        u32 argv;
        u16 code_dma_base1;
        u16 data_dma_base1;
        u16 overlay_dma_base1;
    }

.. _`acr_r352_pmu_bl_desc.members`:

Members
-------

dma_idx
    DMA context to be used by BL while loading code/data

code_dma_base
    256B-aligned Physical FB Address where code is located

code_size_total
    *undescribed*

code_size_to_load
    size of the code part to load in PMU IMEM.

code_entry_point
    entry point in the code.

data_dma_base
    Physical FB address where data part of ucode is located

data_size
    Total size of the data portion.

overlay_dma_base
    Physical Fb address for resident code present in ucode

argc
    Total number of args

argv
    offset where args are copied into PMU's DMEM.

code_dma_base1
    *undescribed*

data_dma_base1
    *undescribed*

overlay_dma_base1
    *undescribed*

.. _`acr_r352_pmu_bl_desc.description`:

Description
-----------

Structure used by the PMU bootloader to load the rest of the code

.. _`acr_r352_generate_pmu_bl_desc`:

acr_r352_generate_pmu_bl_desc
=============================

.. c:function:: void acr_r352_generate_pmu_bl_desc(const struct nvkm_acr *acr, const struct ls_ucode_img *img, u64 wpr_addr, void *_desc)

    populate a DMEM BL descriptor for PMU LS image

    :param const struct nvkm_acr \*acr:
        *undescribed*

    :param const struct ls_ucode_img \*img:
        *undescribed*

    :param u64 wpr_addr:
        *undescribed*

    :param void \*_desc:
        *undescribed*

.. This file was automatic generated / don't edit.

