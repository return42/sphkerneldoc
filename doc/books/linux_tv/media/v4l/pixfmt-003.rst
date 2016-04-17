
==============================
Multi-planar format structures
==============================

The ``v4l2_plane_pix_format`` structures define size and layout for each of the planes in a multi-planar format. The ``v4l2_pix_format_mplane`` structure contains information
common to all planes (such as image width and height) and an array of ``v4l2_plane_pix_format`` structures, describing all planes of that format.


.. _v4l2-plane-pix-format:

.. table:: struct v4l2_plane_pix_format

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``sizeimage``                                 | Maximum size in bytes required for image data in this plane.                               |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``bytesperline``                              | Distance in bytes between the leftmost pixels in two adjacent lines. See struct            |
    |                                               |                                               | :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                               |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16                                         | ``reserved[6]``                               | Reserved for future extensions. Should be zeroed by drivers and applications.              |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-pix-format-mplane:

.. table:: struct v4l2_pix_format_mplane

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``width``                                     | Image width in pixels. See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``height``                                    | Image height in pixels. See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``pixelformat``                               | The pixel format. Both single- and multi-planar four character codes can be used.          |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum :ref:`v4l2_field   <v4l2-field>`         | ``field``                                     | See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                    |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``colorspace``                                | See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                    |
    | :ref:`v4l2_colorspace   <v4l2-colorspace>`    |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ``plane_fmt[VIDEO_MAX_PLANES]``               | An array of structures describing format of each plane this pixel format consists of. The  |
    | :ref:`v4l2_plane_pix_format     <v4l2-plane-p |                                               | number of valid entries in this array has to be put in the ``num_planes`` field.           |
    | ix-format>`                                   |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``num_planes``                                | Number of planes (i.e. separate memory buffers) for this format and the number of valid    |
    |                                               |                                               | entries in the ``plane_fmt`` array.                                                        |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``flags``                                     | Flags set by the application or driver, see :ref:`format-flags`.                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``ycbcr_enc``                                 | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_ycbcr_encoding    <v4l2-ycbcr-enco |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    | ding>`                                        |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``quantization``                              | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_quantization   <v4l2-quantization> |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    | `                                             |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``xfer_func``                                 | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_xfer_func    <v4l2-xfer-func>`     |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``reserved[7]``                               | Reserved for future extensions. Should be zeroed by drivers and applications.              |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


