
.. _vidioc-subdev-enum-mbus-code:

==================================
ioctl VIDIOC_SUBDEV_ENUM_MBUS_CODE
==================================

*man VIDIOC_SUBDEV_ENUM_MBUS_CODE(2)*

Enumerate media bus formats


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_subdev_mbus_code_enum * argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_SUBDEV_ENUM_MBUS_CODE

``argp``


Description
===========

    **Note**

    This is an :ref:`experimental <experimental>` interface and may change in the future.

To enumerate media bus formats available at a given sub-device pad applications initialize the ``pad``, ``which`` and ``index`` fields of struct
:ref:`v4l2_subdev_mbus_code_enum <v4l2-subdev-mbus-code-enum>` and call the ``VIDIOC_SUBDEV_ENUM_MBUS_CODE`` ioctl with a pointer to this structure. Drivers fill the rest of
the structure or return an EINVAL error code if either the ``pad`` or ``index`` are invalid. All media bus formats are enumerable by beginning at index zero and incrementing by one
until EINVAL is returned.

Available media bus formats may depend on the current 'try' formats at other pads of the sub-device, as well as on the current active links. See
:ref:`VIDIOC_SUBDEV_G_FMT <vidioc-subdev-g-fmt>` for more information about the try formats.


.. _v4l2-subdev-mbus-code-enum:

.. table:: struct v4l2_subdev_mbus_code_enum

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``pad``                                       | Pad number as reported by the media controller API.                                        |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``index``                                     | Number of the format in the enumeration, set by the application.                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``code``                                      | The media bus format code, as defined in :ref:`v4l2-mbus-format`.                          |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``which``                                     | Media bus format codes to be enumerated, from enum                                         |
    |                                               |                                               | :ref:`v4l2_subdev_format_whence     <v4l2-subdev-format-whence>`.                          |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``reserved``  [8]                             | Reserved for future extensions. Applications and drivers must set the array to zero.       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The struct :ref:`v4l2_subdev_mbus_code_enum <v4l2-subdev-mbus-code-enum>` ``pad`` references a non-existing pad, or the ``index`` field is out of bounds.
