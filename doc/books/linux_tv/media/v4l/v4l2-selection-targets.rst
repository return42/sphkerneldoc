
.. _v4l2-selection-targets:

=================
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


