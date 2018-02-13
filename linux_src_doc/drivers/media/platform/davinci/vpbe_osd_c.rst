.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpbe_osd.c

.. _`_osd_dm6446_vid0_pingpong`:

\_osd_dm6446_vid0_pingpong
==========================

.. c:function:: int _osd_dm6446_vid0_pingpong(struct osd_state *sd, int field_inversion, unsigned long fb_base_phys, const struct osd_layer_config *lconfig)

    field inversion fix for DM6446 \ ``sd``\  - ptr to struct osd_state \ ``field_inversion``\  - inversion flag \ ``fb_base_phys``\  - frame buffer address \ ``lconfig``\  - ptr to layer config

    :param struct osd_state \*sd:
        *undescribed*

    :param int field_inversion:
        *undescribed*

    :param unsigned long fb_base_phys:
        *undescribed*

    :param const struct osd_layer_config \*lconfig:
        *undescribed*

.. _`_osd_dm6446_vid0_pingpong.description`:

Description
-----------

This routine implements a workaround for the field signal inversion silicon
erratum described in Advisory 1.3.8 for the DM6446.  The fb_base_phys and
lconfig parameters apply to the vid0 window.  This routine should be called
whenever the vid0 layer configuration or start address is modified, or when
the OSD field inversion setting is modified.

.. _`_osd_dm6446_vid0_pingpong.return`:

Return
------

1 if the ping-pong buffers need to be toggled in the vsync isr, or
0 otherwise

.. _`try_layer_config`:

try_layer_config
================

.. c:function:: int try_layer_config(struct osd_state *sd, enum osd_layer layer, struct osd_layer_config *lconfig)

    Try a specific configuration for the layer \ ``sd``\   - ptr to struct osd_state \ ``layer``\  - layer to configure \ ``lconfig``\  - layer configuration to try

    :param struct osd_state \*sd:
        *undescribed*

    :param enum osd_layer layer:
        *undescribed*

    :param struct osd_layer_config \*lconfig:
        *undescribed*

.. _`try_layer_config.description`:

Description
-----------

If the requested lconfig is completely rejected and the value of lconfig on
exit is the current lconfig, then \ :c:func:`try_layer_config`\  returns 1.  Otherwise,
\ :c:func:`try_layer_config`\  returns 0.  A return value of 0 does not necessarily mean
that the value of lconfig on exit is identical to the value of lconfig on
entry, but merely that it represents a change from the current lconfig.

.. This file was automatic generated / don't edit.

