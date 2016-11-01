.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos_drm_g2d.c

.. _`g2d_remove_runqueue_nodes`:

g2d_remove_runqueue_nodes
=========================

.. c:function:: void g2d_remove_runqueue_nodes(struct g2d_data *g2d, struct drm_file*file)

    remove items from the list of runqueue nodes

    :param struct g2d_data \*g2d:
        G2D state object

    :param struct drm_file\*file:
        if not zero, only remove items with this DRM file

.. _`g2d_remove_runqueue_nodes.description`:

Description
-----------

Has to be called under runqueue lock.

.. _`g2d_wait_finish`:

g2d_wait_finish
===============

.. c:function:: void g2d_wait_finish(struct g2d_data *g2d, struct drm_file *file)

    wait for the G2D engine to finish the current runqueue node

    :param struct g2d_data \*g2d:
        G2D state object

    :param struct drm_file \*file:
        if not zero, only wait if the current runqueue node belongs
        to the DRM file

.. _`g2d_wait_finish.description`:

Description
-----------

Should the engine not become idle after a 100ms timeout, a hardware
reset is issued.

.. This file was automatic generated / don't edit.

