.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lovsub_object.c

.. _`lovsub_req_attr_set`:

lovsub_req_attr_set
===================

.. c:function:: void lovsub_req_attr_set(const struct lu_env *env, struct cl_object *obj, struct cl_req_attr *attr)

    :coo_req_attr_set() for lovsub layer. Lov and lovsub are responsible only for struct obdo::o_stripe_idx field, which is filled there.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_req_attr \*attr:
        *undescribed*

.. This file was automatic generated / don't edit.

