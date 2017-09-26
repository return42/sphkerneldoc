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

    :param ellipsis ellipsis:
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

    :param ellipsis ellipsis:
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

.. _`fiemap_calc_last_stripe`:

fiemap_calc_last_stripe
=======================

.. c:function:: int fiemap_calc_last_stripe(struct lov_stripe_md *lsm, u64 fm_start, u64 fm_end, int start_stripe, int *stripe_count)

    is greater than (stripe_size \* stripe_count) then the last_stripe will will be one just before start_stripe. Else we check if the mapping intersects each OST and find last_stripe. This function returns the last_stripe and also sets the stripe_count over which the mapping is spread

    :param struct lov_stripe_md \*lsm:
        *undescribed*

    :param u64 fm_start:
        *undescribed*

    :param u64 fm_end:
        *undescribed*

    :param int start_stripe:
        *undescribed*

    :param int \*stripe_count:
        *undescribed*

.. _`fiemap_calc_last_stripe.description`:

Description
-----------

\param lsm [in]              striping information for the file
\param fm_start [in]         logical start of mapping
\param fm_end [in]           logical end of mapping
\param start_stripe [in]     starting stripe of the mapping
\param stripe_count [out]    the number of stripes across which to map is
returned

\retval last_stripe          return the last stripe of the mapping

.. _`fiemap_prepare_and_copy_exts`:

fiemap_prepare_and_copy_exts
============================

.. c:function:: void fiemap_prepare_and_copy_exts(struct fiemap *fiemap, struct fiemap_extent *lcl_fm_ext, int ost_index, unsigned int ext_count, int current_extent)

    :param struct fiemap \*fiemap:
        *undescribed*

    :param struct fiemap_extent \*lcl_fm_ext:
        *undescribed*

    :param int ost_index:
        *undescribed*

    :param unsigned int ext_count:
        *undescribed*

    :param int current_extent:
        *undescribed*

.. _`fiemap_prepare_and_copy_exts.description`:

Description
-----------

\param fiemap [out]          fiemap to hold all extents
\param lcl_fm_ext [in]       array of fiemap extents get from OSC layer
\param ost_index [in]        OST index to be written into the fm_device
field for each extent
\param ext_count [in]        number of extents to be copied
\param current_extent [in]   where to start copying in the extent array

.. _`fiemap_calc_fm_end_offset`:

fiemap_calc_fm_end_offset
=========================

.. c:function:: u64 fiemap_calc_fm_end_offset(struct fiemap *fiemap, struct lov_stripe_md *lsm, u64 fm_start, u64 fm_end, int *start_stripe)

    zero fe_logical indicates that this is a continuation FIEMAP call. The local end offset and the device are sent in the first fm_extent. This function calculates the stripe number from the index. This function returns a stripe_no on which mapping is to be restarted.

    :param struct fiemap \*fiemap:
        *undescribed*

    :param struct lov_stripe_md \*lsm:
        *undescribed*

    :param u64 fm_start:
        *undescribed*

    :param u64 fm_end:
        *undescribed*

    :param int \*start_stripe:
        *undescribed*

.. _`fiemap_calc_fm_end_offset.description`:

Description
-----------

This function returns fm_end_offset which is the in-OST offset at which
mapping should be restarted. If fm_end_offset=0 is returned then caller
will re-calculate proper offset in next stripe.
Note that the first extent is passed to lov_get_info via the value field.

\param fiemap [in]           fiemap request header
\param lsm [in]              striping information for the file
\param fm_start [in]         logical start of mapping
\param fm_end [in]           logical end of mapping
\param start_stripe [out]    starting stripe will be returned in this

.. _`lov_object_fiemap`:

lov_object_fiemap
=================

.. c:function:: int lov_object_fiemap(const struct lu_env *env, struct cl_object *obj, struct ll_fiemap_info_key *fmkey, struct fiemap *fiemap, size_t *buflen)

    This also handles the restarting of FIEMAP calls in case mapping overflows the available number of extents in single call.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct ll_fiemap_info_key \*fmkey:
        *undescribed*

    :param struct fiemap \*fiemap:
        *undescribed*

    :param size_t \*buflen:
        *undescribed*

.. _`lov_object_fiemap.description`:

Description
-----------

\param env [in]              lustre environment
\param obj [in]              file object
\param fmkey [in]            fiemap request header and other info
\param fiemap [out]          fiemap buffer holding retrived map extents
\param buflen [in/out]       max buffer length of \ ``fiemap``\ , when iterate
each OST, it is used to limit max map needed
\retval 0    success
\retval < 0  error

.. This file was automatic generated / don't edit.

