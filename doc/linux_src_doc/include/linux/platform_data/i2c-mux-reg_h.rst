.. -*- coding: utf-8; mode: rst -*-

=============
i2c-mux-reg.h
=============


.. _`i2c_mux_reg_platform_data`:

struct i2c_mux_reg_platform_data
================================

.. c:type:: i2c_mux_reg_platform_data

    Platform-dependent data for i2c-mux-reg


.. _`i2c_mux_reg_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct i2c_mux_reg_platform_data {
    int parent;
    int base_nr;
    const unsigned int * values;
    int n_values;
    bool little_endian;
    bool write_only;
    const unsigned int * classes;
    u32 idle;
    bool idle_in_use;
    void __iomem * reg;
    resource_size_t reg_size;
  };


.. _`i2c_mux_reg_platform_data.members`:

Members
-------

:``parent``:
    Parent I2C bus adapter number

:``base_nr``:
    Base I2C bus number to number adapters from or zero for dynamic

:``values``:
    Array of value for each channel

:``n_values``:
    Number of multiplexer channels

:``little_endian``:
    Indicating if the register is in little endian

:``write_only``:
    Reading the register is not allowed by hardware

:``classes``:
    Optional I2C auto-detection classes

:``idle``:
    Value to write to mux when idle

:``idle_in_use``:
    indicate if idle value is in use

:``reg``:
    Virtual address of the register to switch channel

:``reg_size``:
    register size in bytes


