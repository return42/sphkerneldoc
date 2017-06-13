.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/hs_ucode.h

.. _`hsf_fw_header`:

struct hsf_fw_header
====================

.. c:type:: struct hsf_fw_header

    HS firmware descriptor

.. _`hsf_fw_header.definition`:

Definition
----------

.. code-block:: c

    struct hsf_fw_header {
        u32 sig_dbg_offset;
        u32 sig_dbg_size;
        u32 sig_prod_offset;
        u32 sig_prod_size;
        u32 patch_loc;
        u32 patch_sig;
        u32 hdr_offset;
        u32 hdr_size;
    }

.. _`hsf_fw_header.members`:

Members
-------

sig_dbg_offset
    offset of the debug signature

sig_dbg_size
    size of the debug signature

sig_prod_offset
    offset of the production signature

sig_prod_size
    size of the production signature

patch_loc
    offset of the offset (sic) of where the signature is

patch_sig
    offset of the offset (sic) to add to sig\_\*\_offset

hdr_offset
    offset of the load header (see struct hs_load_header)

hdr_size
    size of above header

.. _`hsf_fw_header.description`:

Description
-----------

This structure is embedded in the HS firmware image at
hs_bin_hdr.header_offset.

.. _`hsf_load_header`:

struct hsf_load_header
======================

.. c:type:: struct hsf_load_header

    HS firmware load header

.. _`hsf_load_header.definition`:

Definition
----------

.. code-block:: c

    struct hsf_load_header {
        u32 non_sec_code_off;
        u32 non_sec_code_size;
        u32 data_dma_base;
        u32 data_size;
        u32 num_apps;
        u32 apps;
    }

.. _`hsf_load_header.members`:

Members
-------

non_sec_code_off
    *undescribed*

non_sec_code_size
    *undescribed*

data_dma_base
    *undescribed*

data_size
    *undescribed*

num_apps
    *undescribed*

apps
    *undescribed*

.. This file was automatic generated / don't edit.

