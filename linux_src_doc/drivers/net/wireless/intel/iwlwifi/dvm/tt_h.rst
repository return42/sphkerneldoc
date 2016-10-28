.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/tt.h

.. _`iwl_tt_restriction`:

struct iwl_tt_restriction
=========================

.. c:type:: struct iwl_tt_restriction

    Thermal Throttling restriction table

.. _`iwl_tt_restriction.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tt_restriction {
        enum iwl_antenna_ok tx_stream;
        enum iwl_antenna_ok rx_stream;
        bool is_ht;
    }

.. _`iwl_tt_restriction.members`:

Members
-------

tx_stream
    number of tx stream allowed

rx_stream
    number of rx stream allowed

is_ht
    ht enable/disable

.. _`iwl_tt_restriction.description`:

Description
-----------

This table is used by advance thermal throttling management
based on the current thermal throttling state, and determines
the number of tx/rx streams and the status of HT operation.

.. _`iwl_tt_trans`:

struct iwl_tt_trans
===================

.. c:type:: struct iwl_tt_trans

    Thermal Throttling transaction table

.. _`iwl_tt_trans.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tt_trans {
        enum iwl_tt_state next_state;
        u32 tt_low;
        u32 tt_high;
    }

.. _`iwl_tt_trans.members`:

Members
-------

next_state
    next thermal throttling mode

tt_low
    low temperature threshold to change state

tt_high
    high temperature threshold to change state

.. _`iwl_tt_trans.description`:

Description
-----------

This is used by the advanced thermal throttling algorithm
to determine the next thermal state to go based on the
current temperature.

.. _`iwl_tt_mgmt`:

struct iwl_tt_mgmt
==================

.. c:type:: struct iwl_tt_mgmt

    Thermal Throttling Management structure

.. _`iwl_tt_mgmt.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tt_mgmt {
        enum iwl_tt_state state;
        bool advanced_tt;
        u8 tt_power_mode;
        bool ct_kill_toggle;
    #ifdef CONFIG_IWLWIFI_DEBUG
        s32 tt_previous_temp;
    #endif
        struct iwl_tt_restriction *restriction;
        struct iwl_tt_trans *transaction;
        struct timer_list ct_kill_exit_tm;
        struct timer_list ct_kill_waiting_tm;
    }

.. _`iwl_tt_mgmt.members`:

Members
-------

state
    current Thermal Throttling state

advanced_tt
    advanced thermal throttle required

tt_power_mode
    Thermal Throttling power mode index
    being used to set power level when
    when thermal throttling state != IWL_TI_0
    the tt_power_mode should set to different
    power mode based on the current tt state

ct_kill_toggle
    used to toggle the CSR bit when checking uCode temperature

tt_previous_temp
    *undescribed*

restriction
    *undescribed*

transaction
    *undescribed*

ct_kill_exit_tm
    timer to exit thermal kill

ct_kill_waiting_tm
    *undescribed*

.. This file was automatic generated / don't edit.

