.. -*- coding: utf-8; mode: rst -*-

===========
spear_smi.h
===========


.. _`spear_smi_flash_info`:

struct spear_smi_flash_info
===========================

.. c:type:: spear_smi_flash_info

    platform structure for passing flash information


.. _`spear_smi_flash_info.definition`:

Definition
----------

.. code-block:: c

  struct spear_smi_flash_info {
  };


.. _`spear_smi_flash_info.members`:

Members
-------




.. _`spear_smi_flash_info.name`:

name
----

name of the serial nor flash for identification



.. _`spear_smi_flash_info.mem_base`:

mem_base
--------

the memory base on which the flash is mapped



.. _`spear_smi_flash_info.size`:

size
----

size of the flash in bytes



.. _`spear_smi_flash_info.partitions`:

partitions
----------

parition details



.. _`spear_smi_flash_info.nr_partitions`:

nr_partitions
-------------

number of partitions



.. _`spear_smi_flash_info.fast_mode`:

fast_mode
---------

whether flash supports fast mode



.. _`spear_smi_plat_data`:

struct spear_smi_plat_data
==========================

.. c:type:: spear_smi_plat_data

    platform structure for configuring smi


.. _`spear_smi_plat_data.definition`:

Definition
----------

.. code-block:: c

  struct spear_smi_plat_data {
  };


.. _`spear_smi_plat_data.members`:

Members
-------




.. _`spear_smi_plat_data.clk_rate`:

clk_rate
--------

clk rate at which SMI must operate



.. _`spear_smi_plat_data.num_flashes`:

num_flashes
-----------

number of flashes present on board



.. _`spear_smi_plat_data.board_flash_info`:

board_flash_info
----------------

specific details of each flash present on board

