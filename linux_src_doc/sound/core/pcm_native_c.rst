.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_native.c

.. _`snd_pcm_stream_lock`:

snd_pcm_stream_lock
===================

.. c:function:: void snd_pcm_stream_lock(struct snd_pcm_substream *substream)

    Lock the PCM stream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_lock.description`:

Description
-----------

This locks the PCM stream's spinlock or mutex depending on the nonatomic
flag of the given substream.  This also takes the global link rw lock
(or rw sem), too, for avoiding the race with linked streams.

.. _`snd_pcm_stream_unlock`:

snd_pcm_stream_unlock
=====================

.. c:function:: void snd_pcm_stream_unlock(struct snd_pcm_substream *substream)

    Unlock the PCM stream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_unlock.description`:

Description
-----------

This unlocks the PCM stream that has been locked via \ :c:func:`snd_pcm_stream_lock`\ .

.. _`snd_pcm_stream_lock_irq`:

snd_pcm_stream_lock_irq
=======================

.. c:function:: void snd_pcm_stream_lock_irq(struct snd_pcm_substream *substream)

    Lock the PCM stream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_lock_irq.description`:

Description
-----------

This locks the PCM stream like \ :c:func:`snd_pcm_stream_lock`\  and disables the local
IRQ (only when nonatomic is false).  In nonatomic case, this is identical
as \ :c:func:`snd_pcm_stream_lock`\ .

.. _`snd_pcm_stream_unlock_irq`:

snd_pcm_stream_unlock_irq
=========================

.. c:function:: void snd_pcm_stream_unlock_irq(struct snd_pcm_substream *substream)

    Unlock the PCM stream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_unlock_irq.description`:

Description
-----------

This is a counter-part of \ :c:func:`snd_pcm_stream_lock_irq`\ .

.. _`snd_pcm_stream_unlock_irqrestore`:

snd_pcm_stream_unlock_irqrestore
================================

.. c:function:: void snd_pcm_stream_unlock_irqrestore(struct snd_pcm_substream *substream, unsigned long flags)

    Unlock the PCM stream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param flags:
        irq flags
    :type flags: unsigned long

.. _`snd_pcm_stream_unlock_irqrestore.description`:

Description
-----------

This is a counter-part of \ :c:func:`snd_pcm_stream_lock_irqsave`\ .

.. _`snd_pcm_hw_params_choose`:

snd_pcm_hw_params_choose
========================

.. c:function:: int snd_pcm_hw_params_choose(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params)

    choose a configuration defined by \ ``params``\ 

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

.. _`snd_pcm_hw_params_choose.description`:

Description
-----------

Choose one configuration from configuration space defined by \ ``params``\ .

.. _`snd_pcm_hw_params_choose.the-configuration-chosen-is-that-obtained-fixing-in-this-order`:

The configuration chosen is that obtained fixing in this order
--------------------------------------------------------------

first access, first format, first subformat, min channels,
min rate, min period time, max buffer size, min tick time

.. _`snd_pcm_hw_params_choose.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_start`:

snd_pcm_start
=============

.. c:function:: int snd_pcm_start(struct snd_pcm_substream *substream)

    start all linked streams

    :param substream:
        the PCM substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_start.return`:

Return
------

Zero if successful, or a negative error code.
The stream lock must be acquired before calling this function.

.. _`snd_pcm_stop`:

snd_pcm_stop
============

.. c:function:: int snd_pcm_stop(struct snd_pcm_substream *substream, snd_pcm_state_t state)

    try to stop all running streams in the substream group

    :param substream:
        the PCM substream instance
    :type substream: struct snd_pcm_substream \*

    :param state:
        PCM state after stopping the stream
    :type state: snd_pcm_state_t

.. _`snd_pcm_stop.description`:

Description
-----------

The state of each stream is then changed to the given state unconditionally.

.. _`snd_pcm_stop.return`:

Return
------

Zero if successful, or a negative error code.

.. _`snd_pcm_drain_done`:

snd_pcm_drain_done
==================

.. c:function:: int snd_pcm_drain_done(struct snd_pcm_substream *substream)

    stop the DMA only when the given stream is playback

    :param substream:
        the PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_drain_done.description`:

Description
-----------

After stopping, the state is changed to SETUP.
Unlike \ :c:func:`snd_pcm_stop`\ , this affects only the given stream.

.. _`snd_pcm_drain_done.return`:

Return
------

Zero if succesful, or a negative error code.

.. _`snd_pcm_stop_xrun`:

snd_pcm_stop_xrun
=================

.. c:function:: int snd_pcm_stop_xrun(struct snd_pcm_substream *substream)

    stop the running streams as XRUN

    :param substream:
        the PCM substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stop_xrun.description`:

Description
-----------

This stops the given running substream (and all linked substreams) as XRUN.
Unlike \ :c:func:`snd_pcm_stop`\ , this function takes the substream lock by itself.

.. _`snd_pcm_stop_xrun.return`:

Return
------

Zero if successful, or a negative error code.

.. _`snd_pcm_suspend`:

snd_pcm_suspend
===============

.. c:function:: int snd_pcm_suspend(struct snd_pcm_substream *substream)

    trigger SUSPEND to all linked streams

    :param substream:
        the PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_suspend.description`:

Description
-----------

After this call, all streams are changed to SUSPENDED state.

.. _`snd_pcm_suspend.return`:

Return
------

Zero if successful (or \ ``substream``\  is \ ``NULL``\ ), or a negative error
code.

.. _`snd_pcm_suspend_all`:

snd_pcm_suspend_all
===================

.. c:function:: int snd_pcm_suspend_all(struct snd_pcm *pcm)

    trigger SUSPEND to all substreams in the given pcm

    :param pcm:
        the PCM instance
    :type pcm: struct snd_pcm \*

.. _`snd_pcm_suspend_all.description`:

Description
-----------

After this call, all streams are changed to SUSPENDED state.

.. _`snd_pcm_suspend_all.return`:

Return
------

Zero if successful (or \ ``pcm``\  is \ ``NULL``\ ), or a negative error code.

.. _`snd_pcm_prepare`:

snd_pcm_prepare
===============

.. c:function:: int snd_pcm_prepare(struct snd_pcm_substream *substream, struct file *file)

    prepare the PCM substream to be triggerable

    :param substream:
        the PCM substream instance
    :type substream: struct snd_pcm_substream \*

    :param file:
        file to refer f_flags
    :type file: struct file \*

.. _`snd_pcm_prepare.return`:

Return
------

Zero if successful, or a negative error code.

.. _`snd_pcm_kernel_ioctl`:

snd_pcm_kernel_ioctl
====================

.. c:function:: int snd_pcm_kernel_ioctl(struct snd_pcm_substream *substream, unsigned int cmd, void *arg)

    Execute PCM ioctl in the kernel-space

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        IOCTL cmd
    :type cmd: unsigned int

    :param arg:
        IOCTL argument
    :type arg: void \*

.. _`snd_pcm_kernel_ioctl.description`:

Description
-----------

The function is provided primarily for OSS layer and USB gadget drivers,
and it allows only the limited set of ioctls (hw_params, sw_params,
prepare, start, drain, drop, forward).

.. _`snd_pcm_lib_default_mmap`:

snd_pcm_lib_default_mmap
========================

.. c:function:: int snd_pcm_lib_default_mmap(struct snd_pcm_substream *substream, struct vm_area_struct *area)

    Default PCM data mmap function

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param area:
        VMA
    :type area: struct vm_area_struct \*

.. _`snd_pcm_lib_default_mmap.description`:

Description
-----------

This is the default mmap handler for PCM data.  When mmap pcm_ops is NULL,
this function is invoked implicitly.

.. _`snd_pcm_lib_mmap_iomem`:

snd_pcm_lib_mmap_iomem
======================

.. c:function:: int snd_pcm_lib_mmap_iomem(struct snd_pcm_substream *substream, struct vm_area_struct *area)

    Default PCM data mmap function for I/O mem

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param area:
        VMA
    :type area: struct vm_area_struct \*

.. _`snd_pcm_lib_mmap_iomem.description`:

Description
-----------

When your hardware uses the iomapped pages as the hardware buffer and
wants to mmap it, pass this function as mmap pcm_ops.  Note that this
is supposed to work only on limited architectures.

.. This file was automatic generated / don't edit.

