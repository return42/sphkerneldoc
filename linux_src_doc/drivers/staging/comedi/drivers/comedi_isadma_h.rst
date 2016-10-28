.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_isadma.h

.. _`comedi_isadma_desc`:

struct comedi_isadma_desc
=========================

.. c:type:: struct comedi_isadma_desc

    cookie for ISA DMA

.. _`comedi_isadma_desc.definition`:

Definition
----------

.. code-block:: c

    struct comedi_isadma_desc {
        void *virt_addr;
        dma_addr_t hw_addr;
        unsigned int chan;
        unsigned int maxsize;
        unsigned int size;
        char mode;
    }

.. _`comedi_isadma_desc.members`:

Members
-------

virt_addr
    virtual address of buffer

hw_addr
    hardware (bus) address of buffer

chan
    DMA channel

maxsize
    allocated size of buffer (in bytes)

size
    transfer size (in bytes)

mode
    DMA_MODE_READ or DMA_MODE_WRITE

.. _`comedi_isadma`:

struct comedi_isadma
====================

.. c:type:: struct comedi_isadma

    ISA DMA data

.. _`comedi_isadma.definition`:

Definition
----------

.. code-block:: c

    struct comedi_isadma {
        struct comedi_isadma_desc *desc;
        int n_desc;
        int cur_dma;
        unsigned int chan;
        unsigned int chan2;
    }

.. _`comedi_isadma.members`:

Members
-------

desc
    cookie for each DMA buffer

n_desc
    the number of cookies

cur_dma
    the current cookie in use

chan
    the first DMA channel requested

chan2
    the second DMA channel requested

.. This file was automatic generated / don't edit.

