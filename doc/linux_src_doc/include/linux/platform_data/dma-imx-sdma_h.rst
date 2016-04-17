.. -*- coding: utf-8; mode: rst -*-

==============
dma-imx-sdma.h
==============


.. _`sdma_script_start_addrs`:

struct sdma_script_start_addrs
==============================

.. c:type:: sdma_script_start_addrs

    SDMA script start pointers


.. _`sdma_script_start_addrs.definition`:

Definition
----------

.. code-block:: c

  struct sdma_script_start_addrs {
  };


.. _`sdma_script_start_addrs.members`:

Members
-------




.. _`sdma_script_start_addrs.description`:

Description
-----------


start addresses of the different functions in the physical
address space of the SDMA engine.



.. _`sdma_platform_data`:

struct sdma_platform_data
=========================

.. c:type:: sdma_platform_data

    platform specific data for SDMA engine


.. _`sdma_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct sdma_platform_data {
  };


.. _`sdma_platform_data.members`:

Members
-------




.. _`sdma_platform_data.description`:

Description
-----------


``fw_name``                The firmware name
``script_addrs``        SDMA scripts addresses in SDMA ROM

