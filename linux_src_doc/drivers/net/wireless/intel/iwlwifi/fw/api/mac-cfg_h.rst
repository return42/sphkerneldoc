.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/mac-cfg.h

.. _`iwl_mac_conf_subcmd_ids`:

enum iwl_mac_conf_subcmd_ids
============================

.. c:type:: enum iwl_mac_conf_subcmd_ids

    mac configuration command IDs

.. _`iwl_mac_conf_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_conf_subcmd_ids {
        LINK_QUALITY_MEASUREMENT_CMD,
        LINK_QUALITY_MEASUREMENT_COMPLETE_NOTIF,
        CHANNEL_SWITCH_NOA_NOTIF
    };

.. _`iwl_mac_conf_subcmd_ids.constants`:

Constants
---------

LINK_QUALITY_MEASUREMENT_CMD
    &struct iwl_link_qual_msrmnt_cmd

LINK_QUALITY_MEASUREMENT_COMPLETE_NOTIF
    &struct iwl_link_qual_msrmnt_notif

CHANNEL_SWITCH_NOA_NOTIF
    &struct iwl_channel_switch_noa_notif

.. _`iwl_link_qual_msrmnt_cmd`:

struct iwl_link_qual_msrmnt_cmd
===============================

.. c:type:: struct iwl_link_qual_msrmnt_cmd

    Link Quality Measurement command

.. _`iwl_link_qual_msrmnt_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_link_qual_msrmnt_cmd {
        __le32 cmd_operation;
        __le32 mac_id;
        __le32 measurement_time;
        __le32 timeout;
    }

.. _`iwl_link_qual_msrmnt_cmd.members`:

Members
-------

cmd_operation
    command operation to be performed (start or stop)
    as defined above.

mac_id
    MAC ID the measurement applies to.

measurement_time
    time of the total measurement to be performed, in uSec.

timeout
    maximum time allowed until a response is sent, in uSec.

.. _`iwl_link_qual_msrmnt_notif`:

struct iwl_link_qual_msrmnt_notif
=================================

.. c:type:: struct iwl_link_qual_msrmnt_notif

    Link Quality Measurement notification

.. _`iwl_link_qual_msrmnt_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_link_qual_msrmnt_notif {
        __le32 frequent_stations_air_time[LQM_NUMBER_OF_STATIONS_IN_REPORT];
        __le32 number_of_stations;
        __le32 total_air_time_other_stations;
        __le32 time_in_measurement_window;
        __le32 tx_frame_dropped;
        __le32 mac_id;
        __le32 status;
        u8 reserved[12];
    }

.. _`iwl_link_qual_msrmnt_notif.members`:

Members
-------

frequent_stations_air_time
    an array containing the total air time
    (in uSec) used by the most frequently transmitting stations.

number_of_stations
    the number of uniqe stations included in the array
    (a number between 0 to 16)

total_air_time_other_stations
    the total air time (uSec) used by all the
    stations which are not included in the above report.

time_in_measurement_window
    the total time in uSec in which a measurement
    took place.

tx_frame_dropped
    the number of TX frames dropped due to retry limit during
    measurement

mac_id
    MAC ID the measurement applies to.

status
    return status. may be one of the LQM_STATUS\_\* defined above.

reserved
    reserved.

.. _`iwl_channel_switch_noa_notif`:

struct iwl_channel_switch_noa_notif
===================================

.. c:type:: struct iwl_channel_switch_noa_notif

    Channel switch NOA notification

.. _`iwl_channel_switch_noa_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_channel_switch_noa_notif {
        __le32 id_and_color;
    }

.. _`iwl_channel_switch_noa_notif.members`:

Members
-------

id_and_color
    ID and color of the MAC

.. This file was automatic generated / don't edit.

