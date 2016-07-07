.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/v4l2-subdev.h

.. _`v4l2_subdev_format_whence`:

enum v4l2_subdev_format_whence
==============================

.. c:type:: enum v4l2_subdev_format_whence

    Media bus format type

.. _`v4l2_subdev_format_whence.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_subdev_format_whence {
        V4L2_SUBDEV_FORMAT_TRY,
        V4L2_SUBDEV_FORMAT_ACTIVE
    };

.. _`v4l2_subdev_format_whence.constants`:

Constants
---------

V4L2_SUBDEV_FORMAT_TRY
    try format, for negotiation only

V4L2_SUBDEV_FORMAT_ACTIVE
    active format, applied to the device

.. _`v4l2_subdev_format`:

struct v4l2_subdev_format
=========================

.. c:type:: struct v4l2_subdev_format

    Pad-level media bus format

.. _`v4l2_subdev_format.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_format {
        __u32 which;
        __u32 pad;
        struct v4l2_mbus_framefmt format;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_format.members`:

Members
-------

which
    format type (from enum v4l2_subdev_format_whence)

pad
    pad number, as reported by the media API

format
    media bus format (format code and frame size)

.. _`v4l2_subdev_crop`:

struct v4l2_subdev_crop
=======================

.. c:type:: struct v4l2_subdev_crop

    Pad-level crop settings

.. _`v4l2_subdev_crop.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_crop {
        __u32 which;
        __u32 pad;
        struct v4l2_rect rect;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_crop.members`:

Members
-------

which
    format type (from enum v4l2_subdev_format_whence)

pad
    pad number, as reported by the media API

rect
    pad crop rectangle boundaries

.. _`v4l2_subdev_mbus_code_enum`:

struct v4l2_subdev_mbus_code_enum
=================================

.. c:type:: struct v4l2_subdev_mbus_code_enum

    Media bus format enumeration

.. _`v4l2_subdev_mbus_code_enum.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_mbus_code_enum {
        __u32 pad;
        __u32 index;
        __u32 code;
        __u32 which;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_mbus_code_enum.members`:

Members
-------

pad
    pad number, as reported by the media API

index
    format index during enumeration

code
    format code (MEDIA_BUS_FMT\_ definitions)

which
    format type (from enum v4l2_subdev_format_whence)

.. _`v4l2_subdev_frame_size_enum`:

struct v4l2_subdev_frame_size_enum
==================================

.. c:type:: struct v4l2_subdev_frame_size_enum

    Media bus format enumeration

.. _`v4l2_subdev_frame_size_enum.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_frame_size_enum {
        __u32 index;
        __u32 pad;
        __u32 code;
        __u32 min_width;
        __u32 max_width;
        __u32 min_height;
        __u32 max_height;
        __u32 which;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_frame_size_enum.members`:

Members
-------

index
    format index during enumeration

pad
    pad number, as reported by the media API

code
    format code (MEDIA_BUS_FMT\_ definitions)

min_width
    *undescribed*

max_width
    *undescribed*

min_height
    *undescribed*

max_height
    *undescribed*

which
    format type (from enum v4l2_subdev_format_whence)

.. _`v4l2_subdev_frame_interval`:

struct v4l2_subdev_frame_interval
=================================

.. c:type:: struct v4l2_subdev_frame_interval

    Pad-level frame rate

.. _`v4l2_subdev_frame_interval.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_frame_interval {
        __u32 pad;
        struct v4l2_fract interval;
        __u32 reserved[9];
    }

.. _`v4l2_subdev_frame_interval.members`:

Members
-------

pad
    pad number, as reported by the media API

interval
    frame interval in seconds

.. _`v4l2_subdev_frame_interval_enum`:

struct v4l2_subdev_frame_interval_enum
======================================

.. c:type:: struct v4l2_subdev_frame_interval_enum

    Frame interval enumeration

.. _`v4l2_subdev_frame_interval_enum.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_frame_interval_enum {
        __u32 index;
        __u32 pad;
        __u32 code;
        __u32 width;
        __u32 height;
        struct v4l2_fract interval;
        __u32 which;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_frame_interval_enum.members`:

Members
-------

index
    frame interval index during enumeration

pad
    pad number, as reported by the media API

code
    format code (MEDIA_BUS_FMT\_ definitions)

width
    frame width in pixels

height
    frame height in pixels

interval
    frame interval in seconds

which
    format type (from enum v4l2_subdev_format_whence)

.. _`v4l2_subdev_selection`:

struct v4l2_subdev_selection
============================

.. c:type:: struct v4l2_subdev_selection

    selection info

.. _`v4l2_subdev_selection.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_selection {
        __u32 which;
        __u32 pad;
        __u32 target;
        __u32 flags;
        struct v4l2_rect r;
        __u32 reserved[8];
    }

.. _`v4l2_subdev_selection.members`:

Members
-------

which
    either V4L2_SUBDEV_FORMAT_ACTIVE or V4L2_SUBDEV_FORMAT_TRY

pad
    pad number, as reported by the media API

target
    Selection target, used to choose one of possible rectangles,
    defined in v4l2-common.h; V4L2_SEL_TGT\_\* .

flags
    constraint flags, defined in v4l2-common.h; V4L2_SEL_FLAG\_\*.

r
    coordinates of the selection window

reserved
    for future use, set to zero for now

.. _`v4l2_subdev_selection.description`:

Description
-----------

Hardware may use multiple helper windows to process a video stream.
The structure is used to exchange this selection areas between
an application and a driver.

.. This file was automatic generated / don't edit.

