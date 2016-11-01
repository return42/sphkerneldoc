.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_panel.h

.. _`drm_panel_funcs`:

struct drm_panel_funcs
======================

.. c:type:: struct drm_panel_funcs

    perform operations on a given panel

.. _`drm_panel_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_panel_funcs {
        int (*disable)(struct drm_panel *panel);
        int (*unprepare)(struct drm_panel *panel);
        int (*prepare)(struct drm_panel *panel);
        int (*enable)(struct drm_panel *panel);
        int (*get_modes)(struct drm_panel *panel);
        int (*get_timings)(struct drm_panel *panel, unsigned int num_timings,struct display_timing *timings);
    }

.. _`drm_panel_funcs.members`:

Members
-------

disable
    disable panel (turn off back light, etc.)

unprepare
    turn off panel

prepare
    turn on panel and perform set up

enable
    enable panel (turn on back light, etc.)

get_modes
    add modes to the connector that the panel is attached to and
    return the number of modes added

get_timings
    copy display timings into the provided array and return
    the number of display timings available

.. _`drm_panel_funcs.description`:

Description
-----------

The .prepare() function is typically called before the display controller
starts to transmit video data. Panel drivers can use this to turn the panel
on and wait for it to become ready. If additional configuration is required
(via a control bus such as I2C, SPI or DSI for example) this is a good time
to do that.

After the display controller has started transmitting video data, it's safe
to call the .enable() function. This will typically enable the backlight to
make the image on screen visible. Some panels require a certain amount of
time or frames before the image is displayed. This function is responsible
for taking this into account before enabling the backlight to avoid visual
glitches.

Before stopping video transmission from the display controller it can be
necessary to turn off the panel to avoid visual glitches. This is done in
the .disable() function. Analogously to .enable() this typically involves
turning off the backlight and waiting for some time to make sure no image
is visible on the panel. It is then safe for the display controller to
cease transmission of video data.

To save power when no video data is transmitted, a driver can power down
the panel. This is the job of the .unprepare() function.

.. _`drm_panel`:

struct drm_panel
================

.. c:type:: struct drm_panel

    DRM panel object

.. _`drm_panel.definition`:

Definition
----------

.. code-block:: c

    struct drm_panel {
        struct drm_device *drm;
        struct drm_connector *connector;
        struct device *dev;
        const struct drm_panel_funcs *funcs;
        struct list_head list;
    }

.. _`drm_panel.members`:

Members
-------

drm
    DRM device owning the panel

connector
    DRM connector that the panel is attached to

dev
    parent device of the panel

funcs
    operations that can be performed on the panel

list
    panel entry in registry

.. _`drm_panel_unprepare`:

drm_panel_unprepare
===================

.. c:function:: int drm_panel_unprepare(struct drm_panel *panel)

    power off a panel

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_unprepare.description`:

Description
-----------

Calling this function will completely power off a panel (assert the panel's
reset, turn off power supplies, ...). After this function has completed, it
is usually no longer possible to communicate with the panel until another
call to \ :c:func:`drm_panel_prepare`\ .

.. _`drm_panel_unprepare.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_disable`:

drm_panel_disable
=================

.. c:function:: int drm_panel_disable(struct drm_panel *panel)

    disable a panel

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_disable.description`:

Description
-----------

This will typically turn off the panel's backlight or disable the display
drivers. For smart panels it should still be possible to communicate with
the integrated circuitry via any command bus after this call.

.. _`drm_panel_disable.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_prepare`:

drm_panel_prepare
=================

.. c:function:: int drm_panel_prepare(struct drm_panel *panel)

    power on a panel

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_prepare.description`:

Description
-----------

Calling this function will enable power and deassert any reset signals to
the panel. After this has completed it is possible to communicate with any
integrated circuitry via a command bus.

.. _`drm_panel_prepare.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_enable`:

drm_panel_enable
================

.. c:function:: int drm_panel_enable(struct drm_panel *panel)

    enable a panel

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_enable.description`:

Description
-----------

Calling this function will cause the panel display drivers to be turned on
and the backlight to be enabled. Content will be visible on screen after
this call completes.

.. _`drm_panel_enable.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_get_modes`:

drm_panel_get_modes
===================

.. c:function:: int drm_panel_get_modes(struct drm_panel *panel)

    probe the available display modes of a panel

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_get_modes.description`:

Description
-----------

The modes probed from the panel are automatically added to the connector
that the panel is attached to.

.. _`drm_panel_get_modes.return`:

Return
------

The number of modes available from the panel on success or a
negative error code on failure.

.. This file was automatic generated / don't edit.

