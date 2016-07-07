.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/soc-dapm.h

.. _`snd_soc_dapm_init_bias_level`:

snd_soc_dapm_init_bias_level
============================

.. c:function:: void snd_soc_dapm_init_bias_level(struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level)

    Initialize DAPM bias level

    :param struct snd_soc_dapm_context \*dapm:
        The DAPM context to initialize

    :param enum snd_soc_bias_level level:
        The DAPM level to initialize to

.. _`snd_soc_dapm_init_bias_level.description`:

Description
-----------

This function only sets the driver internal state of the DAPM level and will
not modify the state of the device. Hence it should not be used during normal
operation, but only to synchronize the internal state to the device state.
E.g. during driver probe to set the DAPM level to the one corresponding with
the power-on reset state of the device.

To change the DAPM state of the device use \ :c:func:`snd_soc_dapm_set_bias_level`\ .

.. _`snd_soc_dapm_get_bias_level`:

snd_soc_dapm_get_bias_level
===========================

.. c:function:: enum snd_soc_bias_level snd_soc_dapm_get_bias_level(struct snd_soc_dapm_context *dapm)

    Get current DAPM bias level

    :param struct snd_soc_dapm_context \*dapm:
        The context for which to get the bias level

.. _`snd_soc_dapm_get_bias_level.return`:

Return
------

The current bias level of the passed DAPM context.

.. _`snd_soc_dapm_widget_for_each_path`:

snd_soc_dapm_widget_for_each_path
=================================

.. c:function::  snd_soc_dapm_widget_for_each_path( w,  dir,  p)

    Iterates over all paths in the specified direction of a widget

    :param  w:
        The widget

    :param  dir:
        Whether to iterate over the paths where the specified widget is the
        incoming or outgoing widgets

    :param  p:
        The path iterator variable

.. _`snd_soc_dapm_widget_for_each_path_safe`:

snd_soc_dapm_widget_for_each_path_safe
======================================

.. c:function::  snd_soc_dapm_widget_for_each_path_safe( w,  dir,  p,  next_p)

    Iterates over all paths in the specified direction of a widget

    :param  w:
        The widget

    :param  dir:
        Whether to iterate over the paths where the specified widget is the
        incoming or outgoing widgets

    :param  p:
        The path iterator variable

    :param  next_p:
        Temporary storage for the next path

.. _`snd_soc_dapm_widget_for_each_path_safe.description`:

Description
-----------

This function works like snd_soc_dapm_widget_for_each_sink_path, expect that
it is safe to remove the current path from the list while iterating

.. _`snd_soc_dapm_widget_for_each_sink_path`:

snd_soc_dapm_widget_for_each_sink_path
======================================

.. c:function::  snd_soc_dapm_widget_for_each_sink_path( w,  p)

    Iterates over all paths leaving a widget

    :param  w:
        The widget

    :param  p:
        The path iterator variable

.. _`snd_soc_dapm_widget_for_each_source_path`:

snd_soc_dapm_widget_for_each_source_path
========================================

.. c:function::  snd_soc_dapm_widget_for_each_source_path( w,  p)

    Iterates over all paths leading to a widget

    :param  w:
        The widget

    :param  p:
        The path iterator variable

.. This file was automatic generated / don't edit.

