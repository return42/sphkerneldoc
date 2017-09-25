.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/sf.h

.. _`iwl_sf_cfg_cmd`:

struct iwl_sf_cfg_cmd
=====================

.. c:type:: struct iwl_sf_cfg_cmd

    Smart Fifo configuration command.

.. _`iwl_sf_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_sf_cfg_cmd {
        __le32 state;
        __le32 watermark[SF_TRANSIENT_STATES_NUMBER];
        __le32 long_delay_timeouts[SF_NUM_SCENARIO][SF_NUM_TIMEOUT_TYPES];
        __le32 full_on_timeouts[SF_NUM_SCENARIO][SF_NUM_TIMEOUT_TYPES];
    }

.. _`iwl_sf_cfg_cmd.members`:

Members
-------

state
    smart fifo state, types listed in \ :c:type:`enum iwl_sf_state <iwl_sf_state>`\ .

watermark
    Minimum allowed available free space in RXF for transient state.

long_delay_timeouts
    aging and idle timer values for each scenario
    in long delay state.

full_on_timeouts
    timer values for each scenario in full on state.

.. This file was automatic generated / don't edit.

