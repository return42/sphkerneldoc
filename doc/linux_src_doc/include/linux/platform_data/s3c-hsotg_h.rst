.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/s3c-hsotg.h

.. _`dwc2_hsotg_plat`:

struct dwc2_hsotg_plat
======================

.. c:type:: struct dwc2_hsotg_plat

    platform data for high-speed otg/udc

.. _`dwc2_hsotg_plat.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hsotg_plat {
        enum dwc2_hsotg_dmamode dma;
        unsigned int is_osc:1;
        int phy_type;
        int (* phy_init) (struct platform_device *pdev, int type);
        int (* phy_exit) (struct platform_device *pdev, int type);
    }

.. _`dwc2_hsotg_plat.members`:

Members
-------

dma
    Whether to use DMA or not.

is_osc
    The clock source is an oscillator, not a crystal

phy_type
    *undescribed*

phy_init
    *undescribed*

phy_exit
    *undescribed*

.. This file was automatic generated / don't edit.

