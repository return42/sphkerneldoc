.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/trace.h

.. _`trace_s390_cio_stsch`:

trace_s390_cio_stsch
====================

.. c:function:: void trace_s390_cio_stsch(struct subchannel_id schid, struct schib *schib, int cc)

    Store Subchannel instruction (STSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param struct schib \*schib:
        Subchannel-Information block

    :param int cc:
        Condition code

.. _`trace_s390_cio_msch`:

trace_s390_cio_msch
===================

.. c:function:: void trace_s390_cio_msch(struct subchannel_id schid, struct schib *schib, int cc)

    Modify Subchannel instruction (MSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param struct schib \*schib:
        Subchannel-Information block

    :param int cc:
        Condition code

.. _`trace_s390_cio_tsch`:

trace_s390_cio_tsch
===================

.. c:function:: void trace_s390_cio_tsch(struct subchannel_id schid, struct irb *irb, int cc)

    Test Subchannel instruction (TSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param struct irb \*irb:
        Interruption-Response Block

    :param int cc:
        Condition code

.. _`trace_s390_cio_tpi`:

trace_s390_cio_tpi
==================

.. c:function:: void trace_s390_cio_tpi(struct tpi_info *addr, int cc)

    Test Pending Interruption instruction (TPI) was performed

    :param struct tpi_info \*addr:
        Address of the I/O interruption code or \ ``NULL``\ 

    :param int cc:
        Condition code

.. _`trace_s390_cio_ssch`:

trace_s390_cio_ssch
===================

.. c:function:: void trace_s390_cio_ssch(struct subchannel_id schid, union orb *orb, int cc)

    Start Subchannel instruction (SSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param union orb \*orb:
        Operation-Request Block

    :param int cc:
        Condition code

.. _`trace_s390_cio_csch`:

trace_s390_cio_csch
===================

.. c:function:: void trace_s390_cio_csch(struct subchannel_id schid, int cc)

    Clear Subchannel instruction (CSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param int cc:
        Condition code

.. _`trace_s390_cio_hsch`:

trace_s390_cio_hsch
===================

.. c:function:: void trace_s390_cio_hsch(struct subchannel_id schid, int cc)

    Halt Subchannel instruction (HSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param int cc:
        Condition code

.. _`trace_s390_cio_xsch`:

trace_s390_cio_xsch
===================

.. c:function:: void trace_s390_cio_xsch(struct subchannel_id schid, int cc)

    Cancel Subchannel instruction (XSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param int cc:
        Condition code

.. _`trace_s390_cio_rsch`:

trace_s390_cio_rsch
===================

.. c:function:: void trace_s390_cio_rsch(struct subchannel_id schid, int cc)

    Resume Subchannel instruction (RSCH) was performed

    :param struct subchannel_id schid:
        Subchannel ID

    :param int cc:
        Condition code

.. _`trace_s390_cio_rchp`:

trace_s390_cio_rchp
===================

.. c:function:: void trace_s390_cio_rchp(struct chp_id chpid, int cc)

    Reset Channel Path (RCHP) instruction was performed

    :param struct chp_id chpid:
        Channel-Path Identifier

    :param int cc:
        Condition code

.. _`trace_s390_cio_chsc`:

trace_s390_cio_chsc
===================

.. c:function:: void trace_s390_cio_chsc(struct chsc_header *chsc, int cc)

    Channel Subsystem Call (CHSC) instruction was performed

    :param struct chsc_header \*chsc:
        CHSC block

    :param int cc:
        Condition code

.. _`trace_s390_cio_interrupt`:

trace_s390_cio_interrupt
========================

.. c:function:: void trace_s390_cio_interrupt(struct tpi_info *tpi_info)

    An I/O interrupt occurred

    :param struct tpi_info \*tpi_info:
        Address of the I/O interruption code

.. _`trace_s390_cio_adapter_int`:

trace_s390_cio_adapter_int
==========================

.. c:function:: void trace_s390_cio_adapter_int(struct tpi_info *tpi_info)

    An adapter interrupt occurred

    :param struct tpi_info \*tpi_info:
        Address of the I/O interruption code

.. _`trace_s390_cio_stcrw`:

trace_s390_cio_stcrw
====================

.. c:function:: void trace_s390_cio_stcrw(struct crw *crw, int cc)

    Store Channel Report Word (STCRW) was performed

    :param struct crw \*crw:
        Channel Report Word

    :param int cc:
        Condition code

.. This file was automatic generated / don't edit.

