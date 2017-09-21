.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/lu_object.c

.. _`lu_site_bkt_bits`:

LU_SITE_BKT_BITS
================

.. c:function::  LU_SITE_BKT_BITS()

    - consume too much memory - avoid unbalanced LRU list

.. _`lu_object_put`:

lu_object_put
=============

.. c:function:: void lu_object_put(const struct lu_env *env, struct lu_object *o)

    object to the cache, unless lu_object_is_dying(o) holds. In the latter case, free object immediately.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_unhash`:

lu_object_unhash
================

.. c:function:: void lu_object_unhash(const struct lu_env *env, struct lu_object *o)

    Currently used by client code for layout change.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_alloc`:

lu_object_alloc
===============

.. c:function:: struct lu_object *lu_object_alloc(const struct lu_env *env, struct lu_device *dev, const struct lu_fid *f, const struct lu_object_conf *conf)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*dev:
        *undescribed*

    :param const struct lu_fid \*f:
        *undescribed*

    :param const struct lu_object_conf \*conf:
        *undescribed*

.. _`lu_object_alloc.description`:

Description
-----------

This follows object creation protocol, described in the comment within
struct lu_device_operations definition.

.. _`lu_object_free`:

lu_object_free
==============

.. c:function:: void lu_object_free(const struct lu_env *env, struct lu_object *o)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_site_purge_objects`:

lu_site_purge_objects
=====================

.. c:function:: int lu_site_purge_objects(const struct lu_env *env, struct lu_site *s, int nr, bool canblock)

    if canblock is false, then don't block awaiting for another instance of \ :c:func:`lu_site_purge`\  to complete

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_site \*s:
        *undescribed*

    :param int nr:
        *undescribed*

    :param bool canblock:
        *undescribed*

.. _`lu_cdebug_printer`:

lu_cdebug_printer
=================

.. c:function:: int lu_cdebug_printer(const struct lu_env *env, void *cookie, const char *format,  ...)

    :param const struct lu_env \*env:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param const char \*format:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_object_header_print`:

lu_object_header_print
======================

.. c:function:: void lu_object_header_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct lu_object_header *hdr)

    :param const struct lu_env \*env:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param lu_printer_t printer:
        *undescribed*

    :param const struct lu_object_header \*hdr:
        *undescribed*

.. _`lu_object_print`:

lu_object_print
===============

.. c:function:: void lu_object_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct lu_object *o)

    :param const struct lu_env \*env:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param lu_printer_t printer:
        *undescribed*

    :param const struct lu_object \*o:
        *undescribed*

.. _`lu_object_find`:

lu_object_find
==============

.. c:function:: struct lu_object *lu_object_find(const struct lu_env *env, struct lu_device *dev, const struct lu_fid *f, const struct lu_object_conf *conf)

    return it. Otherwise, create new object, insert it into cache and return it. In any case, additional reference is acquired on the returned object.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*dev:
        *undescribed*

    :param const struct lu_fid \*f:
        *undescribed*

    :param const struct lu_object_conf \*conf:
        *undescribed*

.. _`lu_object_find_try`:

lu_object_find_try
==================

.. c:function:: struct lu_object *lu_object_find_try(const struct lu_env *env, struct lu_device *dev, const struct lu_fid *f, const struct lu_object_conf *conf, wait_queue_entry_t *waiter)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*dev:
        *undescribed*

    :param const struct lu_fid \*f:
        *undescribed*

    :param const struct lu_object_conf \*conf:
        *undescribed*

    :param wait_queue_entry_t \*waiter:
        *undescribed*

.. _`lu_object_find_at`:

lu_object_find_at
=================

.. c:function:: struct lu_object *lu_object_find_at(const struct lu_env *env, struct lu_device *dev, const struct lu_fid *f, const struct lu_object_conf *conf)

    \a dev rather than top level device of the site. This interface allows objects of different "stacking" to be created within the same site.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*dev:
        *undescribed*

    :param const struct lu_fid \*f:
        *undescribed*

    :param const struct lu_object_conf \*conf:
        *undescribed*

.. _`lu_object_find_slice`:

lu_object_find_slice
====================

.. c:function:: struct lu_object *lu_object_find_slice(const struct lu_env *env, struct lu_device *dev, const struct lu_fid *f, const struct lu_object_conf *conf)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*dev:
        *undescribed*

    :param const struct lu_fid \*f:
        *undescribed*

    :param const struct lu_object_conf \*conf:
        *undescribed*

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( lu_device_types)

    :param  lu_device_types:
        *undescribed*

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( lu_sites)

    :param  lu_sites:
        *undescribed*

.. _`lu_site_print`:

lu_site_print
=============

.. c:function:: void lu_site_print(const struct lu_env *env, struct lu_site *s, void *cookie, lu_printer_t printer)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_site \*s:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param lu_printer_t printer:
        *undescribed*

.. _`lu_htable_order`:

lu_htable_order
===============

.. c:function:: unsigned long lu_htable_order(struct lu_device *top)

    :param struct lu_device \*top:
        *undescribed*

.. _`lu_site_init`:

lu_site_init
============

.. c:function:: int lu_site_init(struct lu_site *s, struct lu_device *top)

    :param struct lu_site \*s:
        *undescribed*

    :param struct lu_device \*top:
        *undescribed*

.. _`lu_site_fini`:

lu_site_fini
============

.. c:function:: void lu_site_fini(struct lu_site *s)

    :param struct lu_site \*s:
        *undescribed*

.. _`lu_site_init_finish`:

lu_site_init_finish
===================

.. c:function:: int lu_site_init_finish(struct lu_site *s)

    :param struct lu_site \*s:
        *undescribed*

.. _`lu_device_get`:

lu_device_get
=============

.. c:function:: void lu_device_get(struct lu_device *d)

    :param struct lu_device \*d:
        *undescribed*

.. _`lu_device_put`:

lu_device_put
=============

.. c:function:: void lu_device_put(struct lu_device *d)

    :param struct lu_device \*d:
        *undescribed*

.. _`lu_device_init`:

lu_device_init
==============

.. c:function:: int lu_device_init(struct lu_device *d, struct lu_device_type *t)

    :param struct lu_device \*d:
        *undescribed*

    :param struct lu_device_type \*t:
        *undescribed*

.. _`lu_device_fini`:

lu_device_fini
==============

.. c:function:: void lu_device_fini(struct lu_device *d)

    :param struct lu_device \*d:
        *undescribed*

.. _`lu_object_init`:

lu_object_init
==============

.. c:function:: int lu_object_init(struct lu_object *o, struct lu_object_header *h, struct lu_device *d)

    by device \a d.

    :param struct lu_object \*o:
        *undescribed*

    :param struct lu_object_header \*h:
        *undescribed*

    :param struct lu_device \*d:
        *undescribed*

.. _`lu_object_fini`:

lu_object_fini
==============

.. c:function:: void lu_object_fini(struct lu_object *o)

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_add_top`:

lu_object_add_top
=================

.. c:function:: void lu_object_add_top(struct lu_object_header *h, struct lu_object *o)

    :param struct lu_object_header \*h:
        *undescribed*

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_add_top.description`:

Description
-----------

This is typically called by the ->ldo_object_alloc() method of top-level
device.

.. _`lu_object_add`:

lu_object_add
=============

.. c:function:: void lu_object_add(struct lu_object *before, struct lu_object *o)

    :param struct lu_object \*before:
        *undescribed*

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_add.description`:

Description
-----------

This is typically called by the ->ldo_object_alloc() method of \a
before->lo_dev.

.. _`lu_object_header_init`:

lu_object_header_init
=====================

.. c:function:: int lu_object_header_init(struct lu_object_header *h)

    :param struct lu_object_header \*h:
        *undescribed*

.. _`lu_object_header_fini`:

lu_object_header_fini
=====================

.. c:function:: void lu_object_header_fini(struct lu_object_header *h)

    :param struct lu_object_header \*h:
        *undescribed*

.. _`lu_object_locate`:

lu_object_locate
================

.. c:function:: struct lu_object *lu_object_locate(struct lu_object_header *h, const struct lu_device_type *dtype)

    \a dtype.

    :param struct lu_object_header \*h:
        *undescribed*

    :param const struct lu_device_type \*dtype:
        *undescribed*

.. _`lu_stack_fini`:

lu_stack_fini
=============

.. c:function:: void lu_stack_fini(const struct lu_env *env, struct lu_device *top)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct lu_device \*top:
        *undescribed*

.. _`lu_stack_fini.description`:

Description
-----------

Finalize device stack by purging object cache, and calling
lu_device_type_operations::ldto_device_fini() and
lu_device_type_operations::ldto_device_free() on all devices in the stack.

.. _`lu_context_key_register`:

lu_context_key_register
=======================

.. c:function:: int lu_context_key_register(struct lu_context_key *key)

    :param struct lu_context_key \*key:
        *undescribed*

.. _`lu_context_key_degister`:

lu_context_key_degister
=======================

.. c:function:: void lu_context_key_degister(struct lu_context_key *key)

    :param struct lu_context_key \*key:
        *undescribed*

.. _`lu_context_key_register_many`:

lu_context_key_register_many
============================

.. c:function:: int lu_context_key_register_many(struct lu_context_key *k,  ...)

    initialized by a call to \ :c:func:`LU_CONTEXT_KEY_INIT`\ .

    :param struct lu_context_key \*k:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_context_key_degister_many`:

lu_context_key_degister_many
============================

.. c:function:: void lu_context_key_degister_many(struct lu_context_key *k,  ...)

    register a number of keys. This is a dual to \ :c:func:`lu_context_key_register_many`\ .

    :param struct lu_context_key \*k:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_context_key_revive_many`:

lu_context_key_revive_many
==========================

.. c:function:: void lu_context_key_revive_many(struct lu_context_key *k,  ...)

    :param struct lu_context_key \*k:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_context_key_quiesce_many`:

lu_context_key_quiesce_many
===========================

.. c:function:: void lu_context_key_quiesce_many(struct lu_context_key *k,  ...)

    :param struct lu_context_key \*k:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_context_key_get`:

lu_context_key_get
==================

.. c:function:: void *lu_context_key_get(const struct lu_context *ctx, const struct lu_context_key *key)

    :param const struct lu_context \*ctx:
        *undescribed*

    :param const struct lu_context_key \*key:
        *undescribed*

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( lu_context_remembered)

    :param  lu_context_remembered:
        *undescribed*

.. _`lu_context_key_quiesce`:

lu_context_key_quiesce
======================

.. c:function:: void lu_context_key_quiesce(struct lu_context_key *key)

    values in "shared" contexts (like service threads), when a module owning the key is about to be unloaded.

    :param struct lu_context_key \*key:
        *undescribed*

.. _`lu_context_init`:

lu_context_init
===============

.. c:function:: int lu_context_init(struct lu_context *ctx, __u32 tags)

    structure. Create values for all keys.

    :param struct lu_context \*ctx:
        *undescribed*

    :param __u32 tags:
        *undescribed*

.. _`lu_context_fini`:

lu_context_fini
===============

.. c:function:: void lu_context_fini(struct lu_context *ctx)

    structure. Destroy key values.

    :param struct lu_context \*ctx:
        *undescribed*

.. _`lu_context_enter`:

lu_context_enter
================

.. c:function:: void lu_context_enter(struct lu_context *ctx)

    :param struct lu_context \*ctx:
        *undescribed*

.. _`lu_context_exit`:

lu_context_exit
===============

.. c:function:: void lu_context_exit(struct lu_context *ctx)

    :param struct lu_context \*ctx:
        *undescribed*

.. _`lu_context_refill`:

lu_context_refill
=================

.. c:function:: int lu_context_refill(struct lu_context *ctx)

    creation. key_set_version is only changed in rare cases when modules are loaded and removed.

    :param struct lu_context \*ctx:
        *undescribed*

.. _`lu_global_init`:

lu_global_init
==============

.. c:function:: int lu_global_init( void)

    :param  void:
        no arguments

.. _`lu_global_fini`:

lu_global_fini
==============

.. c:function:: void lu_global_fini( void)

    :param  void:
        no arguments

.. _`lu_site_stats_print`:

lu_site_stats_print
===================

.. c:function:: int lu_site_stats_print(const struct lu_site *s, struct seq_file *m)

    lprocfs_rd\_\*()-style functions.

    :param const struct lu_site \*s:
        *undescribed*

    :param struct seq_file \*m:
        *undescribed*

.. _`lu_kmem_init`:

lu_kmem_init
============

.. c:function:: int lu_kmem_init(struct lu_kmem_descr *caches)

    :param struct lu_kmem_descr \*caches:
        *undescribed*

.. _`lu_kmem_fini`:

lu_kmem_fini
============

.. c:function:: void lu_kmem_fini(struct lu_kmem_descr *caches)

    lu_kmem_init().

    :param struct lu_kmem_descr \*caches:
        *undescribed*

.. _`lu_buf_check_and_grow`:

lu_buf_check_and_grow
=====================

.. c:function:: int lu_buf_check_and_grow(struct lu_buf *buf, size_t len)

    preserves old data in buffer old buffer remains unchanged on error \retval 0 or -ENOMEM

    :param struct lu_buf \*buf:
        *undescribed*

    :param size_t len:
        *undescribed*

.. This file was automatic generated / don't edit.

