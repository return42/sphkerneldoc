.. -*- coding: utf-8; mode: rst -*-

=========
cl_page.c
=========


.. _`cl_page_top_trusted`:

cl_page_top_trusted
===================

.. c:function:: struct cl_page *cl_page_top_trusted (struct cl_page *page)

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_top_trusted.description`:

Description
-----------

known to be not freed, says with page referenced, or radix tree lock held,
or page owned.



.. _`cl_page_get_trust`:

cl_page_get_trust
=================

.. c:function:: void cl_page_get_trust (struct cl_page *page)

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_get_trust.description`:

Description
-----------


This function can be used to obtain initial reference to previously
unreferenced cached object. It can be called only if concurrent page
reclamation is somehow prevented, e.g., by locking page radix-tree
(cl_object_header::hdr->coh_page_guard), or by keeping a lock on a VM page,
associated with \a page.

Use with care! Not exported.



.. _`cl_page_at_trusted`:

cl_page_at_trusted
==================

.. c:function:: const struct cl_page_slice *cl_page_at_trusted (const struct cl_page *page, const struct lu_device_type *dtype)

    :param const struct cl_page \*page:

        *undescribed*

    :param const struct lu_device_type \*dtype:

        *undescribed*



.. _`cl_page_at_trusted.description`:

Description
-----------

device stack.

\see :c:func:`cl_lock_at`



.. _`cl_page_lookup`:

cl_page_lookup
==============

.. c:function:: struct cl_page *cl_page_lookup (struct cl_object_header *hdr, pgoff_t index)

    :param struct cl_object_header \*hdr:

        *undescribed*

    :param pgoff_t index:

        *undescribed*



.. _`cl_page_lookup.description`:

Description
-----------

found. Acquires a reference on \a page.



.. _`cl_page_lookup.locking`:

Locking
-------

called under cl_object_header::coh_page_guard spin-lock.



.. _`cl_page_gang_lookup`:

cl_page_gang_lookup
===================

.. c:function:: int cl_page_gang_lookup (const struct lu_env *env, struct cl_object *obj, struct cl_io *io, pgoff_t start, pgoff_t end, cl_page_gang_cb_t cb, void *cbdata)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param pgoff_t start:

        *undescribed*

    :param pgoff_t end:

        *undescribed*

    :param cl_page_gang_cb_t cb:

        *undescribed*

    :param void \*cbdata:

        *undescribed*



.. _`cl_page_gang_lookup.description`:

Description
-----------


\param resched If not NULL, then we give up before hogging CPU for too
long and set \*resched = 1, in that case caller should implement a retry
logic.

Gang tree lookup (:c:func:`radix_tree_gang_lookup`) optimization is absolutely
crucial in the face of [offset, EOF] locks.

Return at least one page in ``queue`` unless there is no covered page.



.. _`cl_page_state_set_trust`:

cl_page_state_set_trust
=======================

.. c:function:: void cl_page_state_set_trust (struct cl_page *page, enum cl_page_state state)

    :param struct cl_page \*page:

        *undescribed*

    :param enum cl_page_state state:

        *undescribed*



.. _`cl_page_state_set_trust.where-cl_page`:

where cl_page
-------------

:cp_state field is mutated.



.. _`cl_page_find0`:

cl_page_find0
=============

.. c:function:: struct cl_page *cl_page_find0 (const struct lu_env *env, struct cl_object *o, pgoff_t idx, struct page *vmpage, enum cl_page_type type, struct cl_page *parent)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_object \*o:

        *undescribed*

    :param pgoff_t idx:

        *undescribed*

    :param struct page \*vmpage:

        *undescribed*

    :param enum cl_page_type type:

        *undescribed*

    :param struct cl_page \*parent:

        *undescribed*



.. _`cl_page_find0.description`:

Description
-----------

the VM page \a vmpage.

This is the main entry point into the cl_page caching interface. First, a
cache (implemented as a per-object radix tree) is consulted. If page is
found there, it is returned immediately. Otherwise new page is allocated
and returned. In any case, additional reference to page is acquired.

\see :c:func:`cl_object_find`, :c:func:`cl_lock_find`



.. _`cl_page_get`:

cl_page_get
===========

.. c:function:: void cl_page_get (struct cl_page *page)

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_get.description`:

Description
-----------


This can be called only by caller already possessing a reference to \a
page.

\see :c:func:`cl_object_get`, :c:func:`cl_lock_get`.



.. _`cl_page_put`:

cl_page_put
===========

.. c:function:: void cl_page_put (const struct lu_env *env, struct cl_page *page)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_put.description`:

Description
-----------


When last reference is released, page is returned to the cache, unless it



.. _`cl_page_put.is-in-cl_page_state`:

is in cl_page_state
-------------------

:CPS_FREEING state, in which case it is immediately
destroyed.

\see :c:func:`cl_object_put`, :c:func:`cl_lock_put`.



.. _`cl_page_vmpage`:

cl_page_vmpage
==============

.. c:function:: struct page *cl_page_vmpage (const struct lu_env *env, struct cl_page *page)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_vmpage_page`:

cl_vmpage_page
==============

.. c:function:: struct cl_page *cl_vmpage_page (struct page *vmpage, struct cl_object *obj)

    :param struct page \*vmpage:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*



.. _`cl_page_top`:

cl_page_top
===========

.. c:function:: struct cl_page *cl_page_top (struct cl_page *page)

    page for a given page.

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_top.description`:

Description
-----------


\see :c:func:`cl_object_top`, :c:func:`cl_io_top`



.. _`cl_page_is_owned`:

cl_page_is_owned
================

.. c:function:: int cl_page_is_owned (const struct cl_page *pg, const struct cl_io *io)

    :param const struct cl_page \*pg:

        *undescribed*

    :param const struct cl_io \*io:

        *undescribed*



.. _`cl_page_own0`:

cl_page_own0
============

.. c:function:: int cl_page_own0 (const struct lu_env *env, struct cl_io *io, struct cl_page *pg, int nonblock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param int nonblock:

        *undescribed*



.. _`cl_page_own0.waits-until-page-is-in-cl_page_state`:

Waits until page is in cl_page_state
------------------------------------

:CPS_CACHED state, and then switch it



.. _`cl_page_own0.into-cl_page_state`:

into cl_page_state
------------------

:CPS_OWNED state.

\pre  !cl_page_is_owned(pg, io)
\post result == 0 iff cl_page_is_owned(pg, io)

\retval 0   success

\retval -ve failure, e.g., page was destroyed (and landed in



.. _`cl_page_own0.cl_page_state`:

cl_page_state
-------------

:CPS_FREEING instead of cl_page_state::CPS_CACHED).
or, page was owned by another thread, or in IO.

\see :c:func:`cl_page_disown`
\see cl_page_operations:::c:func:`cpo_own`
\see :c:func:`cl_page_own_try`
\see cl_page_own



.. _`cl_page_own`:

cl_page_own
===========

.. c:function:: int cl_page_own (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_own.description`:

Description
-----------


\see :c:func:`cl_page_own0`



.. _`cl_page_own_try`:

cl_page_own_try
===============

.. c:function:: int cl_page_own_try (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_own_try.description`:

Description
-----------


\see :c:func:`cl_page_own0`



.. _`cl_page_assume`:

cl_page_assume
==============

.. c:function:: void cl_page_assume (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_assume.description`:

Description
-----------


Called when page is already locked by the hosting VM.

\pre !cl_page_is_owned(pg, io)
\post cl_page_is_owned(pg, io)

\see cl_page_operations:::c:func:`cpo_assume`



.. _`cl_page_unassume`:

cl_page_unassume
================

.. c:function:: void cl_page_unassume (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_unassume.moves-page-into-cl_page_state`:

Moves page into cl_page_state
-----------------------------

:CPS_CACHED without releasing a lock on the
underlying VM page (as VM is supposed to do this itself).

\pre   cl_page_is_owned(pg, io)
\post !cl_page_is_owned(pg, io)

\see :c:func:`cl_page_assume`



.. _`cl_page_disown`:

cl_page_disown
==============

.. c:function:: void cl_page_disown (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_disown.moves-page-into-cl_page_state`:

Moves page into cl_page_state
-----------------------------

:CPS_CACHED.

\pre   cl_page_is_owned(pg, io)
\post !cl_page_is_owned(pg, io)

\see :c:func:`cl_page_own`
\see cl_page_operations:::c:func:`cpo_disown`



.. _`cl_page_discard`:

cl_page_discard
===============

.. c:function:: void cl_page_discard (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_discard.description`:

Description
-----------

truncate.



.. _`cl_page_discard.calls-cl_page_operations`:

Calls cl_page_operations
------------------------

::c:func:`cpo_discard` top-to-bottom.

\pre cl_page_is_owned(pg, io)

\see cl_page_operations:::c:func:`cpo_discard`



.. _`cl_page_delete0`:

cl_page_delete0
===============

.. c:function:: void cl_page_delete0 (const struct lu_env *env, struct cl_page *pg, int radix)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param int radix:

        *undescribed*



.. _`cl_page_delete0.description`:

Description
-----------

pages, e.g,. in a error handling :c:func:`cl_page_find`->:c:func:`cl_page_delete0`
path. Doesn't check page invariant.



.. _`cl_page_delete`:

cl_page_delete
==============

.. c:function:: void cl_page_delete (const struct lu_env *env, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_delete.description`:

Description
-----------


Notifies all layers about page destruction by calling



.. _`cl_page_delete.cl_page_operations`:

cl_page_operations
------------------

::c:func:`cpo_delete` method top-to-bottom.



.. _`cl_page_delete.moves-page-into-cl_page_state`:

Moves page into cl_page_state
-----------------------------

:CPS_FREEING state (this is the only place
where transition to this state happens).

Eliminates all venues through which new references to the page can be



.. _`cl_page_delete.obtained`:

obtained
--------


- removes page from the radix trees,

- breaks linkage from VM page to cl_page.



.. _`cl_page_delete.once-page-reaches-cl_page_state`:

Once page reaches cl_page_state
-------------------------------

:CPS_FREEING, all remaining references will
drain after some time, at which point page will be recycled.

\pre  pg == cl_page_top(pg)
\pre  VM page is locked
\post pg->cp_state == CPS_FREEING

\see cl_page_operations:::c:func:`cpo_delete`



.. _`cl_page_unmap`:

cl_page_unmap
=============

.. c:function:: int cl_page_unmap (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_unmap.calls-cl_page_operations`:

Calls cl_page_operations
------------------------

::c:func:`cpo_unmap` through all layers top-to-bottom. The
layer responsible for VM interaction has to unmap page from user space
virtual memory.

\see cl_page_operations:::c:func:`cpo_unmap`



.. _`cl_page_export`:

cl_page_export
==============

.. c:function:: void cl_page_export (const struct lu_env *env, struct cl_page *pg, int uptodate)

    to-date.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param int uptodate:

        *undescribed*



.. _`cl_page_export.call-cl_page_operations`:

Call cl_page_operations
-----------------------

::c:func:`cpo_export` through all layers top-to-bottom. The
layer responsible for VM interaction has to mark/clear page as up-to-date
by the \a uptodate argument.

\see cl_page_operations:::c:func:`cpo_export`



.. _`cl_page_is_vmlocked`:

cl_page_is_vmlocked
===================

.. c:function:: int cl_page_is_vmlocked (const struct lu_env *env, const struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_page \*pg:

        *undescribed*



.. _`cl_page_is_vmlocked.description`:

Description
-----------

thread.



.. _`cl_page_prep`:

cl_page_prep
============

.. c:function:: int cl_page_prep (const struct lu_env *env, struct cl_io *io, struct cl_page *pg, enum cl_req_type crt)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param enum cl_req_type crt:

        *undescribed*



.. _`cl_page_prep.description`:

Description
-----------

called top-to-bottom. Every layer either agrees to submit this page (by
returning 0), or requests to omit this page (by returning -EALREADY). Layer
handling interactions with the VM also has to inform VM that page is under
transfer now.



.. _`cl_page_completion`:

cl_page_completion
==================

.. c:function:: void cl_page_completion (const struct lu_env *env, struct cl_page *pg, enum cl_req_type crt, int ioret)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param enum cl_req_type crt:

        *undescribed*

    :param int ioret:

        *undescribed*



.. _`cl_page_completion.description`:

Description
-----------


Invoked by transfer sub-system (which is a part of osc) to notify layers
that a transfer, of which this page is a part of has completed.

Completion call-backs are executed in the bottom-up order, so that
uppermost layer (llite), responsible for the VFS/VM interaction runs last
and can release locks safely.

\pre  pg->cp_state == CPS_PAGEIN || pg->cp_state == CPS_PAGEOUT
\post pg->cp_state == CPS_CACHED

\see cl_page_operations:::c:func:`cpo_completion`



.. _`cl_page_make_ready`:

cl_page_make_ready
==================

.. c:function:: int cl_page_make_ready (const struct lu_env *env, struct cl_page *pg, enum cl_req_type crt)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param enum cl_req_type crt:

        *undescribed*



.. _`cl_page_make_ready.description`:

Description
-----------

the cache and to make it a part of a transfer.

\pre  pg->cp_state == CPS_CACHED
\post pg->cp_state == CPS_PAGEIN || pg->cp_state == CPS_PAGEOUT

\see cl_page_operations:::c:func:`cpo_make_ready`



.. _`cl_page_cache_add`:

cl_page_cache_add
=================

.. c:function:: int cl_page_cache_add (const struct lu_env *env, struct cl_io *io, struct cl_page *pg, enum cl_req_type crt)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param enum cl_req_type crt:

        *undescribed*



.. _`cl_page_cache_add.description`:

Description
-----------

for future transfer.

The layer implementing transfer engine (osc) has to register this page in
its queues.

\pre  cl_page_is_owned(pg, io)
\post cl_page_is_owned(pg, io)

\see cl_page_operations:::c:func:`cpo_cache_add`



.. _`cl_page_flush`:

cl_page_flush
=============

.. c:function:: int cl_page_flush (const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*



.. _`cl_page_flush.description`:

Description
-----------


\pre  cl_page_is_owned(pg, io)
\post ergo(result == 0, pg->cp_state == CPS_PAGEOUT)

\see cl_page_operations:::c:func:`cpo_flush`



.. _`cl_page_is_under_lock`:

cl_page_is_under_lock
=====================

.. c:function:: int cl_page_is_under_lock (const struct lu_env *env, struct cl_io *io, struct cl_page *page)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_page_is_under_lock.description`:

Description
-----------

mode.

\return the same as in cl_page_operations:::c:func:`cpo_is_under_lock` method.
\see cl_page_operations:::c:func:`cpo_is_under_lock`



.. _`cl_pages_prune`:

cl_pages_prune
==============

.. c:function:: int cl_pages_prune (const struct lu_env *env, struct cl_object *clobj)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_object \*clobj:

        *undescribed*



.. _`cl_page_clip`:

cl_page_clip
============

.. c:function:: void cl_page_clip (const struct lu_env *env, struct cl_page *pg, int from, int to)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*pg:

        *undescribed*

    :param int from:

        *undescribed*

    :param int to:

        *undescribed*



.. _`cl_page_clip.description`:

Description
-----------


\see cl_page_operations:::c:func:`cpo_clip`



.. _`cl_page_header_print`:

cl_page_header_print
====================

.. c:function:: void cl_page_header_print (const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param void \*cookie:

        *undescribed*

    :param lu_printer_t printer:

        *undescribed*

    :param const struct cl_page \*pg:

        *undescribed*



.. _`cl_page_print`:

cl_page_print
=============

.. c:function:: void cl_page_print (const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_page *pg)

    :param const struct lu_env \*env:

        *undescribed*

    :param void \*cookie:

        *undescribed*

    :param lu_printer_t printer:

        *undescribed*

    :param const struct cl_page \*pg:

        *undescribed*



.. _`cl_page_cancel`:

cl_page_cancel
==============

.. c:function:: int cl_page_cancel (const struct lu_env *env, struct cl_page *page)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_page \*page:

        *undescribed*



.. _`cl_offset`:

cl_offset
=========

.. c:function:: loff_t cl_offset (const struct cl_object *obj, pgoff_t idx)

    :param const struct cl_object \*obj:

        *undescribed*

    :param pgoff_t idx:

        *undescribed*



.. _`cl_index`:

cl_index
========

.. c:function:: pgoff_t cl_index (const struct cl_object *obj, loff_t offset)

    :param const struct cl_object \*obj:

        *undescribed*

    :param loff_t offset:

        *undescribed*



.. _`cl_page_slice_add`:

cl_page_slice_add
=================

.. c:function:: void cl_page_slice_add (struct cl_page *page, struct cl_page_slice *slice, struct cl_object *obj, const struct cl_page_operations *ops)

    :param struct cl_page \*page:

        *undescribed*

    :param struct cl_page_slice \*slice:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*

    :param const struct cl_page_operations \*ops:

        *undescribed*



.. _`cl_page_slice_add.this-is-called-by-cl_object_operations`:

This is called by cl_object_operations
--------------------------------------

::c:func:`coo_page_init` methods to add a
per-layer state to the page. New state is added at the end of



.. _`cl_page_slice_add.cl_page`:

cl_page
-------

:cp_layers list, that is, it is at the bottom of the stack.

\see :c:func:`cl_lock_slice_add`, :c:func:`cl_req_slice_add`, :c:func:`cl_io_slice_add`

