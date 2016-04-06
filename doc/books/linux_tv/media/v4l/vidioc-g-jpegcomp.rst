
.. _vidioc-g-jpegcomp:

==========================================
ioctl VIDIOC_G_JPEGCOMP, VIDIOC_S_JPEGCOMP
==========================================

*man VIDIOC_G_JPEGCOMP(2)*

VIDIOC_S_JPEGCOMP

Synopsis
========

.. c:function:: int ioctl( int fd, int request, v4l2_jpegcompression *argp )

.. c:function:: int ioctl( int fd, int request, const v4l2_jpegcompression *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_G_JPEGCOMP, VIDIOC_S_JPEGCOMP

``argp``


Description
===========

These ioctls are **deprecated**. New drivers and applications should use :ref:`JPEG class controls <jpeg-controls>` for image quality and JPEG markers control.

[to do]

Ronald Bultje elaborates:

APP is some application-specific information. The application can set it itself, and it'll be stored in the JPEG-encoded fields (eg; interlacing information for in an AVI or so).
COM is the same, but it's comments, like 'encoded by me' or so.

jpeg_markers describes whether the huffman tables, quantization tables and the restart interval information (all JPEG-specific stuff) should be stored in the JPEG-encoded fields.
These define how the JPEG field is encoded. If you omit them, applications assume you've used standard encoding. You usually do want to add them.


.. _v4l2-jpegcompression:

.. table:: struct v4l2_jpegcompression

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | int                                           | ``quality``                                   | Deprecated. If :ref:`V4L2_CID_JPEG_COMPRESSION_QUALITY      <jpeg-quality-control>`        |
    |                                               |                                               | control is exposed by a driver applications should use it instead and ignore this field.   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | int                                           | ``APPn``                                      |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | int                                           | ``APP_len``                                   |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | char                                          | ``APP_data``\ [60]                            |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | int                                           | ``COM_len``                                   |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | char                                          | ``COM_data``\ [60]                            |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``jpeg_markers``                              | See :ref:`jpeg-markers`.   Deprecated. If                                                  |
    |                                               |                                               | :ref:`V4L2_CID_JPEG_ACTIVE_MARKER      <jpeg-active-marker-control>`  control is exposed   |
    |                                               |                                               | by a driver applications should use it instead and ignore this field.                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _jpeg-markers:

.. table:: JPEG Markers Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_JPEG_MARKER_DHT``                                            | (1<<3)                 | Define Huffman Tables                                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_JPEG_MARKER_DQT``                                            | (1<<4)                 | Define Quantization Tables                                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_JPEG_MARKER_DRI``                                            | (1<<5)                 | Define Restart Interval                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_JPEG_MARKER_COM``                                            | (1<<6)                 | Comment segment                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_JPEG_MARKER_APP``                                            | (1<<7)                 | App segment, driver will always use APP0                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
