.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/fb_decoder.c

.. _`intel_vgpu_decode_primary_plane`:

intel_vgpu_decode_primary_plane
===============================

.. c:function:: int intel_vgpu_decode_primary_plane(struct intel_vgpu *vgpu, struct intel_vgpu_primary_plane_format *plane)

    Decode primary plane

    :param struct intel_vgpu \*vgpu:
        input vgpu

    :param struct intel_vgpu_primary_plane_format \*plane:
        primary plane to save decoded info
        This function is called for decoding plane

.. _`intel_vgpu_decode_primary_plane.return`:

Return
------

0 on success, non-zero if failed.

.. _`intel_vgpu_decode_cursor_plane`:

intel_vgpu_decode_cursor_plane
==============================

.. c:function:: int intel_vgpu_decode_cursor_plane(struct intel_vgpu *vgpu, struct intel_vgpu_cursor_plane_format *plane)

    Decode sprite plane

    :param struct intel_vgpu \*vgpu:
        input vgpu

    :param struct intel_vgpu_cursor_plane_format \*plane:
        cursor plane to save decoded info
        This function is called for decoding plane

.. _`intel_vgpu_decode_cursor_plane.return`:

Return
------

0 on success, non-zero if failed.

.. _`intel_vgpu_decode_sprite_plane`:

intel_vgpu_decode_sprite_plane
==============================

.. c:function:: int intel_vgpu_decode_sprite_plane(struct intel_vgpu *vgpu, struct intel_vgpu_sprite_plane_format *plane)

    Decode sprite plane

    :param struct intel_vgpu \*vgpu:
        input vgpu

    :param struct intel_vgpu_sprite_plane_format \*plane:
        sprite plane to save decoded info
        This function is called for decoding plane

.. _`intel_vgpu_decode_sprite_plane.return`:

Return
------

0 on success, non-zero if failed.

.. This file was automatic generated / don't edit.

