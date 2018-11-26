.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vkms/vkms_crc.c

.. _`compute_crc`:

compute_crc
===========

.. c:function:: uint32_t compute_crc(void *vaddr_out, struct vkms_crc_data *crc_out)

    Compute CRC value on output frame

    :param vaddr_out:
        address to final framebuffer
    :type vaddr_out: void \*

    :param crc_out:
        framebuffer's metadata
    :type crc_out: struct vkms_crc_data \*

.. _`compute_crc.description`:

Description
-----------

returns CRC value computed using crc32 on the visible portion of
the final framebuffer at vaddr_out

.. _`blend`:

blend
=====

.. c:function:: void blend(void *vaddr_dst, void *vaddr_src, struct vkms_crc_data *crc_dst, struct vkms_crc_data *crc_src)

    belnd value at vaddr_src with value at vaddr_dst

    :param vaddr_dst:
        destination address
    :type vaddr_dst: void \*

    :param vaddr_src:
        source address
    :type vaddr_src: void \*

    :param crc_dst:
        destination framebuffer's metadata
    :type crc_dst: struct vkms_crc_data \*

    :param crc_src:
        source framebuffer's metadata
    :type crc_src: struct vkms_crc_data \*

.. _`blend.description`:

Description
-----------

Blend value at vaddr_src with value at vaddr_dst.
Currently, this function write value at vaddr_src on value
at vaddr_dst using buffer's metadata to locate the new values
from vaddr_src and their distenation at vaddr_dst.

.. _`blend.todo`:

Todo
----

Use the alpha value to blend vaddr_src with vaddr_dst
instead of overwriting it.

.. _`vkms_crc_work_handle`:

vkms_crc_work_handle
====================

.. c:function:: void vkms_crc_work_handle(struct work_struct *work)

    ordered work_struct to compute CRC

    :param work:
        work_struct
    :type work: struct work_struct \*

.. _`vkms_crc_work_handle.description`:

Description
-----------

Work handler for computing CRCs. work_struct scheduled in
an ordered workqueue that's periodically scheduled to run by
\_vblank_handle() and flushed at \ :c:func:`vkms_atomic_crtc_destroy_state`\ .

.. This file was automatic generated / don't edit.

