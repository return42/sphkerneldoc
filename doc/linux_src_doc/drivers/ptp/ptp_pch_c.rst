.. -*- coding: utf-8; mode: rst -*-

=========
ptp_pch.c
=========


.. _`pch_ts_regs`:

struct pch_ts_regs
==================

.. c:type:: pch_ts_regs

    IEEE 1588 registers


.. _`pch_ts_regs.definition`:

Definition
----------

.. code-block:: c

  struct pch_ts_regs {
  };


.. _`pch_ts_regs.members`:

Members
-------




.. _`pch_dev`:

struct pch_dev
==============

.. c:type:: pch_dev

    Driver private data


.. _`pch_dev.definition`:

Definition
----------

.. code-block:: c

  struct pch_dev {
  };


.. _`pch_dev.members`:

Members
-------




.. _`pch_params`:

struct pch_params
=================

.. c:type:: pch_params

    1588 module parameter


.. _`pch_params.definition`:

Definition
----------

.. code-block:: c

  struct pch_params {
  };


.. _`pch_params.members`:

Members
-------




.. _`pch_set_station_address`:

pch_set_station_address
=======================

.. c:function:: int pch_set_station_address (u8 *addr, struct pci_dev *pdev)

    This API sets the station address used by IEEE 1588 hardware when looking at PTP traffic on the ethernet interface

    :param u8 \*addr:
        dress which contain the column separated address to be used.

    :param struct pci_dev \*pdev:

        *undescribed*

