.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/tcm.h

.. _`tcm_deinit`:

tcm_deinit
==========

.. c:function:: void tcm_deinit(struct tcm *tcm)

    :param tcm:
        *undescribed*
    :type tcm: struct tcm \*

.. _`tcm_deinit.description`:

Description
-----------

\ ``param``\  tcm   Pointer to container manager.

\ ``return``\  0 on success, non-0 error value on error.  The call
should free as much memory as possible and meaningful
even on failure.  Some error codes: -ENODEV: invalid
manager.

.. _`tcm_reserve_2d`:

tcm_reserve_2d
==============

.. c:function:: s32 tcm_reserve_2d(struct tcm *tcm, u16 width, u16 height, u16 align, s16 offset, u16 slot_bytes, struct tcm_area *area)

    :param tcm:
        *undescribed*
    :type tcm: struct tcm \*

    :param width:
        *undescribed*
    :type width: u16

    :param height:
        *undescribed*
    :type height: u16

    :param align:
        *undescribed*
    :type align: u16

    :param offset:
        *undescribed*
    :type offset: s16

    :param slot_bytes:
        *undescribed*
    :type slot_bytes: u16

    :param area:
        *undescribed*
    :type area: struct tcm_area \*

.. _`tcm_reserve_2d.description`:

Description
-----------

\ ``param``\  tcm           Pointer to container manager.
\ ``param``\  height        Height(in pages) of area to be reserved.
\ ``param``\  width         Width(in pages) of area to be reserved.
\ ``param``\  align         Alignment requirement for top-left corner of area. Not
all values may be supported by the container manager,
but it must support 0 (1), 32 and 64.
0 value is equivalent to 1.
\ ``param``\  offset        Offset requirement, in bytes.  This is the offset
from a 4KiB aligned virtual address.
\ ``param``\  slot_bytes    Width of slot in bytes
\ ``param``\  area          Pointer to where the reserved area should be stored.

\ ``return``\  0 on success.  Non-0 error code on failure.  Also,
the tcm field of the area will be set to NULL on
failure.  Some error codes: -ENODEV: invalid manager,
-EINVAL: invalid area, -ENOMEM: not enough space for
allocation.

.. _`tcm_reserve_1d`:

tcm_reserve_1d
==============

.. c:function:: s32 tcm_reserve_1d(struct tcm *tcm, u32 slots, struct tcm_area *area)

    :param tcm:
        *undescribed*
    :type tcm: struct tcm \*

    :param slots:
        *undescribed*
    :type slots: u32

    :param area:
        *undescribed*
    :type area: struct tcm_area \*

.. _`tcm_reserve_1d.description`:

Description
-----------

\ ``param``\  tcm           Pointer to container manager.
\ ``param``\  slots         Number of (contiguous) slots to reserve.
\ ``param``\  area          Pointer to where the reserved area should be stored.

\ ``return``\  0 on success.  Non-0 error code on failure.  Also,
the tcm field of the area will be set to NULL on
failure.  Some error codes: -ENODEV: invalid manager,
-EINVAL: invalid area, -ENOMEM: not enough space for
allocation.

.. _`tcm_free`:

tcm_free
========

.. c:function:: s32 tcm_free(struct tcm_area *area)

    :param area:
        *undescribed*
    :type area: struct tcm_area \*

.. _`tcm_free.description`:

Description
-----------

\ ``param``\  area  Pointer to area reserved by a prior call to
tcm_reserve_1d or tcm_reserve_2d call, whether
it was successful or not. (Note: all fields of
the structure must match.)

\ ``return``\  0 on success.  Non-0 error code on failure.  Also, the tcm
field of the area is set to NULL on success to avoid subsequent
freeing.  This call will succeed even if supplying
the area from a failed reserved call.

.. _`tcm_slice`:

tcm_slice
=========

.. c:function:: void tcm_slice(struct tcm_area *parent, struct tcm_area *slice)

    it in the 'slice' parameter.  The 'parent' parameter will get modified to contain the remaining portion of the area.  If the whole parent area can fit in a 2D slice, its tcm pointer is set to NULL to mark that it is no longer a valid area.

    :param parent:
        *undescribed*
    :type parent: struct tcm_area \*

    :param slice:
        *undescribed*
    :type slice: struct tcm_area \*

.. _`tcm_slice.description`:

Description
-----------

\ ``param``\  parent        Pointer to a VALID parent area that will get modified
\ ``param``\  slice         Pointer to the slice area that will get modified

.. _`tcm_for_each_slice`:

tcm_for_each_slice
==================

.. c:function::  tcm_for_each_slice( var,  area,  safe)

    syntactically as a for(;;) statement.

    :param var:
        *undescribed*
    :type var: 

    :param area:
        *undescribed*
    :type area: 

    :param safe:
        *undescribed*
    :type safe: 

.. _`tcm_for_each_slice.description`:

Description
-----------

\ ``param``\  var           Name of a local variable of type 'struct
tcm_area \*' that will get modified to
contain each slice.
\ ``param``\  area          Pointer to the VALID parent area. This
structure will not get modified
throughout the loop.

.. This file was automatic generated / don't edit.

