.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/usb/endpoint.c

.. _`snd_usb_endpoint_implicit_feedback_sink`:

snd_usb_endpoint_implicit_feedback_sink
=======================================

.. c:function:: int snd_usb_endpoint_implicit_feedback_sink(struct snd_usb_endpoint *ep)

    Report endpoint usage type

    :param ep:
        The snd_usb_endpoint
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_implicit_feedback_sink.description`:

Description
-----------

Determine whether an endpoint is driven by an implicit feedback
data endpoint source.

.. _`snd_usb_add_endpoint`:

snd_usb_add_endpoint
====================

.. c:function:: struct snd_usb_endpoint *snd_usb_add_endpoint(struct snd_usb_audio *chip, struct usb_host_interface *alts, int ep_num, int direction, int type)

    Add an endpoint to an USB audio chip

    :param chip:
        The chip
    :type chip: struct snd_usb_audio \*

    :param alts:
        The USB host interface
    :type alts: struct usb_host_interface \*

    :param ep_num:
        The number of the endpoint to use
    :type ep_num: int

    :param direction:
        SNDRV_PCM_STREAM_PLAYBACK or SNDRV_PCM_STREAM_CAPTURE
    :type direction: int

    :param type:
        SND_USB_ENDPOINT_TYPE_DATA or SND_USB_ENDPOINT_TYPE_SYNC
    :type type: int

.. _`snd_usb_add_endpoint.description`:

Description
-----------

If the requested endpoint has not been added to the given chip before,
a new instance is created. Otherwise, a pointer to the previoulsy
created instance is returned. In case of any error, NULL is returned.

New endpoints will be added to chip->ep_list and must be freed by
calling \ :c:func:`snd_usb_endpoint_free`\ .

For SND_USB_ENDPOINT_TYPE_SYNC, the caller needs to guarantee that
bNumEndpoints > 1 beforehand.

.. _`snd_usb_endpoint_set_params`:

snd_usb_endpoint_set_params
===========================

.. c:function:: int snd_usb_endpoint_set_params(struct snd_usb_endpoint *ep, snd_pcm_format_t pcm_format, unsigned int channels, unsigned int period_bytes, unsigned int period_frames, unsigned int buffer_periods, unsigned int rate, struct audioformat *fmt, struct snd_usb_endpoint *sync_ep)

    configure an snd_usb_endpoint

    :param ep:
        the snd_usb_endpoint to configure
    :type ep: struct snd_usb_endpoint \*

    :param pcm_format:
        the audio fomat.
    :type pcm_format: snd_pcm_format_t

    :param channels:
        the number of audio channels.
    :type channels: unsigned int

    :param period_bytes:
        the number of bytes in one alsa period.
    :type period_bytes: unsigned int

    :param period_frames:
        the number of frames in one alsa period.
    :type period_frames: unsigned int

    :param buffer_periods:
        the number of periods in one alsa buffer.
    :type buffer_periods: unsigned int

    :param rate:
        the frame rate.
    :type rate: unsigned int

    :param fmt:
        the USB audio format information
    :type fmt: struct audioformat \*

    :param sync_ep:
        the sync endpoint to use, if any
    :type sync_ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_set_params.description`:

Description
-----------

Determine the number of URBs to be used on this endpoint.
An endpoint must be configured before it can be started.
An endpoint that is already running can not be reconfigured.

.. _`snd_usb_endpoint_start`:

snd_usb_endpoint_start
======================

.. c:function:: int snd_usb_endpoint_start(struct snd_usb_endpoint *ep)

    start an snd_usb_endpoint

    :param ep:
        the endpoint to start
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_start.description`:

Description
-----------

A call to this function will increment the use count of the endpoint.
In case it is not already running, the URBs for this endpoint will be
submitted. Otherwise, this function does nothing.

Must be balanced to calls of \ :c:func:`snd_usb_endpoint_stop`\ .

Returns an error if the URB submission failed, 0 in all other cases.

.. _`snd_usb_endpoint_stop`:

snd_usb_endpoint_stop
=====================

.. c:function:: void snd_usb_endpoint_stop(struct snd_usb_endpoint *ep)

    stop an snd_usb_endpoint

    :param ep:
        the endpoint to stop (may be NULL)
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_stop.description`:

Description
-----------

A call to this function will decrement the use count of the endpoint.
In case the last user has requested the endpoint stop, the URBs will
actually be deactivated.

Must be balanced to calls of \ :c:func:`snd_usb_endpoint_start`\ .

The caller needs to synchronize the pending stop operation via
\ :c:func:`snd_usb_endpoint_sync_pending_stop`\ .

.. _`snd_usb_endpoint_deactivate`:

snd_usb_endpoint_deactivate
===========================

.. c:function:: void snd_usb_endpoint_deactivate(struct snd_usb_endpoint *ep)

    deactivate an snd_usb_endpoint

    :param ep:
        the endpoint to deactivate
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_deactivate.description`:

Description
-----------

If the endpoint is not currently in use, this functions will
deactivate its associated URBs.

In case of any active users, this functions does nothing.

.. _`snd_usb_endpoint_release`:

snd_usb_endpoint_release
========================

.. c:function:: void snd_usb_endpoint_release(struct snd_usb_endpoint *ep)

    Tear down an snd_usb_endpoint

    :param ep:
        the endpoint to release
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_release.description`:

Description
-----------

This function does not care for the endpoint's use count but will tear
down all the streaming URBs immediately.

.. _`snd_usb_endpoint_free`:

snd_usb_endpoint_free
=====================

.. c:function:: void snd_usb_endpoint_free(struct snd_usb_endpoint *ep)

    Free the resources of an snd_usb_endpoint

    :param ep:
        the endpoint to free
    :type ep: struct snd_usb_endpoint \*

.. _`snd_usb_endpoint_free.description`:

Description
-----------

This free all resources of the given ep.

.. _`snd_usb_handle_sync_urb`:

snd_usb_handle_sync_urb
=======================

.. c:function:: void snd_usb_handle_sync_urb(struct snd_usb_endpoint *ep, struct snd_usb_endpoint *sender, const struct urb *urb)

    parse an USB sync packet

    :param ep:
        the endpoint to handle the packet
    :type ep: struct snd_usb_endpoint \*

    :param sender:
        the sending endpoint
    :type sender: struct snd_usb_endpoint \*

    :param urb:
        the received packet
    :type urb: const struct urb \*

.. _`snd_usb_handle_sync_urb.description`:

Description
-----------

This function is called from the context of an endpoint that received
the packet and is used to let another endpoint object handle the payload.

.. This file was automatic generated / don't edit.

