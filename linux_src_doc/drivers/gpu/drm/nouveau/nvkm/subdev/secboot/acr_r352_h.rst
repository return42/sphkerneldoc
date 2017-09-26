.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/acr_r352.h

.. _`acr_r352_ls_func`:

struct acr_r352_ls_func
=======================

.. c:type:: struct acr_r352_ls_func

    manages a single LS firmware

.. _`acr_r352_ls_func.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_ls_func {
        int (*load)(const struct nvkm_secboot *, struct ls_ucode_img *);
        void (*generate_bl_desc)(const struct nvkm_acr *, const struct ls_ucode_img *, u64, void *);
        u32 bl_desc_size;
        int (*post_run)(const struct nvkm_acr *, const struct nvkm_secboot *);
        u32 lhdr_flags;
    }

.. _`acr_r352_ls_func.members`:

Members
-------

load
    load the external firmware into a ls_ucode_img

generate_bl_desc
    function called on a block of bl_desc_size to generate the
    proper bootloader descriptor for this LS firmware

bl_desc_size
    size of the bootloader descriptor

post_run
    hook called right after the ACR is executed

lhdr_flags
    LS flags

.. _`acr_r352_func`:

struct acr_r352_func
====================

.. c:type:: struct acr_r352_func

    manages nuances between ACR versions

.. _`acr_r352_func.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352_func {
        void (*generate_hs_bl_desc)(const struct hsf_load_header *, void *, u64);
        void (*fixup_hs_desc)(struct acr_r352 *, struct nvkm_secboot *, void *);
        u32 hs_bl_desc_size;
        bool shadow_blob;
        struct ls_ucode_img *(*ls_ucode_img_load)(const struct acr_r352 *,const struct nvkm_secboot *, enum nvkm_secboot_falcon);
        int (*ls_fill_headers)(struct acr_r352 *, struct list_head *);
        int (*ls_write_wpr)(struct acr_r352 *, struct list_head *, struct nvkm_gpuobj *, u64);
        const struct acr_r352_ls_func *ls_func[NVKM_SECBOOT_FALCON_END];
    }

.. _`acr_r352_func.members`:

Members
-------

generate_hs_bl_desc
    function called on a block of bl_desc_size to generate
    the proper HS bootloader descriptor

fixup_hs_desc
    *undescribed*

hs_bl_desc_size
    size of the HS bootloader descriptor

shadow_blob
    *undescribed*

ls_ucode_img_load
    *undescribed*

ls_fill_headers
    *undescribed*

ls_write_wpr
    *undescribed*

ls_func
    *undescribed*

.. _`acr_r352`:

struct acr_r352
===============

.. c:type:: struct acr_r352

    ACR data for driver release 352 (and beyond)

.. _`acr_r352.definition`:

Definition
----------

.. code-block:: c

    struct acr_r352 {
        struct nvkm_acr base;
        const struct acr_r352_func *func;
        struct nvkm_gpuobj *load_blob;
        struct {
            struct hsf_load_header load_bl_header;
            u32 __load_apps[ACR_R352_MAX_APPS * 2];
        } ;
        struct nvkm_gpuobj *unload_blob;
        struct {
            struct hsf_load_header unload_bl_header;
            u32 __unload_apps[ACR_R352_MAX_APPS * 2];
        } ;
        void *hsbl_blob;
        void *hsbl_unload_blob;
        struct nvkm_gpuobj *ls_blob;
        bool firmware_ok;
        u32 lazy_bootstrap;
        enum {
            NON_SECURE = 0,RESET,RUNNING, } falcon_state[NVKM_SECBOOT_FALCON_END];
    }

.. _`acr_r352.members`:

Members
-------

base
    *undescribed*

func
    *undescribed*

load_blob
    *undescribed*

{unnamed_struct}
    anonymous

load_bl_header
    *undescribed*

__load_apps
    *undescribed*

unload_blob
    *undescribed*

{unnamed_struct}
    anonymous

unload_bl_header
    *undescribed*

__unload_apps
    *undescribed*

hsbl_blob
    *undescribed*

hsbl_unload_blob
    *undescribed*

ls_blob
    *undescribed*

firmware_ok
    *undescribed*

lazy_bootstrap
    *undescribed*

falcon_state
    *undescribed*

.. This file was automatic generated / don't edit.

