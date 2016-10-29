.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8188eu/include/wifi.h

.. _`rtw_ieee80211_bar`:

struct rtw_ieee80211_bar
========================

.. c:type:: struct rtw_ieee80211_bar

    HT Block Ack Request

.. _`rtw_ieee80211_bar.definition`:

Definition
----------

.. code-block:: c

    struct rtw_ieee80211_bar {
        unsigned short frame_control;
        unsigned short duration;
        unsigned char ra[6];
        unsigned char ta[6];
        unsigned short control;
        unsigned short start_seq_num;
    }

.. _`rtw_ieee80211_bar.members`:

Members
-------

frame_control
    *undescribed*

duration
    *undescribed*

control
    *undescribed*

start_seq_num
    *undescribed*

.. _`rtw_ieee80211_bar.description`:

Description
-----------

This structure refers to "HT BlockAckReq" as
described in 802.11n draft section 7.2.1.7.1

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

.. _`ieee80211_ht_addt_info.description`:

Description
-----------

This structure refers to "HT information element" as
described in 802.11n draft section 7.3.2.53

.. This file was automatic generated / don't edit.
