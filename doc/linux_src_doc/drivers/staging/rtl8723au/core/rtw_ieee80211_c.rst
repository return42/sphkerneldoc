.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723au/core/rtw_ieee80211.c

.. _`rtw_get_ie23a_ex`:

rtw_get_ie23a_ex
================

.. c:function:: u8 *rtw_get_ie23a_ex(u8 *in_ie, uint in_len, u8 eid, u8 *oui, u8 oui_len, u8 *ie, uint *ielen)

    Search specific IE from a series of IEs

    :param u8 \*in_ie:
        Address of IEs to search

    :param uint in_len:
        Length limit from in_ie

    :param u8 eid:
        Element ID to match

    :param u8 \*oui:
        OUI to match

    :param u8 oui_len:
        OUI length

    :param u8 \*ie:
        If not NULL and the specific IE is found, the IE will be copied
        to the buf starting from the specific IE

    :param uint \*ielen:
        If not NULL and the specific IE is found, will set to the length
        of the entire IE

.. _`rtw_get_ie23a_ex.return`:

Return
------

The address of the specific IE found, or NULL

.. _`rtw_ies_remove_ie23a`:

rtw_ies_remove_ie23a
====================

.. c:function:: int rtw_ies_remove_ie23a(u8 *ies, uint *ies_len, uint offset, u8 eid, u8 *oui, u8 oui_len)

    Find matching IEs and remove

    :param u8 \*ies:
        Address of IEs to search

    :param uint \*ies_len:
        Pointer of length of ies, will update to new length

    :param uint offset:
        The offset to start search

    :param u8 eid:
        Element ID to match

    :param u8 \*oui:
        OUI to match

    :param u8 oui_len:
        OUI length

.. _`rtw_ies_remove_ie23a.return`:

Return
------

_SUCCESS: ies is updated, \_FAIL: not updated

.. _`rtw_get_wps_attr23a`:

rtw_get_wps_attr23a
===================

.. c:function:: const u8 *rtw_get_wps_attr23a(const u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_attr, u32 *len_attr)

    Search a specific WPS attribute from a given WPS IE

    :param const u8 \*wps_ie:
        Address of WPS IE to search

    :param uint wps_ielen:
        Length limit from wps_ie

    :param u16 target_attr_id:
        The attribute ID of WPS attribute to search

    :param u8 \*buf_attr:
        If not NULL and the WPS attribute is found, WPS attribute
        will be copied to the buf starting from buf_attr

    :param u32 \*len_attr:
        If not NULL and the WPS attribute is found, will set to the
        length of the entire WPS attribute

.. _`rtw_get_wps_attr23a.return`:

Return
------

the address of the specific WPS attribute found, or NULL

.. _`rtw_get_wps_attr_content23a`:

rtw_get_wps_attr_content23a
===========================

.. c:function:: const u8 *rtw_get_wps_attr_content23a(const u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_content)

    Search a specific WPS attribute content from a given WPS IE

    :param const u8 \*wps_ie:
        Address of WPS IE to search

    :param uint wps_ielen:
        Length limit from wps_ie

    :param u16 target_attr_id:
        The attribute ID of WPS attribute to search

    :param u8 \*buf_content:
        If not NULL and the WPS attribute is found, WPS attribute
        content will be copied to the buf starting from buf_content

.. _`rtw_get_wps_attr_content23a.return`:

Return
------

the address of the specific WPS attribute content found, or NULL

.. This file was automatic generated / don't edit.

