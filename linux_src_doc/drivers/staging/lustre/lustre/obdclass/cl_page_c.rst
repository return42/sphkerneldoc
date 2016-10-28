.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/cl_page.c

.. _`cl_page_get_trust`:

cl_page_get_trust
=================

.. c:function:: void cl_page_get_trust(struct cl_page *page)

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_get_trust.description`:

Description
-----------

This function can be used to obtain initial reference to previously
unreferenced cached object. It can be called only if concurrent page
reclamation is somehow prevented, e.g., by keeping a lock on a VM page,
associated with \a page.

Use with care! Not exported.

.. _`cl_page_at_trusted`:

cl_page_at_trusted
==================

.. c:function:: const struct cl_page_slice *cl_page_at_trusted(const struct cl_page *page, const struct lu_device_type *dtype)

    device stack.

    :param const struct cl_page \*page:
        *undescribed*

    :param const struct lu_device_type \*dtype:
        *undescribed*

.. _`cl_page_at_trusted.description`:

Description
-----------

\see \ :c:func:`cl_lock_at`\ 

.. _`cl_page_state_set_trust`:

cl_page_state_set_trust
=======================

.. c:function:: void cl_page_state_set_trust(struct cl_page *page, enum cl_page_state state)

    where cl_page::cp_state field is mutated.

    :param struct cl_page \*page:
        *undescribed*

    :param enum cl_page_state state:
        *undescribed*

.. _`cl_page_find`:

cl_page_find
============

.. c:function:: struct cl_page *cl_page_find(const struct lu_env *env, struct cl_object *o, pgoff_t idx, struct page *vmpage, enum cl_page_type type)

    the VM page \a vmpage.

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

.. _`cl_page_find.description`:

Description
-----------

This is the main entry point into the cl_page caching interface. First, a
cache (implemented as a per-object radix tree) is consulted. If page is
found there, it is returned immediately. Otherwise new page is allocated
and returned. In any case, additional reference to page is acquired.

\see \ :c:func:`cl_object_find`\ , \ :c:func:`cl_lock_find`\ 

.. _`cl_page_get`:

cl_page_get
===========

.. c:function:: void cl_page_get(struct cl_page *page)

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_get.description`:

Description
-----------

This can be called only by caller already possessing a reference to \a
page.

\see \ :c:func:`cl_object_get`\ , \ :c:func:`cl_lock_get`\ .

.. _`cl_page_put`:

cl_page_put
===========

.. c:function:: void cl_page_put(const struct lu_env *env, struct cl_page *page)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_page_put.description`:

Description
-----------

When last reference is released, page is returned to the cache, unless it
is in cl_page_state::CPS_FREEING state, in which case it is immediately
destroyed.

\see \ :c:func:`cl_object_put`\ , \ :c:func:`cl_lock_put`\ .

.. _`cl_vmpage_page`:

cl_vmpage_page
==============

.. c:function:: struct cl_page *cl_vmpage_page(struct page *vmpage, struct cl_object *obj)

    :param struct page \*vmpage:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_page_is_owned`:

cl_page_is_owned
================

.. c:function:: int cl_page_is_owned(const struct cl_page *pg, const struct cl_io *io)

    :param const struct cl_page \*pg:
        *undescribed*

    :param const struct cl_io \*io:
        *undescribed*

.. _`cl_page_own0`:

cl_page_own0
============

.. c:function:: int cl_page_own0(const struct lu_env *env, struct cl_io *io, struct cl_page *pg, int nonblock)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

    :param int nonblock:
        *undescribed*

.. _`cl_page_own0.description`:

Description
-----------

Waits until page is in cl_page_state::CPS_CACHED state, and then switch it
into cl_page_state::CPS_OWNED state.

\pre  !cl_page_is_owned(pg, io)
\post result == 0 iff cl_page_is_owned(pg, io)

\retval 0   success

\retval -ve failure, e.g., page was destroyed (and landed in
cl_page_state::CPS_FREEING instead of cl_page_state::CPS_CACHED).
or, page was owned by another thread, or in IO.

\see \ :c:func:`cl_page_disown`\ 
\see cl_page_operations::\ :c:func:`cpo_own`\ 
\see \ :c:func:`cl_page_own_try`\ 
\see cl_page_own

.. _`cl_page_own`:

cl_page_own
===========

.. c:function:: int cl_page_own(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_own.description`:

Description
-----------

\see \ :c:func:`cl_page_own0`\ 

.. _`cl_page_own_try`:

cl_page_own_try
===============

.. c:function:: int cl_page_own_try(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_own_try.description`:

Description
-----------

\see \ :c:func:`cl_page_own0`\ 

.. _`cl_page_assume`:

cl_page_assume
==============

.. c:function:: void cl_page_assume(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

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

\see cl_page_operations::\ :c:func:`cpo_assume`\ 

.. _`cl_page_unassume`:

cl_page_unassume
================

.. c:function:: void cl_page_unassume(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_unassume.description`:

Description
-----------

Moves page into cl_page_state::CPS_CACHED without releasing a lock on the
underlying VM page (as VM is supposed to do this itself).

\pre   cl_page_is_owned(pg, io)
\post !cl_page_is_owned(pg, io)

\see \ :c:func:`cl_page_assume`\ 

.. _`cl_page_disown`:

cl_page_disown
==============

.. c:function:: void cl_page_disown(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_disown.description`:

Description
-----------

Moves page into cl_page_state::CPS_CACHED.

\pre   cl_page_is_owned(pg, io)
\post !cl_page_is_owned(pg, io)

\see \ :c:func:`cl_page_own`\ 
\see cl_page_operations::\ :c:func:`cpo_disown`\ 

.. _`cl_page_discard`:

cl_page_discard
===============

.. c:function:: void cl_page_discard(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    truncate.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_discard.description`:

Description
-----------

Calls cl_page_operations::\ :c:func:`cpo_discard`\  top-to-bottom.

\pre cl_page_is_owned(pg, io)

\see cl_page_operations::\ :c:func:`cpo_discard`\ 

.. _`cl_page_delete0`:

cl_page_delete0
===============

.. c:function:: void cl_page_delete0(const struct lu_env *env, struct cl_page *pg)

    pages, e.g,. in a error handling \ :c:func:`cl_page_find`\ ->\ :c:func:`cl_page_delete0`\  path. Doesn't check page invariant.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_delete`:

cl_page_delete
==============

.. c:function:: void cl_page_delete(const struct lu_env *env, struct cl_page *pg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. _`cl_page_delete.description`:

Description
-----------

Notifies all layers about page destruction by calling
cl_page_operations::\ :c:func:`cpo_delete`\  method top-to-bottom.

Moves page into cl_page_state::CPS_FREEING state (this is the only place
where transition to this state happens).

Eliminates all venues through which new references to the page can be

.. _`cl_page_delete.obtained`:

obtained
--------


- removes page from the radix trees,

- breaks linkage from VM page to cl_page.

Once page reaches cl_page_state::CPS_FREEING, all remaining references will
drain after some time, at which point page will be recycled.

\pre  VM page is locked
\post pg->cp_state == CPS_FREEING

\see cl_page_operations::\ :c:func:`cpo_delete`\ 

.. _`cl_page_export`:

cl_page_export
==============

.. c:function:: void cl_page_export(const struct lu_env *env, struct cl_page *pg, int uptodate)

    to-date.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

    :param int uptodate:
        *undescribed*

.. _`cl_page_export.description`:

Description
-----------

Call cl_page_operations::\ :c:func:`cpo_export`\  through all layers top-to-bottom. The
layer responsible for VM interaction has to mark/clear page as up-to-date
by the \a uptodate argument.

\see cl_page_operations::\ :c:func:`cpo_export`\ 

.. _`cl_page_is_vmlocked`:

cl_page_is_vmlocked
===================

.. c:function:: int cl_page_is_vmlocked(const struct lu_env *env, const struct cl_page *pg)

    thread.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_page \*pg:
        *undescribed*

.. _`cl_page_prep`:

cl_page_prep
============

.. c:function:: int cl_page_prep(const struct lu_env *env, struct cl_io *io, struct cl_page *pg, enum cl_req_type crt)

    :\ :c:func:`cpo_prep`\  is called top-to-bottom. Every layer either agrees to submit this page (by returning 0), or requests to omit this page (by returning -EALREADY). Layer handling interactions with the VM also has to inform VM that page is under transfer now.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

.. _`cl_page_completion`:

cl_page_completion
==================

.. c:function:: void cl_page_completion(const struct lu_env *env, struct cl_page *pg, enum cl_req_type crt, int ioret)

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

\pre  pg->cp_state == CPS_PAGEIN \|\| pg->cp_state == CPS_PAGEOUT
\post pg->cp_state == CPS_CACHED

\see cl_page_operations::\ :c:func:`cpo_completion`\ 

.. _`cl_page_make_ready`:

cl_page_make_ready
==================

.. c:function:: int cl_page_make_ready(const struct lu_env *env, struct cl_page *pg, enum cl_req_type crt)

    the cache and to make it a part of a transfer.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

.. _`cl_page_make_ready.description`:

Description
-----------

\pre  pg->cp_state == CPS_CACHED
\post pg->cp_state == CPS_PAGEIN \|\| pg->cp_state == CPS_PAGEOUT

\see cl_page_operations::\ :c:func:`cpo_make_ready`\ 

.. _`cl_page_flush`:

cl_page_flush
=============

.. c:function:: int cl_page_flush(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

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

\see cl_page_operations::\ :c:func:`cpo_flush`\ 

.. _`cl_page_is_under_lock`:

cl_page_is_under_lock
=====================

.. c:function:: int cl_page_is_under_lock(const struct lu_env *env, struct cl_io *io, struct cl_page *page, pgoff_t *max_index)

    mode.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

    :param pgoff_t \*max_index:
        *undescribed*

.. _`cl_page_is_under_lock.description`:

Description
-----------

\return the same as in cl_page_operations::\ :c:func:`cpo_is_under_lock`\  method.
\see cl_page_operations::\ :c:func:`cpo_is_under_lock`\ 

.. _`cl_page_clip`:

cl_page_clip
============

.. c:function:: void cl_page_clip(const struct lu_env *env, struct cl_page *pg, int from, int to)

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

\see cl_page_operations::\ :c:func:`cpo_clip`\ 

.. _`cl_page_header_print`:

cl_page_header_print
====================

.. c:function:: void cl_page_header_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_page *pg)

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

.. c:function:: void cl_page_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_page *pg)

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

.. c:function:: int cl_page_cancel(const struct lu_env *env, struct cl_page *page)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`cl_offset`:

cl_offset
=========

.. c:function:: loff_t cl_offset(const struct cl_object *obj, pgoff_t idx)

    :param const struct cl_object \*obj:
        *undescribed*

    :param pgoff_t idx:
        *undescribed*

.. _`cl_index`:

cl_index
========

.. c:function:: pgoff_t cl_index(const struct cl_object *obj, loff_t offset)

    :param const struct cl_object \*obj:
        *undescribed*

    :param loff_t offset:
        *undescribed*

.. _`cl_page_slice_add`:

cl_page_slice_add
=================

.. c:function:: void cl_page_slice_add(struct cl_page *page, struct cl_page_slice *slice, struct cl_object *obj, pgoff_t index, const struct cl_page_operations *ops)

    :param struct cl_page \*page:
        *undescribed*

    :param struct cl_page_slice \*slice:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

    :param const struct cl_page_operations \*ops:
        *undescribed*

.. _`cl_page_slice_add.description`:

Description
-----------

This is called by cl_object_operations::\ :c:func:`coo_page_init`\  methods to add a
per-layer state to the page. New state is added at the end of
cl_page::cp_layers list, that is, it is at the bottom of the stack.

\see \ :c:func:`cl_lock_slice_add`\ , \ :c:func:`cl_req_slice_add`\ , \ :c:func:`cl_io_slice_add`\ 

.. This file was automatic generated / don't edit.

