.. -*- coding: utf-8; mode: rst -*-

======
drxk.h
======



.. _xref_struct_drxk_config:

struct drxk_config
==================

.. c:type:: struct drxk_config

    Configure the initial parameters for DRX-K



Definition
----------

.. code-block:: c

  struct drxk_config {
    u8 adr;
    bool single_master;
    bool no_i2c_bridge;
    bool parallel_ts;
    bool dynamic_clk;
    bool enable_merr_cfg;
    bool antenna_dvbt;
    u16 antenna_gpio;
    u8 mpeg_out_clk_strength;
    const char * microcode_name;
    int qam_demod_parameter_count;
  };



Members
-------

:``u8 adr``:
    I2C address of the DRX-K

:``bool single_master``:
    Device is on the single master mode

:``bool no_i2c_bridge``:
    Don't switch the I2C bridge to talk with tuner

:``bool parallel_ts``:
    True means that the device uses parallel TS,
    			Serial otherwise.

:``bool dynamic_clk``:
    True means that the clock will be dynamically
    			adjusted. Static clock otherwise.

:``bool enable_merr_cfg``:
    Enable SIO_PDR_PERR_CFG/SIO_PDR_MVAL_CFG.

:``bool antenna_dvbt``:
    GPIO bit for changing antenna to DVB-C. A value of 1
    			means that 1=DVBC, 0 = DVBT. Zero means the opposite.

:``u16 antenna_gpio``:
    GPIO bit used to control the antenna

:``u8 mpeg_out_clk_strength``:
    DRXK Mpeg output clock drive strength.

:``const char * microcode_name``:
    Name of the firmware file with the microcode

:``int qam_demod_parameter_count``:
    The number of parameters used for the command
    				to set the demodulator parameters. All
    				firmwares are using the 2-parameter commmand.
    				An exception is the "drxk_a3.mc" firmware,
    				which uses the 4-parameter command.
    				A value of 0 (default) or lower indicates that
    				the correct number of parameters will be
    				automatically detected.




Description
-----------

On the *_gpio vars, bit 0 is UIO-1, bit 1 is UIO-2 and bit 2 is
UIO-3.


