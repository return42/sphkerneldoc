.. -*- coding: utf-8; mode: rst -*-

============
pcm_native.c
============

.. _`snd_pcm_stream_lock`:

snd_pcm_stream_lock
===================

.. c:function:: void snd_pcm_stream_lock (struct snd_pcm_substream *substream)

    Lock the PCM stream

    :param struct snd_pcm_substream \*substream:
        PCM substream


.. _`snd_pcm_stream_lock.description`:

Description
-----------

This locks the PCM stream's spinlock or mutex depending on the nonatomic
flag of the given substream.  This also takes the global link rw lock
(or rw sem), too, for avoiding the race with linked streams.


.. _`snd_pcm_stream_unlock`:

snd_pcm_stream_unlock
=====================

.. c:function:: void snd_pcm_stream_unlock (struct snd_pcm_substream *substream)

    Unlock the PCM stream

    :param struct snd_pcm_substream \*substream:
        PCM substream


.. _`snd_pcm_stream_unlock.description`:

Description
-----------

This unlocks the PCM stream that has been locked via :c:func:`snd_pcm_stream_lock`.


.. _`snd_pcm_stream_lock_irq`:

snd_pcm_stream_lock_irq
=======================

.. c:function:: void snd_pcm_stream_lock_irq (struct snd_pcm_substream *substream)

    Lock the PCM stream

    :param struct snd_pcm_substream \*substream:
        PCM substream


.. _`snd_pcm_stream_lock_irq.description`:

Description
-----------

This locks the PCM stream like :c:func:`snd_pcm_stream_lock` and disables the local
IRQ (only when nonatomic is false).  In nonatomic case, this is identical
as :c:func:`snd_pcm_stream_lock`.


.. _`snd_pcm_stream_unlock_irq`:

snd_pcm_stream_unlock_irq
=========================

.. c:function:: void snd_pcm_stream_unlock_irq (struct snd_pcm_substream *substream)

    Unlock the PCM stream

    :param struct snd_pcm_substream \*substream:
        PCM substream


.. _`snd_pcm_stream_unlock_irq.description`:

Description
-----------

This is a counter-part of :c:func:`snd_pcm_stream_lock_irq`.


.. _`snd_pcm_stream_unlock_irqrestore`:

snd_pcm_stream_unlock_irqrestore
================================

.. c:function:: void snd_pcm_stream_unlock_irqrestore (struct snd_pcm_substream *substream, unsigned long flags)

    Unlock the PCM stream

    :param struct snd_pcm_substream \*substream:
        PCM substream

    :param unsigned long flags:
        irq flags


.. _`snd_pcm_stream_unlock_irqrestore.description`:

Description
-----------

This is a counter-part of :c:func:`snd_pcm_stream_lock_irqsave`.


.. _`snd_pcm_start`:

snd_pcm_start
=============

.. c:function:: int snd_pcm_start (struct snd_pcm_substream *substream)

    start all linked streams

    :param struct snd_pcm_substream \*substream:
        the PCM substream instance


.. _`snd_pcm_start.description`:

Description
-----------

Return: Zero if successful, or a negative error code.


.. _`snd_pcm_stop`:

snd_pcm_stop
============

.. c:function:: int snd_pcm_stop (struct snd_pcm_substream *substream, snd_pcm_state_t state)

    try to stop all running streams in the substream group

    :param struct snd_pcm_substream \*substream:
        the PCM substream instance

    :param snd_pcm_state_t state:
        PCM state after stopping the stream


.. _`snd_pcm_stop.description`:

Description
-----------

The state of each stream is then changed to the given state unconditionally.

Return: Zero if successful, or a negative error code.


.. _`snd_pcm_drain_done`:

snd_pcm_drain_done
==================

.. c:function:: int snd_pcm_drain_done (struct snd_pcm_substream *substream)

    stop the DMA only when the given stream is playback

    :param struct snd_pcm_substream \*substream:
        the PCM substream


.. _`snd_pcm_drain_done.description`:

Description
-----------

After stopping, the state is changed to SETUP.
Unlike :c:func:`snd_pcm_stop`, this affects only the given stream.

Return: Zero if succesful, or a negative error code.


.. _`snd_pcm_stop_xrun`:

snd_pcm_stop_xrun
=================

.. c:function:: int snd_pcm_stop_xrun (struct snd_pcm_substream *substream)

    stop the running streams as XRUN

    :param struct snd_pcm_substream \*substream:
        the PCM substream instance


.. _`snd_pcm_stop_xrun.description`:

Description
-----------

This stops the given running substream (and all linked substreams) as XRUN.
Unlike :c:func:`snd_pcm_stop`, this function takes the substream lock by itself.

Return: Zero if successful, or a negative error code.


.. _`snd_pcm_suspend`:

snd_pcm_suspend
===============

.. c:function:: int snd_pcm_suspend (struct snd_pcm_substream *substream)

    trigger SUSPEND to all linked streams

    :param struct snd_pcm_substream \*substream:
        the PCM substream


.. _`snd_pcm_suspend.description`:

Description
-----------

After this call, all streams are changed to SUSPENDED state.

Return: Zero if successful (or ``substream`` is ``NULL``\ ), or a negative error
code.


.. _`snd_pcm_suspend_all`:

snd_pcm_suspend_all
===================

.. c:function:: int snd_pcm_suspend_all (struct snd_pcm *pcm)

    trigger SUSPEND to all substreams in the given pcm

    :param struct snd_pcm \*pcm:
        the PCM instance


.. _`snd_pcm_suspend_all.description`:

Description
-----------

After this call, all streams are changed to SUSPENDED state.

Return: Zero if successful (or ``pcm`` is ``NULL``\ ), or a negative error code.


.. _`snd_pcm_prepare`:

snd_pcm_prepare
===============

.. c:function:: int snd_pcm_prepare (struct snd_pcm_substream *substream, struct file *file)

    prepare the PCM substream to be triggerable

    :param struct snd_pcm_substream \*substream:
        the PCM substream instance

    :param struct file \*file:
        file to refer f_flags


.. _`snd_pcm_prepare.description`:

Description
-----------

Return: Zero if successful, or a negative error code.


.. _`snd_pcm_lib_default_mmap`:

snd_pcm_lib_default_mmap
========================

.. c:function:: int snd_pcm_lib_default_mmap (struct snd_pcm_substream *substream, struct vm_area_struct *area)

    Default PCM data mmap function

    :param struct snd_pcm_substream \*substream:
        PCM substream

    :param struct vm_area_struct \*area:
        VMA


.. _`snd_pcm_lib_default_mmap.description`:

Description
-----------

This is the default mmap handler for PCM data.  When mmap pcm_ops is NULL,
this function is invoked implicitly.


.. _`snd_pcm_lib_mmap_iomem`:

snd_pcm_lib_mmap_iomem
======================

.. c:function:: int snd_pcm_lib_mmap_iomem (struct snd_pcm_substream *substream, struct vm_area_struct *area)

    Default PCM data mmap function for I/O mem

    :param struct snd_pcm_substream \*substream:
        PCM substream

    :param struct vm_area_struct \*area:
        VMA


.. _`snd_pcm_lib_mmap_iomem.description`:

Description
-----------

When your hardware uses the iomapped pages as the hardware buffer and
wants to mmap it, pass this function as mmap pcm_ops.  Note that this
is supposed to work only on limited architectures.

