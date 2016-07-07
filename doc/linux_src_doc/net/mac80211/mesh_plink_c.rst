.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh_plink.c

.. _`mesh_plink_fsm_restart`:

mesh_plink_fsm_restart
======================

.. c:function:: void mesh_plink_fsm_restart(struct sta_info *sta)

    restart a mesh peer link finite state machine

    :param struct sta_info \*sta:
        mesh peer link to restart

.. _`mesh_plink_fsm_restart.locking`:

Locking
-------

this function must be called holding sta->mesh->plink_lock

.. _`mesh_set_ht_prot_mode`:

mesh_set_ht_prot_mode
=====================

.. c:function:: u32 mesh_set_ht_prot_mode(struct ieee80211_sub_if_data *sdata)

    set correct HT protection mode

    :param struct ieee80211_sub_if_data \*sdata:
        *undescribed*

.. _`mesh_set_ht_prot_mode.description`:

Description
-----------

Section 9.23.3.5 of IEEE 80211-2012 describes the protection rules for HT
mesh STA in a MBSS. Three HT protection modes are supported for now, non-HT
mixed mode, 20MHz-protection and no-protection mode. non-HT mixed mode is
selected if any non-HT peers are present in our MBSS.  20MHz-protection mode
is selected if all peers in our 20/40MHz MBSS support HT and atleast one
HT20 peer is present. Otherwise no-protection mode is selected.

.. _`__mesh_plink_deactivate`:

__mesh_plink_deactivate
=======================

.. c:function:: u32 __mesh_plink_deactivate(struct sta_info *sta)

    deactivate mesh peer link

    :param struct sta_info \*sta:
        mesh peer link to deactivate

.. _`__mesh_plink_deactivate.description`:

Description
-----------

Mesh paths with this peer as next hop should be flushed
by the caller outside of plink_lock.

Returns beacon changed flag if the beacon content changed.

.. _`__mesh_plink_deactivate.locking`:

Locking
-------

the caller must hold sta->mesh->plink_lock

.. _`mesh_plink_deactivate`:

mesh_plink_deactivate
=====================

.. c:function:: u32 mesh_plink_deactivate(struct sta_info *sta)

    deactivate mesh peer link

    :param struct sta_info \*sta:
        mesh peer link to deactivate

.. _`mesh_plink_deactivate.description`:

Description
-----------

All mesh paths with this peer as next hop will be flushed

.. _`mesh_plink_fsm`:

mesh_plink_fsm
==============

.. c:function:: u32 mesh_plink_fsm(struct ieee80211_sub_if_data *sdata, struct sta_info *sta, enum plink_event event)

    step \ ``sta``\  MPM based on \ ``event``\ 

    :param struct ieee80211_sub_if_data \*sdata:
        interface

    :param struct sta_info \*sta:
        mesh neighbor

    :param enum plink_event event:
        peering event

.. _`mesh_plink_fsm.return`:

Return
------

changed MBSS flags

.. This file was automatic generated / don't edit.

