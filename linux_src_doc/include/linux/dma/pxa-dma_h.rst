.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma/pxa-dma.h

.. _`pxad_param`:

struct pxad_param
=================

.. c:type:: struct pxad_param

    dma channel request parameters

.. _`pxad_param.definition`:

Definition
----------

.. code-block:: c

    struct pxad_param {
        unsigned int drcmr;
        enum pxad_chan_prio prio;
    }

.. _`pxad_param.members`:

Members
-------

drcmr
    requestor line number

prio
    minimal mandatory priority of the channel

.. _`pxad_param.description`:

Description
-----------

If a requested channel is granted, its priority will be at least \ ``prio``\ ,
ie. if PXAD_PRIO_LOW is required, the requested channel will be either
PXAD_PRIO_LOW, PXAD_PRIO_NORMAL or PXAD_PRIO_HIGHEST.

.. This file was automatic generated / don't edit.

