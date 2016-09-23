.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/musb/musb_core.h

.. _`musb_platform_ops`:

struct musb_platform_ops
========================

.. c:type:: struct musb_platform_ops

    Operations passed to musb_core by HW glue layer

.. _`musb_platform_ops.definition`:

Definition
----------

.. code-block:: c

    struct musb_platform_ops {
    #define MUSB_DMA_UX500 BIT(6)
    #define MUSB_DMA_CPPI41 BIT(5)
    #define MUSB_DMA_CPPI BIT(4)
    #define MUSB_DMA_TUSB_OMAP BIT(3)
    #define MUSB_DMA_INVENTRA BIT(2)
    #define MUSB_IN_TUSB BIT(1)
    #define MUSB_INDEXED_EP BIT(0)
        u32 quirks;
        int (*init)(struct musb *musb);
        int (*exit)(struct musb *musb);
        void (*enable)(struct musb *musb);
        void (*disable)(struct musb *musb);
        u32 (*ep_offset)(u8 epnum, u16 offset);
        void (*ep_select)(void __iomem *mbase, u8 epnum);
        u16 fifo_mode;
        u32 (*fifo_offset)(u8 epnum);
        u32 (*busctl_offset)(u8 epnum, u16 offset);
        u8 (*readb)(const void __iomem *addr, unsigned offset);
        void (*writeb)(void __iomem *addr, unsigned offset, u8 data);
        u16 (*readw)(const void __iomem *addr, unsigned offset);
        void (*writew)(void __iomem *addr, unsigned offset, u16 data);
        u32 (*readl)(const void __iomem *addr, unsigned offset);
        void (*writel)(void __iomem *addr, unsigned offset, u32 data);
        void (*read_fifo)(struct musb_hw_ep *hw_ep, u16 len, u8 *buf);
        void (*write_fifo)(struct musb_hw_ep *hw_ep, u16 len, const u8 *buf);
        struct dma_controller *(*dma_init)(struct musb *musb, void __iomem *base);
        void (*dma_exit)(struct dma_controller *c);
        int (*set_mode)(struct musb *musb, u8 mode);
        void (*try_idle)(struct musb *musb, unsigned long timeout);
        int (*recover)(struct musb *musb);
        int (*vbus_status)(struct musb *musb);
        void (*set_vbus)(struct musb *musb, int on);
        int (*adjust_channel_params)(struct dma_channel *channel,u16 packet_sz, u8 *mode,dma_addr_t *dma_addr, u32 *len);
        void (*pre_root_reset_end)(struct musb *musb);
        void (*post_root_reset_end)(struct musb *musb);
        int (*phy_callback)(enum musb_vbus_id_status status);
    }

.. _`musb_platform_ops.members`:

Members
-------

quirks
    flags for platform specific quirks

init
    turns on clocks, sets up platform-specific registers, etc

exit
    undoes \ ``init``\ 

enable
    enable device

disable
    disable device

ep_offset
    returns the end point offset

ep_select
    selects the specified end point

fifo_mode
    sets the fifo mode

fifo_offset
    returns the fifo offset

busctl_offset
    *undescribed*

readb
    read 8 bits

writeb
    write 8 bits

readw
    read 16 bits

writew
    write 16 bits

readl
    read 32 bits

writel
    write 32 bits

read_fifo
    reads the fifo

write_fifo
    writes to fifo

dma_init
    platform specific dma init function

dma_exit
    platform specific dma exit function

set_mode
    forcefully changes operating mode

try_idle
    tries to idle the IP

recover
    platform-specific babble recovery

vbus_status
    returns vbus status if possible

set_vbus
    forces vbus status

adjust_channel_params
    pre check for standard dma channel_program func

pre_root_reset_end
    called before the root usb port reset flag gets cleared

post_root_reset_end
    called after the root usb port reset flag gets cleared

phy_callback
    optional callback function for the phy to call

.. This file was automatic generated / don't edit.

