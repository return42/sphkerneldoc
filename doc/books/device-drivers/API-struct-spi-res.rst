
.. _API-struct-spi-res:

==============
struct spi_res
==============

*man struct spi_res(9)*

*4.6.0-rc1*

spi resource management structure


Synopsis
========

.. code-block:: c

    struct spi_res {
      struct list_head entry;
      spi_res_release_t release;
      unsigned long long data[];
    };


Members
=======

entry
    list entry

release
    release code called prior to freeing this resource

data[]
    extra data allocated for the specific use-case


Description
===========

this is based on ideas from devres, but focused on life-cycle management during spi_message processing
