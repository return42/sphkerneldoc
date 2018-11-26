.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/opa_addr.h

.. _`opa_mcast_nr`:

OPA_MCAST_NR
============

.. c:function::  OPA_MCAST_NR()

    4 bits of multicast range and 1 bit for collective range

.. _`opa_mcast_nr.example`:

Example
-------

.. code-block:: c

    For 24 bit LID space,


.. _`opa_mcast_nr.multicast-range`:

Multicast range
---------------

0xF00000 to 0xF7FFFF

.. _`opa_mcast_nr.collective-range`:

Collective range
----------------

0xF80000 to 0xFFFFFE

.. _`ib_is_opa_gid`:

ib_is_opa_gid
=============

.. c:function:: bool ib_is_opa_gid(const union ib_gid *gid)

    Returns true if the top 24 bits of the gid contains the OPA_STL_OUI identifier. This identifies that the provided gid is a special purpose GID meant to carry extended LID information.

    :param gid:
        The Global identifier
    :type gid: const union ib_gid \*

.. _`opa_get_lid_from_gid`:

opa_get_lid_from_gid
====================

.. c:function:: u32 opa_get_lid_from_gid(const union ib_gid *gid)

    Returns the last 32 bits of the gid. OPA devices use one of the gids in the gid table to also store the lid.

    :param gid:
        The Global identifier
    :type gid: const union ib_gid \*

.. _`opa_is_extended_lid`:

opa_is_extended_lid
===================

.. c:function:: bool opa_is_extended_lid(__be32 dlid, __be32 slid)

    Returns true if dlid or slid are extended.

    :param dlid:
        The DLID
    :type dlid: __be32

    :param slid:
        The SLID
    :type slid: __be32

.. This file was automatic generated / don't edit.

