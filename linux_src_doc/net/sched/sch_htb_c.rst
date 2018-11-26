.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sched/sch_htb.c

.. _`htb_direct`:

HTB_DIRECT
==========

.. c:function::  HTB_DIRECT()

    classify a packet into class

.. _`htb_direct.description`:

Description
-----------

It returns NULL if the packet should be dropped or -1 if the packet
should be passed directly thru. In all other cases leaf class is returned.
We allow direct class selection by classid in priority. The we examine
filters in qdisc and in inner nodes (if higher filter points to the inner
node). If we end up with classid MAJOR:0 we enqueue the skb into special
internal fifo (direct). These packets then go directly thru. If we still
have no valid leaf we try to use MAJOR:default leaf. It still unsuccessful
then finish and return direct queue.

.. _`htb_add_to_id_tree`:

htb_add_to_id_tree
==================

.. c:function:: void htb_add_to_id_tree(struct rb_root *root, struct htb_class *cl, int prio)

    adds class to the round robin list

    :param root:
        *undescribed*
    :type root: struct rb_root \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param prio:
        *undescribed*
    :type prio: int

.. _`htb_add_to_id_tree.description`:

Description
-----------

Routine adds class to the list (actually tree) sorted by classid.
Make sure that class is not already on such list for given prio.

.. _`htb_add_to_wait_tree`:

htb_add_to_wait_tree
====================

.. c:function:: void htb_add_to_wait_tree(struct htb_sched *q, struct htb_class *cl, s64 delay)

    adds class to the event queue with delay

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param delay:
        *undescribed*
    :type delay: s64

.. _`htb_add_to_wait_tree.description`:

Description
-----------

The class is added to priority event queue to indicate that class will
change its mode in cl->pq_key microseconds. Make sure that class is not
already in the queue.

.. _`htb_next_rb_node`:

htb_next_rb_node
================

.. c:function:: void htb_next_rb_node(struct rb_node **n)

    finds next node in binary tree

    :param n:
        *undescribed*
    :type n: struct rb_node \*\*

.. _`htb_next_rb_node.description`:

Description
-----------

When we are past last key we return NULL.
Average complexity is 2 steps per call.

.. _`htb_add_class_to_row`:

htb_add_class_to_row
====================

.. c:function:: void htb_add_class_to_row(struct htb_sched *q, struct htb_class *cl, int mask)

    add class to its row

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param mask:
        *undescribed*
    :type mask: int

.. _`htb_add_class_to_row.description`:

Description
-----------

The class is added to row at priorities marked in mask.
It does nothing if mask == 0.

.. _`htb_remove_class_from_row`:

htb_remove_class_from_row
=========================

.. c:function:: void htb_remove_class_from_row(struct htb_sched *q, struct htb_class *cl, int mask)

    removes class from its row

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param mask:
        *undescribed*
    :type mask: int

.. _`htb_remove_class_from_row.description`:

Description
-----------

The class is removed from row at priorities marked in mask.
It does nothing if mask == 0.

.. _`htb_activate_prios`:

htb_activate_prios
==================

.. c:function:: void htb_activate_prios(struct htb_sched *q, struct htb_class *cl)

    creates active classe's feed chain

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

.. _`htb_activate_prios.description`:

Description
-----------

The class is connected to ancestors and/or appropriate rows
for priorities it is participating on. cl->cmode must be new
(activated) mode. It does nothing if cl->prio_activity == 0.

.. _`htb_deactivate_prios`:

htb_deactivate_prios
====================

.. c:function:: void htb_deactivate_prios(struct htb_sched *q, struct htb_class *cl)

    remove class from feed chain

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

.. _`htb_deactivate_prios.description`:

Description
-----------

cl->cmode must represent old mode (before deactivation). It does
nothing if cl->prio_activity == 0. Class is removed from all feed
chains and rows.

.. _`htb_class_mode`:

htb_class_mode
==============

.. c:function:: enum htb_cmode htb_class_mode(struct htb_class *cl, s64 *diff)

    computes and returns current class mode

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param diff:
        *undescribed*
    :type diff: s64 \*

.. _`htb_class_mode.description`:

Description
-----------

It computes cl's mode at time cl->t_c+diff and returns it. If mode
is not HTB_CAN_SEND then cl->pq_key is updated to time difference
from now to time when cl will change its state.
Also it is worth to note that class mode doesn't change simply
at cl->{c,}tokens == 0 but there can rather be hysteresis of
0 .. -cl->{c,}buffer range. It is meant to limit number of
mode transitions per time unit. The speed gain is about 1/6.

.. _`htb_change_class_mode`:

htb_change_class_mode
=====================

.. c:function:: void htb_change_class_mode(struct htb_sched *q, struct htb_class *cl, s64 *diff)

    changes classe's mode

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param diff:
        *undescribed*
    :type diff: s64 \*

.. _`htb_change_class_mode.description`:

Description
-----------

This should be the only way how to change classe's mode under normal
cirsumstances. Routine will update feed lists linkage, change mode
and add class to the wait event queue if appropriate. New mode should
be different from old one and cl->pq_key has to be valid if changing
to mode other than HTB_CAN_SEND (see htb_add_to_wait_tree).

.. _`htb_activate`:

htb_activate
============

.. c:function:: void htb_activate(struct htb_sched *q, struct htb_class *cl)

    inserts leaf cl into appropriate active feeds

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

.. _`htb_activate.description`:

Description
-----------

Routine learns (new) priority of leaf and activates feed chain
for the prio. It can be called on already active leaf safely.
It also adds leaf into droplist.

.. _`htb_deactivate`:

htb_deactivate
==============

.. c:function:: void htb_deactivate(struct htb_sched *q, struct htb_class *cl)

    remove leaf cl from active feeds

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

.. _`htb_deactivate.description`:

Description
-----------

Make sure that leaf is active. In the other words it can't be called
with non-active leaf. It also removes class from the drop list.

.. _`htb_charge_class`:

htb_charge_class
================

.. c:function:: void htb_charge_class(struct htb_sched *q, struct htb_class *cl, int level, struct sk_buff *skb)

    charges amount "bytes" to leaf and ancestors

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param cl:
        *undescribed*
    :type cl: struct htb_class \*

    :param level:
        *undescribed*
    :type level: int

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`htb_charge_class.description`:

Description
-----------

Routine assumes that packet "bytes" long was dequeued from leaf cl
borrowing from "level". It accounts bytes to ceil leaky bucket for
leaf and all ancestors and to rate bucket for ancestors at levels
"level" and higher. It also handles possible change of mode resulting
from the update. Note that mode can also increase here (MAY_BORROW to
CAN_SEND) because we can use more precise clock that event queue here.
In such case we remove class from event queue first.

.. _`htb_do_events`:

htb_do_events
=============

.. c:function:: s64 htb_do_events(struct htb_sched *q, const int level, unsigned long start)

    make mode changes to classes at the level

    :param q:
        *undescribed*
    :type q: struct htb_sched \*

    :param level:
        *undescribed*
    :type level: const int

    :param start:
        *undescribed*
    :type start: unsigned long

.. _`htb_do_events.description`:

Description
-----------

Scans event queue for pending events and applies them. Returns time of
next pending event (0 for no event in pq, q->now for too many events).

.. _`htb_do_events.note`:

Note
----

Applied are events whose have cl->pq_key <= q->now.

.. _`htb_lookup_leaf`:

htb_lookup_leaf
===============

.. c:function:: struct htb_class *htb_lookup_leaf(struct htb_prio *hprio, const int prio)

    returns next leaf class in DRR order

    :param hprio:
        *undescribed*
    :type hprio: struct htb_prio \*

    :param prio:
        *undescribed*
    :type prio: const int

.. _`htb_lookup_leaf.description`:

Description
-----------

Find leaf where current feed pointers points to.

.. This file was automatic generated / don't edit.

