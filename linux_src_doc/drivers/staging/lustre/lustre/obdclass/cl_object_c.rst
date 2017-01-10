.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/cl_object.c

.. _`cl_object_header_init`:

cl_object_header_init
=====================

.. c:function:: int cl_object_header_init(struct cl_object_header *h)

    :param struct cl_object_header \*h:
        *undescribed*

.. _`cl_object_find`:

cl_object_find
==============

.. c:function:: struct cl_object *cl_object_find(const struct lu_env *env, struct cl_device *cd, const struct lu_fid *fid, const struct cl_object_conf *c)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_device \*cd:
        *undescribed*

    :param const struct lu_fid \*fid:
        *undescribed*

    :param const struct cl_object_conf \*c:
        *undescribed*

.. _`cl_object_find.description`:

Description
-----------

Returns either cached or newly created object. Additional reference on the
returned object is acquired.

\see \ :c:func:`lu_object_find`\ , \ :c:func:`cl_page_find`\ , \ :c:func:`cl_lock_find`\ 

.. _`cl_object_put`:

cl_object_put
=============

.. c:function:: void cl_object_put(const struct lu_env *env, struct cl_object *o)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_put.description`:

Description
-----------

When last reference is released object is returned to the cache, unless
lu_object_header_flags::LU_OBJECT_HEARD_BANSHEE bit is set in its header.

\see \ :c:func:`cl_page_put`\ , \ :c:func:`cl_lock_put`\ .

.. _`cl_object_get`:

cl_object_get
=============

.. c:function:: void cl_object_get(struct cl_object *o)

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_get.description`:

Description
-----------

This can only be used to acquire \_additional\_ reference, i.e., caller
already has to possess at least one reference to \a o before calling this.

\see \ :c:func:`cl_page_get`\ , \ :c:func:`cl_lock_get`\ .

.. _`cl_object_top`:

cl_object_top
=============

.. c:function:: struct cl_object *cl_object_top(struct cl_object *o)

    object for a given \a o.

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_top.description`:

Description
-----------

\see \ :c:func:`cl_io_top`\ 

.. _`cl_object_attr_guard`:

cl_object_attr_guard
====================

.. c:function:: spinlock_t *cl_object_attr_guard(struct cl_object *o)

    attributes for the given object \a o.

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_attr_guard.description`:

Description
-----------

Data-attributes are protected by the cl_object_header::coh_attr_guard
spin-lock in the top-object.

\see cl_attr, \ :c:func:`cl_object_attr_lock`\ , cl_object_operations::coo_attr_get().

.. _`cl_object_attr_lock`:

cl_object_attr_lock
===================

.. c:function:: void cl_object_attr_lock(struct cl_object *o)

    attributes.

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_attr_lock.description`:

Description
-----------

Prevents data-attributes from changing, until lock is released by
\ :c:func:`cl_object_attr_unlock`\ . This has to be called before calls to
\ :c:func:`cl_object_attr_get`\ , \ :c:func:`cl_object_attr_update`\ .

.. _`cl_object_attr_unlock`:

cl_object_attr_unlock
=====================

.. c:function:: void cl_object_attr_unlock(struct cl_object *o)

    attributes lock, acquired by \ :c:func:`cl_object_attr_lock`\ .

    :param struct cl_object \*o:
        *undescribed*

.. _`cl_object_attr_get`:

cl_object_attr_get
==================

.. c:function:: int cl_object_attr_get(const struct lu_env *env, struct cl_object *obj, struct cl_attr *attr)

    attributes of an object \a obj.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_attr \*attr:
        *undescribed*

.. _`cl_object_attr_get.description`:

Description
-----------

Every layer is asked (by calling cl_object_operations::coo_attr_get())
top-to-bottom to fill in parts of \a attr that this layer is responsible
for.

.. _`cl_object_attr_update`:

cl_object_attr_update
=====================

.. c:function:: int cl_object_attr_update(const struct lu_env *env, struct cl_object *obj, const struct cl_attr *attr, unsigned int v)

    attributes of an object \a obj.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param const struct cl_attr \*attr:
        *undescribed*

    :param unsigned int v:
        *undescribed*

.. _`cl_object_attr_update.description`:

Description
-----------

Only attributes, mentioned in a validness bit-mask \a v are
updated. Calls cl_object_operations::coo_attr_update() on every layer,
bottom to top.

.. _`cl_object_glimpse`:

cl_object_glimpse
=================

.. c:function:: int cl_object_glimpse(const struct lu_env *env, struct cl_object *obj, struct ost_lvb *lvb)

    to-top) that glimpse AST was received.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct ost_lvb \*lvb:
        *undescribed*

.. _`cl_object_glimpse.description`:

Description
-----------

Layers have to fill \a lvb fields with information that will be shipped
back to glimpse issuer.

\see cl_lock_operations::clo_glimpse()

.. _`cl_conf_set`:

cl_conf_set
===========

.. c:function:: int cl_conf_set(const struct lu_env *env, struct cl_object *obj, const struct cl_object_conf *conf)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param const struct cl_object_conf \*conf:
        *undescribed*

.. _`cl_object_prune`:

cl_object_prune
===============

.. c:function:: int cl_object_prune(const struct lu_env *env, struct cl_object *obj)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_object_getstripe`:

cl_object_getstripe
===================

.. c:function:: int cl_object_getstripe(const struct lu_env *env, struct cl_object *obj, struct lov_user_md __user *uarg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct lov_user_md __user \*uarg:
        *undescribed*

.. _`cl_object_fiemap`:

cl_object_fiemap
================

.. c:function:: int cl_object_fiemap(const struct lu_env *env, struct cl_object *obj, struct ll_fiemap_info_key *key, struct fiemap *fiemap, size_t *buflen)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct ll_fiemap_info_key \*key:
        *undescribed*

    :param struct fiemap \*fiemap:
        *undescribed*

    :param size_t \*buflen:
        *undescribed*

.. _`cl_object_fiemap.description`:

Description
-----------

\param env [in]      lustre environment
\param obj [in]      file object
\param key [in]      fiemap request argument
\param fiemap [out]  fiemap extents mapping retrived
\param buflen [in]   max buffer length of \ ``fiemap``\ 

\retval 0    success
\retval < 0  error

.. _`cl_object_kill`:

cl_object_kill
==============

.. c:function:: void cl_object_kill(const struct lu_env *env, struct cl_object *obj)

    deletion. All object pages must have been deleted at this point.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_object_kill.description`:

Description
-----------

This is called by \ :c:func:`cl_inode_fini`\  and \ :c:func:`lov_object_delete`\  to destroy top-
and sub- objects respectively.

.. _`cl_site_init`:

cl_site_init
============

.. c:function:: int cl_site_init(struct cl_site *s, struct cl_device *d)

    :param struct cl_site \*s:
        *undescribed*

    :param struct cl_device \*d:
        *undescribed*

.. _`cl_site_init.description`:

Description
-----------

Perform common initialization (lu_site_init()), and initialize statistical
counters. Also perform global initializations on the first call.

.. _`cl_site_fini`:

cl_site_fini
============

.. c:function:: void cl_site_fini(struct cl_site *s)

    :param struct cl_site \*s:
        *undescribed*

.. _`cl_site_stats_print`:

cl_site_stats_print
===================

.. c:function:: int cl_site_stats_print(const struct cl_site *site, struct seq_file *m)

    ll_rd\_\*()-style functions.

    :param const struct cl_site \*site:
        *undescribed*

    :param struct seq_file \*m:
        *undescribed*

.. _`cl_env_get`:

cl_env_get
==========

.. c:function:: struct lu_env *cl_env_get(int *refcheck)

    if there already is an environment associated with the current thread, it is returned, otherwise, new environment is allocated.

    :param int \*refcheck:
        *undescribed*

.. _`cl_env_get.description`:

Description
-----------

Allocations are amortized through the global cache of environments.

\param refcheck pointer to a counter used to detect environment leaks. In
the usual case \ :c:func:`cl_env_get`\  and \ :c:func:`cl_env_put`\  are called in the same lexical
scope and pointer to the same integer is passed as \a refcheck. This is
used to detect missed \ :c:func:`cl_env_put`\ .

\see \ :c:func:`cl_env_put`\ 

.. _`cl_env_alloc`:

cl_env_alloc
============

.. c:function:: struct lu_env *cl_env_alloc(int *refcheck, __u32 tags)

    :param int \*refcheck:
        *undescribed*

    :param __u32 tags:
        *undescribed*

.. _`cl_env_alloc.description`:

Description
-----------

\see \ :c:func:`cl_env_get`\ 

.. _`cl_env_cache_purge`:

cl_env_cache_purge
==================

.. c:function:: unsigned int cl_env_cache_purge(unsigned int nr)

    (1) free some memory (not currently hooked into VM), or (2) release references to modules.

    :param unsigned int nr:
        *undescribed*

.. _`cl_env_put`:

cl_env_put
==========

.. c:function:: void cl_env_put(struct lu_env *env, int *refcheck)

    :param struct lu_env \*env:
        *undescribed*

    :param int \*refcheck:
        *undescribed*

.. _`cl_env_put.description`:

Description
-----------

Decrement \a env reference counter. When counter drops to 0, nothing in
this thread is using environment and it is returned to the allocation
cache, or freed straight away, if cache is large enough.

.. _`cl_lvb2attr`:

cl_lvb2attr
===========

.. c:function:: void cl_lvb2attr(struct cl_attr *attr, const struct ost_lvb *lvb)

    :param struct cl_attr \*attr:
        *undescribed*

    :param const struct ost_lvb \*lvb:
        *undescribed*

.. _`cl_lvb2attr.description`:

Description
-----------

\see cl_attr2lvb

.. _`cl_stack_fini`:

cl_stack_fini
=============

.. c:function:: void cl_stack_fini(const struct lu_env *env, struct cl_device *cl)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_device \*cl:
        *undescribed*

.. _`cl_global_init`:

cl_global_init
==============

.. c:function:: int cl_global_init( void)

    data. Create kmem caches, register lu_context_key's, etc.

    :param  void:
        no arguments

.. _`cl_global_init.description`:

Description
-----------

\see \ :c:func:`cl_global_fini`\ 

.. _`cl_global_fini`:

cl_global_fini
==============

.. c:function:: void cl_global_fini( void)

    data. Dual to \ :c:func:`cl_global_init`\ .

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

