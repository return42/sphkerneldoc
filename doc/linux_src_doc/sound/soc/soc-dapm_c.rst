.. -*- coding: utf-8; mode: rst -*-

==========
soc-dapm.c
==========

.. _`snd_soc_dapm_kcontrol_widget`:

snd_soc_dapm_kcontrol_widget
============================

.. c:function:: struct snd_soc_dapm_widget *snd_soc_dapm_kcontrol_widget (struct snd_kcontrol *kcontrol)

    Returns the widget associated to a kcontrol

    :param struct snd_kcontrol \*kcontrol:
        The kcontrol


.. _`snd_soc_dapm_kcontrol_dapm`:

snd_soc_dapm_kcontrol_dapm
==========================

.. c:function:: struct snd_soc_dapm_context *snd_soc_dapm_kcontrol_dapm (struct snd_kcontrol *kcontrol)

    Returns the dapm context associated to a kcontrol

    :param struct snd_kcontrol \*kcontrol:
        The kcontrol


.. _`snd_soc_dapm_kcontrol_dapm.description`:

Description
-----------

Note: This function must only be used on kcontrols that are known to have
been registered for a CODEC. Otherwise the behaviour is undefined.


.. _`snd_soc_dapm_force_bias_level`:

snd_soc_dapm_force_bias_level
=============================

.. c:function:: int snd_soc_dapm_force_bias_level (struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level)

    Sets the DAPM bias level

    :param struct snd_soc_dapm_context \*dapm:
        The DAPM context for which to set the level

    :param enum snd_soc_bias_level level:
        The level to set


.. _`snd_soc_dapm_force_bias_level.description`:

Description
-----------

Forces the DAPM bias level to a specific state. It will call the bias level
callback of DAPM context with the specified level. This will even happen if
the context is already at the same level. Furthermore it will not go through
the normal bias level sequencing, meaning any intermediate states between the
current and the target state will not be entered.

Note that the change in bias level is only temporary and the next time
:c:func:`snd_soc_dapm_sync` is called the state will be set to the level as
determined by the DAPM core. The function is mainly intended to be used to
used during probe or resume from suspend to power up the device so
initialization can be done, before the DAPM core takes over.


.. _`snd_soc_dapm_set_bias_level`:

snd_soc_dapm_set_bias_level
===========================

.. c:function:: int snd_soc_dapm_set_bias_level (struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level)

    set the bias level for the system

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param enum snd_soc_bias_level level:
        level to configure


.. _`snd_soc_dapm_set_bias_level.description`:

Description
-----------

Configure the bias (power) levels for the SoC audio device.

Returns 0 for success else error.


.. _`snd_soc_dapm_dai_get_connected_widgets`:

snd_soc_dapm_dai_get_connected_widgets
======================================

.. c:function:: int snd_soc_dapm_dai_get_connected_widgets (struct snd_soc_dai *dai, int stream, struct snd_soc_dapm_widget_list **list)

    query audio path and it's widgets.

    :param struct snd_soc_dai \*dai:
        the soc DAI.

    :param int stream:
        stream direction.

    :param struct snd_soc_dapm_widget_list \*\*list:
        list of active widgets for this stream.


.. _`snd_soc_dapm_dai_get_connected_widgets.description`:

Description
-----------

Queries DAPM graph as to whether an valid audio stream path exists for
the initial stream specified by name. This takes into account
current mixer and mux kcontrol settings. Creates list of valid widgets.

Returns the number of valid paths or negative error.


.. _`snd_soc_dapm_sync_unlocked`:

snd_soc_dapm_sync_unlocked
==========================

.. c:function:: int snd_soc_dapm_sync_unlocked (struct snd_soc_dapm_context *dapm)

    scan and power dapm paths

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context


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

.. c:function:: int snd_soc_dapm_sync (struct snd_soc_dapm_context *dapm)

    scan and power dapm paths

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context


.. _`snd_soc_dapm_sync.description`:

Description
-----------

Walks all dapm audio paths and powers widgets according to their
stream or path usage.

Returns 0 for success.


.. _`snd_soc_dapm_add_routes`:

snd_soc_dapm_add_routes
=======================

.. c:function:: int snd_soc_dapm_add_routes (struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Add routes between DAPM widgets

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const struct snd_soc_dapm_route \*route:
        audio routes

    :param int num:
        number of routes


.. _`snd_soc_dapm_add_routes.description`:

Description
-----------

Connects 2 dapm widgets together via a named audio path. The sink is
the widget receiving the audio signal, whilst the source is the sender
of the audio signal.

Returns 0 for success else error. On error all resources can be freed
with a call to :c:func:`snd_soc_card_free`.


.. _`snd_soc_dapm_del_routes`:

snd_soc_dapm_del_routes
=======================

.. c:function:: int snd_soc_dapm_del_routes (struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Remove routes between DAPM widgets

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const struct snd_soc_dapm_route \*route:
        audio routes

    :param int num:
        number of routes


.. _`snd_soc_dapm_del_routes.description`:

Description
-----------

Removes routes from the DAPM context.


.. _`snd_soc_dapm_weak_routes`:

snd_soc_dapm_weak_routes
========================

.. c:function:: int snd_soc_dapm_weak_routes (struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num)

    Mark routes between DAPM widgets as weak

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const struct snd_soc_dapm_route \*route:
        audio routes

    :param int num:
        number of routes


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

.. c:function:: int snd_soc_dapm_new_widgets (struct snd_soc_card *card)

    add new dapm widgets

    :param struct snd_soc_card \*card:
        card to be checked for new dapm widgets


.. _`snd_soc_dapm_new_widgets.description`:

Description
-----------

Checks the codec for any new dapm widgets and creates them if found.

Returns 0 for success.


.. _`snd_soc_dapm_get_volsw`:

snd_soc_dapm_get_volsw
======================

.. c:function:: int snd_soc_dapm_get_volsw (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm mixer get callback

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        control element information


.. _`snd_soc_dapm_get_volsw.description`:

Description
-----------

Callback to get the value of a dapm mixer control.

Returns 0 for success.


.. _`snd_soc_dapm_put_volsw`:

snd_soc_dapm_put_volsw
======================

.. c:function:: int snd_soc_dapm_put_volsw (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm mixer set callback

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        control element information


.. _`snd_soc_dapm_put_volsw.description`:

Description
-----------

Callback to set the value of a dapm mixer control.

Returns 0 for success.


.. _`snd_soc_dapm_get_enum_double`:

snd_soc_dapm_get_enum_double
============================

.. c:function:: int snd_soc_dapm_get_enum_double (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm enumerated double mixer get callback

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        control element information


.. _`snd_soc_dapm_get_enum_double.description`:

Description
-----------

Callback to get the value of a dapm enumerated double mixer control.

Returns 0 for success.


.. _`snd_soc_dapm_put_enum_double`:

snd_soc_dapm_put_enum_double
============================

.. c:function:: int snd_soc_dapm_put_enum_double (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    dapm enumerated double mixer set callback

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        control element information


.. _`snd_soc_dapm_put_enum_double.description`:

Description
-----------

Callback to set the value of a dapm enumerated double mixer control.

Returns 0 for success.


.. _`snd_soc_dapm_info_pin_switch`:

snd_soc_dapm_info_pin_switch
============================

.. c:function:: int snd_soc_dapm_info_pin_switch (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Info for a pin switch

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_info \*uinfo:
        control element information


.. _`snd_soc_dapm_info_pin_switch.description`:

Description
-----------

Callback to provide information about a pin switch control.


.. _`snd_soc_dapm_get_pin_switch`:

snd_soc_dapm_get_pin_switch
===========================

.. c:function:: int snd_soc_dapm_get_pin_switch (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Get information for a pin switch

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        Value


.. _`snd_soc_dapm_put_pin_switch`:

snd_soc_dapm_put_pin_switch
===========================

.. c:function:: int snd_soc_dapm_put_pin_switch (struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Set information for a pin switch

    :param struct snd_kcontrol \*kcontrol:
        mixer control

    :param struct snd_ctl_elem_value \*ucontrol:
        Value


.. _`snd_soc_dapm_new_controls`:

snd_soc_dapm_new_controls
=========================

.. c:function:: int snd_soc_dapm_new_controls (struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_widget *widget, int num)

    create new dapm controls

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const struct snd_soc_dapm_widget \*widget:
        widget array

    :param int num:
        number of widgets


.. _`snd_soc_dapm_new_controls.description`:

Description
-----------

Creates new DAPM controls based upon the templates.

Returns 0 for success else error.


.. _`snd_soc_dapm_stream_event`:

snd_soc_dapm_stream_event
=========================

.. c:function:: void snd_soc_dapm_stream_event (struct snd_soc_pcm_runtime *rtd, int stream, int event)

    send a stream event to the dapm core

    :param struct snd_soc_pcm_runtime \*rtd:
        PCM runtime data

    :param int stream:
        stream name

    :param int event:
        stream event


.. _`snd_soc_dapm_stream_event.description`:

Description
-----------

Sends a stream event to the dapm core. The core then makes any
necessary widget power changes.

Returns 0 for success else error.


.. _`snd_soc_dapm_enable_pin_unlocked`:

snd_soc_dapm_enable_pin_unlocked
================================

.. c:function:: int snd_soc_dapm_enable_pin_unlocked (struct snd_soc_dapm_context *dapm, const char *pin)

    enable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_enable_pin_unlocked.description`:

Description
-----------

Enables input/output pin and its parents or children widgets iff there is
a valid audio route and active audio stream.

Requires external locking.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_enable_pin`:

snd_soc_dapm_enable_pin
=======================

.. c:function:: int snd_soc_dapm_enable_pin (struct snd_soc_dapm_context *dapm, const char *pin)

    enable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_enable_pin.description`:

Description
-----------

Enables input/output pin and its parents or children widgets iff there is
a valid audio route and active audio stream.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_force_enable_pin_unlocked`:

snd_soc_dapm_force_enable_pin_unlocked
======================================

.. c:function:: int snd_soc_dapm_force_enable_pin_unlocked (struct snd_soc_dapm_context *dapm, const char *pin)

    force a pin to be enabled

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_force_enable_pin_unlocked.description`:

Description
-----------

Enables input/output pin regardless of any other state.  This is
intended for use with microphone bias supplies used in microphone
jack detection.

Requires external locking.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_force_enable_pin`:

snd_soc_dapm_force_enable_pin
=============================

.. c:function:: int snd_soc_dapm_force_enable_pin (struct snd_soc_dapm_context *dapm, const char *pin)

    force a pin to be enabled

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_force_enable_pin.description`:

Description
-----------

Enables input/output pin regardless of any other state.  This is
intended for use with microphone bias supplies used in microphone
jack detection.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_disable_pin_unlocked`:

snd_soc_dapm_disable_pin_unlocked
=================================

.. c:function:: int snd_soc_dapm_disable_pin_unlocked (struct snd_soc_dapm_context *dapm, const char *pin)

    disable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_disable_pin_unlocked.description`:

Description
-----------

Disables input/output pin and its parents or children widgets.

Requires external locking.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_disable_pin`:

snd_soc_dapm_disable_pin
========================

.. c:function:: int snd_soc_dapm_disable_pin (struct snd_soc_dapm_context *dapm, const char *pin)

    disable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_disable_pin.description`:

Description
-----------

Disables input/output pin and its parents or children widgets.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_nc_pin_unlocked`:

snd_soc_dapm_nc_pin_unlocked
============================

.. c:function:: int snd_soc_dapm_nc_pin_unlocked (struct snd_soc_dapm_context *dapm, const char *pin)

    permanently disable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_nc_pin_unlocked.description`:

Description
-----------

Marks the specified pin as being not connected, disabling it along
any parent or child widgets.  At present this is identical to
:c:func:`snd_soc_dapm_disable_pin` but in future it will be extended to do
additional things such as disabling controls which only affect
paths through the pin.

Requires external locking.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_nc_pin`:

snd_soc_dapm_nc_pin
===================

.. c:function:: int snd_soc_dapm_nc_pin (struct snd_soc_dapm_context *dapm, const char *pin)

    permanently disable pin.

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        pin name


.. _`snd_soc_dapm_nc_pin.description`:

Description
-----------

Marks the specified pin as being not connected, disabling it along
any parent or child widgets.  At present this is identical to
:c:func:`snd_soc_dapm_disable_pin` but in future it will be extended to do
additional things such as disabling controls which only affect
paths through the pin.

NOTE: :c:func:`snd_soc_dapm_sync` needs to be called after this for DAPM to
do any widget power switching.


.. _`snd_soc_dapm_get_pin_status`:

snd_soc_dapm_get_pin_status
===========================

.. c:function:: int snd_soc_dapm_get_pin_status (struct snd_soc_dapm_context *dapm, const char *pin)

    get audio pin status

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        audio signal pin endpoint (or start point)


.. _`snd_soc_dapm_get_pin_status.description`:

Description
-----------

Get audio pin status - connected or disconnected.

Returns 1 for connected otherwise 0.


.. _`snd_soc_dapm_ignore_suspend`:

snd_soc_dapm_ignore_suspend
===========================

.. c:function:: int snd_soc_dapm_ignore_suspend (struct snd_soc_dapm_context *dapm, const char *pin)

    ignore suspend status for DAPM endpoint

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context

    :param const char \*pin:
        audio signal pin endpoint (or start point)


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

.. c:function:: void snd_soc_dapm_free (struct snd_soc_dapm_context *dapm)

    free dapm resources

    :param struct snd_soc_dapm_context \*dapm:
        DAPM context


.. _`snd_soc_dapm_free.description`:

Description
-----------

Free all dapm widgets and resources.

