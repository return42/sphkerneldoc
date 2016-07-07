.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/nhi_regs.h

.. _`ring_desc`:

struct ring_desc
================

.. c:type:: struct ring_desc

    TX/RX ring entry

.. _`ring_desc.definition`:

Definition
----------

.. code-block:: c

    struct ring_desc {
        u64 phys;
        u32 length:12;
        u32 eof:4;
        u32 sof:4;
        enum ring_desc_flags flags:12;
        u32 time;
    }

.. _`ring_desc.members`:

Members
-------

phys
    *undescribed*

length
    *undescribed*

eof
    *undescribed*

sof
    *undescribed*

flags
    *undescribed*

time
    *undescribed*

.. _`ring_desc.description`:

Description
-----------

For TX set length/eof/sof.
For RX length/eof/sof are set by the NHI.

.. This file was automatic generated / don't edit.

