.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/page_track.c

.. _`intel_vgpu_find_page_track`:

intel_vgpu_find_page_track
==========================

.. c:function:: struct intel_vgpu_page_track *intel_vgpu_find_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    find page track rcord of guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest page
    :type gfn: unsigned long

.. _`intel_vgpu_find_page_track.return`:

Return
------

A pointer to struct intel_vgpu_page_track if found, else NULL returned.

.. _`intel_vgpu_register_page_track`:

intel_vgpu_register_page_track
==============================

.. c:function:: int intel_vgpu_register_page_track(struct intel_vgpu *vgpu, unsigned long gfn, gvt_page_track_handler_t handler, void *priv)

    register a guest page to be tacked

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest page
    :type gfn: unsigned long

    :param handler:
        page track handler
    :type handler: gvt_page_track_handler_t

    :param priv:
        tracker private
    :type priv: void \*

.. _`intel_vgpu_register_page_track.return`:

Return
------

zero on success, negative error code if failed.

.. _`intel_vgpu_unregister_page_track`:

intel_vgpu_unregister_page_track
================================

.. c:function:: void intel_vgpu_unregister_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    unregister the tracked guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest page
    :type gfn: unsigned long

.. _`intel_vgpu_enable_page_track`:

intel_vgpu_enable_page_track
============================

.. c:function:: int intel_vgpu_enable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    set write-protection on guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest page
    :type gfn: unsigned long

.. _`intel_vgpu_enable_page_track.return`:

Return
------

zero on success, negative error code if failed.

.. _`intel_vgpu_disable_page_track`:

intel_vgpu_disable_page_track
=============================

.. c:function:: int intel_vgpu_disable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    cancel write-protection on guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest page
    :type gfn: unsigned long

.. _`intel_vgpu_disable_page_track.return`:

Return
------

zero on success, negative error code if failed.

.. _`intel_vgpu_page_track_handler`:

intel_vgpu_page_track_handler
=============================

.. c:function:: int intel_vgpu_page_track_handler(struct intel_vgpu *vgpu, u64 gpa, void *data, unsigned int bytes)

    called when write to write-protected page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gpa:
        the gpa of this write
    :type gpa: u64

    :param data:
        the writed data
    :type data: void \*

    :param bytes:
        the length of this write
    :type bytes: unsigned int

.. _`intel_vgpu_page_track_handler.return`:

Return
------

zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

