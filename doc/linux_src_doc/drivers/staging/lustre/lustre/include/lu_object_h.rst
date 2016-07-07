.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lu_object.h

.. _`int`:

int
===

.. c:function:: typedef int(*lu_printer_t)

    :\ :c:func:`loo_object_print`\  method.

    :param \*lu_printer_t:
        *undescribed*

.. _`int.description`:

Description
-----------

Printer function is needed to provide some flexibility in (semi-)debugging

.. _`int.output`:

output
------

possible implementations: printk, CDEBUG, sysfs/seq_file

.. _`lu_device_type_init`:

lu_device_type_init
===================

.. c:function:: int lu_device_type_init(struct lu_device_type *ldt)

    :param struct lu_device_type \*ldt:
        *undescribed*

.. _`lu_object_get`:

lu_object_get
=============

.. c:function:: void lu_object_get(struct lu_object *o)

    attain additional reference. To acquire initial reference use \ :c:func:`lu_object_find`\ .

    :param struct lu_object \*o:
        *undescribed*

.. _`lu_object_is_dying`:

lu_object_is_dying
==================

.. c:function:: int lu_object_is_dying(const struct lu_object_header *h)

    released.

    :param const struct lu_object_header \*h:
        *undescribed*

.. _`lu_object_top`:

lu_object_top
=============

.. c:function:: struct lu_object *lu_object_top(struct lu_object_header *h)

    object of given compound object

    :param struct lu_object_header \*h:
        *undescribed*

.. _`lu_object_next`:

lu_object_next
==============

.. c:function:: struct lu_object *lu_object_next(const struct lu_object *o)

    object in the layering

    :param const struct lu_object \*o:
        *undescribed*

.. _`lu_object_fid`:

lu_object_fid
=============

.. c:function:: const struct lu_fid *lu_object_fid(const struct lu_object *o)

    :param const struct lu_object \*o:
        *undescribed*

.. _`lu_object_ops`:

lu_object_ops
=============

.. c:function:: const struct lu_device_operations *lu_object_ops(const struct lu_object *o)

    :param const struct lu_object \*o:
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

.. _`lu_object_debug`:

LU_OBJECT_DEBUG
===============

.. c:function::  LU_OBJECT_DEBUG( mask,  env,  object,  format,  ...)

    supplied message.

    :param  mask:
        *undescribed*

    :param  env:
        *undescribed*

    :param  object:
        *undescribed*

    :param  format:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_object_header`:

LU_OBJECT_HEADER
================

.. c:function::  LU_OBJECT_HEADER( mask,  env,  object,  format,  ...)

    supplied message.

    :param  mask:
        *undescribed*

    :param  env:
        *undescribed*

    :param  object:
        *undescribed*

    :param  format:
        *undescribed*

    :param ... :
        variable arguments

.. _`lu_object_invariant`:

lu_object_invariant
===================

.. c:function:: int lu_object_invariant(const struct lu_object *o)

    :param const struct lu_object \*o:
        *undescribed*

.. _`lu_object_exists`:

lu_object_exists
================

.. c:function::  lu_object_exists( o)

    :param  o:
        *undescribed*

.. _`lu_object_exists.note`:

Note
----

LOHA_EXISTS will be set once some one created the object,
and it does not needs to be committed to storage.

.. _`lu_object_remote`:

lu_object_remote
================

.. c:function::  lu_object_remote( o)

    :param  o:
        *undescribed*

.. _`lu_object_attr`:

lu_object_attr
==============

.. c:function:: __u32 lu_object_attr(const struct lu_object *o)

    :param const struct lu_object \*o:
        *undescribed*

.. _`lu_site_stats_print`:

lu_site_stats_print
===================

.. c:function:: int lu_site_stats_print(const struct lu_site *s, struct seq_file *m)

    ll_rd\_\*()-style functions.

    :param const struct lu_site \*s:
        *undescribed*

    :param struct seq_file \*m:
        *undescribed*

.. _`lu_global_init`:

lu_global_init
==============

.. c:function:: int lu_global_init( void)

    time initializers, called at obdclass module initialization, not exported.

    :param  void:
        no arguments

.. _`lu_global_fini`:

lu_global_fini
==============

.. c:function:: void lu_global_fini( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

