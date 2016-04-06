
.. _API-struct-drm-rect:

===============
struct drm_rect
===============

*man struct drm_rect(9)*

*4.6.0-rc1*

two dimensional rectangle


Synopsis
========

.. code-block:: c

    struct drm_rect {
      int x1;
      int y1;
      int x2;
      int y2;
    };


Members
=======

x1
    horizontal starting coordinate (inclusive)

y1
    vertical starting coordinate (inclusive)

x2
    horizontal ending coordinate (exclusive)

y2
    vertical ending coordinate (exclusive)
