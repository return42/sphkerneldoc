.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/offload.h

.. _`iwl_prot_offload_subcmd_ids`:

enum iwl_prot_offload_subcmd_ids
================================

.. c:type:: enum iwl_prot_offload_subcmd_ids

    protocol offload commands

.. _`iwl_prot_offload_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_prot_offload_subcmd_ids {
        STORED_BEACON_NTF
    };

.. _`iwl_prot_offload_subcmd_ids.constants`:

Constants
---------

STORED_BEACON_NTF
    &struct iwl_stored_beacon_notif

.. _`iwl_stored_beacon_notif`:

struct iwl_stored_beacon_notif
==============================

.. c:type:: struct iwl_stored_beacon_notif

    Stored beacon notification

.. _`iwl_stored_beacon_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_stored_beacon_notif {
        __le32 system_time;
        __le64 tsf;
        __le32 beacon_timestamp;
        __le16 band;
        __le16 channel;
        __le32 rates;
        __le32 byte_count;
        u8 data;
    }

.. _`iwl_stored_beacon_notif.members`:

Members
-------

system_time
    system time on air rise

tsf
    TSF on air rise

beacon_timestamp
    beacon on air rise

band
    band, matches \ :c:type:`struct RX_RES_PHY_FLAGS_BAND_24 <RX_RES_PHY_FLAGS_BAND_24>`\  definition

channel
    channel this beacon was received on

rates
    rate in ucode internal format

byte_count
    frame's byte count

data
    beacon data, length in \ ``byte_count``\ 

.. This file was automatic generated / don't edit.

