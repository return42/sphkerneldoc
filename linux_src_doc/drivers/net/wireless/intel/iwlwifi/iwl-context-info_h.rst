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
        IWL_CTXT_INFO_RB_SIZE_4K,
        IWL_CTXT_INFO_RB_CB_SIZE_POS,
        IWL_CTXT_INFO_TFD_FORMAT_LONG
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

IWL_CTXT_INFO_RB_SIZE_4K
    Use 4K RB size (the default is 2K)

IWL_CTXT_INFO_RB_CB_SIZE_POS
    position of the RBD Cyclic Buffer Size
    exponent, the actual size is 2\*\*value, valid sizes are 8-2048.
    The value is four bits long. Maximum valid exponent is 12

IWL_CTXT_INFO_TFD_FORMAT_LONG
    use long TFD Format (the
    default is short format - not supported by the driver)

.. This file was automatic generated / don't edit.

