.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/cio.c

.. _`cio_cancel_halt_clear`:

cio_cancel_halt_clear
=====================

.. c:function:: int cio_cancel_halt_clear(struct subchannel *sch, int *iretry)

    Cancel running I/O by performing cancel, halt and clear ordinally if subchannel is valid.

    :param struct subchannel \*sch:
        subchannel on which to perform the cancel_halt_clear operation

    :param int \*iretry:
        the number of the times remained to retry the next operation

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

    :param struct subchannel \*sch:
        subchannel on which to perform stsch
        Return zero on success, -ENODEV otherwise.

.. _`cio_enable_subchannel`:

cio_enable_subchannel
=====================

.. c:function:: int cio_enable_subchannel(struct subchannel *sch, u32 intparm)

    enable a subchannel.

    :param struct subchannel \*sch:
        subchannel to be enabled

    :param u32 intparm:
        interruption parameter to set

.. _`cio_disable_subchannel`:

cio_disable_subchannel
======================

.. c:function:: int cio_disable_subchannel(struct subchannel *sch)

    disable a subchannel.

    :param struct subchannel \*sch:
        subchannel to disable

.. _`cio_validate_subchannel`:

cio_validate_subchannel
=======================

.. c:function:: int cio_validate_subchannel(struct subchannel *sch, struct subchannel_id schid)

    basic validation of subchannel

    :param struct subchannel \*sch:
        subchannel structure to be filled out

    :param struct subchannel_id schid:
        subchannel id

.. _`cio_validate_subchannel.description`:

Description
-----------

Find out subchannel type and initialize struct subchannel.

.. _`cio_validate_subchannel.return-codes`:

Return codes
------------

0 on success
-ENXIO for non-defined subchannels
-ENODEV for invalid subchannels or blacklisted devices
-EIO for subchannels in an invalid subchannel set

.. _`cio_tm_start_key`:

cio_tm_start_key
================

.. c:function:: int cio_tm_start_key(struct subchannel *sch, struct tcw *tcw, u8 lpm, u8 key)

    perform start function

    :param struct subchannel \*sch:
        subchannel on which to perform the start function

    :param struct tcw \*tcw:
        transport-command word to be started

    :param u8 lpm:
        mask of paths to use

    :param u8 key:
        storage key to use for storage access

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

    :param struct subchannel \*sch:
        subchannel on which to perform the interrogate function

.. _`cio_tm_intrg.description`:

Description
-----------

If the specified subchannel is running in transport-mode, perform the
interrogate function. Return zero on success, non-zero otherwie.

.. This file was automatic generated / don't edit.

