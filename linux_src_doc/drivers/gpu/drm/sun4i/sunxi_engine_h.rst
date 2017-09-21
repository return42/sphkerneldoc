.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sun4i/sunxi_engine.h

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

