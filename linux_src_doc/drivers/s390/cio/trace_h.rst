.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/trace.h

.. _`trace_s390_cio_stsch`:

trace_s390_cio_stsch
====================

.. c:function:: void trace_s390_cio_stsch(struct subchannel_id schid, struct schib *schib, int cc)

    Store Subchannel instruction (STSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param schib:
        Subchannel-Information block
    :type schib: struct schib \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_msch`:

trace_s390_cio_msch
===================

.. c:function:: void trace_s390_cio_msch(struct subchannel_id schid, struct schib *schib, int cc)

    Modify Subchannel instruction (MSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param schib:
        Subchannel-Information block
    :type schib: struct schib \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_tsch`:

trace_s390_cio_tsch
===================

.. c:function:: void trace_s390_cio_tsch(struct subchannel_id schid, struct irb *irb, int cc)

    Test Subchannel instruction (TSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param irb:
        Interruption-Response Block
    :type irb: struct irb \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_tpi`:

trace_s390_cio_tpi
==================

.. c:function:: void trace_s390_cio_tpi(struct tpi_info *addr, int cc)

    Test Pending Interruption instruction (TPI) was performed

    :param addr:
        Address of the I/O interruption code or \ ``NULL``\ 
    :type addr: struct tpi_info \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_ssch`:

trace_s390_cio_ssch
===================

.. c:function:: void trace_s390_cio_ssch(struct subchannel_id schid, union orb *orb, int cc)

    Start Subchannel instruction (SSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param orb:
        Operation-Request Block
    :type orb: union orb \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_csch`:

trace_s390_cio_csch
===================

.. c:function:: void trace_s390_cio_csch(struct subchannel_id schid, int cc)

    Clear Subchannel instruction (CSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_hsch`:

trace_s390_cio_hsch
===================

.. c:function:: void trace_s390_cio_hsch(struct subchannel_id schid, int cc)

    Halt Subchannel instruction (HSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_xsch`:

trace_s390_cio_xsch
===================

.. c:function:: void trace_s390_cio_xsch(struct subchannel_id schid, int cc)

    Cancel Subchannel instruction (XSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_rsch`:

trace_s390_cio_rsch
===================

.. c:function:: void trace_s390_cio_rsch(struct subchannel_id schid, int cc)

    Resume Subchannel instruction (RSCH) was performed

    :param schid:
        Subchannel ID
    :type schid: struct subchannel_id

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_rchp`:

trace_s390_cio_rchp
===================

.. c:function:: void trace_s390_cio_rchp(struct chp_id chpid, int cc)

    Reset Channel Path (RCHP) instruction was performed

    :param chpid:
        Channel-Path Identifier
    :type chpid: struct chp_id

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_chsc`:

trace_s390_cio_chsc
===================

.. c:function:: void trace_s390_cio_chsc(struct chsc_header *chsc, int cc)

    Channel Subsystem Call (CHSC) instruction was performed

    :param chsc:
        CHSC block
    :type chsc: struct chsc_header \*

    :param cc:
        Condition code
    :type cc: int

.. _`trace_s390_cio_interrupt`:

trace_s390_cio_interrupt
========================

.. c:function:: void trace_s390_cio_interrupt(struct tpi_info *tpi_info)

    An I/O interrupt occurred

    :param tpi_info:
        Address of the I/O interruption code
    :type tpi_info: struct tpi_info \*

.. _`trace_s390_cio_adapter_int`:

trace_s390_cio_adapter_int
==========================

.. c:function:: void trace_s390_cio_adapter_int(struct tpi_info *tpi_info)

    An adapter interrupt occurred

    :param tpi_info:
        Address of the I/O interruption code
    :type tpi_info: struct tpi_info \*

.. _`trace_s390_cio_stcrw`:

trace_s390_cio_stcrw
====================

.. c:function:: void trace_s390_cio_stcrw(struct crw *crw, int cc)

    Store Channel Report Word (STCRW) was performed

    :param crw:
        Channel Report Word
    :type crw: struct crw \*

    :param cc:
        Condition code
    :type cc: int

.. This file was automatic generated / don't edit.

