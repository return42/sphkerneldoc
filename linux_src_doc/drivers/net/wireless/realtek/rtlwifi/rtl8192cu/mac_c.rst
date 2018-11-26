.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/realtek/rtlwifi/rtl8192cu/mac.c

.. _`rtl92c_llt_write`:

rtl92c_llt_write
================

.. c:function:: bool rtl92c_llt_write(struct ieee80211_hw *hw, u32 address, u32 data)

    LLT table write access

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param address:
        LLT logical address.
    :type address: u32

    :param data:
        LLT data content
    :type data: u32

.. _`rtl92c_llt_write.description`:

Description
-----------

Realtek hardware access function.

.. _`rtl92c_init_llt_table`:

rtl92c_init_llt_table
=====================

.. c:function:: bool rtl92c_init_llt_table(struct ieee80211_hw *hw, u32 boundary)

    Init LLT table

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param boundary:
        *undescribed*
    :type boundary: u32

.. _`rtl92c_init_llt_table.description`:

Description
-----------

Realtek hardware access function.

.. This file was automatic generated / don't edit.

