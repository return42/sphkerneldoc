.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wcn36xx/dxe.h

.. _`wcn36xx_dxe_desc`:

struct wcn36xx_dxe_desc
=======================

.. c:type:: struct wcn36xx_dxe_desc

    describes descriptor of one DXE buffer

.. _`wcn36xx_dxe_desc.definition`:

Definition
----------

.. code-block:: c

    struct wcn36xx_dxe_desc {
        u32 ctrl;
        u32 fr_len;
        u32 src_addr_l;
        u32 dst_addr_l;
        u32 phy_next_l;
        u32 src_addr_h;
        u32 dst_addr_h;
        u32 phy_next_h;
    }

.. _`wcn36xx_dxe_desc.members`:

Members
-------

ctrl
    is a union that consists of following bits:
    union {
    u32     valid           :1; //0 = DMA stop, 1 = DMA continue with this
    //descriptor
    u32     transfer_type   :2; //0 = Host to Host space
    u32     eop             :1; //End of Packet
    u32     bd_handling     :1; //if transferType = Host to BMU, then 0
    // means first 128 bytes contain BD, and 1
    // means create new empty BD
    u32     siq             :1; // SIQ
    u32     diq             :1; // DIQ
    u32     pdu_rel         :1; //0 = don't release BD and PDUs when done,
    // 1 = release them
    u32     bthld_sel       :4; //BMU Threshold Select
    u32     prio            :3; //Specifies the priority level to use for
    // the transfer
    u32     stop_channel    :1; //1 = DMA stops processing further, channel
    //requires re-enabling after this
    u32     intr            :1; //Interrupt on Descriptor Done
    u32     rsvd            :1; //reserved
    u32     size            :14;//14 bits used - ignored for BMU transfers,
    //only used for host to host transfers?
    } ctrl;

fr_len
    *undescribed*

src_addr_l
    *undescribed*

dst_addr_l
    *undescribed*

phy_next_l
    *undescribed*

src_addr_h
    *undescribed*

dst_addr_h
    *undescribed*

phy_next_h
    *undescribed*

.. This file was automatic generated / don't edit.

