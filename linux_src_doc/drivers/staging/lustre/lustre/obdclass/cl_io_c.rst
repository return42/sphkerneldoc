.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/cl_io.c

.. _`cl_io_is_going`:

cl_io_is_going
==============

.. c:function:: int cl_io_is_going(const struct lu_env *env)

    :param const struct lu_env \*env:
        *undescribed*

.. _`cl_io_invariant`:

cl_io_invariant
===============

.. c:function:: int cl_io_invariant(const struct cl_io *io)

    are entered and left.

    :param const struct cl_io \*io:
        *undescribed*

.. _`cl_io_fini`:

cl_io_fini
==========

.. c:function:: void cl_io_fini(const struct lu_env *env, struct cl_io *io)

    :cio_fini() bottom-to-top.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_sub_init`:

cl_io_sub_init
==============

.. c:function:: int cl_io_sub_init(const struct lu_env *env, struct cl_io *io, enum cl_io_type iot, struct cl_object *obj)

    io, by calling cl_io_operations::cio_init() top-to-bottom.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param enum cl_io_type iot:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_io_sub_init.description`:

Description
-----------

\pre obj != cl_object_top(obj)

.. _`cl_io_init`:

cl_io_init
==========

.. c:function:: int cl_io_init(const struct lu_env *env, struct cl_io *io, enum cl_io_type iot, struct cl_object *obj)

    :cio_init() top-to-bottom.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param enum cl_io_type iot:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_io_init.description`:

Description
-----------

Caller has to call \ :c:func:`cl_io_fini`\  after a call to \ :c:func:`cl_io_init`\ , no matter
what the latter returned.

\pre obj == cl_object_top(obj)
\pre cl_io_type_is_valid(iot)
\post cl_io_type_is_valid(io->ci_type) && io->ci_type == iot

.. _`cl_io_rw_init`:

cl_io_rw_init
=============

.. c:function:: int cl_io_rw_init(const struct lu_env *env, struct cl_io *io, enum cl_io_type iot, loff_t pos, size_t count)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param enum cl_io_type iot:
        *undescribed*

    :param loff_t pos:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`cl_io_rw_init.description`:

Description
-----------

\pre iot == CIT_READ \|\| iot == CIT_WRITE

.. _`cl_io_lock`:

cl_io_lock
==========

.. c:function:: int cl_io_lock(const struct lu_env *env, struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_lock.description`:

Description
-----------

Calls cl_io_operations::cio_lock() top-to-bottom to collect locks required
by layers for the current iteration. Then sort locks (to avoid dead-locks),
and acquire them.

.. _`cl_io_unlock`:

cl_io_unlock
============

.. c:function:: void cl_io_unlock(const struct lu_env *env, struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_iter_init`:

cl_io_iter_init
===============

.. c:function:: int cl_io_iter_init(const struct lu_env *env, struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_iter_init.description`:

Description
-----------

Calls cl_io_operations::cio_iter_init() top-to-bottom. This exists to give
layers a chance to modify io parameters, e.g., so that lov can restrict io
to a single stripe.

.. _`cl_io_iter_fini`:

cl_io_iter_fini
===============

.. c:function:: void cl_io_iter_fini(const struct lu_env *env, struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_iter_fini.description`:

Description
-----------

Calls cl_io_operations::cio_iter_fini() bottom-to-top.

.. _`cl_io_rw_advance`:

cl_io_rw_advance
================

.. c:function:: void cl_io_rw_advance(const struct lu_env *env, struct cl_io *io, size_t nob)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param size_t nob:
        *undescribed*

.. _`cl_io_lock_add`:

cl_io_lock_add
==============

.. c:function:: int cl_io_lock_add(const struct lu_env *env, struct cl_io *io, struct cl_io_lock_link *link)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_io_lock_link \*link:
        *undescribed*

.. _`cl_io_lock_alloc_add`:

cl_io_lock_alloc_add
====================

.. c:function:: int cl_io_lock_alloc_add(const struct lu_env *env, struct cl_io *io, struct cl_lock_descr *descr)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_lock_descr \*descr:
        *undescribed*

.. _`cl_io_start`:

cl_io_start
===========

.. c:function:: int cl_io_start(const struct lu_env *env, struct cl_io *io)

    :cio_start() top-to-bottom.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_end`:

cl_io_end
=========

.. c:function:: void cl_io_end(const struct lu_env *env, struct cl_io *io)

    cl_io_operations::cio_end() bottom-to-top.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_read_ahead`:

cl_io_read_ahead
================

.. c:function:: int cl_io_read_ahead(const struct lu_env *env, struct cl_io *io, pgoff_t start, struct cl_read_ahead *ra)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param pgoff_t start:
        *undescribed*

    :param struct cl_read_ahead \*ra:
        *undescribed*

.. _`cl_io_read_ahead.description`:

Description
-----------

\see cl_io_operations::cio_read_ahead()

.. _`cl_io_commit_async`:

cl_io_commit_async
==================

.. c:function:: int cl_io_commit_async(const struct lu_env *env, struct cl_io *io, struct cl_page_list *queue, int from, int to, cl_commit_cbt cb)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page_list \*queue:
        *undescribed*

    :param int from:
        *undescribed*

    :param int to:
        *undescribed*

    :param cl_commit_cbt cb:
        *undescribed*

.. _`cl_io_commit_async.description`:

Description
-----------

\returns 0 if all pages committed, or errcode if error occurred.
\see cl_io_operations::cio_commit_async()

.. _`cl_io_submit_rw`:

cl_io_submit_rw
===============

.. c:function:: int cl_io_submit_rw(const struct lu_env *env, struct cl_io *io, enum cl_req_type crt, struct cl_2queue *queue)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`cl_io_submit_rw.description`:

Description
-----------

After the function gets returned, The submitted pages are moved to
queue->c2_qout queue, and queue->c2_qin contain both the pages don't need
to be submitted, and the pages are errant to submit.

\returns 0 if at least one page was submitted, error code otherwise.
\see cl_io_operations::cio_submit()

.. _`cl_io_submit_sync`:

cl_io_submit_sync
=================

.. c:function:: int cl_io_submit_sync(const struct lu_env *env, struct cl_io *io, enum cl_req_type iot, struct cl_2queue *queue, long timeout)

    If \a timeout is zero, it means to wait for the IO unconditionally.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param enum cl_req_type iot:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

    :param long timeout:
        *undescribed*

.. _`cl_io_loop`:

cl_io_loop
==========

.. c:function:: int cl_io_loop(const struct lu_env *env, struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_loop.description`:

Description
-----------

Pumps io through iterations calling

- \ :c:func:`cl_io_iter_init`\ 

- \ :c:func:`cl_io_lock`\ 

- \ :c:func:`cl_io_start`\ 

- \ :c:func:`cl_io_end`\ 

- \ :c:func:`cl_io_unlock`\ 

- \ :c:func:`cl_io_iter_fini`\ 

repeatedly until there is no more io to do.

.. _`cl_io_slice_add`:

cl_io_slice_add
===============

.. c:function:: void cl_io_slice_add(struct cl_io *io, struct cl_io_slice *slice, struct cl_object *obj, const struct cl_io_operations *ops)

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_io_slice \*slice:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param const struct cl_io_operations \*ops:
        *undescribed*

.. _`cl_io_slice_add.description`:

Description
-----------

This is called by cl_object_operations::coo_io_init() methods to add a
per-layer state to the io. New state is added at the end of
cl_io::ci_layers list, that is, it is at the bottom of the stack.

\see \ :c:func:`cl_lock_slice_add`\ , \ :c:func:`cl_req_slice_add`\ , \ :c:func:`cl_page_slice_add`\ 

.. _`cl_page_list_init`:

cl_page_list_init
=================

.. c:function:: void cl_page_list_init(struct cl_page_list *plist)

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_page_list_add`:

cl_page_list_add
================

.. c:function:: void cl_page_list_add(struct cl_page_list *plist, struct cl_page *page)

    :param struct cl_page_list \*plist:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_list_del`:

cl_page_list_del
================

.. c:function:: void cl_page_list_del(const struct lu_env *env, struct cl_page_list *plist, struct cl_page *page)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page_list \*plist:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_list_move`:

cl_page_list_move
=================

.. c:function:: void cl_page_list_move(struct cl_page_list *dst, struct cl_page_list *src, struct cl_page *page)

    :param struct cl_page_list \*dst:
        *undescribed*

    :param struct cl_page_list \*src:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_list_move_head`:

cl_page_list_move_head
======================

.. c:function:: void cl_page_list_move_head(struct cl_page_list *dst, struct cl_page_list *src, struct cl_page *page)

    :param struct cl_page_list \*dst:
        *undescribed*

    :param struct cl_page_list \*src:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_list_splice`:

cl_page_list_splice
===================

.. c:function:: void cl_page_list_splice(struct cl_page_list *list, struct cl_page_list *head)

    :param struct cl_page_list \*list:
        *undescribed*

    :param struct cl_page_list \*head:
        *undescribed*

.. _`cl_page_list_disown`:

cl_page_list_disown
===================

.. c:function:: void cl_page_list_disown(const struct lu_env *env, struct cl_io *io, struct cl_page_list *plist)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_page_list_fini`:

cl_page_list_fini
=================

.. c:function:: void cl_page_list_fini(const struct lu_env *env, struct cl_page_list *plist)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_page_list_assume`:

cl_page_list_assume
===================

.. c:function:: void cl_page_list_assume(const struct lu_env *env, struct cl_io *io, struct cl_page_list *plist)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_page_list_discard`:

cl_page_list_discard
====================

.. c:function:: void cl_page_list_discard(const struct lu_env *env, struct cl_io *io, struct cl_page_list *plist)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_2queue_init`:

cl_2queue_init
==============

.. c:function:: void cl_2queue_init(struct cl_2queue *queue)

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`cl_2queue_disown`:

cl_2queue_disown
================

.. c:function:: void cl_2queue_disown(const struct lu_env *env, struct cl_io *io, struct cl_2queue *queue)

    queue.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`cl_2queue_discard`:

cl_2queue_discard
=================

.. c:function:: void cl_2queue_discard(const struct lu_env *env, struct cl_io *io, struct cl_2queue *queue)

    queue.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`cl_2queue_fini`:

cl_2queue_fini
==============

.. c:function:: void cl_2queue_fini(const struct lu_env *env, struct cl_2queue *queue)

    queue.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`cl_2queue_init_page`:

cl_2queue_init_page
===================

.. c:function:: void cl_2queue_init_page(struct cl_2queue *queue, struct cl_page *page)

    queue to contain \a page in its incoming page list.

    :param struct cl_2queue \*queue:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_io_top`:

cl_io_top
=========

.. c:function:: struct cl_io *cl_io_top(struct cl_io *io)

    level io.

    :param struct cl_io \*io:
        *undescribed*

.. _`cl_io_top.description`:

Description
-----------

\see \ :c:func:`cl_object_top`\ 

.. _`cl_req_attr_set`:

cl_req_attr_set
===============

.. c:function:: void cl_req_attr_set(const struct lu_env *env, struct cl_object *obj, struct cl_req_attr *attr)

    attributes from \a flags may be touched. This can be called multiple times for the same request.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_req_attr \*attr:
        *undescribed*

.. _`cl_sync_io_init`:

cl_sync_io_init
===============

.. c:function:: void cl_sync_io_init(struct cl_sync_io *anchor, int nr, void (*end)(const struct lu_env *, struct cl_sync_io *))

    :param struct cl_sync_io \*anchor:
        *undescribed*

    :param int nr:
        *undescribed*

    :param void (\*end)(const struct lu_env \*, struct cl_sync_io \*):
        *undescribed*

.. _`cl_sync_io_wait`:

cl_sync_io_wait
===============

.. c:function:: int cl_sync_io_wait(const struct lu_env *env, struct cl_sync_io *anchor, long timeout)

    cl_sync_io_note() for every entity.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_sync_io \*anchor:
        *undescribed*

    :param long timeout:
        *undescribed*

.. _`cl_sync_io_note`:

cl_sync_io_note
===============

.. c:function:: void cl_sync_io_note(const struct lu_env *env, struct cl_sync_io *anchor, int ioret)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_sync_io \*anchor:
        *undescribed*

    :param int ioret:
        *undescribed*

.. This file was automatic generated / don't edit.

