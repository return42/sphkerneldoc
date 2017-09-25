.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/binding.h

.. _`iwl_binding_cmd_v1`:

struct iwl_binding_cmd_v1
=========================

.. c:type:: struct iwl_binding_cmd_v1

    configuring bindings ( BINDING_CONTEXT_CMD = 0x2b )

.. _`iwl_binding_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_binding_cmd_v1 {
        __le32 id_and_color;
        __le32 action;
        __le32 macs[MAX_MACS_IN_BINDING];
        __le32 phy;
    }

.. _`iwl_binding_cmd_v1.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

action
    action to perform, one of FW_CTXT_ACTION\_\*

macs
    array of MAC id and colors which belong to the binding,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

phy
    PHY id and color which belongs to the binding,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

.. _`iwl_binding_cmd`:

struct iwl_binding_cmd
======================

.. c:type:: struct iwl_binding_cmd

    configuring bindings ( BINDING_CONTEXT_CMD = 0x2b )

.. _`iwl_binding_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_binding_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 macs[MAX_MACS_IN_BINDING];
        __le32 phy;
        __le32 lmac_id;
    }

.. _`iwl_binding_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

action
    action to perform, one of FW_CTXT_ACTION\_\*

macs
    array of MAC id and colors which belong to the binding
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

phy
    PHY id and color which belongs to the binding
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

lmac_id
    the lmac id the binding belongs to

.. _`iwl_time_quota_data`:

struct iwl_time_quota_data
==========================

.. c:type:: struct iwl_time_quota_data

    configuration of time quota per binding

.. _`iwl_time_quota_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_quota_data {
        __le32 id_and_color;
        __le32 quota;
        __le32 max_duration;
    }

.. _`iwl_time_quota_data.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

quota
    absolute time quota in TU. The scheduler will try to divide the
    remainig quota (after Time Events) according to this quota.

max_duration
    max uninterrupted context duration in TU

.. _`iwl_time_quota_cmd`:

struct iwl_time_quota_cmd
=========================

.. c:type:: struct iwl_time_quota_cmd

    configuration of time quota between bindings ( TIME_QUOTA_CMD = 0x2c )

.. _`iwl_time_quota_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_quota_cmd {
        struct iwl_time_quota_data quotas[MAX_BINDINGS];
    }

.. _`iwl_time_quota_cmd.members`:

Members
-------

quotas
    allocations per binding

.. _`iwl_time_quota_cmd.note`:

Note
----

on non-CDB the fourth one is the auxilary mac and is
essentially zero.
On CDB the fourth one is a regular binding.

.. This file was automatic generated / don't edit.

