.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bfq-wf2q.c

.. _`bfq_gt`:

bfq_gt
======

.. c:function:: int bfq_gt(u64 a, u64 b)

    compare two timestamps.

    :param u64 a:
        first ts.

    :param u64 b:
        second ts.

.. _`bfq_gt.description`:

Description
-----------

Return \ ``a``\  > \ ``b``\ , dealing with wrapping correctly.

.. _`bfq_update_next_in_service`:

bfq_update_next_in_service
==========================

.. c:function:: bool bfq_update_next_in_service(struct bfq_sched_data *sd, struct bfq_entity *new_entity)

    update sd->next_in_service

    :param struct bfq_sched_data \*sd:
        sched_data for which to perform the update.

    :param struct bfq_entity \*new_entity:
        if not NULL, pointer to the entity whose activation,
        requeueing or repositionig triggered the invocation of
        this function.

.. _`bfq_update_next_in_service.description`:

Description
-----------

This function is called to update sd->next_in_service, which, in
its turn, may change as a consequence of the insertion or
extraction of an entity into/from one of the active trees of
sd. These insertions/extractions occur as a consequence of
activations/deactivations of entities, with some activations being
'true' activations, and other activations being requeueings (i.e.,
implementing the second, requeueing phase of the mechanism used to
reposition an entity in its active tree; see comments on
\__bfq_activate_entity and \__bfq_requeue_entity for details). In
both the last two activation sub-cases, new_entity points to the
just activated or requeued entity.

Returns true if sd->next_in_service changes in such a way that
entity->parent may become the next_in_service for its parent
entity.

.. _`bfq_delta`:

bfq_delta
=========

.. c:function:: u64 bfq_delta(unsigned long service, unsigned long weight)

    map service into the virtual time domain.

    :param unsigned long service:
        amount of service.

    :param unsigned long weight:
        scale factor (weight of an entity or weight sum).

.. _`bfq_calc_finish`:

bfq_calc_finish
===============

.. c:function:: void bfq_calc_finish(struct bfq_entity *entity, unsigned long service)

    assign the finish time to an entity.

    :param struct bfq_entity \*entity:
        the entity to act upon.

    :param unsigned long service:
        the service to be charged to the entity.

.. _`bfq_entity_of`:

bfq_entity_of
=============

.. c:function:: struct bfq_entity *bfq_entity_of(struct rb_node *node)

    get an entity from a node.

    :param struct rb_node \*node:
        the node field of the entity.

.. _`bfq_entity_of.description`:

Description
-----------

Convert a node pointer to the relative entity.  This is used only
to simplify the logic of some functions and not as the generic
conversion mechanism because, e.g., in the tree walking functions,
the check for a \ ``NULL``\  value would be redundant.

.. _`bfq_extract`:

bfq_extract
===========

.. c:function:: void bfq_extract(struct rb_root *root, struct bfq_entity *entity)

    remove an entity from a tree.

    :param struct rb_root \*root:
        the tree root.

    :param struct bfq_entity \*entity:
        the entity to remove.

.. _`bfq_idle_extract`:

bfq_idle_extract
================

.. c:function:: void bfq_idle_extract(struct bfq_service_tree *st, struct bfq_entity *entity)

    extract an entity from the idle tree.

    :param struct bfq_service_tree \*st:
        the service tree of the owning \ ``entity``\ .

    :param struct bfq_entity \*entity:
        the entity being removed.

.. _`bfq_insert`:

bfq_insert
==========

.. c:function:: void bfq_insert(struct rb_root *root, struct bfq_entity *entity)

    generic tree insertion.

    :param struct rb_root \*root:
        tree root.

    :param struct bfq_entity \*entity:
        entity to insert.

.. _`bfq_insert.description`:

Description
-----------

This is used for the idle and the active tree, since they are both
ordered by finish time.

.. _`bfq_update_min`:

bfq_update_min
==============

.. c:function:: void bfq_update_min(struct bfq_entity *entity, struct rb_node *node)

    update the min_start field of a entity.

    :param struct bfq_entity \*entity:
        the entity to update.

    :param struct rb_node \*node:
        one of its children.

.. _`bfq_update_min.description`:

Description
-----------

This function is called when \ ``entity``\  may store an invalid value for
min_start due to updates to the active tree.  The function  assumes
that the subtree rooted at \ ``node``\  (which may be its left or its right
child) has a valid min_start value.

.. _`bfq_update_active_node`:

bfq_update_active_node
======================

.. c:function:: void bfq_update_active_node(struct rb_node *node)

    recalculate min_start.

    :param struct rb_node \*node:
        the node to update.

.. _`bfq_update_active_node.description`:

Description
-----------

@node may have changed position or one of its children may have moved,
this function updates its min_start value.  The left and right subtrees
are assumed to hold a correct min_start value.

.. _`bfq_update_active_tree`:

bfq_update_active_tree
======================

.. c:function:: void bfq_update_active_tree(struct rb_node *node)

    update min_start for the whole active tree.

    :param struct rb_node \*node:
        the starting node.

.. _`bfq_update_active_tree.description`:

Description
-----------

@node must be the deepest modified node after an update.  This function
updates its min_start using the values held by its children, assuming
that they did not change, and then updates all the nodes that may have
changed in the path to the root.  The only nodes that may have changed
are the ones in the path or their siblings.

.. _`bfq_active_insert`:

bfq_active_insert
=================

.. c:function:: void bfq_active_insert(struct bfq_service_tree *st, struct bfq_entity *entity)

    insert an entity in the active tree of its group/device.

    :param struct bfq_service_tree \*st:
        the service tree of the entity.

    :param struct bfq_entity \*entity:
        the entity being inserted.

.. _`bfq_active_insert.description`:

Description
-----------

The active tree is ordered by finish time, but an extra key is kept
per each node, containing the minimum value for the start times of
its children (and the node itself), so it's possible to search for
the eligible node with the lowest finish time in logarithmic time.

.. _`bfq_ioprio_to_weight`:

bfq_ioprio_to_weight
====================

.. c:function:: unsigned short bfq_ioprio_to_weight(int ioprio)

    calc a weight from an ioprio.

    :param int ioprio:
        the ioprio value to convert.

.. _`bfq_weight_to_ioprio`:

bfq_weight_to_ioprio
====================

.. c:function:: unsigned short bfq_weight_to_ioprio(int weight)

    calc an ioprio from a weight.

    :param int weight:
        the weight value to convert.

.. _`bfq_weight_to_ioprio.description`:

Description
-----------

To preserve as much as possible the old only-ioprio user interface,
0 is used as an escape ioprio value for weights (numerically) equal or
larger than IOPRIO_BE_NR \* BFQ_WEIGHT_CONVERSION_COEFF.

.. _`bfq_find_deepest`:

bfq_find_deepest
================

.. c:function:: struct rb_node *bfq_find_deepest(struct rb_node *node)

    find the deepest node that an extraction can modify.

    :param struct rb_node \*node:
        the node being removed.

.. _`bfq_find_deepest.description`:

Description
-----------

Do the first step of an extraction in an rb tree, looking for the
node that will replace \ ``node``\ , and returning the deepest node that
the following modifications to the tree can touch.  If \ ``node``\  is the
last node in the tree return \ ``NULL``\ .

.. _`bfq_active_extract`:

bfq_active_extract
==================

.. c:function:: void bfq_active_extract(struct bfq_service_tree *st, struct bfq_entity *entity)

    remove an entity from the active tree.

    :param struct bfq_service_tree \*st:
        the service_tree containing the tree.

    :param struct bfq_entity \*entity:
        the entity being removed.

.. _`bfq_idle_insert`:

bfq_idle_insert
===============

.. c:function:: void bfq_idle_insert(struct bfq_service_tree *st, struct bfq_entity *entity)

    insert an entity into the idle tree.

    :param struct bfq_service_tree \*st:
        the service tree containing the tree.

    :param struct bfq_entity \*entity:
        the entity to insert.

.. _`bfq_forget_entity`:

bfq_forget_entity
=================

.. c:function:: void bfq_forget_entity(struct bfq_service_tree *st, struct bfq_entity *entity, bool is_in_service)

    do not consider entity any longer for scheduling

    :param struct bfq_service_tree \*st:
        the service tree.

    :param struct bfq_entity \*entity:
        the entity being removed.

    :param bool is_in_service:
        true if entity is currently the in-service entity.

.. _`bfq_forget_entity.description`:

Description
-----------

Forget everything about \ ``entity``\ . In addition, if entity represents
a queue, and the latter is not in service, then release the service
reference to the queue (the one taken through bfq_get_entity). In
fact, in this case, there is really no more service reference to
the queue, as the latter is also outside any service tree. If,
instead, the queue is in service, then \__bfq_bfqd_reset_in_service
will take care of putting the reference when the queue finally
stops being served.

.. _`bfq_put_idle_entity`:

bfq_put_idle_entity
===================

.. c:function:: void bfq_put_idle_entity(struct bfq_service_tree *st, struct bfq_entity *entity)

    release the idle tree ref of an entity.

    :param struct bfq_service_tree \*st:
        service tree for the entity.

    :param struct bfq_entity \*entity:
        the entity being released.

.. _`bfq_forget_idle`:

bfq_forget_idle
===============

.. c:function:: void bfq_forget_idle(struct bfq_service_tree *st)

    update the idle tree if necessary.

    :param struct bfq_service_tree \*st:
        the service tree to act upon.

.. _`bfq_forget_idle.description`:

Description
-----------

To preserve the global O(log N) complexity we only remove one entry here;
as the idle tree will not grow indefinitely this can be done safely.

.. _`bfq_bfqq_served`:

bfq_bfqq_served
===============

.. c:function:: void bfq_bfqq_served(struct bfq_queue *bfqq, int served)

    update the scheduler status after selection for service.

    :param struct bfq_queue \*bfqq:
        the queue being served.

    :param int served:
        bytes to transfer.

.. _`bfq_bfqq_served.note`:

NOTE
----

this can be optimized, as the timestamps of upper level entities
are synchronized every time a new bfqq is selected for service.  By now,
we keep it to better check consistency.

.. _`bfq_bfqq_charge_time`:

bfq_bfqq_charge_time
====================

.. c:function:: void bfq_bfqq_charge_time(struct bfq_data *bfqd, struct bfq_queue *bfqq, unsigned long time_ms)

    charge an amount of service equivalent to the length of the time interval during which bfqq has been in service.

    :param struct bfq_data \*bfqd:
        the device

    :param struct bfq_queue \*bfqq:
        the queue that needs a service update.

    :param unsigned long time_ms:
        the amount of time during which the queue has received service

.. _`bfq_bfqq_charge_time.description`:

Description
-----------

If a queue does not consume its budget fast enough, then providing
the queue with service fairness may impair throughput, more or less
severely. For this reason, queues that consume their budget slowly
are provided with time fairness instead of service fairness. This
goal is achieved through the BFQ scheduling engine, even if such an
engine works in the service, and not in the time domain. The trick
is charging these queues with an inflated amount of service, equal
to the amount of service that they would have received during their
service slot if they had been fast, i.e., if their requests had
been dispatched at a rate equal to the estimated peak rate.

It is worth noting that time fairness can cause important
distortions in terms of bandwidth distribution, on devices with
internal queueing. The reason is that I/O requests dispatched
during the service slot of a queue may be served after that service
slot is finished, and may have a total processing time loosely
correlated with the duration of the service slot. This is
especially true for short service slots.

.. _`__bfq_activate_entity`:

__bfq_activate_entity
=====================

.. c:function:: void __bfq_activate_entity(struct bfq_entity *entity, bool non_blocking_wait_rq)

    handle activation of entity.

    :param struct bfq_entity \*entity:
        the entity being activated.

    :param bool non_blocking_wait_rq:
        true if entity was waiting for a request

.. _`__bfq_activate_entity.description`:

Description
-----------

Called for a 'true' activation, i.e., if entity is not active and
one of its children receives a new request.

Basically, this function updates the timestamps of entity and
inserts entity into its active tree, ater possible extracting it
from its idle tree.

.. _`__bfq_requeue_entity`:

__bfq_requeue_entity
====================

.. c:function:: void __bfq_requeue_entity(struct bfq_entity *entity)

    handle requeueing or repositioning of an entity.

    :param struct bfq_entity \*entity:
        the entity being requeued or repositioned.

.. _`__bfq_requeue_entity.description`:

Description
-----------

Requeueing is needed if this entity stops being served, which
happens if a leaf descendant entity has expired. On the other hand,
repositioning is needed if the next_inservice_entity for the child
entity has changed. See the comments inside the function for
details.

Basically, this function: 1) removes entity from its active tree if
present there, 2) updates the timestamps of entity and 3) inserts
entity back into its active tree (in the new, right position for
the new values of the timestamps).

.. _`bfq_activate_requeue_entity`:

bfq_activate_requeue_entity
===========================

.. c:function:: void bfq_activate_requeue_entity(struct bfq_entity *entity, bool non_blocking_wait_rq, bool requeue)

    activate or requeue an entity representing a bfq_queue, and activate, requeue or reposition all ancestors for which such an update becomes necessary.

    :param struct bfq_entity \*entity:
        the entity to activate.

    :param bool non_blocking_wait_rq:
        true if this entity was waiting for a request

    :param bool requeue:
        true if this is a requeue, which implies that bfqq is
        being expired; thus ALL its ancestors stop being served and must
        therefore be requeued

.. _`__bfq_deactivate_entity`:

__bfq_deactivate_entity
=======================

.. c:function:: bool __bfq_deactivate_entity(struct bfq_entity *entity, bool ins_into_idle_tree)

    deactivate an entity from its service tree.

    :param struct bfq_entity \*entity:
        the entity to deactivate.

    :param bool ins_into_idle_tree:
        if false, the entity will not be put into the
        idle tree.

.. _`__bfq_deactivate_entity.description`:

Description
-----------

Deactivates an entity, independently from its previous state.  Must
be invoked only if entity is on a service tree. Extracts the entity
from that tree, and if necessary and allowed, puts it on the idle
tree.

.. _`bfq_deactivate_entity`:

bfq_deactivate_entity
=====================

.. c:function:: void bfq_deactivate_entity(struct bfq_entity *entity, bool ins_into_idle_tree, bool expiration)

    deactivate an entity representing a bfq_queue.

    :param struct bfq_entity \*entity:
        the entity to deactivate.

    :param bool ins_into_idle_tree:
        true if the entity can be put on the idle tree

    :param bool expiration:
        *undescribed*

.. _`bfq_calc_vtime_jump`:

bfq_calc_vtime_jump
===================

.. c:function:: u64 bfq_calc_vtime_jump(struct bfq_service_tree *st)

    compute the value to which the vtime should jump, if needed, to have at least one entity eligible.

    :param struct bfq_service_tree \*st:
        the service tree to act upon.

.. _`bfq_calc_vtime_jump.description`:

Description
-----------

Assumes that st is not empty.

.. _`bfq_first_active_entity`:

bfq_first_active_entity
=======================

.. c:function:: struct bfq_entity *bfq_first_active_entity(struct bfq_service_tree *st, u64 vtime)

    find the eligible entity with the smallest finish time

    :param struct bfq_service_tree \*st:
        the service tree to select from.

    :param u64 vtime:
        the system virtual to use as a reference for eligibility

.. _`bfq_first_active_entity.description`:

Description
-----------

This function searches the first schedulable entity, starting from the
root of the tree and going on the left every time on this side there is
a subtree with at least one eligible (start >= vtime) entity. The path on
the right is followed only if a) the left subtree contains no eligible
entities and b) no eligible entity has been found yet.

.. _`__bfq_lookup_next_entity`:

__bfq_lookup_next_entity
========================

.. c:function:: struct bfq_entity *__bfq_lookup_next_entity(struct bfq_service_tree *st, bool in_service)

    return the first eligible entity in \ ``st``\ .

    :param struct bfq_service_tree \*st:
        the service tree.

    :param bool in_service:
        *undescribed*

.. _`__bfq_lookup_next_entity.description`:

Description
-----------

If there is no in-service entity for the sched_data st belongs to,

.. _`__bfq_lookup_next_entity.then-return-the-entity-that-will-be-set-in-service-if`:

then return the entity that will be set in service if
-----------------------------------------------------

1) the parent entity this st belongs to is set in service;
2) no entity belonging to such parent entity undergoes a state change
that would influence the timestamps of the entity (e.g., becomes idle,
becomes backlogged, changes its budget, ...).

In this first case, update the virtual time in \ ``st``\  too (see the
comments on this update inside the function).

In constrast, if there is an in-service entity, then return the
entity that would be set in service if not only the above
conditions, but also the next one held true: the currently
in-service entity, on expiration,
1) gets a finish time equal to the current one, or
2) is not eligible any more, or
3) is idle.

.. _`bfq_lookup_next_entity`:

bfq_lookup_next_entity
======================

.. c:function:: struct bfq_entity *bfq_lookup_next_entity(struct bfq_sched_data *sd)

    return the first eligible entity in \ ``sd``\ .

    :param struct bfq_sched_data \*sd:
        the sched_data.

.. _`bfq_lookup_next_entity.description`:

Description
-----------

This function is invoked when there has been a change in the trees
for sd, and we need know what is the new next entity after this
change.

.. This file was automatic generated / don't edit.

