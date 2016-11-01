.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_object.c

.. _`lov_attr_get_empty`:

lov_attr_get_empty
==================

.. c:function:: int lov_attr_get_empty(const struct lu_env *env, struct cl_object *obj, struct cl_attr *attr)

    :coo_attr_get() method for an object without stripes (LLT_EMPTY layout type).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_attr \*attr:
        *undescribed*

.. _`lov_attr_get_empty.description`:

Description
-----------

The only attributes this layer is authoritative in this case is
cl_attr::cat_blocks---it's 0.

.. _`lov_2dispatch_nolock`:

LOV_2DISPATCH_NOLOCK
====================

.. c:function::  LOV_2DISPATCH_NOLOCK( obj,  op,  ...)

    dispatch based on the layout type of an object.

    :param  obj:
        *undescribed*

    :param  op:
        *undescribed*

    :param ... :
        variable arguments

.. _`lov_type`:

lov_type
========

.. c:function:: enum lov_layout_type lov_type(struct lov_stripe_md *lsm)

    :param struct lov_stripe_md \*lsm:
        *undescribed*

.. _`lov_2dispatch`:

LOV_2DISPATCH
=============

.. c:function::  LOV_2DISPATCH( obj,  op,  ...)

    dispatch based on the layout type of an object.

    :param  obj:
        *undescribed*

    :param  op:
        *undescribed*

    :param ... :
        variable arguments

.. _`lov_io_init`:

lov_io_init
===========

.. c:function:: int lov_io_init(const struct lu_env *env, struct cl_object *obj, struct cl_io *io)

    :clo_io_init() method for lov layer. Dispatches to the appropriate layout io initialization method.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

.. _`lov_attr_get`:

lov_attr_get
============

.. c:function:: int lov_attr_get(const struct lu_env *env, struct cl_object *obj, struct cl_attr *attr)

    :clo_attr_get() method for lov layer. For raid0 layout this collects and merges attributes of all sub-objects.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_attr \*attr:
        *undescribed*

.. This file was automatic generated / don't edit.

