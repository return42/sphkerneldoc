.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/core/rtw_ieee80211.c

.. _`rtw_get_ie_ex`:

rtw_get_ie_ex
=============

.. c:function:: u8 *rtw_get_ie_ex(u8 *in_ie, uint in_len, u8 eid, u8 *oui, u8 oui_len, u8 *ie, uint *ielen)

    Search specific IE from a series of IEs

    :param in_ie:
        Address of IEs to search
    :type in_ie: u8 \*

    :param in_len:
        Length limit from in_ie
    :type in_len: uint

    :param eid:
        Element ID to match
    :type eid: u8

    :param oui:
        OUI to match
    :type oui: u8 \*

    :param oui_len:
        OUI length
    :type oui_len: u8

    :param ie:
        If not NULL and the specific IE is found, the IE will be copied to the buf starting from the specific IE
    :type ie: u8 \*

    :param ielen:
        If not NULL and the specific IE is found, will set to the length of the entire IE
    :type ielen: uint \*

.. _`rtw_get_ie_ex.return`:

Return
------

The address of the specific IE found, or NULL

.. _`rtw_ies_remove_ie`:

rtw_ies_remove_ie
=================

.. c:function:: int rtw_ies_remove_ie(u8 *ies, uint *ies_len, uint offset, u8 eid, u8 *oui, u8 oui_len)

    Find matching IEs and remove

    :param ies:
        Address of IEs to search
    :type ies: u8 \*

    :param ies_len:
        Pointer of length of ies, will update to new length
    :type ies_len: uint \*

    :param offset:
        The offset to start scarch
    :type offset: uint

    :param eid:
        Element ID to match
    :type eid: u8

    :param oui:
        OUI to match
    :type oui: u8 \*

    :param oui_len:
        OUI length
    :type oui_len: u8

.. _`rtw_ies_remove_ie.return`:

Return
------

\_SUCCESS: ies is updated, \_FAIL: not updated

.. _`rtw_get_wps_ie`:

rtw_get_wps_ie
==============

.. c:function:: u8 *rtw_get_wps_ie(u8 *in_ie, uint in_len, u8 *wps_ie, uint *wps_ielen)

    Search WPS IE from a series of IEs

    :param in_ie:
        Address of IEs to search
    :type in_ie: u8 \*

    :param in_len:
        Length limit from in_ie
    :type in_len: uint

    :param wps_ie:
        If not NULL and WPS IE is found, WPS IE will be copied to the buf starting from wps_ie
    :type wps_ie: u8 \*

    :param wps_ielen:
        If not NULL and WPS IE is found, will set to the length of the entire WPS IE
    :type wps_ielen: uint \*

.. _`rtw_get_wps_ie.return`:

Return
------

The address of the WPS IE found, or NULL

.. _`rtw_get_wps_attr`:

rtw_get_wps_attr
================

.. c:function:: u8 *rtw_get_wps_attr(u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_attr, u32 *len_attr)

    Search a specific WPS attribute from a given WPS IE

    :param wps_ie:
        Address of WPS IE to search
    :type wps_ie: u8 \*

    :param wps_ielen:
        Length limit from wps_ie
    :type wps_ielen: uint

    :param target_attr_id:
        The attribute ID of WPS attribute to search
    :type target_attr_id: u16

    :param buf_attr:
        If not NULL and the WPS attribute is found, WPS attribute will be copied to the buf starting from buf_attr
    :type buf_attr: u8 \*

    :param len_attr:
        If not NULL and the WPS attribute is found, will set to the length of the entire WPS attribute
    :type len_attr: u32 \*

.. _`rtw_get_wps_attr.return`:

Return
------

the address of the specific WPS attribute found, or NULL

.. _`rtw_get_wps_attr_content`:

rtw_get_wps_attr_content
========================

.. c:function:: u8 *rtw_get_wps_attr_content(u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_content, uint *len_content)

    Search a specific WPS attribute content from a given WPS IE

    :param wps_ie:
        Address of WPS IE to search
    :type wps_ie: u8 \*

    :param wps_ielen:
        Length limit from wps_ie
    :type wps_ielen: uint

    :param target_attr_id:
        The attribute ID of WPS attribute to search
    :type target_attr_id: u16

    :param buf_content:
        If not NULL and the WPS attribute is found, WPS attribute content will be copied to the buf starting from buf_content
    :type buf_content: u8 \*

    :param len_content:
        If not NULL and the WPS attribute is found, will set to the length of the WPS attribute content
    :type len_content: uint \*

.. _`rtw_get_wps_attr_content.return`:

Return
------

the address of the specific WPS attribute content found, or NULL

.. _`rtw_ieee802_11_parse_elems`:

rtw_ieee802_11_parse_elems
==========================

.. c:function:: ParseRes rtw_ieee802_11_parse_elems(u8 *start, uint len, struct rtw_ieee802_11_elems *elems, int show_errors)

    Parse information elements in management frames

    :param start:
        Pointer to the start of IEs
    :type start: u8 \*

    :param len:
        Length of IE buffer in octets
    :type len: uint

    :param elems:
        Data structure for parsed elements
    :type elems: struct rtw_ieee802_11_elems \*

    :param show_errors:
        Whether to show parsing errors in debug log
    :type show_errors: int

.. _`rtw_ieee802_11_parse_elems.return`:

Return
------

Parsing result

.. This file was automatic generated / don't edit.

