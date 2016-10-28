.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_obd.c

.. _`fiemap_calc_fm_end_offset`:

fiemap_calc_fm_end_offset
=========================

.. c:function:: u64 fiemap_calc_fm_end_offset(struct ll_user_fiemap *fiemap, struct lov_stripe_md *lsm, u64 fm_start, u64 fm_end, int *start_stripe)

    zero fe_logical indicates that this is a continuation FIEMAP call. The local end offset and the device are sent in the first fm_extent. This function calculates the stripe number from the index. This function returns a stripe_no on which mapping is to be restarted.

    :param struct ll_user_fiemap \*fiemap:
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

\param fiemap fiemap request header
\param lsm striping information for the file
\param fm_start logical start of mapping
\param fm_end logical end of mapping
\param start_stripe starting stripe will be returned in this

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

\param lsm striping information for the file
\param fm_start logical start of mapping
\param fm_end logical end of mapping
\param start_stripe starting stripe of the mapping
\param stripe_count the number of stripes across which to map is returned

\retval last_stripe return the last stripe of the mapping

.. _`fiemap_prepare_and_copy_exts`:

fiemap_prepare_and_copy_exts
============================

.. c:function:: void fiemap_prepare_and_copy_exts(struct ll_user_fiemap *fiemap, struct ll_fiemap_extent *lcl_fm_ext, int ost_index, unsigned int ext_count, int current_extent)

    :param struct ll_user_fiemap \*fiemap:
        *undescribed*

    :param struct ll_fiemap_extent \*lcl_fm_ext:
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

\param fiemap fiemap request header
\param lcl_fm_ext array of local fiemap extents to be copied
\param ost_index OST index to be written into the fm_device field for each
\param ext_count number of extents to be copied
\param current_extent where to start copying in main extent array

.. _`lov_fiemap`:

lov_fiemap
==========

.. c:function:: int lov_fiemap(struct lov_obd *lov, __u32 keylen, void *key, __u32 *vallen, void *val, struct lov_stripe_md *lsm)

    This also handles the restarting of FIEMAP calls in case mapping overflows the available number of extents in single call.

    :param struct lov_obd \*lov:
        *undescribed*

    :param __u32 keylen:
        *undescribed*

    :param void \*key:
        *undescribed*

    :param __u32 \*vallen:
        *undescribed*

    :param void \*val:
        *undescribed*

    :param struct lov_stripe_md \*lsm:
        *undescribed*

.. This file was automatic generated / don't edit.

