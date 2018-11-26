.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/vfio_ccw_drv.c

.. _`vfio_ccw_sch_event`:

vfio_ccw_sch_event
==================

.. c:function:: int vfio_ccw_sch_event(struct subchannel *sch, int process)

    process subchannel event

    :param sch:
        subchannel
    :type sch: struct subchannel \*

    :param process:
        non-zero if function is called in process context
    :type process: int

.. _`vfio_ccw_sch_event.description`:

Description
-----------

An unspecified event occurred for this subchannel. Adjust data according
to the current operational state of the subchannel. Return zero when the
event has been handled sufficiently or -EAGAIN when this function should
be called again in process context.

.. This file was automatic generated / don't edit.

