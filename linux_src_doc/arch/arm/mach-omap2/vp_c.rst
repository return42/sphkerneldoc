.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/vp.c

.. _`omap_vp_enable`:

omap_vp_enable
==============

.. c:function:: void omap_vp_enable(struct voltagedomain *voltdm)

    API to enable a particular VP

    :param voltdm:
        pointer to the VDD whose VP is to be enabled.
    :type voltdm: struct voltagedomain \*

.. _`omap_vp_enable.description`:

Description
-----------

This API enables a particular voltage processor. Needed by the smartreflex
class drivers.

.. _`omap_vp_disable`:

omap_vp_disable
===============

.. c:function:: void omap_vp_disable(struct voltagedomain *voltdm)

    API to disable a particular VP

    :param voltdm:
        pointer to the VDD whose VP is to be disabled.
    :type voltdm: struct voltagedomain \*

.. _`omap_vp_disable.description`:

Description
-----------

This API disables a particular voltage processor. Needed by the smartreflex
class drivers.

.. This file was automatic generated / don't edit.

