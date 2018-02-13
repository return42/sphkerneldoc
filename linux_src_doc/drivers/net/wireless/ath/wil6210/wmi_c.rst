.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/wmi.c

.. _`wmi_addr_remap`:

wmi_addr_remap
==============

.. c:function:: u32 wmi_addr_remap(u32 x)

    \ ``x``\  - internal address If address have no valid AHB mapping, return 0

    :param u32 x:
        *undescribed*

.. _`wil_find_fw_mapping`:

wil_find_fw_mapping
===================

.. c:function:: struct fw_map *wil_find_fw_mapping(const char *section)

    \ ``section``\  - section name

    :param const char \*section:
        *undescribed*

.. _`wil_find_fw_mapping.description`:

Description
-----------

Return pointer to section or NULL if not found

.. _`wmi_buffer_block`:

wmi_buffer_block
================

.. c:function:: void __iomem *wmi_buffer_block(struct wil6210_priv *wil, __le32 ptr_, u32 size)

    \ ``ptr``\  - internal (linker) fw/ucode address \ ``size``\  - if non zero, validate the block does not exceed the device memory (bar)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param __le32 ptr_:
        *undescribed*

    :param u32 size:
        *undescribed*

.. _`wmi_buffer_block.description`:

Description
-----------

Valid buffer should be DWORD aligned

return address for accessing buffer from the host;
if buffer is not valid, return NULL.

.. _`wmi_addr`:

wmi_addr
========

.. c:function:: void __iomem *wmi_addr(struct wil6210_priv *wil, u32 ptr)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param u32 ptr:
        *undescribed*

.. _`wmi_evt_ignore`:

wmi_evt_ignore
==============

.. c:function:: void wmi_evt_ignore(struct wil6210_priv *wil, int id, void *d, int len)

    "unhandled events"

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param int id:
        *undescribed*

    :param void \*d:
        *undescribed*

    :param int len:
        *undescribed*

.. _`wmi_rxon`:

wmi_rxon
========

.. c:function:: int wmi_rxon(struct wil6210_priv *wil, bool on)

    turn radio on/off

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param bool on:
        turn on if true, off otherwise

.. _`wmi_rxon.description`:

Description
-----------

Only switch radio. Channel should be set separately.
No timeout for rxon - radio turned on forever unless some other call
turns it off

.. This file was automatic generated / don't edit.

