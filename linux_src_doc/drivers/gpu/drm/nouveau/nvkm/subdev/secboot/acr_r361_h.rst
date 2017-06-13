.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/acr_r361.h

.. _`acr_r361_flcn_bl_desc`:

struct acr_r361_flcn_bl_desc
============================

.. c:type:: struct acr_r361_flcn_bl_desc

    DMEM bootloader descriptor

.. _`acr_r361_flcn_bl_desc.definition`:

Definition
----------

.. code-block:: c

    struct acr_r361_flcn_bl_desc {
        u32 reserved[4];
        u32 signature[4];
        u32 ctx_dma;
        struct flcn_u64 code_dma_base;
        u32 non_sec_code_off;
        u32 non_sec_code_size;
        u32 sec_code_off;
        u32 sec_code_size;
        u32 code_entry_point;
        struct flcn_u64 data_dma_base;
        u32 data_size;
    }

.. _`acr_r361_flcn_bl_desc.members`:

Members
-------

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

.. _`acr_r361_flcn_bl_desc.description`:

Description
-----------

Structure used by the bootloader to load the rest of the code. This has
to be filled by host and copied into DMEM at offset provided in the
hsflcn_bl_desc.bl_desc_dmem_load_off.

.. This file was automatic generated / don't edit.

