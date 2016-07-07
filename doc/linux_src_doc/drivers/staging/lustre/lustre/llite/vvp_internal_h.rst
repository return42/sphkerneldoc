.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/vvp_internal.h

.. _`lov_lsm_get`:

lov_lsm_get
===========

.. c:function:: struct lov_stripe_md *lov_lsm_get(struct cl_object *clobj)

    layering because lov_stripe_md is supposed to be a private data in lov.

    :param struct cl_object \*clobj:
        *undescribed*

.. _`lov_lsm_get.description`:

Description
-----------

NB: If you find you have to use these interfaces for your new code, please
think about it again. These interfaces may be removed in the future for
better layering.

.. This file was automatic generated / don't edit.

