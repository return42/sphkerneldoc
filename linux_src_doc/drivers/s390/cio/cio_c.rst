.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/cio.c

.. _`cio_cancel_halt_clear`:

cio_cancel_halt_clear
=====================

.. c:function:: int cio_cancel_halt_clear(struct subchannel *sch, int *iretry)

    Cancel running I/O by performing cancel, halt and clear ordinally if subchannel is valid.

    :param sch:
        subchannel on which to perform the cancel_halt_clear operation
    :type sch: struct subchannel \*

    :param iretry:
        the number of the times remained to retry the next operation
    :type iretry: int \*

.. _`cio_cancel_halt_clear.description`:

Description
-----------

This should be called repeatedly since halt/clear are asynchronous
operations. We do one try with cio_cancel, three tries with cio_halt,
255 tries with cio_clear. The caller should initialize \ ``iretry``\  with
the value 255 for its first call to this, and keep using the same
\ ``iretry``\  in the subsequent calls until it gets a non -EBUSY return.

Returns 0 if device now idle, -ENODEV for device not operational,
-EBUSY if an interrupt is expected (either from halt/clear or from a
status pending), and -EIO if out of retries.

.. _`cio_update_schib`:

cio_update_schib
================

.. c:function:: int cio_update_schib(struct subchannel *sch)

    Perform stsch and update schib if subchannel is valid.

    :param sch:
        subchannel on which to perform stsch
        Return zero on success, -ENODEV otherwise.
    :type sch: struct subchannel \*

.. _`cio_enable_subchannel`:

cio_enable_subchannel
=====================

.. c:function:: int cio_enable_subchannel(struct subchannel *sch, u32 intparm)

    enable a subchannel.

    :param sch:
        subchannel to be enabled
    :type sch: struct subchannel \*

    :param intparm:
        interruption parameter to set
    :type intparm: u32

.. _`cio_disable_subchannel`:

cio_disable_subchannel
======================

.. c:function:: int cio_disable_subchannel(struct subchannel *sch)

    disable a subchannel.

    :param sch:
        subchannel to disable
    :type sch: struct subchannel \*

.. _`cio_tm_start_key`:

cio_tm_start_key
================

.. c:function:: int cio_tm_start_key(struct subchannel *sch, struct tcw *tcw, u8 lpm, u8 key)

    perform start function

    :param sch:
        subchannel on which to perform the start function
    :type sch: struct subchannel \*

    :param tcw:
        transport-command word to be started
    :type tcw: struct tcw \*

    :param lpm:
        mask of paths to use
    :type lpm: u8

    :param key:
        storage key to use for storage access
    :type key: u8

.. _`cio_tm_start_key.description`:

Description
-----------

Start the tcw on the given subchannel. Return zero on success, non-zero
otherwise.

.. _`cio_tm_intrg`:

cio_tm_intrg
============

.. c:function:: int cio_tm_intrg(struct subchannel *sch)

    perform interrogate function

    :param sch:
        subchannel on which to perform the interrogate function
    :type sch: struct subchannel \*

.. _`cio_tm_intrg.description`:

Description
-----------

If the specified subchannel is running in transport-mode, perform the
interrogate function. Return zero on success, non-zero otherwie.

.. This file was automatic generated / don't edit.

