.. -*- coding: utf-8; mode: rst -*-

============
blk-cgroup.h
============


.. _`blkcg_parent`:

blkcg_parent
============

.. c:function:: struct blkcg *blkcg_parent (struct blkcg *blkcg)

    get the parent of a blkcg

    :param struct blkcg \*blkcg:
        blkcg of interest



.. _`blkcg_parent.description`:

Description
-----------

Return the parent blkcg of ``blkcg``\ .  Can be called anytime.



.. _`__blkg_lookup`:

__blkg_lookup
=============

.. c:function:: struct blkcg_gq *__blkg_lookup (struct blkcg *blkcg, struct request_queue *q, bool update_hint)

    internal version of blkg_lookup()

    :param struct blkcg \*blkcg:
        blkcg of interest

    :param struct request_queue \*q:
        request_queue of interest

    :param bool update_hint:
        whether to update lookup hint with the result or not



.. _`__blkg_lookup.description`:

Description
-----------

This is internal version and shouldn't be used by policy
implementations.  Looks up blkgs for the ``blkcg`` - ``q`` pair regardless of
``q``\ 's bypass state.  If ``update_hint`` is ``true``\ , the caller should be
holding ``q``\ ->queue_lock and lookup hint is updated on success.



.. _`blkg_lookup`:

blkg_lookup
===========

.. c:function:: struct blkcg_gq *blkg_lookup (struct blkcg *blkcg, struct request_queue *q)

    lookup blkg for the specified blkcg - q pair

    :param struct blkcg \*blkcg:
        blkcg of interest

    :param struct request_queue \*q:
        request_queue of interest



.. _`blkg_lookup.description`:

Description
-----------

Lookup blkg for the ``blkcg`` - ``q`` pair.  This function should be called
under RCU read lock and is guaranteed to return ``NULL`` if ``q`` is bypassing
- see :c:func:`blk_queue_bypass_start` for details.



.. _`blkg_to_pd`:

blkg_to_pd
==========

.. c:function:: struct blkg_policy_data *blkg_to_pd (struct blkcg_gq *blkg, struct blkcg_policy *pol)

    get policy private data

    :param struct blkcg_gq \*blkg:
        blkg of interest

    :param struct blkcg_policy \*pol:
        policy of interest



.. _`blkg_to_pd.description`:

Description
-----------

Return pointer to private data associated with the ``blkg``\ -\ ``pol`` pair.



.. _`pd_to_blkg`:

pd_to_blkg
==========

.. c:function:: struct blkcg_gq *pd_to_blkg (struct blkg_policy_data *pd)

    get blkg associated with policy private data

    :param struct blkg_policy_data \*pd:
        policy private data of interest



.. _`pd_to_blkg.description`:

Description
-----------

``pd`` is policy private data.  Determine the blkg it's associated with.



.. _`blkg_path`:

blkg_path
=========

.. c:function:: int blkg_path (struct blkcg_gq *blkg, char *buf, int buflen)

    format cgroup path of blkg

    :param struct blkcg_gq \*blkg:
        blkg of interest

    :param char \*buf:
        target buffer

    :param int buflen:
        target buffer length



.. _`blkg_path.description`:

Description
-----------

Format the path of the cgroup of ``blkg`` into ``buf``\ .



.. _`blkg_get`:

blkg_get
========

.. c:function:: void blkg_get (struct blkcg_gq *blkg)

    get a blkg reference

    :param struct blkcg_gq \*blkg:
        blkg to get



.. _`blkg_get.description`:

Description
-----------

The caller should be holding an existing reference.



.. _`blkg_put`:

blkg_put
========

.. c:function:: void blkg_put (struct blkcg_gq *blkg)

    put a blkg reference

    :param struct blkcg_gq \*blkg:
        blkg to put



.. _`blkg_for_each_descendant_pre`:

blkg_for_each_descendant_pre
============================

.. c:function:: blkg_for_each_descendant_pre ( d_blkg,  pos_css,  p_blkg)

    pre-order walk of a blkg's descendants

    :param d_blkg:
        loop cursor pointing to the current descendant

    :param pos_css:
        used for iteration

    :param p_blkg:
        target blkg to walk descendants of



.. _`blkg_for_each_descendant_pre.description`:

Description
-----------

Walk ``c_blkg`` through the descendants of ``p_blkg``\ .  Must be used with RCU
read locked.  If called under either blkcg or queue lock, the iteration
is guaranteed to include all and only online blkgs.  The caller may
update ``pos_css`` by calling :c:func:`css_rightmost_descendant` to skip subtree.
``p_blkg`` is included in the iteration and the first node to be visited.



.. _`blkg_for_each_descendant_post`:

blkg_for_each_descendant_post
=============================

.. c:function:: blkg_for_each_descendant_post ( d_blkg,  pos_css,  p_blkg)

    post-order walk of a blkg's descendants

    :param d_blkg:
        loop cursor pointing to the current descendant

    :param pos_css:
        used for iteration

    :param p_blkg:
        target blkg to walk descendants of



.. _`blkg_for_each_descendant_post.description`:

Description
-----------

Similar to :c:func:`blkg_for_each_descendant_pre` but performs post-order
traversal instead.  Synchronization rules are the same.  ``p_blkg`` is
included in the iteration and the last node to be visited.



.. _`blk_get_rl`:

blk_get_rl
==========

.. c:function:: struct request_list *blk_get_rl (struct request_queue *q, struct bio *bio)

    get request_list to use

    :param struct request_queue \*q:
        request_queue of interest

    :param struct bio \*bio:
        bio which will be attached to the allocated request (may be ``NULL``\ )



.. _`blk_get_rl.description`:

Description
-----------

The caller wants to allocate a request from ``q`` to use for ``bio``\ .  Find
the request_list to use and obtain a reference on it.  Should be called
under queue_lock.  This function is guaranteed to return non-\ ``NULL``
request_list.



.. _`blk_put_rl`:

blk_put_rl
==========

.. c:function:: void blk_put_rl (struct request_list *rl)

    put request_list

    :param struct request_list \*rl:
        request_list to put



.. _`blk_put_rl.description`:

Description
-----------

Put the reference acquired by :c:func:`blk_get_rl`.  Should be called under
queue_lock.



.. _`blk_rq_set_rl`:

blk_rq_set_rl
=============

.. c:function:: void blk_rq_set_rl (struct request *rq, struct request_list *rl)

    associate a request with a request_list

    :param struct request \*rq:
        request of interest

    :param struct request_list \*rl:
        target request_list



.. _`blk_rq_set_rl.description`:

Description
-----------

Associate ``rq`` with ``rl`` so that accounting and freeing can know the
request_list ``rq`` came from.



.. _`blk_rq_rl`:

blk_rq_rl
=========

.. c:function:: struct request_list *blk_rq_rl (struct request *rq)

    return the request_list a request came from

    :param struct request \*rq:
        request of interest



.. _`blk_rq_rl.description`:

Description
-----------

Return the request_list ``rq`` is allocated from.



.. _`blk_queue_for_each_rl`:

blk_queue_for_each_rl
=====================

.. c:function:: blk_queue_for_each_rl ( rl,  q)

    iterate through all request_lists of a request_queue

    :param rl:

        *undescribed*

    :param q:

        *undescribed*



.. _`blk_queue_for_each_rl.description`:

Description
-----------


Should be used under queue_lock.



.. _`blkg_stat_add`:

blkg_stat_add
=============

.. c:function:: void blkg_stat_add (struct blkg_stat *stat, uint64_t val)

    add a value to a blkg_stat

    :param struct blkg_stat \*stat:
        target blkg_stat

    :param uint64_t val:
        value to add



.. _`blkg_stat_add.description`:

Description
-----------

Add ``val`` to ``stat``\ .  The caller must ensure that IRQ on the same CPU
don't re-enter this function for the same counter.



.. _`blkg_stat_read`:

blkg_stat_read
==============

.. c:function:: uint64_t blkg_stat_read (struct blkg_stat *stat)

    read the current value of a blkg_stat

    :param struct blkg_stat \*stat:
        blkg_stat to read



.. _`blkg_stat_reset`:

blkg_stat_reset
===============

.. c:function:: void blkg_stat_reset (struct blkg_stat *stat)

    reset a blkg_stat

    :param struct blkg_stat \*stat:
        blkg_stat to reset



.. _`blkg_stat_add_aux`:

blkg_stat_add_aux
=================

.. c:function:: void blkg_stat_add_aux (struct blkg_stat *to, struct blkg_stat *from)

    add a blkg_stat into another's aux count

    :param struct blkg_stat \*to:
        the destination blkg_stat

    :param struct blkg_stat \*from:
        the source



.. _`blkg_stat_add_aux.description`:

Description
-----------

Add ``from``\ 's count including the aux one to ``to``\ 's aux count.



.. _`blkg_rwstat_add`:

blkg_rwstat_add
===============

.. c:function:: void blkg_rwstat_add (struct blkg_rwstat *rwstat, int rw, uint64_t val)

    add a value to a blkg_rwstat

    :param struct blkg_rwstat \*rwstat:
        target blkg_rwstat

    :param int rw:
        mask of REQ_{WRITE|SYNC}

    :param uint64_t val:
        value to add



.. _`blkg_rwstat_add.description`:

Description
-----------

Add ``val`` to ``rwstat``\ .  The counters are chosen according to ``rw``\ .  The
caller is responsible for synchronizing calls to this function.



.. _`blkg_rwstat_read`:

blkg_rwstat_read
================

.. c:function:: struct blkg_rwstat blkg_rwstat_read (struct blkg_rwstat *rwstat)

    read the current values of a blkg_rwstat

    :param struct blkg_rwstat \*rwstat:
        blkg_rwstat to read



.. _`blkg_rwstat_read.description`:

Description
-----------

Read the current snapshot of ``rwstat`` and return it in the aux counts.



.. _`blkg_rwstat_total`:

blkg_rwstat_total
=================

.. c:function:: uint64_t blkg_rwstat_total (struct blkg_rwstat *rwstat)

    read the total count of a blkg_rwstat

    :param struct blkg_rwstat \*rwstat:
        blkg_rwstat to read



.. _`blkg_rwstat_total.description`:

Description
-----------

Return the total count of ``rwstat`` regardless of the IO direction.  This
function can be called without synchronization and takes care of u64
atomicity.



.. _`blkg_rwstat_reset`:

blkg_rwstat_reset
=================

.. c:function:: void blkg_rwstat_reset (struct blkg_rwstat *rwstat)

    reset a blkg_rwstat

    :param struct blkg_rwstat \*rwstat:
        blkg_rwstat to reset



.. _`blkg_rwstat_add_aux`:

blkg_rwstat_add_aux
===================

.. c:function:: void blkg_rwstat_add_aux (struct blkg_rwstat *to, struct blkg_rwstat *from)

    add a blkg_rwstat into another's aux count

    :param struct blkg_rwstat \*to:
        the destination blkg_rwstat

    :param struct blkg_rwstat \*from:
        the source



.. _`blkg_rwstat_add_aux.description`:

Description
-----------

Add ``from``\ 's count including the aux one to ``to``\ 's aux count.

