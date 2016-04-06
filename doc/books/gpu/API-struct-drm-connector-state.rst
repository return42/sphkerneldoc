
.. _API-struct-drm-connector-state:

==========================
struct drm_connector_state
==========================

*man struct drm_connector_state(9)*

*4.6.0-rc1*

mutable connector state


Synopsis
========

.. code-block:: c

    struct drm_connector_state {
      struct drm_connector * connector;
      struct drm_crtc * crtc;
      struct drm_encoder * best_encoder;
      struct drm_atomic_state * state;
    };


Members
=======

connector
    backpointer to the connector

crtc
    CRTC to connect connector to, NULL if disabled

best_encoder
    can be used by helpers and drivers to select the encoder

state
    backpointer to global drm_atomic_state
