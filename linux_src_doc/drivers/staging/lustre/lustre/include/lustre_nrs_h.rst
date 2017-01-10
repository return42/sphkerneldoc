.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_nrs.h

.. _`nrs_pol_desc_compat_t`:

nrs_pol_desc_compat_t
=====================

.. c:function:: bool nrs_pol_desc_compat_t(const struct ptlrpc_service *svc, const struct ptlrpc_nrs_pol_desc *desc)

    for handling RPCs of a particular PTLRPC service.

    :param const struct ptlrpc_service \*svc:
        *undescribed*

    :param const struct ptlrpc_nrs_pol_desc \*desc:
        *undescribed*

.. _`nrs_pol_desc_compat_t.description`:

Description
-----------

XXX:This should give the same result during policy registration and
unregistration, and for all partitions of a service; so the result should not
depend on temporal service or other properties, that may influence the
result.

.. This file was automatic generated / don't edit.

