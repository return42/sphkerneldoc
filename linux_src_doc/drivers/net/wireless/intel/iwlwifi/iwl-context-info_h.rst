.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-context-info.h

.. _`iwl_context_info_flags`:

enum iwl_context_info_flags
===========================

.. c:type:: enum iwl_context_info_flags

    Context information control flags

.. _`iwl_context_info_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_context_info_flags {
        IWL_CTXT_INFO_AUTO_FUNC_INIT,
        IWL_CTXT_INFO_EARLY_DEBUG,
        IWL_CTXT_INFO_ENABLE_CDMP,
        IWL_CTXT_INFO_RB_CB_SIZE_POS,
        IWL_CTXT_INFO_TFD_FORMAT_LONG,
        IWL_CTXT_INFO_RB_SIZE_POS,
        IWL_CTXT_INFO_RB_SIZE_1K,
        IWL_CTXT_INFO_RB_SIZE_2K,
        IWL_CTXT_INFO_RB_SIZE_4K,
        IWL_CTXT_INFO_RB_SIZE_8K,
        IWL_CTXT_INFO_RB_SIZE_12K,
        IWL_CTXT_INFO_RB_SIZE_16K,
        IWL_CTXT_INFO_RB_SIZE_20K,
        IWL_CTXT_INFO_RB_SIZE_24K,
        IWL_CTXT_INFO_RB_SIZE_28K,
        IWL_CTXT_INFO_RB_SIZE_32K
    };

.. _`iwl_context_info_flags.constants`:

Constants
---------

IWL_CTXT_INFO_AUTO_FUNC_INIT
    If set, FW will not wait before interrupting
    the init done for driver command that configures several system modes

IWL_CTXT_INFO_EARLY_DEBUG
    enable early debug

IWL_CTXT_INFO_ENABLE_CDMP
    enable core dump

IWL_CTXT_INFO_RB_CB_SIZE_POS
    position of the RBD Cyclic Buffer Size
    exponent, the actual size is 2\*\*value, valid sizes are 8-2048.
    The value is four bits long. Maximum valid exponent is 12

IWL_CTXT_INFO_TFD_FORMAT_LONG
    use long TFD Format (the
    default is short format - not supported by the driver)

IWL_CTXT_INFO_RB_SIZE_POS
    RB size position
    (values are IWL_CTXT_INFO_RB_SIZE\_\*K)

IWL_CTXT_INFO_RB_SIZE_1K
    Value for 1K RB size

IWL_CTXT_INFO_RB_SIZE_2K
    Value for 2K RB size

IWL_CTXT_INFO_RB_SIZE_4K
    Value for 4K RB size

IWL_CTXT_INFO_RB_SIZE_8K
    Value for 8K RB size

IWL_CTXT_INFO_RB_SIZE_12K
    Value for 12K RB size

IWL_CTXT_INFO_RB_SIZE_16K
    Value for 16K RB size

IWL_CTXT_INFO_RB_SIZE_20K
    Value for 20K RB size

IWL_CTXT_INFO_RB_SIZE_24K
    Value for 24K RB size

IWL_CTXT_INFO_RB_SIZE_28K
    Value for 28K RB size

IWL_CTXT_INFO_RB_SIZE_32K
    Value for 32K RB size

.. This file was automatic generated / don't edit.

