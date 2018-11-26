.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/wmi.c

.. _`wmi_addr_remap`:

wmi_addr_remap
==============

.. c:function:: u32 wmi_addr_remap(u32 x)

    \ ``x``\  - internal address If address have no valid AHB mapping, return 0

    :param x:
        *undescribed*
    :type x: u32

.. _`wil_find_fw_mapping`:

wil_find_fw_mapping
===================

.. c:function:: struct fw_map *wil_find_fw_mapping(const char *section)

    \ ``section``\  - section name

    :param section:
        *undescribed*
    :type section: const char \*

.. _`wil_find_fw_mapping.description`:

Description
-----------

Return pointer to section or NULL if not found

.. _`wmi_buffer_block`:

wmi_buffer_block
================

.. c:function:: void __iomem *wmi_buffer_block(struct wil6210_priv *wil, __le32 ptr_, u32 size)

    \ ``ptr``\  - internal (linker) fw/ucode address \ ``size``\  - if non zero, validate the block does not exceed the device memory (bar)

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param ptr_:
        *undescribed*
    :type ptr_: __le32

    :param size:
        *undescribed*
    :type size: u32

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

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param ptr:
        *undescribed*
    :type ptr: u32

.. _`wil_find_cid_ringid_sta`:

wil_find_cid_ringid_sta
=======================

.. c:function:: int wil_find_cid_ringid_sta(struct wil6210_priv *wil, struct wil6210_vif *vif, int *cid, int *ringid)

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param vif:
        *undescribed*
    :type vif: struct wil6210_vif \*

    :param cid:
        *undescribed*
    :type cid: int \*

    :param ringid:
        *undescribed*
    :type ringid: int \*

.. _`wil_find_cid_ringid_sta.description`:

Description
-----------

return error, if other interfaces are used or ring was not found

.. _`wmi_evt_ignore`:

wmi_evt_ignore
==============

.. c:function:: void wmi_evt_ignore(struct wil6210_vif *vif, int id, void *d, int len)

    "unhandled events"

    :param vif:
        *undescribed*
    :type vif: struct wil6210_vif \*

    :param id:
        *undescribed*
    :type id: int

    :param d:
        *undescribed*
    :type d: void \*

    :param len:
        *undescribed*
    :type len: int

.. _`wmi_rxon`:

wmi_rxon
========

.. c:function:: int wmi_rxon(struct wil6210_priv *wil, bool on)

    turn radio on/off

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param on:
        turn on if true, off otherwise
    :type on: bool

.. _`wmi_rxon.description`:

Description
-----------

Only switch radio. Channel should be set separately.
No timeout for rxon - radio turned on forever unless some other call
turns it off

.. This file was automatic generated / don't edit.

