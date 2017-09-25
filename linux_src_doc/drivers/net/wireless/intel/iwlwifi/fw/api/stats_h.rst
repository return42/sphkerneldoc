.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/stats.h

.. _`mvm_statistics_rx_non_phy`:

struct mvm_statistics_rx_non_phy
================================

.. c:type:: struct mvm_statistics_rx_non_phy


.. _`mvm_statistics_rx_non_phy.definition`:

Definition
----------

.. code-block:: c

    struct mvm_statistics_rx_non_phy {
        __le32 bogus_cts;
        __le32 bogus_ack;
        __le32 non_channel_beacons;
        __le32 channel_beacons;
        __le32 num_missed_bcon;
        __le32 adc_rx_saturation_time;
        __le32 ina_detection_search_time;
        __le32 beacon_silence_rssi_a;
        __le32 beacon_silence_rssi_b;
        __le32 beacon_silence_rssi_c;
        __le32 interference_data_flag;
        __le32 channel_load;
        __le32 beacon_rssi_a;
        __le32 beacon_rssi_b;
        __le32 beacon_rssi_c;
        __le32 beacon_energy_a;
        __le32 beacon_energy_b;
        __le32 beacon_energy_c;
        __le32 num_bt_kills;
        __le32 mac_id;
    }

.. _`mvm_statistics_rx_non_phy.members`:

Members
-------

bogus_cts
    CTS received when not expecting CTS

bogus_ack
    ACK received when not expecting ACK

non_channel_beacons
    beacons with our bss id but not on our serving channel

channel_beacons
    beacons with our bss id and in our serving channel

num_missed_bcon
    number of missed beacons

adc_rx_saturation_time
    count in 0.8us units the time the ADC was in
    saturation

ina_detection_search_time
    total time (in 0.8us) searched for INA

beacon_silence_rssi_a
    RSSI silence after beacon frame

beacon_silence_rssi_b
    RSSI silence after beacon frame

beacon_silence_rssi_c
    RSSI silence after beacon frame

interference_data_flag
    flag for interference data availability. 1 when data
    is available.

channel_load
    counts RX Enable time in uSec

beacon_rssi_a
    beacon RSSI on anntena A

beacon_rssi_b
    beacon RSSI on antenna B

beacon_rssi_c
    beacon RSSI on antenna C

beacon_energy_a
    beacon energy on antenna A

beacon_energy_b
    beacon energy on antenna B

beacon_energy_c
    beacon energy on antenna C

num_bt_kills
    number of BT "kills" (frame TX aborts)

mac_id
    mac ID

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
        __le32 air_time[MAC_INDEX_AUX];
        __le32 byte_count[MAC_INDEX_AUX];
        __le32 pkt_count[MAC_INDEX_AUX];
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

.. _`iwl_statistics_notif_flags`:

enum iwl_statistics_notif_flags
===============================

.. c:type:: enum iwl_statistics_notif_flags

    flags used in statistics notification

.. _`iwl_statistics_notif_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_statistics_notif_flags {
        IWL_STATISTICS_REPLY_FLG_CLEAR
    };

.. _`iwl_statistics_notif_flags.constants`:

Constants
---------

IWL_STATISTICS_REPLY_FLG_CLEAR
    statistics were cleared after this report

.. _`iwl_statistics_cmd_flags`:

enum iwl_statistics_cmd_flags
=============================

.. c:type:: enum iwl_statistics_cmd_flags

    flags used in statistics command

.. _`iwl_statistics_cmd_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_statistics_cmd_flags {
        IWL_STATISTICS_FLG_CLEAR,
        IWL_STATISTICS_FLG_DISABLE_NOTIF
    };

.. _`iwl_statistics_cmd_flags.constants`:

Constants
---------

IWL_STATISTICS_FLG_CLEAR
    request to clear statistics after the report
    that's sent after this command

IWL_STATISTICS_FLG_DISABLE_NOTIF
    disable unilateral statistics
    notifications

.. _`iwl_statistics_cmd`:

struct iwl_statistics_cmd
=========================

.. c:type:: struct iwl_statistics_cmd

    statistics config command

.. _`iwl_statistics_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_statistics_cmd {
        __le32 flags;
    }

.. _`iwl_statistics_cmd.members`:

Members
-------

flags
    flags from \ :c:type:`enum iwl_statistics_cmd_flags <iwl_statistics_cmd_flags>`\ 

.. This file was automatic generated / don't edit.

