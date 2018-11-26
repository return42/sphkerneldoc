.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/utils.c

.. _`iwl_mvm_send_lq_cmd`:

iwl_mvm_send_lq_cmd
===================

.. c:function:: int iwl_mvm_send_lq_cmd(struct iwl_mvm *mvm, struct iwl_lq_cmd *lq, bool sync)

    Send link quality command

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param lq:
        *undescribed*
    :type lq: struct iwl_lq_cmd \*

    :param sync:
        This command can be sent synchronously.
    :type sync: bool

.. _`iwl_mvm_send_lq_cmd.description`:

Description
-----------

The link quality command is sent as the last step of station creation.
This is the special case in which init is set and we call a callback in
this case to clear the state indicating that station creation is in
progress.

.. _`iwl_mvm_update_smps`:

iwl_mvm_update_smps
===================

.. c:function:: void iwl_mvm_update_smps(struct iwl_mvm *mvm, struct ieee80211_vif *vif, enum iwl_mvm_smps_type_request req_type, enum ieee80211_smps_mode smps_request)

    Get a request to change the SMPS mode

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

    :param req_type:
        The part of the driver who call for a change.
    :type req_type: enum iwl_mvm_smps_type_request

    :param smps_request:
        *undescribed*
    :type smps_request: enum ieee80211_smps_mode

.. _`iwl_mvm_update_smps.description`:

Description
-----------

Get a requst to change the SMPS mode,
and change it according to all other requests in the driver.

.. This file was automatic generated / don't edit.

