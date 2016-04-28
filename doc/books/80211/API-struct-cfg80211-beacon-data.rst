.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-beacon-data:

===========================
struct cfg80211_beacon_data
===========================

*man struct cfg80211_beacon_data(9)*

*4.6.0-rc5*

beacon data


Synopsis
========

.. code-block:: c

    struct cfg80211_beacon_data {
      const u8 * head;
      const u8 * tail;
      const u8 * beacon_ies;
      const u8 * proberesp_ies;
      const u8 * assocresp_ies;
      const u8 * probe_resp;
      size_t head_len;
      size_t tail_len;
      size_t beacon_ies_len;
      size_t proberesp_ies_len;
      size_t assocresp_ies_len;
      size_t probe_resp_len;
    };


Members
=======

head
    head portion of beacon (before TIM IE) or ``NULL`` if not changed

tail
    tail portion of beacon (after TIM IE) or ``NULL`` if not changed

beacon_ies
    extra information element(s) to add into Beacon frames or ``NULL``

proberesp_ies
    extra information element(s) to add into Probe Response frames or
    ``NULL``

assocresp_ies
    extra information element(s) to add into (Re)Association Response
    frames or ``NULL``

probe_resp
    probe response template (AP mode only)

head_len
    length of ``head``

tail_len
    length of ``tail``

beacon_ies_len
    length of beacon_ies in octets

proberesp_ies_len
    length of proberesp_ies in octets

assocresp_ies_len
    length of assocresp_ies in octets

probe_resp_len
    length of probe response template (``probe_resp``)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
