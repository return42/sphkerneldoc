
.. _selection-api:

Experimental API for cropping, composing and scaling
====================================================

    **Note**

    This is an :ref:`experimental <experimental>` interface and may change in the future.


Introduction
============

Some video capture devices can sample a subsection of a picture and shrink or enlarge it to an image of arbitrary size. Next, the devices can insert the image into larger one. Some
video output devices can crop part of an input image, scale it up or down and insert it at an arbitrary scan line and horizontal offset into a video signal. We call these abilities
cropping, scaling and composing.

On a video *capture* device the source is a video signal, and the cropping target determine the area actually sampled. The sink is an image stored in a memory buffer. The composing
area specifies which part of the buffer is actually written to by the hardware.

On a video *output* device the source is an image in a memory buffer, and the cropping target is a part of an image to be shown on a display. The sink is the display or the
graphics screen. The application may select the part of display where the image should be displayed. The size and position of such a window is controlled by the compose target.

Rectangles for all cropping and composing targets are defined even if the device does supports neither cropping nor composing. Their size and position will be fixed in such a case.
If the device does not support scaling then the cropping and composing rectangles have the same size.


Selection targets
=================


.. _sel-targets-capture:

.. figure::  selection-api_files/selection.*
    :alt:    selection.png
    :align:  center

    Cropping and composing targets

    Targets used by a cropping, composing and scaling process



See :ref:`v4l2-selection-targets` for more information.


Configuration
=============

Applications can use the :ref:`selection API <vidioc-g-selection>` to select an area in a video signal or a buffer, and to query for default settings and hardware limits.

Video hardware can have various cropping, composing and scaling limitations. It may only scale up or down, support only discrete scaling factors, or have different scaling
abilities in the horizontal and vertical directions. Also it may not support scaling at all. At the same time the cropping/composing rectangles may have to be aligned, and both the
source and the sink may have arbitrary upper and lower size limits. Therefore, as usual, drivers are expected to adjust the requested parameters and return the actual values
selected. An application can control the rounding behaviour using :ref:`constraint flags <v4l2-selection-flags>`.


Configuration of video capture
==============================

See figure :ref:`sel-targets-capture` for examples of the selection targets available for a video capture device. It is recommended to configure the cropping targets before to
the composing targets.

The range of coordinates of the top left corner, width and height of areas that can be sampled is given by the ``V4L2_SEL_TGT_CROP_BOUNDS`` target. It is recommended for the driver
developers to put the top/left corner at position ``(0,0)``. The rectangle's coordinates are expressed in pixels.

The top left corner, width and height of the source rectangle, that is the area actually sampled, is given by the ``V4L2_SEL_TGT_CROP`` target. It uses the same coordinate system
as ``V4L2_SEL_TGT_CROP_BOUNDS``. The active cropping area must lie completely inside the capture boundaries. The driver may further adjust the requested size and/or position
according to hardware limitations.

Each capture device has a default source rectangle, given by the ``V4L2_SEL_TGT_CROP_DEFAULT`` target. This rectangle shall over what the driver writer considers the complete
picture. Drivers shall set the active crop rectangle to the default when the driver is first loaded, but not later.

The composing targets refer to a memory buffer. The limits of composing coordinates are obtained using ``V4L2_SEL_TGT_COMPOSE_BOUNDS``. All coordinates are expressed in pixels. The
rectangle's top/left corner must be located at position ``(0,0)``. The width and height are equal to the image size set by ``VIDIOC_S_FMT``.

The part of a buffer into which the image is inserted by the hardware is controlled by the ``V4L2_SEL_TGT_COMPOSE`` target. The rectangle's coordinates are also expressed in the
same coordinate system as the bounds rectangle. The composing rectangle must lie completely inside bounds rectangle. The driver must adjust the composing rectangle to fit to the
bounding limits. Moreover, the driver can perform other adjustments according to hardware limitations. The application can control rounding behaviour using
:ref:`constraint flags <v4l2-selection-flags>`.

For capture devices the default composing rectangle is queried using ``V4L2_SEL_TGT_COMPOSE_DEFAULT``. It is usually equal to the bounding rectangle.

The part of a buffer that is modified by the hardware is given by ``V4L2_SEL_TGT_COMPOSE_PADDED``. It contains all pixels defined using ``V4L2_SEL_TGT_COMPOSE`` plus all padding
data modified by hardware during insertion process. All pixels outside this rectangle *must not* be changed by the hardware. The content of pixels that lie inside the padded area
but outside active area is undefined. The application can use the padded and active rectangles to detect where the rubbish pixels are located and remove them if needed.


Configuration of video output
=============================

For output devices targets and ioctls are used similarly to the video capture case. The *composing* rectangle refers to the insertion of an image into a video signal. The cropping
rectangles refer to a memory buffer. It is recommended to configure the composing targets before to the cropping targets.

The cropping targets refer to the memory buffer that contains an image to be inserted into a video signal or graphical screen. The limits of cropping coordinates are obtained using
``V4L2_SEL_TGT_CROP_BOUNDS``. All coordinates are expressed in pixels. The top/left corner is always point ``(0,0)``. The width and height is equal to the image size specified
using ``VIDIOC_S_FMT`` ioctl.

The top left corner, width and height of the source rectangle, that is the area from which image date are processed by the hardware, is given by the ``V4L2_SEL_TGT_CROP``. Its
coordinates are expressed in in the same coordinate system as the bounds rectangle. The active cropping area must lie completely inside the crop boundaries and the driver may
further adjust the requested size and/or position according to hardware limitations.

For output devices the default cropping rectangle is queried using ``V4L2_SEL_TGT_CROP_DEFAULT``. It is usually equal to the bounding rectangle.

The part of a video signal or graphics display where the image is inserted by the hardware is controlled by ``V4L2_SEL_TGT_COMPOSE`` target. The rectangle's coordinates are
expressed in pixels. The composing rectangle must lie completely inside the bounds rectangle. The driver must adjust the area to fit to the bounding limits. Moreover, the driver
can perform other adjustments according to hardware limitations.

The device has a default composing rectangle, given by the ``V4L2_SEL_TGT_COMPOSE_DEFAULT`` target. This rectangle shall cover what the driver writer considers the complete
picture. It is recommended for the driver developers to put the top/left corner at position ``(0,0)``. Drivers shall set the active composing rectangle to the default one when the
driver is first loaded.

The devices may introduce additional content to video signal other than an image from memory buffers. It includes borders around an image. However, such a padded area is
driver-dependent feature not covered by this document. Driver developers are encouraged to keep padded rectangle equal to active one. The padded target is accessed by the
``V4L2_SEL_TGT_COMPOSE_PADDED`` identifier. It must contain all pixels from the ``V4L2_SEL_TGT_COMPOSE`` target.


Scaling control
===============

An application can detect if scaling is performed by comparing the width and the height of rectangles obtained using ``V4L2_SEL_TGT_CROP`` and ``V4L2_SEL_TGT_COMPOSE`` targets. If
these are not equal then the scaling is applied. The application can compute the scaling ratios using these values.


Comparison with old cropping API
================================

The selection API was introduced to cope with deficiencies of previous :ref:`API <crop>`, that was designed to control simple capture devices. Later the cropping API was adopted
by video output drivers. The ioctls are used to select a part of the display were the video signal is inserted. It should be considered as an API abuse because the described
operation is actually the composing. The selection API makes a clear distinction between composing and cropping operations by setting the appropriate targets. The V4L2 API lacks
any support for composing to and cropping from an image inside a memory buffer. The application could configure a capture device to fill only a part of an image by abusing V4L2
API. Cropping a smaller image from a larger one is achieved by setting the field struct :ref:`v4l2_pix_format <v4l2-pix-format>```::bytesperline``. Introducing an image offsets
could be done by modifying field struct :ref:`v4l2_buffer <v4l2-buffer>```::m_userptr`` before calling ``VIDIOC_QBUF``. Those operations should be avoided because they are not
portable (endianness), and do not work for macroblock and Bayer formats and mmap buffers. The selection API deals with configuration of buffer cropping/composing in a clear,
intuitive and portable way. Next, with the selection API the concepts of the padded target and constraints flags are introduced. Finally, struct :ref:`v4l2_crop <v4l2-crop>` and
struct :ref:`v4l2_cropcap <v4l2-cropcap>` have no reserved fields. Therefore there is no way to extend their functionality. The new struct
:ref:`v4l2_selection <v4l2-selection>` provides a lot of place for future extensions. Driver developers are encouraged to implement only selection API. The former cropping API
would be simulated using the new one.


Examples
========

(A video capture device is assumed; change ``V4L2_BUF_TYPE_VIDEO_CAPTURE`` for other devices; change target to ``V4L2_SEL_TGT_COMPOSE_⋆`` family to configure composing area)


.. code-block:: c

        struct v4l2_selection sel = {
            .type = V4L2_BUF_TYPE_VIDEO_CAPTURE,
            .target = V4L2_SEL_TGT_CROP_DEFAULT,
        };
        ret = ioctl(fd, VIDIOC_G_SELECTION, &sel);
        if (ret)
            exit(-1);
        sel.target = V4L2_SEL_TGT_CROP;
        ret = ioctl(fd, VIDIOC_S_SELECTION, &sel);
        if (ret)
            exit(-1);

Setting a composing area on output of size of *at most* half of limit placed at a center of a display.


.. code-block:: c

        struct v4l2_selection sel = {
            .type = V4L2_BUF_TYPE_VIDEO_OUTPUT,
            .target = V4L2_SEL_TGT_COMPOSE_BOUNDS,
        };
        struct v4l2_rect r;

        ret = ioctl(fd, VIDIOC_G_SELECTION, &sel);
        if (ret)
            exit(-1);
        /* setting smaller compose rectangle */
        r.width = sel.r.width / 2;
        r.height = sel.r.height / 2;
        r.left = sel.r.width / 4;
        r.top = sel.r.height / 4;
        sel.r = r;
        sel.target = V4L2_SEL_TGT_COMPOSE;
        sel.flags = V4L2_SEL_FLAG_LE;
        ret = ioctl(fd, VIDIOC_S_SELECTION, &sel);
        if (ret)
            exit(-1);

A video output device is assumed; change ``V4L2_BUF_TYPE_VIDEO_OUTPUT`` for other devices


.. code-block:: c

        struct v4l2_selection compose = {
            .type = V4L2_BUF_TYPE_VIDEO_OUTPUT,
            .target = V4L2_SEL_TGT_COMPOSE,
        };
        struct v4l2_selection crop = {
            .type = V4L2_BUF_TYPE_VIDEO_OUTPUT,
            .target = V4L2_SEL_TGT_CROP,
        };
        double hscale, vscale;

        ret = ioctl(fd, VIDIOC_G_SELECTION, &compose);
        if (ret)
            exit(-1);
        ret = ioctl(fd, VIDIOC_G_SELECTION, &crop);
        if (ret)
            exit(-1);

        /* computing scaling factors */
        hscale = (double)compose.r.width / crop.r.width;
        vscale = (double)compose.r.height / crop.r.height;


