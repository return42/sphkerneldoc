.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/ieee80211_radiotap.h

.. _`ieee80211_radiotap_header`:

struct ieee80211_radiotap_header
================================

.. c:type:: struct ieee80211_radiotap_header

    base radiotap header

.. _`ieee80211_radiotap_header.definition`:

Definition
----------

.. code-block:: c

    struct ieee80211_radiotap_header {
        uint8_t it_version;
        uint8_t it_pad;
        __le16 it_len;
        __le32 it_present;
    }

.. _`ieee80211_radiotap_header.members`:

Members
-------

it_version
    radiotap version, always 0

it_pad
    padding (or alignment)

it_len
    overall radiotap header length

it_present
    (first) present word

.. _`ieee80211_get_radiotap_len`:

ieee80211_get_radiotap_len
==========================

.. c:function:: u16 ieee80211_get_radiotap_len(const char *data)

    get radiotap header length

    :param data:
        *undescribed*
    :type data: const char \*

.. This file was automatic generated / don't edit.

