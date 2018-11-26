.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/uverbs_ioctl.h

.. _`uverbs_attr_get_uobjs_arr`:

uverbs_attr_get_uobjs_arr
=========================

.. c:function:: int uverbs_attr_get_uobjs_arr(const struct uverbs_attr_bundle *attrs_bundle, u16 attr_idx, struct ib_uobject ***arr)

    Provides array's properties for attribute for UVERBS_ATTR_TYPE_IDRS_ARRAY.

    :param attrs_bundle:
        *undescribed*
    :type attrs_bundle: const struct uverbs_attr_bundle \*

    :param attr_idx:
        *undescribed*
    :type attr_idx: u16

    :param arr:
        Returned pointer to array of pointers for uobjects or NULL if
        the attribute isn't provided.
    :type arr: struct ib_uobject \*\*\*

.. _`uverbs_attr_get_uobjs_arr.return`:

Return
------

The array length or 0 if no attribute was provided.

.. This file was automatic generated / don't edit.

