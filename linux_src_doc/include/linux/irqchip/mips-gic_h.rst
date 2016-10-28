.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/irqchip/mips-gic.h

.. _`gic_read_local_vp_id`:

gic_read_local_vp_id
====================

.. c:function:: unsigned gic_read_local_vp_id( void)

    read the local VPs VCNUM

    :param  void:
        no arguments

.. _`gic_read_local_vp_id.description`:

Description
-----------

Read the VCNUM of the local VP from the GIC_VP_IDENT register and
return it to the caller. This ID should be used to refer to the VP
via the GICs VP-other region, or when calculating an offset to a
bit representing the VP in interrupt masks.

.. _`gic_read_local_vp_id.return`:

Return
------

The VCNUM value for the local VP.

.. This file was automatic generated / don't edit.

