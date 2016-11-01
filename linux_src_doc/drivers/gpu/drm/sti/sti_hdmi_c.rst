.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_hdmi.c

.. _`hdmi_irq_thread`:

hdmi_irq_thread
===============

.. c:function:: irqreturn_t hdmi_irq_thread(int irq, void *arg)

    :param int irq:
        irq number

    :param void \*arg:
        connector structure

.. _`hdmi_irq`:

hdmi_irq
========

.. c:function:: irqreturn_t hdmi_irq(int irq, void *arg)

    :param int irq:
        irq number

    :param void \*arg:
        connector structure

.. _`hdmi_active_area`:

hdmi_active_area
================

.. c:function:: void hdmi_active_area(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`hdmi_config`:

hdmi_config
===========

.. c:function:: void hdmi_config(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`hdmi_infoframe_subpack`:

hdmi_infoframe_subpack
======================

.. c:function:: unsigned int hdmi_infoframe_subpack(const u8 *ptr, size_t size)

    :param const u8 \*ptr:
        pointer on the hdmi internal structure

    :param size_t size:
        size to write

.. _`hdmi_infoframe_write_infopack`:

hdmi_infoframe_write_infopack
=============================

.. c:function:: void hdmi_infoframe_write_infopack(struct sti_hdmi *hdmi, const u8 *data, size_t size)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

    :param const u8 \*data:
        infoframe to write

    :param size_t size:
        size to write

.. _`hdmi_avi_infoframe_config`:

hdmi_avi_infoframe_config
=========================

.. c:function:: int hdmi_avi_infoframe_config(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`hdmi_avi_infoframe_config.description`:

Description
-----------

AVI infoframe are transmitted at least once per two video field and
contains information about HDMI transmission mode such as color space,
colorimetry, ...

Return negative value if error occurs

.. _`hdmi_audio_infoframe_config`:

hdmi_audio_infoframe_config
===========================

.. c:function:: int hdmi_audio_infoframe_config(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`hdmi_audio_infoframe_config.description`:

Description
-----------

AUDIO infoframe are transmitted once per frame and
contains information about HDMI transmission mode such as audio codec,
sample size, ...

Return negative value if error occurs

.. _`hdmi_timeout_swreset`:

HDMI_TIMEOUT_SWRESET
====================

.. c:function::  HDMI_TIMEOUT_SWRESET()

.. _`sti_hdmi_audio_get_non_coherent_n`:

sti_hdmi_audio_get_non_coherent_n
=================================

.. c:function:: int sti_hdmi_audio_get_non_coherent_n(unsigned int audio_fs)

    get N parameter for non-coherent clocks. None-coherent clocks means that audio and TMDS clocks have not the same source (drifts between clocks). In this case assumption is that CTS is automatically calculated by hardware.

    :param unsigned int audio_fs:
        audio frame clock frequency in Hz

.. _`sti_hdmi_audio_get_non_coherent_n.description`:

Description
-----------

Values computed are based on table described in HDMI specification 1.4b

Returns n value.

.. This file was automatic generated / don't edit.

