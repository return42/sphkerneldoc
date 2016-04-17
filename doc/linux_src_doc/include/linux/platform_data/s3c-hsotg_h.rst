.. -*- coding: utf-8; mode: rst -*-

===========
s3c-hsotg.h
===========


.. _`dwc2_hsotg_plat`:

struct dwc2_hsotg_plat
======================

.. c:type:: dwc2_hsotg_plat

    platform data for high-speed otg/udc


.. _`dwc2_hsotg_plat.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hsotg_plat {
    enum dwc2_hsotg_dmamode dma;
    unsigned int is_osc:1;
  };


.. _`dwc2_hsotg_plat.members`:

Members
-------

:``dma``:
    Whether to use DMA or not.

:``is_osc``:
    The clock source is an oscillator, not a crystal


