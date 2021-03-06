.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8188eu/include/wifi.h

.. _`ieee80211_ht_addt_info`:

struct ieee80211_ht_addt_info
=============================

.. c:type:: struct ieee80211_ht_addt_info

    HT additional information

.. _`ieee80211_ht_addt_info.definition`:

Definition
----------

.. code-block:: c

    struct ieee80211_ht_addt_info {
        unsigned char control_chan;
        unsigned char ht_param;
        unsigned short operation_mode;
        unsigned short stbc_param;
        unsigned char basic_set[16];
    }

.. _`ieee80211_ht_addt_info.members`:

Members
-------

control_chan
    *undescribed*

ht_param
    *undescribed*

operation_mode
    *undescribed*

stbc_param
    *undescribed*

basic_set
    *undescribed*

.. _`ieee80211_ht_addt_info.description`:

Description
-----------

This structure refers to "HT information element" as
described in 802.11n draft section 7.3.2.53

.. This file was automatic generated / don't edit.

