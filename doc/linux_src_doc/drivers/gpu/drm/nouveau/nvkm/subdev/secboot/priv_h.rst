.. -*- coding: utf-8; mode: rst -*-

======
priv.h
======


.. _`gm200_flcn_bl_desc`:

struct gm200_flcn_bl_desc
=========================

.. c:type:: gm200_flcn_bl_desc

    DMEM bootloader descriptor


.. _`gm200_flcn_bl_desc.definition`:

Definition
----------

.. code-block:: c

  struct gm200_flcn_bl_desc {
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
  };


.. _`gm200_flcn_bl_desc.members`:

Members
-------

:``signature[4]``:
    16B signature for secure code. 0s if no secure code

:``ctx_dma``:
    DMA context to be used by BL while loading code/data

:``code_dma_base``:
    256B-aligned Physical FB Address where code is located
    (falcon's $xcbase register)

:``non_sec_code_off``:
    offset from code_dma_base where the non-secure code is
    located. The offset must be multiple of 256 to help perf

:``non_sec_code_size``:
    the size of the nonSecure code part.

:``sec_code_off``:
    offset from code_dma_base where the secure code is
    located. The offset must be multiple of 256 to help perf

:``sec_code_size``:
    offset from code_dma_base where the secure code is
    located. The offset must be multiple of 256 to help perf

:``code_entry_point``:
    code entry point which will be invoked by BL after
    code is loaded.

:``data_dma_base``:
    256B aligned Physical FB Address where data is located.
    (falcon's $xdbase register)

:``data_size``:
    size of data block. Should be multiple of 256B




.. _`gm200_flcn_bl_desc.description`:

Description
-----------

Structure used by the bootloader to load the rest of the code. This has
to be filled by host and copied into DMEM at offset provided in the
hsflcn_bl_desc.bl_desc_dmem_load_off.



.. _`hsflcn_acr_desc`:

struct hsflcn_acr_desc
======================

.. c:type:: hsflcn_acr_desc

    data section of the HS firmware


.. _`hsflcn_acr_desc.definition`:

Definition
----------

.. code-block:: c

  struct hsflcn_acr_desc {
  };


.. _`hsflcn_acr_desc.members`:

Members
-------




.. _`hsflcn_acr_desc.description`:

Description
-----------


This header is to be copied at the beginning of DMEM by the HS bootloader.

