.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/testmode.h

.. _`iwl_mvm_testmode_attrs`:

enum iwl_mvm_testmode_attrs
===========================

.. c:type:: enum iwl_mvm_testmode_attrs

    testmode attributes inside NL80211_ATTR_TESTDATA

.. _`iwl_mvm_testmode_attrs.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_testmode_attrs {
        IWL_MVM_TM_ATTR_UNSPEC,
        IWL_MVM_TM_ATTR_CMD,
        IWL_MVM_TM_ATTR_NOA_DURATION,
        IWL_MVM_TM_ATTR_BEACON_FILTER_STATE,
        NUM_IWL_MVM_TM_ATTRS,
        IWL_MVM_TM_ATTR_MAX
    };

.. _`iwl_mvm_testmode_attrs.constants`:

Constants
---------

IWL_MVM_TM_ATTR_UNSPEC
    (invalid attribute)

IWL_MVM_TM_ATTR_CMD
    sub command, see \ :c:type:`enum iwl_mvm_testmode_commands <iwl_mvm_testmode_commands>`\  (u32)

IWL_MVM_TM_ATTR_NOA_DURATION
    requested NoA duration (u32)

IWL_MVM_TM_ATTR_BEACON_FILTER_STATE
    beacon filter state (0 or 1, u32)

NUM_IWL_MVM_TM_ATTRS
    *undescribed*

IWL_MVM_TM_ATTR_MAX
    *undescribed*

.. _`iwl_mvm_testmode_commands`:

enum iwl_mvm_testmode_commands
==============================

.. c:type:: enum iwl_mvm_testmode_commands

    MVM testmode commands

.. _`iwl_mvm_testmode_commands.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_testmode_commands {
        IWL_MVM_TM_CMD_SET_NOA,
        IWL_MVM_TM_CMD_SET_BEACON_FILTER
    };

.. _`iwl_mvm_testmode_commands.constants`:

Constants
---------

IWL_MVM_TM_CMD_SET_NOA
    set NoA on GO vif for testing

IWL_MVM_TM_CMD_SET_BEACON_FILTER
    turn beacon filtering off/on

.. This file was automatic generated / don't edit.

