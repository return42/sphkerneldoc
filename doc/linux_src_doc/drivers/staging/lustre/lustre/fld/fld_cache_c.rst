.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/fld/fld_cache.c

.. _`fld_cache_init`:

fld_cache_init
==============

.. c:function:: struct fld_cache *fld_cache_init(const char *name, int cache_size, int cache_threshold)

    :param const char \*name:
        *undescribed*

    :param int cache_size:
        *undescribed*

    :param int cache_threshold:
        *undescribed*

.. _`fld_cache_fini`:

fld_cache_fini
==============

.. c:function:: void fld_cache_fini(struct fld_cache *cache)

    :param struct fld_cache \*cache:
        *undescribed*

.. _`fld_cache_entry_delete`:

fld_cache_entry_delete
======================

.. c:function:: void fld_cache_entry_delete(struct fld_cache *cache, struct fld_cache_entry *node)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct fld_cache_entry \*node:
        *undescribed*

.. _`fld_fix_new_list`:

fld_fix_new_list
================

.. c:function:: void fld_fix_new_list(struct fld_cache *cache)

    :param struct fld_cache \*cache:
        *undescribed*

.. _`fld_cache_entry_add`:

fld_cache_entry_add
===================

.. c:function:: void fld_cache_entry_add(struct fld_cache *cache, struct fld_cache_entry *f_new, struct list_head *pos)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct fld_cache_entry \*f_new:
        *undescribed*

    :param struct list_head \*pos:
        *undescribed*

.. _`fld_cache_shrink`:

fld_cache_shrink
================

.. c:function:: int fld_cache_shrink(struct fld_cache *cache)

    do it. Remove one entry in list and so on until cache is shrunk enough.

    :param struct fld_cache \*cache:
        *undescribed*

.. _`fld_cache_flush`:

fld_cache_flush
===============

.. c:function:: void fld_cache_flush(struct fld_cache *cache)

    :param struct fld_cache \*cache:
        *undescribed*

.. _`fld_cache_punch_hole`:

fld_cache_punch_hole
====================

.. c:function:: void fld_cache_punch_hole(struct fld_cache *cache, struct fld_cache_entry *f_curr, struct fld_cache_entry *f_new)

    entry accordingly.

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct fld_cache_entry \*f_curr:
        *undescribed*

    :param struct fld_cache_entry \*f_new:
        *undescribed*

.. _`fld_cache_overlap_handle`:

fld_cache_overlap_handle
========================

.. c:function:: void fld_cache_overlap_handle(struct fld_cache *cache, struct fld_cache_entry *f_curr, struct fld_cache_entry *f_new)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct fld_cache_entry \*f_curr:
        *undescribed*

    :param struct fld_cache_entry \*f_new:
        *undescribed*

.. _`fld_cache_insert_nolock`:

fld_cache_insert_nolock
=======================

.. c:function:: int fld_cache_insert_nolock(struct fld_cache *cache, struct fld_cache_entry *f_new)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct fld_cache_entry \*f_new:
        *undescribed*

.. _`fld_cache_insert_nolock.description`:

Description
-----------

This function handles all cases of merging and breaking up of
ranges.

.. _`fld_cache_entry_lookup_nolock`:

fld_cache_entry_lookup_nolock
=============================

.. c:function:: struct fld_cache_entry *fld_cache_entry_lookup_nolock(struct fld_cache *cache, struct lu_seq_range *range)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`fld_cache_entry_lookup`:

fld_cache_entry_lookup
======================

.. c:function:: struct fld_cache_entry *fld_cache_entry_lookup(struct fld_cache *cache, struct lu_seq_range *range)

    :param struct fld_cache \*cache:
        *undescribed*

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`fld_cache_lookup`:

fld_cache_lookup
================

.. c:function:: int fld_cache_lookup(struct fld_cache *cache, const u64 seq, struct lu_seq_range *range)

    :param struct fld_cache \*cache:
        *undescribed*

    :param const u64 seq:
        *undescribed*

    :param struct lu_seq_range \*range:
        *undescribed*

.. This file was automatic generated / don't edit.

