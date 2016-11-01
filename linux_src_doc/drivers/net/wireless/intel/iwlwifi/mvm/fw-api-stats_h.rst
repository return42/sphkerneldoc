.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-stats.h

.. _`mvm_statistics_load`:

struct mvm_statistics_load
==========================

.. c:type:: struct mvm_statistics_load

    RX statistics for multi-queue devices

.. _`mvm_statistics_load.definition`:

Definition
----------

.. code-block:: c

    struct mvm_statistics_load {
        __le32 air_time[NUM_MAC_INDEX];
        __le32 byte_count[NUM_MAC_INDEX];
        __le32 pkt_count[NUM_MAC_INDEX];
        u8 avg_energy[IWL_MVM_STATION_COUNT];
    }

.. _`mvm_statistics_load.members`:

Members
-------

air_time
    accumulated air time, per mac

byte_count
    accumulated byte count, per mac

pkt_count
    accumulated packet count, per mac

avg_energy
    average RSSI, per station

.. This file was automatic generated / don't edit.

