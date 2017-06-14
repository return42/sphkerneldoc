.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_validate.c

.. _`command-list-validator-for-vc4.`:

Command list validator for VC4.
===============================

Since the VC4 has no IOMMU between it and system memory, a user
with access to execute command lists could escalate privilege by
overwriting system memory (drawing to it as a framebuffer) or
reading system memory it shouldn't (reading it as a vertex buffer
or index buffer)

We validate binner command lists to ensure that all accesses are
within the bounds of the GEM objects referenced by the submitted
job.  It explicitly whitelists packets, and looks at the offsets in
any address fields to make sure they're contained within the BOs
they reference.

Note that because CL validation is already reading the
user-submitted CL and writing the validated copy out to the memory
that the GPU will actually read, this is also where GEM relocation
processing (turning BO references into actual addresses for the GPU
to use) happens.

.. _`size_is_lt`:

size_is_lt
==========

.. c:function:: bool size_is_lt(uint32_t width, uint32_t height, int cpp)

    Returns whether a miplevel of the given size will use the lineartile (LT) tiling layout rather than the normal T tiling layout.

    :param uint32_t width:
        Width in pixels of the miplevel

    :param uint32_t height:
        Height in pixels of the miplevel

    :param int cpp:
        Bytes per pixel of the pixel format

.. This file was automatic generated / don't edit.

