.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/opa_addr.h

.. _`ib_is_opa_gid`:

ib_is_opa_gid
=============

.. c:function:: bool ib_is_opa_gid(union ib_gid *gid)

    Returns true if the top 24 bits of the gid contains the OPA_STL_OUI identifier. This identifies that the provided gid is a special purpose GID meant to carry extended LID information.

    :param union ib_gid \*gid:
        The Global identifier

.. _`opa_get_lid_from_gid`:

opa_get_lid_from_gid
====================

.. c:function:: u32 opa_get_lid_from_gid(union ib_gid *gid)

    Returns the last 32 bits of the gid. OPA devices use one of the gids in the gid table to also store the lid.

    :param union ib_gid \*gid:
        The Global identifier

.. This file was automatic generated / don't edit.

