
.. _API-struct-drm-plane-state:

======================
struct drm_plane_state
======================

*man struct drm_plane_state(9)*

*4.6.0-rc1*

mutable plane state


Synopsis
========

.. code-block:: c

    struct drm_plane_state {
      struct drm_plane * plane;
      struct drm_crtc * crtc;
      struct drm_framebuffer * fb;
      struct fence * fence;
      int32_t crtc_x;
      int32_t crtc_y;
      uint32_t crtc_w;
      uint32_t crtc_h;
      uint32_t src_x;
      uint32_t src_y;
      uint32_t src_h;
      uint32_t src_w;
      struct drm_atomic_state * state;
    };


Members
=======

plane
    backpointer to the plane

crtc
    currently bound CRTC, NULL if disabled

fb
    currently bound framebuffer

fence
    optional fence to wait for before scanning out ``fb``

crtc_x
    left position of visible portion of plane on crtc

crtc_y
    upper position of visible portion of plane on crtc

crtc_w
    width of visible portion of plane on crtc

crtc_h
    height of visible portion of plane on crtc

src_x
    left position of visible portion of plane within plane (in 16.16)

src_y
    upper position of visible portion of plane within plane (in 16.16)

src_h
    height of visible portion of plane (in 16.16)

src_w
    width of visible portion of plane (in 16.16)

state
    backpointer to global drm_atomic_state
