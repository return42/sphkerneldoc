.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-context-info-gen3.h

.. _`iwl_prph_scratch_mtr_format`:

enum iwl_prph_scratch_mtr_format
================================

.. c:type:: enum iwl_prph_scratch_mtr_format

    tfd size configuration

.. _`iwl_prph_scratch_mtr_format.definition`:

Definition
----------

.. code-block:: c

    enum iwl_prph_scratch_mtr_format {
        IWL_PRPH_MTR_FORMAT_16B,
        IWL_PRPH_MTR_FORMAT_32B,
        IWL_PRPH_MTR_FORMAT_64B,
        IWL_PRPH_MTR_FORMAT_256B
    };

.. _`iwl_prph_scratch_mtr_format.constants`:

Constants
---------

IWL_PRPH_MTR_FORMAT_16B
    16 bit tfd

IWL_PRPH_MTR_FORMAT_32B
    32 bit tfd

IWL_PRPH_MTR_FORMAT_64B
    64 bit tfd

IWL_PRPH_MTR_FORMAT_256B
    256 bit tfd

.. _`iwl_prph_scratch_flags`:

enum iwl_prph_scratch_flags
===========================

.. c:type:: enum iwl_prph_scratch_flags

    PRPH scratch control flags

.. _`iwl_prph_scratch_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_prph_scratch_flags {
        IWL_PRPH_SCRATCH_EARLY_DEBUG_EN,
        IWL_PRPH_SCRATCH_EDBG_DEST_DRAM,
        IWL_PRPH_SCRATCH_EDBG_DEST_INTERNAL,
        IWL_PRPH_SCRATCH_EDBG_DEST_ST_ARBITER,
        IWL_PRPH_SCRATCH_EDBG_DEST_TB22DTF,
        IWL_PRPH_SCRATCH_RB_SIZE_4K,
        IWL_PRPH_SCRATCH_MTR_MODE,
        IWL_PRPH_SCRATCH_MTR_FORMAT
    };

.. _`iwl_prph_scratch_flags.constants`:

Constants
---------

IWL_PRPH_SCRATCH_EARLY_DEBUG_EN
    enable early debug conf

IWL_PRPH_SCRATCH_EDBG_DEST_DRAM
    use DRAM, with size allocated
    in hwm config.

IWL_PRPH_SCRATCH_EDBG_DEST_INTERNAL
    use buffer on SRAM

IWL_PRPH_SCRATCH_EDBG_DEST_ST_ARBITER
    use st arbiter, mainly for
    multicomm.

IWL_PRPH_SCRATCH_EDBG_DEST_TB22DTF
    route debug data to SoC HW

IWL_PRPH_SCRATCH_RB_SIZE_4K
    *undescribed*

IWL_PRPH_SCRATCH_MTR_MODE
    format used for completion - 0: for
    completion descriptor, 1 for responses (legacy)

IWL_PRPH_SCRATCH_MTR_FORMAT
    a mask for the size of the tfd.

.. _`iwl_prph_scratch_flags.there-are-4-optional-values`:

There are 4 optional values
---------------------------

0: 16 bit, 1: 32 bit, 2: 64 bit,
3: 256 bit.

.. This file was automatic generated / don't edit.

