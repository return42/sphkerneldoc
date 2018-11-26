.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blk-cgroup.h

.. _`bio_issue_as_root_blkg`:

bio_issue_as_root_blkg
======================

.. c:function:: bool bio_issue_as_root_blkg(struct bio *bio)

    see if this bio needs to be issued as root blkg

    :param bio:
        *undescribed*
    :type bio: struct bio \*

.. _`bio_issue_as_root_blkg.description`:

Description
-----------

In order to avoid priority inversions we sometimes need to issue a bio as if
it were attached to the root blkg, and then backcharge to the actual owning
blkg.  The idea is we do \ :c:func:`bio_blkcg`\  to look up the actual context for the
bio and attach the appropriate blkg to the bio.  Then we call this helper and
if it is true run with the root blkg for that queue and then do any
backcharging to the originating cgroup once the io is complete.

.. _`blkcg_parent`:

blkcg_parent
============

.. c:function:: struct blkcg *blkcg_parent(struct blkcg *blkcg)

    get the parent of a blkcg

    :param blkcg:
        blkcg of interest
    :type blkcg: struct blkcg \*

.. _`blkcg_parent.description`:

Description
-----------

Return the parent blkcg of \ ``blkcg``\ .  Can be called anytime.

.. _`__blkg_lookup`:

\__blkg_lookup
==============

.. c:function:: struct blkcg_gq *__blkg_lookup(struct blkcg *blkcg, struct request_queue *q, bool update_hint)

    internal version of \ :c:func:`blkg_lookup`\ 

    :param blkcg:
        blkcg of interest
    :type blkcg: struct blkcg \*

    :param q:
        request_queue of interest
    :type q: struct request_queue \*

    :param update_hint:
        whether to update lookup hint with the result or not
    :type update_hint: bool

.. _`__blkg_lookup.description`:

Description
-----------

This is internal version and shouldn't be used by policy
implementations.  Looks up blkgs for the \ ``blkcg``\  - \ ``q``\  pair regardless of
\ ``q``\ 's bypass state.  If \ ``update_hint``\  is \ ``true``\ , the caller should be
holding \ ``q->queue_lock``\  and lookup hint is updated on success.

.. _`blkg_lookup`:

blkg_lookup
===========

.. c:function:: struct blkcg_gq *blkg_lookup(struct blkcg *blkcg, struct request_queue *q)

    lookup blkg for the specified blkcg - q pair

    :param blkcg:
        blkcg of interest
    :type blkcg: struct blkcg \*

    :param q:
        request_queue of interest
    :type q: struct request_queue \*

.. _`blkg_lookup.description`:

Description
-----------

Lookup blkg for the \ ``blkcg``\  - \ ``q``\  pair.  This function should be called
under RCU read lock and is guaranteed to return \ ``NULL``\  if \ ``q``\  is bypassing
- see \ :c:func:`blk_queue_bypass_start`\  for details.

.. _`blk_queue_root_blkg`:

blk_queue_root_blkg
===================

.. c:function:: struct blkcg_gq *blk_queue_root_blkg(struct request_queue *q)

    return blkg for the (blkcg_root, \ ``q``\ ) pair

    :param q:
        request_queue of interest
    :type q: struct request_queue \*

.. _`blk_queue_root_blkg.description`:

Description
-----------

Lookup blkg for \ ``q``\  at the root level. See also \ :c:func:`blkg_lookup`\ .

.. _`blkg_to_pd`:

blkg_to_pd
==========

.. c:function:: struct blkg_policy_data *blkg_to_pd(struct blkcg_gq *blkg, struct blkcg_policy *pol)

    get policy private data

    :param blkg:
        blkg of interest
    :type blkg: struct blkcg_gq \*

    :param pol:
        policy of interest
    :type pol: struct blkcg_policy \*

.. _`blkg_to_pd.description`:

Description
-----------

Return pointer to private data associated with the \ ``blkg``\ -@pol pair.

.. _`pd_to_blkg`:

pd_to_blkg
==========

.. c:function:: struct blkcg_gq *pd_to_blkg(struct blkg_policy_data *pd)

    get blkg associated with policy private data

    :param pd:
        policy private data of interest
    :type pd: struct blkg_policy_data \*

.. _`pd_to_blkg.description`:

Description
-----------

\ ``pd``\  is policy private data.  Determine the blkg it's associated with.

.. _`blkcg_cgwb_get`:

blkcg_cgwb_get
==============

.. c:function:: void blkcg_cgwb_get(struct blkcg *blkcg)

    get a reference for blkcg->cgwb_list

    :param blkcg:
        blkcg of interest
    :type blkcg: struct blkcg \*

.. _`blkcg_cgwb_get.description`:

Description
-----------

This is used to track the number of active wb's related to a blkcg.

.. _`blkcg_cgwb_put`:

blkcg_cgwb_put
==============

.. c:function:: void blkcg_cgwb_put(struct blkcg *blkcg)

    put a reference for \ ``blkcg->cgwb_list``\ 

    :param blkcg:
        blkcg of interest
    :type blkcg: struct blkcg \*

.. _`blkcg_cgwb_put.description`:

Description
-----------

This is used to track the number of active wb's related to a blkcg.
When this count goes to zero, all active wb has finished so the
blkcg can continue destruction by calling \ :c:func:`blkcg_destroy_blkgs`\ .
This work may occur in \ :c:func:`cgwb_release_workfn`\  on the cgwb_release
workqueue.

.. _`blkg_path`:

blkg_path
=========

.. c:function:: int blkg_path(struct blkcg_gq *blkg, char *buf, int buflen)

    format cgroup path of blkg

    :param blkg:
        blkg of interest
    :type blkg: struct blkcg_gq \*

    :param buf:
        target buffer
    :type buf: char \*

    :param buflen:
        target buffer length
    :type buflen: int

.. _`blkg_path.description`:

Description
-----------

Format the path of the cgroup of \ ``blkg``\  into \ ``buf``\ .

.. _`blkg_get`:

blkg_get
========

.. c:function:: void blkg_get(struct blkcg_gq *blkg)

    get a blkg reference

    :param blkg:
        blkg to get
    :type blkg: struct blkcg_gq \*

.. _`blkg_get.description`:

Description
-----------

The caller should be holding an existing reference.

.. _`blkg_try_get`:

blkg_try_get
============

.. c:function:: struct blkcg_gq *blkg_try_get(struct blkcg_gq *blkg)

    try and get a blkg reference

    :param blkg:
        blkg to get
    :type blkg: struct blkcg_gq \*

.. _`blkg_try_get.description`:

Description
-----------

This is for use when doing an RCU lookup of the blkg.  We may be in the midst
of freeing this blkg, so we can only use it if the refcnt is not zero.

.. _`blkg_put`:

blkg_put
========

.. c:function:: void blkg_put(struct blkcg_gq *blkg)

    put a blkg reference

    :param blkg:
        blkg to put
    :type blkg: struct blkcg_gq \*

.. _`blkg_for_each_descendant_pre`:

blkg_for_each_descendant_pre
============================

.. c:function::  blkg_for_each_descendant_pre( d_blkg,  pos_css,  p_blkg)

    pre-order walk of a blkg's descendants

    :param d_blkg:
        loop cursor pointing to the current descendant
    :type d_blkg: 

    :param pos_css:
        used for iteration
    :type pos_css: 

    :param p_blkg:
        target blkg to walk descendants of
    :type p_blkg: 

.. _`blkg_for_each_descendant_pre.description`:

Description
-----------

Walk \ ``c_blkg``\  through the descendants of \ ``p_blkg``\ .  Must be used with RCU
read locked.  If called under either blkcg or queue lock, the iteration
is guaranteed to include all and only online blkgs.  The caller may
update \ ``pos_css``\  by calling \ :c:func:`css_rightmost_descendant`\  to skip subtree.
\ ``p_blkg``\  is included in the iteration and the first node to be visited.

.. _`blkg_for_each_descendant_post`:

blkg_for_each_descendant_post
=============================

.. c:function::  blkg_for_each_descendant_post( d_blkg,  pos_css,  p_blkg)

    post-order walk of a blkg's descendants

    :param d_blkg:
        loop cursor pointing to the current descendant
    :type d_blkg: 

    :param pos_css:
        used for iteration
    :type pos_css: 

    :param p_blkg:
        target blkg to walk descendants of
    :type p_blkg: 

.. _`blkg_for_each_descendant_post.description`:

Description
-----------

Similar to \ :c:func:`blkg_for_each_descendant_pre`\  but performs post-order
traversal instead.  Synchronization rules are the same.  \ ``p_blkg``\  is
included in the iteration and the last node to be visited.

.. _`blk_get_rl`:

blk_get_rl
==========

.. c:function:: struct request_list *blk_get_rl(struct request_queue *q, struct bio *bio)

    get request_list to use

    :param q:
        request_queue of interest
    :type q: struct request_queue \*

    :param bio:
        bio which will be attached to the allocated request (may be \ ``NULL``\ )
    :type bio: struct bio \*

.. _`blk_get_rl.description`:

Description
-----------

The caller wants to allocate a request from \ ``q``\  to use for \ ``bio``\ .  Find
the request_list to use and obtain a reference on it.  Should be called
under queue_lock.  This function is guaranteed to return non-%NULL
request_list.

.. _`blk_put_rl`:

blk_put_rl
==========

.. c:function:: void blk_put_rl(struct request_list *rl)

    put request_list

    :param rl:
        request_list to put
    :type rl: struct request_list \*

.. _`blk_put_rl.description`:

Description
-----------

Put the reference acquired by \ :c:func:`blk_get_rl`\ .  Should be called under
queue_lock.

.. _`blk_rq_set_rl`:

blk_rq_set_rl
=============

.. c:function:: void blk_rq_set_rl(struct request *rq, struct request_list *rl)

    associate a request with a request_list

    :param rq:
        request of interest
    :type rq: struct request \*

    :param rl:
        target request_list
    :type rl: struct request_list \*

.. _`blk_rq_set_rl.description`:

Description
-----------

Associate \ ``rq``\  with \ ``rl``\  so that accounting and freeing can know the
request_list \ ``rq``\  came from.

.. _`blk_rq_rl`:

blk_rq_rl
=========

.. c:function:: struct request_list *blk_rq_rl(struct request *rq)

    return the request_list a request came from

    :param rq:
        request of interest
    :type rq: struct request \*

.. _`blk_rq_rl.description`:

Description
-----------

Return the request_list \ ``rq``\  is allocated from.

.. _`blk_queue_for_each_rl`:

blk_queue_for_each_rl
=====================

.. c:function::  blk_queue_for_each_rl( rl,  q)

    iterate through all request_lists of a request_queue

    :param rl:
        *undescribed*
    :type rl: 

    :param q:
        *undescribed*
    :type q: 

.. _`blk_queue_for_each_rl.description`:

Description
-----------

Should be used under queue_lock.

.. _`blkg_stat_add`:

blkg_stat_add
=============

.. c:function:: void blkg_stat_add(struct blkg_stat *stat, uint64_t val)

    add a value to a blkg_stat

    :param stat:
        target blkg_stat
    :type stat: struct blkg_stat \*

    :param val:
        value to add
    :type val: uint64_t

.. _`blkg_stat_add.description`:

Description
-----------

Add \ ``val``\  to \ ``stat``\ .  The caller must ensure that IRQ on the same CPU
don't re-enter this function for the same counter.

.. _`blkg_stat_read`:

blkg_stat_read
==============

.. c:function:: uint64_t blkg_stat_read(struct blkg_stat *stat)

    read the current value of a blkg_stat

    :param stat:
        blkg_stat to read
    :type stat: struct blkg_stat \*

.. _`blkg_stat_reset`:

blkg_stat_reset
===============

.. c:function:: void blkg_stat_reset(struct blkg_stat *stat)

    reset a blkg_stat

    :param stat:
        blkg_stat to reset
    :type stat: struct blkg_stat \*

.. _`blkg_stat_add_aux`:

blkg_stat_add_aux
=================

.. c:function:: void blkg_stat_add_aux(struct blkg_stat *to, struct blkg_stat *from)

    add a blkg_stat into another's aux count

    :param to:
        the destination blkg_stat
    :type to: struct blkg_stat \*

    :param from:
        the source
    :type from: struct blkg_stat \*

.. _`blkg_stat_add_aux.description`:

Description
-----------

Add \ ``from``\ 's count including the aux one to \ ``to``\ 's aux count.

.. _`blkg_rwstat_add`:

blkg_rwstat_add
===============

.. c:function:: void blkg_rwstat_add(struct blkg_rwstat *rwstat, unsigned int op, uint64_t val)

    add a value to a blkg_rwstat

    :param rwstat:
        target blkg_rwstat
    :type rwstat: struct blkg_rwstat \*

    :param op:
        REQ_OP and flags
    :type op: unsigned int

    :param val:
        value to add
    :type val: uint64_t

.. _`blkg_rwstat_add.description`:

Description
-----------

Add \ ``val``\  to \ ``rwstat``\ .  The counters are chosen according to \ ``rw``\ .  The
caller is responsible for synchronizing calls to this function.

.. _`blkg_rwstat_read`:

blkg_rwstat_read
================

.. c:function:: struct blkg_rwstat blkg_rwstat_read(struct blkg_rwstat *rwstat)

    read the current values of a blkg_rwstat

    :param rwstat:
        blkg_rwstat to read
    :type rwstat: struct blkg_rwstat \*

.. _`blkg_rwstat_read.description`:

Description
-----------

Read the current snapshot of \ ``rwstat``\  and return it in the aux counts.

.. _`blkg_rwstat_total`:

blkg_rwstat_total
=================

.. c:function:: uint64_t blkg_rwstat_total(struct blkg_rwstat *rwstat)

    read the total count of a blkg_rwstat

    :param rwstat:
        blkg_rwstat to read
    :type rwstat: struct blkg_rwstat \*

.. _`blkg_rwstat_total.description`:

Description
-----------

Return the total count of \ ``rwstat``\  regardless of the IO direction.  This
function can be called without synchronization and takes care of u64
atomicity.

.. _`blkg_rwstat_reset`:

blkg_rwstat_reset
=================

.. c:function:: void blkg_rwstat_reset(struct blkg_rwstat *rwstat)

    reset a blkg_rwstat

    :param rwstat:
        blkg_rwstat to reset
    :type rwstat: struct blkg_rwstat \*

.. _`blkg_rwstat_add_aux`:

blkg_rwstat_add_aux
===================

.. c:function:: void blkg_rwstat_add_aux(struct blkg_rwstat *to, struct blkg_rwstat *from)

    add a blkg_rwstat into another's aux count

    :param to:
        the destination blkg_rwstat
    :type to: struct blkg_rwstat \*

    :param from:
        the source
    :type from: struct blkg_rwstat \*

.. _`blkg_rwstat_add_aux.description`:

Description
-----------

Add \ ``from``\ 's count including the aux one to \ ``to``\ 's aux count.

.. This file was automatic generated / don't edit.

