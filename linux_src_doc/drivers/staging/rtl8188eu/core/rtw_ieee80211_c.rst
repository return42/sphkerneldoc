.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8188eu/core/rtw_ieee80211.c

.. _`rtw_get_wps_ie`:

rtw_get_wps_ie
==============

.. c:function:: u8 *rtw_get_wps_ie(u8 *in_ie, uint in_len, u8 *wps_ie, uint *wps_ielen)

    Search WPS IE from a series of IEs

    :param u8 \*in_ie:
        Address of IEs to search

    :param uint in_len:
        Length limit from in_ie

    :param u8 \*wps_ie:
        If not NULL and WPS IE is found, WPS IE will be copied to the buf starting from wps_ie

    :param uint \*wps_ielen:
        If not NULL and WPS IE is found, will set to the length of the entire WPS IE

.. _`rtw_get_wps_ie.return`:

Return
------

The address of the WPS IE found, or NULL

.. _`rtw_get_wps_attr`:

rtw_get_wps_attr
================

.. c:function:: u8 *rtw_get_wps_attr(u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_attr, u32 *len_attr)

    Search a specific WPS attribute from a given WPS IE

    :param u8 \*wps_ie:
        Address of WPS IE to search

    :param uint wps_ielen:
        Length limit from wps_ie

    :param u16 target_attr_id:
        The attribute ID of WPS attribute to search

    :param u8 \*buf_attr:
        If not NULL and the WPS attribute is found, WPS attribute will be copied to the buf starting from buf_attr

    :param u32 \*len_attr:
        If not NULL and the WPS attribute is found, will set to the length of the entire WPS attribute

.. _`rtw_get_wps_attr.return`:

Return
------

the address of the specific WPS attribute found, or NULL

.. _`rtw_get_wps_attr_content`:

rtw_get_wps_attr_content
========================

.. c:function:: u8 *rtw_get_wps_attr_content(u8 *wps_ie, uint wps_ielen, u16 target_attr_id, u8 *buf_content, uint *len_content)

    Search a specific WPS attribute content from a given WPS IE

    :param u8 \*wps_ie:
        Address of WPS IE to search

    :param uint wps_ielen:
        Length limit from wps_ie

    :param u16 target_attr_id:
        The attribute ID of WPS attribute to search

    :param u8 \*buf_content:
        If not NULL and the WPS attribute is found, WPS attribute content will be copied to the buf starting from buf_content

    :param uint \*len_content:
        If not NULL and the WPS attribute is found, will set to the length of the WPS attribute content

.. _`rtw_get_wps_attr_content.return`:

Return
------

the address of the specific WPS attribute content found, or NULL

.. _`rtw_ieee802_11_parse_elems`:

rtw_ieee802_11_parse_elems
==========================

.. c:function:: enum parse_res rtw_ieee802_11_parse_elems(u8 *start, uint len, struct rtw_ieee802_11_elems *elems, int show_errors)

    Parse information elements in management frames

    :param u8 \*start:
        Pointer to the start of IEs

    :param uint len:
        Length of IE buffer in octets

    :param struct rtw_ieee802_11_elems \*elems:
        Data structure for parsed elements

    :param int show_errors:
        Whether to show parsing errors in debug log

.. _`rtw_ieee802_11_parse_elems.return`:

Return
------

Parsing result

.. This file was automatic generated / don't edit.

