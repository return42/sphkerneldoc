.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_encoder.h

.. _`drm_encoder_funcs`:

struct drm_encoder_funcs
========================

.. c:type:: struct drm_encoder_funcs

    encoder controls

.. _`drm_encoder_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_encoder_funcs {
        void (*reset)(struct drm_encoder *encoder);
        void (*destroy)(struct drm_encoder *encoder);
        int (*late_register)(struct drm_encoder *encoder);
        void (*early_unregister)(struct drm_encoder *encoder);
    }

.. _`drm_encoder_funcs.members`:

Members
-------

reset

    Reset encoder hardware and software state to off. This function isn't
    called by the core directly, only through \ :c:func:`drm_mode_config_reset`\ .
    It's not a helper hook only for historical reasons.

destroy

    Clean up encoder resources. This is only called at driver unload time
    through \ :c:func:`drm_mode_config_cleanup`\  since an encoder cannot be
    hotplugged in DRM.

late_register

    This optional hook can be used to register additional userspace
    interfaces attached to the encoder like debugfs interfaces.
    It is called late in the driver load sequence from \ :c:func:`drm_dev_register`\ .
    Everything added from this callback should be unregistered in
    the early_unregister callback.

    Returns:

    0 on success, or a negative error code on failure.

early_unregister

    This optional hook should be used to unregister the additional
    userspace interfaces attached to the encoder from
    \ ``late_register``\ . It is called from \ :c:func:`drm_dev_unregister`\ ,
    early in the driver unload sequence to disable userspace access
    before data structures are torndown.

.. _`drm_encoder_funcs.description`:

Description
-----------

Encoders sit between CRTCs and connectors.

.. _`drm_encoder`:

struct drm_encoder
==================

.. c:type:: struct drm_encoder

    central DRM encoder structure

.. _`drm_encoder.definition`:

Definition
----------

.. code-block:: c

    struct drm_encoder {
        struct drm_device *dev;
        struct list_head head;
        struct drm_mode_object base;
        char *name;
        int encoder_type;
        unsigned index;
        uint32_t possible_crtcs;
        uint32_t possible_clones;
        struct drm_crtc *crtc;
        struct drm_bridge *bridge;
        const struct drm_encoder_funcs *funcs;
        const struct drm_encoder_helper_funcs *helper_private;
    }

.. _`drm_encoder.members`:

Members
-------

dev
    parent DRM device

head
    list management

base
    base KMS object

name
    human readable name, can be overwritten by the driver

encoder_type

    One of the DRM_MODE_ENCODER_<foo> types in drm_mode.h. The following
    encoder types are defined thus far:

    - DRM_MODE_ENCODER_DAC for VGA and analog on DVI-I/DVI-A.

    - DRM_MODE_ENCODER_TMDS for DVI, HDMI and (embedded) DisplayPort.

    - DRM_MODE_ENCODER_LVDS for display panels, or in general any panel
      with a proprietary parallel connector.

    - DRM_MODE_ENCODER_TVDAC for TV output (Composite, S-Video,
      Component, SCART).

    - DRM_MODE_ENCODER_VIRTUAL for virtual machine displays

    - DRM_MODE_ENCODER_DSI for panels connected using the DSI serial bus.

    - DRM_MODE_ENCODER_DPI for panels connected using the DPI parallel
      bus.

    - DRM_MODE_ENCODER_DPMST for special fake encoders used to allow
      mutliple DP MST streams to share one physical encoder.

index
    Position inside the mode_config.list, can be used as an arrayindex. It is invariant over the lifetime of the encoder.

possible_crtcs
    Bitmask of potential CRTC bindings, \ :c:func:`usingdrm_crtc_index`\  as the index into the bitfield. The driver must set
    the bits for all \ :c:type:`struct drm_crtc <drm_crtc>`\  objects this encoder can be connected to
    before calling \ :c:func:`drm_encoder_init`\ .

    In reality almost every driver gets this wrong.

    Note that since CRTC objects can't be hotplugged the assigned indices
    are stable and hence known before registering all objects.

possible_clones
    Bitmask of potential sibling encoders for cloning,using \ :c:func:`drm_encoder_index`\  as the index into the bitfield. The driver
    must set the bits for all \ :c:type:`struct drm_encoder <drm_encoder>`\  objects which can clone a
    \ :c:type:`struct drm_crtc <drm_crtc>`\  together with this encoder before calling
    \ :c:func:`drm_encoder_init`\ . Drivers should set the bit representing the
    encoder itself, too. Cloning bits should be set such that when two
    encoders can be used in a cloned configuration, they both should have
    each another bits set.

    In reality almost every driver gets this wrong.

    Note that since encoder objects can't be hotplugged the assigned indices
    are stable and hence known before registering all objects.

crtc
    Currently bound CRTC, only really meaningful for non-atomicdrivers.  Atomic drivers should instead check
    \ :c:type:`drm_connector_state.crtc <drm_connector_state>`\ .

bridge
    bridge associated to the encoder

funcs
    control functions

helper_private
    mid-layer private data

.. _`drm_encoder.description`:

Description
-----------

CRTCs drive pixels to encoders, which convert them into signals
appropriate for a given connector or set of connectors.

.. _`drm_encoder_index`:

drm_encoder_index
=================

.. c:function:: unsigned int drm_encoder_index(struct drm_encoder *encoder)

    find the index of a registered encoder

    :param struct drm_encoder \*encoder:
        encoder to find index for

.. _`drm_encoder_index.description`:

Description
-----------

Given a registered encoder, return the index of that encoder within a DRM
device's list of encoders.

.. _`drm_encoder_crtc_ok`:

drm_encoder_crtc_ok
===================

.. c:function:: bool drm_encoder_crtc_ok(struct drm_encoder *encoder, struct drm_crtc *crtc)

    can a given crtc drive a given encoder?

    :param struct drm_encoder \*encoder:
        encoder to test

    :param struct drm_crtc \*crtc:
        crtc to test

.. _`drm_encoder_crtc_ok.description`:

Description
-----------

Returns false if \ ``encoder``\  can't be driven by \ ``crtc``\ , true otherwise.

.. _`drm_encoder_find`:

drm_encoder_find
================

.. c:function:: struct drm_encoder *drm_encoder_find(struct drm_device *dev, struct drm_file *file_priv, uint32_t id)

    find a \ :c:type:`struct drm_encoder <drm_encoder>`\ 

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        drm file to check for lease against.

    :param uint32_t id:
        encoder id

.. _`drm_encoder_find.description`:

Description
-----------

Returns the encoder with \ ``id``\ , NULL if it doesn't exist. Simple wrapper around
\ :c:func:`drm_mode_object_find`\ .

.. _`drm_for_each_encoder_mask`:

drm_for_each_encoder_mask
=========================

.. c:function::  drm_for_each_encoder_mask( encoder,  dev,  encoder_mask)

    iterate over encoders specified by bitmask

    :param  encoder:
        the loop cursor

    :param  dev:
        the DRM device

    :param  encoder_mask:
        bitmask of encoder indices

.. _`drm_for_each_encoder_mask.description`:

Description
-----------

Iterate over all encoders specified by bitmask.

.. _`drm_for_each_encoder`:

drm_for_each_encoder
====================

.. c:function::  drm_for_each_encoder( encoder,  dev)

    iterate over all encoders

    :param  encoder:
        the loop cursor

    :param  dev:
        the DRM device

.. _`drm_for_each_encoder.description`:

Description
-----------

Iterate over all encoders of \ ``dev``\ .

.. This file was automatic generated / don't edit.

