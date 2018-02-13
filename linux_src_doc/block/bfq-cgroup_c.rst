.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bfq-cgroup.c

.. _`bfq_bfqq_move`:

bfq_bfqq_move
=============

.. c:function:: void bfq_bfqq_move(struct bfq_data *bfqd, struct bfq_queue *bfqq, struct bfq_group *bfqg)

    migrate \ ``bfqq``\  to \ ``bfqg``\ .

    :param struct bfq_data \*bfqd:
        queue descriptor.

    :param struct bfq_queue \*bfqq:
        the queue to move.

    :param struct bfq_group \*bfqg:
        the group to move to.

.. _`bfq_bfqq_move.description`:

Description
-----------

Move \ ``bfqq``\  to \ ``bfqg``\ , deactivating it from its old group and reactivating
it on the new one.  Avoid putting the entity on the old group idle tree.

Must be called under the scheduler lock, to make sure that the blkg
owning \ ``bfqg``\  does not disappear (see comments in
bfq_bic_update_cgroup on guaranteeing the consistency of blkg
objects).

.. _`__bfq_bic_change_cgroup`:

\__bfq_bic_change_cgroup
========================

.. c:function:: struct bfq_group *__bfq_bic_change_cgroup(struct bfq_data *bfqd, struct bfq_io_cq *bic, struct blkcg *blkcg)

    move \ ``bic``\  to \ ``cgroup``\ .

    :param struct bfq_data \*bfqd:
        the queue descriptor.

    :param struct bfq_io_cq \*bic:
        the bic to move.

    :param struct blkcg \*blkcg:
        the blk-cgroup to move to.

.. _`__bfq_bic_change_cgroup.description`:

Description
-----------

Move bic to blkcg, assuming that bfqd->lock is held; which makes
sure that the reference to cgroup is valid across the call (see
comments in bfq_bic_update_cgroup on this issue)

.. _`__bfq_bic_change_cgroup.note`:

NOTE
----

an alternative approach might have been to store the current
cgroup in bfqq and getting a reference to it, reducing the lookup
time here, at the price of slightly more complex code.

.. _`bfq_flush_idle_tree`:

bfq_flush_idle_tree
===================

.. c:function:: void bfq_flush_idle_tree(struct bfq_service_tree *st)

    deactivate any entity on the idle tree of \ ``st``\ .

    :param struct bfq_service_tree \*st:
        the service tree being flushed.

.. _`bfq_reparent_leaf_entity`:

bfq_reparent_leaf_entity
========================

.. c:function:: void bfq_reparent_leaf_entity(struct bfq_data *bfqd, struct bfq_entity *entity)

    move leaf entity to the root_group.

    :param struct bfq_data \*bfqd:
        the device data structure with the root group.

    :param struct bfq_entity \*entity:
        the entity to move.

.. _`bfq_reparent_active_entities`:

bfq_reparent_active_entities
============================

.. c:function:: void bfq_reparent_active_entities(struct bfq_data *bfqd, struct bfq_group *bfqg, struct bfq_service_tree *st)

    move to the root group all active entities.

    :param struct bfq_data \*bfqd:
        the device data structure with the root group.

    :param struct bfq_group \*bfqg:
        the group to move from.

    :param struct bfq_service_tree \*st:
        the service tree with the entities.

.. _`bfq_pd_offline`:

bfq_pd_offline
==============

.. c:function:: void bfq_pd_offline(struct blkg_policy_data *pd)

    deactivate the entity associated with \ ``pd``\ , and reparent its children entities.

    :param struct blkg_policy_data \*pd:
        descriptor of the policy going offline.

.. _`bfq_pd_offline.description`:

Description
-----------

blkio already grabs the queue_lock for us, so no need to use
RCU-based magic

.. This file was automatic generated / don't edit.

