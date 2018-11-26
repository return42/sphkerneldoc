.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/drm_fourcc.h

.. _`overview`:

overview
========

In the DRM subsystem, framebuffer pixel formats are described using the
fourcc codes defined in `include/uapi/drm/drm_fourcc.h`. In addition to the
fourcc code, a Format Modifier may optionally be provided, in order to
further describe the buffer's format - for example tiling or compression.

Format Modifiers
----------------

Format modifiers are used in conjunction with a fourcc code, forming a
unique fourcc:modifier pair. This format:modifier pair must fully define the
format and data layout of the buffer, and should be the only way to describe
that particular buffer.

Having multiple fourcc:modifier pairs which describe the same layout should
be avoided, as such aliases run the risk of different drivers exposing
different names for the same data format, forcing userspace to understand
that they are aliases.

Format modifiers may change any property of the buffer, including the number
of planes and/or the required allocation size. Format modifiers are
vendor-namespaced, and as such the relationship between a fourcc code and a
modifier is specific to the modifer being used. For example, some modifiers
may preserve meaning - such as number of planes - from the fourcc code,
whereas others may not.

Vendors should document their modifier usage in as much detail as
possible, to ensure maximum compatibility across devices, drivers and
applications.

The authoritative list of format modifier codes is found in
`include/uapi/drm/drm_fourcc.h`

.. This file was automatic generated / don't edit.

