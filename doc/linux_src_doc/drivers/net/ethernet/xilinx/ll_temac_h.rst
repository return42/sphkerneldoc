.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/ll_temac.h

.. _`cdmac_bd`:

struct cdmac_bd
===============

.. c:type:: struct cdmac_bd

    LocalLink buffer descriptor format

.. _`cdmac_bd.definition`:

Definition
----------

.. code-block:: c

    struct cdmac_bd {
        u32 next;
        u32 phys;
        u32 len;
        u32 app0;
        u32 app1;
        u32 app2;
        u32 app3;
        u32 app4;
    }

.. _`cdmac_bd.members`:

Members
-------

next
    *undescribed*

phys
    *undescribed*

len
    *undescribed*

app0
    *undescribed*

app1
    *undescribed*

app2
    *undescribed*

app3
    *undescribed*

app4
    *undescribed*

.. _`cdmac_bd.app0-bits`:

app0 bits
---------

0    Error
1    IrqOnEnd    generate an interrupt at completion of DMA  op
2    reserved
3    completed   Current descriptor completed
4    SOP         TX - marks first desc/ RX marks first desct
5    EOP         TX marks last desc/RX marks last desc
6    EngBusy     DMA is processing
7    reserved
8:31 application specific

.. This file was automatic generated / don't edit.

