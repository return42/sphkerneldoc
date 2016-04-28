.. -*- coding: utf-8; mode: rst -*-

.. _API-SNDRV-COMPRESS-IOCTL-VERSION:

============================
SNDRV_COMPRESS_IOCTL_VERSION
============================

*man SNDRV_COMPRESS_IOCTL_VERSION(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: SNDRV_COMPRESS_IOCTL_VERSION(  )

Arguments
=========

None


SNDRV_COMPRESS_GET_CAPS
=======================

Query capability of DSP


SNDRV_COMPRESS_GET_CODEC_CAPS
=============================

Query capability of a codec


SNDRV_COMPRESS_SET_PARAMS
=========================

Set codec and stream parameters


Note
====

only codec params can be changed runtime and stream params cant be


SNDRV_COMPRESS_GET_PARAMS
=========================

Query codec params


SNDRV_COMPRESS_TSTAMP
=====================

get the current timestamp value


SNDRV_COMPRESS_AVAIL
====================

get the current buffer avail value. This also queries the tstamp
properties


SNDRV_COMPRESS_PAUSE
====================

Pause the running stream


SNDRV_COMPRESS_RESUME
=====================

resume a paused stream


SNDRV_COMPRESS_START
====================

Start a stream


SNDRV_COMPRESS_STOP
===================

stop a running stream, discarding ring buffer content and the buffers
currently with DSP


SNDRV_COMPRESS_DRAIN
====================

Play till end of buffers and stop after that


SNDRV_COMPRESS_IOCTL_VERSION
============================

Query the API version


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
