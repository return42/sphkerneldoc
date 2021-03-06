.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-dapm.c

.. _`snd_soc_dapm_kcontrol_widget`:

snd_soc_dapm_kcontrol_widget
============================

.. c:function:: struct snd_soc_dapm_widget *snd_soc_dapm_kcontrol_widget(struct snd_kcontrol *kcontrol)

    Returns the widget associated to a kcontrol

    :param kcontrol:
        The kcontrol
    :type kcontrol: struct snd_kcontrol \*

.. _`snd_soc_dapm_kcontrol_dapm`:

snd_soc_dapm_kcontrol_dapm
==========================

.. c:function:: struct snd_soc_dapm_context *snd_soc_dapm_kcontrol_dapm(struct snd_kcontrol *kcontrol)

    Returns the dapm context associated to a kcontrol

    :param kcontrol:
        The kcontrol
    :type kcontrol: struct snd_kcontrol \*

.. _`snd_soc_dapm_kcontrol_dapm.note`:

Note
----

This function must only be used on kcontrols that are known to have
been registered for a CODEC. Otherwise the behaviour is undefined.

.. _`snd_soc_dapm_force_bias_level`:

snd_soc_dapm_force_bias_level
=============================

.. c:function:: int snd_soc_dapm_force_bias_level(struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level)

    Sets the DAPM bias level

    :param dapm:
        The DAPM context for which to set the level
    :type dapm: struct snd_soc_dapm_context \*

    :param level:
        The level to set
    :type level: enum snd_soc_bias_level

.. _`snd_soc_dapm_force_bias_level.description`:

Description
-----------

Forces the DAPM bias level to a specific state. It will call the bias level
callback of DAPM context with the specified level. This will even happen if
the context is already at the same level. Furthermore it will not go through
the normal bias level sequencing, meaning any intermediate states between the
current and the target state will not be entered.

Note that the change in bias level is only temporary and the next time
\ :c:func:`snd_soc_dapm_sync`\  is called the state will be set to the level as
determined by the DAPM core. The function is mainly intended to be used to
used during probe or resume from suspend to power up the device so
initialization can be done, before the DAPM core takes over.

.. _`snd_soc_dapm_set_bias_level`:

snd_soc_dapm_set_bias_level
===========================

.. c:function:: int snd_soc_dapm_set_bias_level(struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level)

    set the bias level for the system

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param level:
        level to configure
    :type level: enum snd_soc_bias_level

.. _`snd_soc_dapm_set_bias_level.description`:

Description
-----------

Configure the bias (power) levels for the SoC audio device.

Returns 0 for success else error.

.. _`snd_soc_dapm_dai_get_connected_widgets`:

snd_soc_dapm_dai_get_connected_widgets
======================================

.. c:function:: int snd_soc_dapm_dai_get_connected_widgets(struct snd_soc_dai *dai, int stream, struct snd_soc_dapm_widget_list **list, bool (*custom_stop_condition)(struct snd_soc_dapm_widget *, enum snd_soc_dapm_direction))

    query audio path and it's widgets.

    :param dai:
        the soc DAI.
    :type dai: struct snd_soc_dai \*

    :param stream:
        stream direction.
    :type stream: int

    :param list:
        list of active widgets for this stream.
    :type list: struct snd_soc_dapm_widget_list \*\*

    :param bool (\*custom_stop_condition)(struct snd_soc_dapm_widget \*, enum snd_soc_dapm_direction):
        (optional) a function meant to stop the widget graph
        walk based on custom logic.

.. _`snd_soc_dapm_dai_get_connected_widgets.description`:

Description
-----------

Queries DAPM graph as to whether a valid audio stream path exists for
the initial stream specified by name. This takes into account
current mixer and mux kcontrol settings. Creates list of valid widgets.

Optionally, can be supplied with a function acting as a stopping condition.
This function takes the dapm widget currently being examined and the walk
direction as an arguments, it should return true if the walk should be
stopped and false otherwise.

Returns the number of valid paths or negative error.

.. _`snd_soc_dapm_sync_unlocked`:

snd_soc_dapm_sync_unlocked
==========================

.. c:function:: int snd_soc_dapm_sync_unlocked(struct snd_soc_dapm_context *dapm)

    scan and power dapm paths

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

.. _`snd_soc_dapm_sync_unlocked.description`:

Description
-----------

Walks all dapm audio paths and powers widgets according to their
stream or path usage.

Requires external locking.

Returns 0 for success.

.. _`snd_soc_dapm_sync`:

snd_soc_dapm_sync
=================

.. c:function:: int snd_soc_dapm_sync(struct snd_soc_dapm_context *dapm)

    scan and power dapm paths

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

.. _`snd_soc_dapm_sync.description`:

Description
-----------

Walks all dapm audio paths and powers widgets according to their
stream or path usage.

Returns 0 for success.

.. _`snd_soc_dapm_add_routes`:

snd_soc_dapm_add_routes
=======================

.. c:function:: int snd_soc_dapm_add_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Add routes between DAPM widgets

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param route:
        audio routes
    :type route: const struct snd_soc_dapm_route \*

    :param num:
        number of routes
    :type num: int

.. _`snd_soc_dapm_add_routes.description`:

Description
-----------

Connects 2 dapm widgets together via a named audio path. The sink is
the widget receiving the audio signal, whilst the source is the sender
of the audio signal.

Returns 0 for success else error. On error all resources can be freed
with a call to \ :c:func:`snd_soc_card_free`\ .

.. _`snd_soc_dapm_del_routes`:

snd_soc_dapm_del_routes
=======================

.. c:function:: int snd_soc_dapm_del_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Remove routes between DAPM widgets

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param route:
        audio routes
    :type route: const struct snd_soc_dapm_route \*

    :param num:
        number of routes
    :type num: int

.. _`snd_soc_dapm_del_routes.description`:

Description
-----------

Removes routes from the DAPM context.

.. _`snd_soc_dapm_weak_routes`:

snd_soc_dapm_weak_routes
========================

.. c:function:: int snd_soc_dapm_weak_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Mark routes between DAPM widgets as weak

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param route:
        audio routes
    :type route: const struct snd_soc_dapm_route \*

    :param num:
        number of routes
    :type num: int

.. _`snd_soc_dapm_weak_routes.description`:

Description
-----------

Mark existing routes matching those specified in the passed array
as being weak, meaning that they are ignored for the purpose of
power decisions.  The main intended use case is for sidetone paths
which couple audio between other independent paths if they are both
active in order to make the combination work better at the user
level but which aren't intended to be "used".

Note that CODEC drivers should not use this as sidetone type paths
can frequently also be used as bypass paths.

.. _`snd_soc_dapm_new_widgets`:

snd_soc_dapm_new_widgets
========================

.. c:function:: int snd_soc_dapm_new_widgets(struct snd_soc_card *card)

    add new dapm widgets

    :param card:
        card to be checked for new dapm widgets
    :type card: struct snd_soc_card \*

.. _`snd_soc_dapm_new_widgets.description`:

Description
-----------

Checks the codec for any new dapm widgets and creates them if found.

Returns 0 for success.

.. _`snd_soc_dapm_get_volsw`:

snd_soc_dapm_get_volsw
======================

.. c:function:: int snd_soc_dapm_get_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm mixer get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_get_volsw.description`:

Description
-----------

Callback to get the value of a dapm mixer control.

Returns 0 for success.

.. _`snd_soc_dapm_put_volsw`:

snd_soc_dapm_put_volsw
======================

.. c:function:: int snd_soc_dapm_put_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm mixer set callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_put_volsw.description`:

Description
-----------

Callback to set the value of a dapm mixer control.

Returns 0 for success.

.. _`snd_soc_dapm_get_enum_double`:

snd_soc_dapm_get_enum_double
============================

.. c:function:: int snd_soc_dapm_get_enum_double(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm enumerated double mixer get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_get_enum_double.description`:

Description
-----------

Callback to get the value of a dapm enumerated double mixer control.

Returns 0 for success.

.. _`snd_soc_dapm_put_enum_double`:

snd_soc_dapm_put_enum_double
============================

.. c:function:: int snd_soc_dapm_put_enum_double(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm enumerated double mixer set callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_put_enum_double.description`:

Description
-----------

Callback to set the value of a dapm enumerated double mixer control.

Returns 0 for success.

.. _`snd_soc_dapm_info_pin_switch`:

snd_soc_dapm_info_pin_switch
============================

.. c:function:: int snd_soc_dapm_info_pin_switch(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Info for a pin switch

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_dapm_info_pin_switch.description`:

Description
-----------

Callback to provide information about a pin switch control.

.. _`snd_soc_dapm_get_pin_switch`:

snd_soc_dapm_get_pin_switch
===========================

.. c:function:: int snd_soc_dapm_get_pin_switch(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Get information for a pin switch

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        Value
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_put_pin_switch`:

snd_soc_dapm_put_pin_switch
===========================

.. c:function:: int snd_soc_dapm_put_pin_switch(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Set information for a pin switch

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        Value
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_dapm_new_control`:

snd_soc_dapm_new_control
========================

.. c:function:: struct snd_soc_dapm_widget *snd_soc_dapm_new_control(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_widget *widget)

    create new dapm control

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param widget:
        widget template
    :type widget: const struct snd_soc_dapm_widget \*

.. _`snd_soc_dapm_new_control.description`:

Description
-----------

Creates new DAPM control based upon a template.

Returns a widget pointer on success or an error pointer on failure

.. _`snd_soc_dapm_new_controls`:

snd_soc_dapm_new_controls
=========================

.. c:function:: int snd_soc_dapm_new_controls(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_widget *widget, int num)

    create new dapm controls

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param widget:
        widget array
    :type widget: const struct snd_soc_dapm_widget \*

    :param num:
        number of widgets
    :type num: int

.. _`snd_soc_dapm_new_controls.description`:

Description
-----------

Creates new DAPM controls based upon the templates.

Returns 0 for success else error.

.. _`snd_soc_dapm_stream_event`:

snd_soc_dapm_stream_event
=========================

.. c:function:: void snd_soc_dapm_stream_event(struct snd_soc_pcm_runtime *rtd, int stream, int event)

    send a stream event to the dapm core

    :param rtd:
        PCM runtime data
    :type rtd: struct snd_soc_pcm_runtime \*

    :param stream:
        stream name
    :type stream: int

    :param event:
        stream event
    :type event: int

.. _`snd_soc_dapm_stream_event.description`:

Description
-----------

Sends a stream event to the dapm core. The core then makes any
necessary widget power changes.

Returns 0 for success else error.

.. _`snd_soc_dapm_enable_pin_unlocked`:

snd_soc_dapm_enable_pin_unlocked
================================

.. c:function:: int snd_soc_dapm_enable_pin_unlocked(struct snd_soc_dapm_context *dapm, const char *pin)

    enable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_enable_pin_unlocked.description`:

Description
-----------

Enables input/output pin and its parents or children widgets iff there is
a valid audio route and active audio stream.

Requires external locking.

.. _`snd_soc_dapm_enable_pin_unlocked.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_enable_pin`:

snd_soc_dapm_enable_pin
=======================

.. c:function:: int snd_soc_dapm_enable_pin(struct snd_soc_dapm_context *dapm, const char *pin)

    enable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_enable_pin.description`:

Description
-----------

Enables input/output pin and its parents or children widgets iff there is
a valid audio route and active audio stream.

.. _`snd_soc_dapm_enable_pin.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_force_enable_pin_unlocked`:

snd_soc_dapm_force_enable_pin_unlocked
======================================

.. c:function:: int snd_soc_dapm_force_enable_pin_unlocked(struct snd_soc_dapm_context *dapm, const char *pin)

    force a pin to be enabled

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_force_enable_pin_unlocked.description`:

Description
-----------

Enables input/output pin regardless of any other state.  This is
intended for use with microphone bias supplies used in microphone
jack detection.

Requires external locking.

.. _`snd_soc_dapm_force_enable_pin_unlocked.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_force_enable_pin`:

snd_soc_dapm_force_enable_pin
=============================

.. c:function:: int snd_soc_dapm_force_enable_pin(struct snd_soc_dapm_context *dapm, const char *pin)

    force a pin to be enabled

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_force_enable_pin.description`:

Description
-----------

Enables input/output pin regardless of any other state.  This is
intended for use with microphone bias supplies used in microphone
jack detection.

.. _`snd_soc_dapm_force_enable_pin.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_disable_pin_unlocked`:

snd_soc_dapm_disable_pin_unlocked
=================================

.. c:function:: int snd_soc_dapm_disable_pin_unlocked(struct snd_soc_dapm_context *dapm, const char *pin)

    disable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_disable_pin_unlocked.description`:

Description
-----------

Disables input/output pin and its parents or children widgets.

Requires external locking.

.. _`snd_soc_dapm_disable_pin_unlocked.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_disable_pin`:

snd_soc_dapm_disable_pin
========================

.. c:function:: int snd_soc_dapm_disable_pin(struct snd_soc_dapm_context *dapm, const char *pin)

    disable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_disable_pin.description`:

Description
-----------

Disables input/output pin and its parents or children widgets.

.. _`snd_soc_dapm_disable_pin.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_nc_pin_unlocked`:

snd_soc_dapm_nc_pin_unlocked
============================

.. c:function:: int snd_soc_dapm_nc_pin_unlocked(struct snd_soc_dapm_context *dapm, const char *pin)

    permanently disable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_nc_pin_unlocked.description`:

Description
-----------

Marks the specified pin as being not connected, disabling it along
any parent or child widgets.  At present this is identical to
\ :c:func:`snd_soc_dapm_disable_pin`\  but in future it will be extended to do
additional things such as disabling controls which only affect
paths through the pin.

Requires external locking.

.. _`snd_soc_dapm_nc_pin_unlocked.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_nc_pin`:

snd_soc_dapm_nc_pin
===================

.. c:function:: int snd_soc_dapm_nc_pin(struct snd_soc_dapm_context *dapm, const char *pin)

    permanently disable pin.

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        pin name
    :type pin: const char \*

.. _`snd_soc_dapm_nc_pin.description`:

Description
-----------

Marks the specified pin as being not connected, disabling it along
any parent or child widgets.  At present this is identical to
\ :c:func:`snd_soc_dapm_disable_pin`\  but in future it will be extended to do
additional things such as disabling controls which only affect
paths through the pin.

.. _`snd_soc_dapm_nc_pin.note`:

NOTE
----

\ :c:func:`snd_soc_dapm_sync`\  needs to be called after this for DAPM to
do any widget power switching.

.. _`snd_soc_dapm_get_pin_status`:

snd_soc_dapm_get_pin_status
===========================

.. c:function:: int snd_soc_dapm_get_pin_status(struct snd_soc_dapm_context *dapm, const char *pin)

    get audio pin status

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        audio signal pin endpoint (or start point)
    :type pin: const char \*

.. _`snd_soc_dapm_get_pin_status.description`:

Description
-----------

Get audio pin status - connected or disconnected.

Returns 1 for connected otherwise 0.

.. _`snd_soc_dapm_ignore_suspend`:

snd_soc_dapm_ignore_suspend
===========================

.. c:function:: int snd_soc_dapm_ignore_suspend(struct snd_soc_dapm_context *dapm, const char *pin)

    ignore suspend status for DAPM endpoint

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

    :param pin:
        audio signal pin endpoint (or start point)
    :type pin: const char \*

.. _`snd_soc_dapm_ignore_suspend.description`:

Description
-----------

Mark the given endpoint or pin as ignoring suspend.  When the
system is disabled a path between two endpoints flagged as ignoring
suspend will not be disabled.  The path must already be enabled via
normal means at suspend time, it will not be turned on if it was not
already enabled.

.. _`snd_soc_dapm_free`:

snd_soc_dapm_free
=================

.. c:function:: void snd_soc_dapm_free(struct snd_soc_dapm_context *dapm)

    free dapm resources

    :param dapm:
        DAPM context
    :type dapm: struct snd_soc_dapm_context \*

.. _`snd_soc_dapm_free.description`:

Description
-----------

Free all dapm widgets and resources.

.. This file was automatic generated / don't edit.

