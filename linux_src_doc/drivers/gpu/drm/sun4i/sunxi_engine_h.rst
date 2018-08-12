.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sun4i/sunxi_engine.h

.. _`sunxi_engine_ops`:

struct sunxi_engine_ops
=======================

.. c:type:: struct sunxi_engine_ops

    helper operations for sunXi engines

.. _`sunxi_engine_ops.definition`:

Definition
----------

.. code-block:: c

    struct sunxi_engine_ops {
        void (*atomic_begin)(struct sunxi_engine *engine, struct drm_crtc_state *old_state);
        int (*atomic_check)(struct sunxi_engine *engine, struct drm_crtc_state *state);
        void (*commit)(struct sunxi_engine *engine);
        struct drm_plane **(*layers_init)(struct drm_device *drm, struct sunxi_engine *engine);
        void (*apply_color_correction)(struct sunxi_engine *engine);
        void (*disable_color_correction)(struct sunxi_engine *engine);
        void (*vblank_quirk)(struct sunxi_engine *engine);
    }

.. _`sunxi_engine_ops.members`:

Members
-------

atomic_begin

    This callback allows to prepare our engine for an atomic
    update. This is mirroring the
    \ :c:type:`drm_crtc_helper_funcs.atomic_begin <drm_crtc_helper_funcs>`\  callback, so any
    documentation there applies.

    This function is optional.

atomic_check

    This callback allows to validate plane-update related CRTC
    constraints specific to engines. This is mirroring the
    \ :c:type:`drm_crtc_helper_funcs.atomic_check <drm_crtc_helper_funcs>`\  callback, so any
    documentation there applies.

    This function is optional.

    RETURNS:

    0 on success or a negative error code.

commit

    This callback will trigger the hardware switch to commit
    the new configuration that has been setup during the next
    vblank period.

    This function is optional.

layers_init

    This callback is used to allocate, initialize and register
    the layers supported by that engine.

    This function is mandatory.

    RETURNS:

    The array of struct drm_plane backing the layers, or an
    error pointer on failure.

apply_color_correction

    This callback will enable the color correction in the
    engine. This is useful only for the composite output.

    This function is optional.

disable_color_correction

    This callback will stop the color correction in the
    engine. This is useful only for the composite output.

    This function is optional.

vblank_quirk

    This callback is used to implement engine-specific
    behaviour part of the VBLANK event. It is run with all the
    constraints of an interrupt (can't sleep, all local
    interrupts disabled) and therefore should be as fast as
    possible.

    This function is optional.

.. _`sunxi_engine_ops.description`:

Description
-----------

These hooks are used by the common part of the DRM driver to
implement the proper behaviour.

.. _`sunxi_engine`:

struct sunxi_engine
===================

.. c:type:: struct sunxi_engine

    the common parts of an engine for sun4i-drm driver

.. _`sunxi_engine.definition`:

Definition
----------

.. code-block:: c

    struct sunxi_engine {
        const struct sunxi_engine_ops *ops;
        struct device_node *node;
        struct regmap *regs;
        int id;
        struct list_head list;
    }

.. _`sunxi_engine.members`:

Members
-------

ops
    the operations of the engine

node
    the of device node of the engine

regs
    the regmap of the engine

id
    the id of the engine (-1 if not used)

list
    *undescribed*

.. _`sunxi_engine_commit`:

sunxi_engine_commit
===================

.. c:function:: void sunxi_engine_commit(struct sunxi_engine *engine)

    commit all changes of the engine

    :param struct sunxi_engine \*engine:
        pointer to the engine

.. _`sunxi_engine_layers_init`:

sunxi_engine_layers_init
========================

.. c:function:: struct drm_plane **sunxi_engine_layers_init(struct drm_device *drm, struct sunxi_engine *engine)

    Create planes (layers) for the engine

    :param struct drm_device \*drm:
        pointer to the drm_device for which planes will be created

    :param struct sunxi_engine \*engine:
        pointer to the engine

.. _`sunxi_engine_apply_color_correction`:

sunxi_engine_apply_color_correction
===================================

.. c:function:: void sunxi_engine_apply_color_correction(struct sunxi_engine *engine)

    Apply the RGB2YUV color correction

    :param struct sunxi_engine \*engine:
        pointer to the engine

.. _`sunxi_engine_apply_color_correction.description`:

Description
-----------

This functionality is optional for an engine, however, if the engine is
intended to be used with TV Encoder, the output will be incorrect
without the color correction, due to TV Encoder expects the engine to
output directly YUV signal.

.. _`sunxi_engine_disable_color_correction`:

sunxi_engine_disable_color_correction
=====================================

.. c:function:: void sunxi_engine_disable_color_correction(struct sunxi_engine *engine)

    Disable the color space correction

    :param struct sunxi_engine \*engine:
        pointer to the engine

.. _`sunxi_engine_disable_color_correction.description`:

Description
-----------

This function is paired with \ :c:func:`apply_color_correction`\ .

.. This file was automatic generated / don't edit.

