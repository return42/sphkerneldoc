.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/context.h

.. _`iwl_ctxt_id_and_color`:

enum iwl_ctxt_id_and_color
==========================

.. c:type:: enum iwl_ctxt_id_and_color

    ID and color fields in context dword

.. _`iwl_ctxt_id_and_color.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ctxt_id_and_color {
        FW_CTXT_ID_POS,
        FW_CTXT_ID_MSK,
        FW_CTXT_COLOR_POS,
        FW_CTXT_COLOR_MSK,
        FW_CTXT_INVALID
    };

.. _`iwl_ctxt_id_and_color.constants`:

Constants
---------

FW_CTXT_ID_POS
    position of the ID

FW_CTXT_ID_MSK
    mask of the ID

FW_CTXT_COLOR_POS
    position of the color

FW_CTXT_COLOR_MSK
    mask of the color

FW_CTXT_INVALID
    value used to indicate unused/invalid

.. This file was automatic generated / don't edit.

