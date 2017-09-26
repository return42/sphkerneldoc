.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/acr_r367.c

.. _`acr_r367_lsf_lsb_header`:

struct acr_r367_lsf_lsb_header
==============================

.. c:type:: struct acr_r367_lsf_lsb_header

    LS firmware header

.. _`acr_r367_lsf_lsb_header.definition`:

Definition
----------

.. code-block:: c

    struct acr_r367_lsf_lsb_header {
        struct {
            u8 prd_keys[2][16];
            u8 dbg_keys[2][16];
            u32 b_prd_present;
            u32 b_dbg_present;
            u32 falcon_id;
            u32 supports_versioning;
            u32 version;
            u32 depmap_count;
            u8 depmap[LSF_LSB_DEPMAP_SIZE * 2 * 4];
            u8 kdf[16];
        } signature;
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

.. _`acr_r367_lsf_lsb_header.members`:

Members
-------

signature
    *undescribed*

prd_keys
    *undescribed*

dbg_keys
    *undescribed*

b_prd_present
    *undescribed*

b_dbg_present
    *undescribed*

falcon_id
    *undescribed*

supports_versioning
    *undescribed*

version
    *undescribed*

depmap_count
    *undescribed*

depmap
    *undescribed*

kdf
    *undescribed*

ucode_off
    *undescribed*

ucode_size
    *undescribed*

data_size
    *undescribed*

bl_code_size
    *undescribed*

bl_imem_off
    *undescribed*

bl_data_off
    *undescribed*

bl_data_size
    *undescribed*

app_code_off
    *undescribed*

app_code_size
    *undescribed*

app_data_off
    *undescribed*

app_data_size
    *undescribed*

flags
    *undescribed*

.. _`acr_r367_lsf_lsb_header.description`:

Description
-----------

See also struct acr_r352_lsf_lsb_header for documentation.

.. _`acr_r367_lsf_wpr_header`:

struct acr_r367_lsf_wpr_header
==============================

.. c:type:: struct acr_r367_lsf_wpr_header

    LS blob WPR Header

.. _`acr_r367_lsf_wpr_header.definition`:

Definition
----------

.. code-block:: c

    struct acr_r367_lsf_wpr_header {
        u32 falcon_id;
        u32 lsb_offset;
        u32 bootstrap_owner;
        u32 lazy_bootstrap;
        u32 bin_version;
        u32 status;
    #define LSF_IMAGE_STATUS_NONE 0
    #define LSF_IMAGE_STATUS_COPY 1
    #define LSF_IMAGE_STATUS_VALIDATION_CODE_FAILED 2
    #define LSF_IMAGE_STATUS_VALIDATION_DATA_FAILED 3
    #define LSF_IMAGE_STATUS_VALIDATION_DONE 4
    #define LSF_IMAGE_STATUS_VALIDATION_SKIPPED 5
    #define LSF_IMAGE_STATUS_BOOTSTRAP_READY 6
    #define LSF_IMAGE_STATUS_REVOCATION_CHECK_FAILED 7
    }

.. _`acr_r367_lsf_wpr_header.members`:

Members
-------

falcon_id
    *undescribed*

lsb_offset
    *undescribed*

bootstrap_owner
    *undescribed*

lazy_bootstrap
    *undescribed*

bin_version
    *undescribed*

status
    *undescribed*

.. _`acr_r367_lsf_wpr_header.description`:

Description
-----------

See also struct acr_r352_lsf_wpr_header for documentation.

.. _`ls_ucode_img_r367`:

struct ls_ucode_img_r367
========================

.. c:type:: struct ls_ucode_img_r367

    ucode image augmented with r367 headers

.. _`ls_ucode_img_r367.definition`:

Definition
----------

.. code-block:: c

    struct ls_ucode_img_r367 {
        struct ls_ucode_img base;
        struct acr_r367_lsf_wpr_header wpr_header;
        struct acr_r367_lsf_lsb_header lsb_header;
    }

.. _`ls_ucode_img_r367.members`:

Members
-------

base
    *undescribed*

wpr_header
    *undescribed*

lsb_header
    *undescribed*

.. This file was automatic generated / don't edit.

