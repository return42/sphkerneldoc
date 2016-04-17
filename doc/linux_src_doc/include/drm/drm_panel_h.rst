.. -*- coding: utf-8; mode: rst -*-

===========
drm_panel.h
===========


.. _`drm_panel_funcs`:

struct drm_panel_funcs
======================

.. c:type:: drm_panel_funcs

    perform operations on a given panel


.. _`drm_panel_funcs.definition`:

Definition
----------

.. code-block:: c

  struct drm_panel_funcs {
    int (* disable) (struct drm_panel *panel);
    int (* unprepare) (struct drm_panel *panel);
    int (* prepare) (struct drm_panel *panel);
    int (* enable) (struct drm_panel *panel);
    int (* get_modes) (struct drm_panel *panel);
    int (* get_timings) (struct drm_panel *panel, unsigned int num_timings,struct display_timing *timings);
  };


.. _`drm_panel_funcs.members`:

Members
-------

:``disable``:
    disable panel (turn off back light, etc.)

:``unprepare``:
    turn off panel

:``prepare``:
    turn on panel and perform set up

:``enable``:
    enable panel (turn on back light, etc.)

:``get_modes``:
    add modes to the connector that the panel is attached to and
    return the number of modes added

:``get_timings``:
    copy display timings into the provided array and return
    the number of display timings available




.. _`drm_panel_funcs.description`:

Description
-----------

The .:c:func:`prepare` function is typically called before the display controller
starts to transmit video data. Panel drivers can use this to turn the panel
on and wait for it to become ready. If additional configuration is required
(via a control bus such as I2C, SPI or DSI for example) this is a good time
to do that.

After the display controller has started transmitting video data, it's safe
to call the .:c:func:`enable` function. This will typically enable the backlight to
make the image on screen visible. Some panels require a certain amount of
time or frames before the image is displayed. This function is responsible
for taking this into account before enabling the backlight to avoid visual
glitches.

Before stopping video transmission from the display controller it can be
necessary to turn off the panel to avoid visual glitches. This is done in
the .:c:func:`disable` function. Analogously to .:c:func:`enable` this typically involves
turning off the backlight and waiting for some time to make sure no image
is visible on the panel. It is then safe for the display controller to
cease transmission of video data.

To save power when no video data is transmitted, a driver can power down
the panel. This is the job of the .:c:func:`unprepare` function.

