.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/vvp_req.c

.. _`vvp_req_attr_set`:

vvp_req_attr_set
================

.. c:function:: void vvp_req_attr_set(const struct lu_env *env, const struct cl_req_slice *slice, const struct cl_object *obj, struct cl_req_attr *attr, u64 flags)

    :cro_attr_set() for VVP layer. VVP is responsible for

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_req_slice \*slice:
        *undescribed*

    :param const struct cl_object \*obj:
        *undescribed*

    :param struct cl_req_attr \*attr:
        *undescribed*

    :param u64 flags:
        *undescribed*

.. _`vvp_req_attr_set.description`:

Description
-----------

- o_[mac]time

- o_mode

- o_parent_seq

- o_[ug]id

- o_parent_oid

- o_parent_ver

- o_ioepoch,

.. This file was automatic generated / don't edit.

