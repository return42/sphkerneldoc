.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/reservations.h

.. _`ocfs2_resv_discard`:

ocfs2_resv_discard
==================

.. c:function:: void ocfs2_resv_discard(struct ocfs2_reservation_map *resmap, struct ocfs2_alloc_reservation *resv)

    truncate a reservation

    :param struct ocfs2_reservation_map \*resmap:
        *undescribed*

    :param struct ocfs2_alloc_reservation \*resv:
        the reservation to truncate.

.. _`ocfs2_resv_discard.description`:

Description
-----------

After this function is called, the reservation will be empty, and
unlinked from the rbtree.

.. _`ocfs2_resmap_init`:

ocfs2_resmap_init
=================

.. c:function:: int ocfs2_resmap_init(struct ocfs2_super *osb, struct ocfs2_reservation_map *resmap)

    Initialize fields of a reservations bitmap

    :param struct ocfs2_super \*osb:
        *undescribed*

    :param struct ocfs2_reservation_map \*resmap:
        struct ocfs2_reservation_map to initialize

.. _`ocfs2_resmap_init.description`:

Description
-----------

Only possible return value other than '0' is -ENOMEM for failure to
allocation mirror bitmap.

.. _`ocfs2_resmap_restart`:

ocfs2_resmap_restart
====================

.. c:function:: void ocfs2_resmap_restart(struct ocfs2_reservation_map *resmap, unsigned int clen, char *disk_bitmap)

    "restart" a reservation bitmap

    :param struct ocfs2_reservation_map \*resmap:
        reservations bitmap

    :param unsigned int clen:
        Number of valid bits in the bitmap

    :param char \*disk_bitmap:
        the disk bitmap this resmap should refer to.

.. _`ocfs2_resmap_restart.description`:

Description
-----------

Re-initialize the parameters of a reservation bitmap. This is
useful for local alloc window slides.

This function will call ocfs2_trunc_resv against all existing
reservations. A future version will recalculate existing
reservations based on the new bitmap.

.. _`ocfs2_resmap_uninit`:

ocfs2_resmap_uninit
===================

.. c:function:: void ocfs2_resmap_uninit(struct ocfs2_reservation_map *resmap)

    uninitialize a reservation bitmap structure

    :param struct ocfs2_reservation_map \*resmap:
        the struct ocfs2_reservation_map to uninitialize

.. _`ocfs2_resmap_resv_bits`:

ocfs2_resmap_resv_bits
======================

.. c:function:: int ocfs2_resmap_resv_bits(struct ocfs2_reservation_map *resmap, struct ocfs2_alloc_reservation *resv, int *cstart, int *clen)

    Return still-valid reservation bits

    :param struct ocfs2_reservation_map \*resmap:
        reservations bitmap

    :param struct ocfs2_alloc_reservation \*resv:
        reservation to base search from

    :param int \*cstart:
        start of proposed allocation

    :param int \*clen:
        length (in clusters) of proposed allocation

.. _`ocfs2_resmap_resv_bits.description`:

Description
-----------

Using the reservation data from resv, this function will compare
resmap and resmap->m_disk_bitmap to determine what part (if any) of
the reservation window is still clear to use. If resv is empty,
this function will try to allocate a window for it.

On success, zero is returned and the valid allocation area is set in cstart
and clen.

Returns -ENOSPC if reservations are disabled.

.. _`ocfs2_resmap_claimed_bits`:

ocfs2_resmap_claimed_bits
=========================

.. c:function:: void ocfs2_resmap_claimed_bits(struct ocfs2_reservation_map *resmap, struct ocfs2_alloc_reservation *resv, u32 cstart, u32 clen)

    Tell the reservation code that bits were used.

    :param struct ocfs2_reservation_map \*resmap:
        reservations bitmap

    :param struct ocfs2_alloc_reservation \*resv:
        optional reservation to recalulate based on new bitmap

    :param u32 cstart:
        start of allocation in clusters

    :param u32 clen:
        end of allocation in clusters.

.. _`ocfs2_resmap_claimed_bits.description`:

Description
-----------

Tell the reservation code that bits were used to fulfill allocation in
resmap. The bits don't have to have been part of any existing
reservation. But we must always call this function when bits are claimed.
Internally, the reservations code will use this information to mark the
reservations bitmap. If resv is passed, it's next allocation window will be
calculated. It also expects that 'cstart' is the same as we passed back
from \ :c:func:`ocfs2_resmap_resv_bits`\ .

.. This file was automatic generated / don't edit.

