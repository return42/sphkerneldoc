
.. _v4l2-selections-common:

Common selection definitions
============================

While the :ref:`V4L2 selection API <selection-api>` and :ref:`V4L2 subdev selection APIs <v4l2-subdev-selections>` are very similar, there's one fundamental difference between
the two. On sub-device API, the selection rectangle refers to the media bus format, and is bound to a sub-device's pad. On the V4L2 interface the selection rectangles refer to the
in-memory pixel format.

This section defines the common definitions of the selection interfaces on the two APIs.


.. _v4l2-selection-targets:

Selection targets
=================

The precise meaning of the selection targets may be dependent on which of the two interfaces they are used.


.. _v4l2-selection-targets-table:

.. table:: Selection target definitions

    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | Target name                          | id                                   | Definition                           | Valid for V4L2                       | Valid for V4L2 subdev                |
    +======================================+======================================+======================================+======================================+======================================+
    | ``V4L2_SEL_TGT_CROP``                | 0x0000                               | Crop rectangle. Defines the cropped  | Yes                                  | Yes                                  |
    |                                      |                                      | area.                                |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_CROP_DEFAULT``        | 0x0001                               | Suggested cropping rectangle that    | Yes                                  | No                                   |
    |                                      |                                      | covers the "whole picture".          |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_CROP_BOUNDS``         | 0x0002                               | Bounds of the crop rectangle. All    | Yes                                  | Yes                                  |
    |                                      |                                      | valid crop rectangles fit inside the |                                      |                                      |
    |                                      |                                      | crop bounds rectangle.               |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_NATIVE_SIZE``         | 0x0003                               | The native size of the device, e.g.  | Yes                                  | Yes                                  |
    |                                      |                                      | a sensor's pixel array. ``left`` and |                                      |                                      |
    |                                      |                                      | ``top`` fields are zero for this     |                                      |                                      |
    |                                      |                                      | target. Setting the native size will |                                      |                                      |
    |                                      |                                      | generally only make sense for memory |                                      |                                      |
    |                                      |                                      | to memory devices where the software |                                      |                                      |
    |                                      |                                      | can create a canvas of a given size  |                                      |                                      |
    |                                      |                                      | in which for example a video frame   |                                      |                                      |
    |                                      |                                      | can be composed. In that case        |                                      |                                      |
    |                                      |                                      | V4L2_SEL_TGT_NATIVE_SIZE     can be  |                                      |                                      |
    |                                      |                                      | used to configure the size of that   |                                      |                                      |
    |                                      |                                      | canvas.                              |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_COMPOSE``             | 0x0100                               | Compose rectangle. Used to configure | Yes                                  | Yes                                  |
    |                                      |                                      | scaling and composition.             |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_COMPOSE_DEFAULT``     | 0x0101                               | Suggested composition rectangle that | Yes                                  | No                                   |
    |                                      |                                      | covers the "whole picture".          |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_COMPOSE_BOUNDS``      | 0x0102                               | Bounds of the compose rectangle. All | Yes                                  | Yes                                  |
    |                                      |                                      | valid compose rectangles fit inside  |                                      |                                      |
    |                                      |                                      | the compose bounds rectangle.        |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_TGT_COMPOSE_PADDED``      | 0x0103                               | The active area and all padding      | Yes                                  | No                                   |
    |                                      |                                      | pixels that are inserted or modified |                                      |                                      |
    |                                      |                                      | by hardware.                         |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+



.. _v4l2-selection-flags:

Selection flags
===============


.. _v4l2-selection-flags-table:

.. table:: Selection flag definitions

    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | Flag name                            | id                                   | Definition                           | Valid for V4L2                       | Valid for V4L2 subdev                |
    +======================================+======================================+======================================+======================================+======================================+
    | ``V4L2_SEL_FLAG_GE``                 | (1 << 0)                             | Suggest the driver it should choose  | Yes                                  | Yes                                  |
    |                                      |                                      | greater or equal rectangle (in size) |                                      |                                      |
    |                                      |                                      | than was requested. Albeit the       |                                      |                                      |
    |                                      |                                      | driver may choose a lesser size, it  |                                      |                                      |
    |                                      |                                      | will only do so due to hardware      |                                      |                                      |
    |                                      |                                      | limitations. Without this flag (and  |                                      |                                      |
    |                                      |                                      | ``V4L2_SEL_FLAG_LE``) the behaviour  |                                      |                                      |
    |                                      |                                      | is to choose the closest possible    |                                      |                                      |
    |                                      |                                      | rectangle.                           |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_FLAG_LE``                 | (1 << 1)                             | Suggest the driver it should choose  | Yes                                  | Yes                                  |
    |                                      |                                      | lesser or equal rectangle (in size)  |                                      |                                      |
    |                                      |                                      | than was requested. Albeit the       |                                      |                                      |
    |                                      |                                      | driver may choose a greater size, it |                                      |                                      |
    |                                      |                                      | will only do so due to hardware      |                                      |                                      |
    |                                      |                                      | limitations.                         |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
    | ``V4L2_SEL_FLAG_KEEP_CONFIG``        | (1 << 2)                             | The configuration must not be        | No                                   | Yes                                  |
    |                                      |                                      | propagated to any further processing |                                      |                                      |
    |                                      |                                      | steps. If this flag is not given,    |                                      |                                      |
    |                                      |                                      | the configuration is propagated      |                                      |                                      |
    |                                      |                                      | inside the subdevice to all further  |                                      |                                      |
    |                                      |                                      | processing steps.                    |                                      |                                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+


