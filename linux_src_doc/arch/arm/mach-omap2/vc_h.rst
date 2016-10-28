.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/vc.h

.. _`omap_vc_common`:

struct omap_vc_common
=====================

.. c:type:: struct omap_vc_common

    per-VC register/bitfield data

.. _`omap_vc_common.definition`:

Definition
----------

.. code-block:: c

    struct omap_vc_common {
        u32 cmd_on_mask;
        u32 valid;
        u8 bypass_val_reg;
        u8 data_shift;
        u8 slaveaddr_shift;
        u8 regaddr_shift;
        u8 cmd_on_shift;
        u8 cmd_onlp_shift;
        u8 cmd_ret_shift;
        u8 cmd_off_shift;
        u8 i2c_cfg_reg;
        u8 i2c_cfg_clear_mask;
        u8 i2c_cfg_hsen_mask;
        u8 i2c_mcode_mask;
    }

.. _`omap_vc_common.members`:

Members
-------

cmd_on_mask
    ON bitmask in PRM_VC_CMD_VAL\* register

valid
    VALID bitmask in PRM_VC_BYPASS_VAL register

bypass_val_reg
    Offset of PRM_VC_BYPASS_VAL reg from PRM start

data_shift
    DATA field shift in PRM_VC_BYPASS_VAL register

slaveaddr_shift
    SLAVEADDR field shift in PRM_VC_BYPASS_VAL register

regaddr_shift
    REGADDR field shift in PRM_VC_BYPASS_VAL register

cmd_on_shift
    ON field shift in PRM_VC_CMD_VAL\_\* register

cmd_onlp_shift
    ONLP field shift in PRM_VC_CMD_VAL\_\* register

cmd_ret_shift
    RET field shift in PRM_VC_CMD_VAL\_\* register

cmd_off_shift
    OFF field shift in PRM_VC_CMD_VAL\_\* register

i2c_cfg_reg
    I2C configuration register offset

i2c_cfg_clear_mask
    high-speed mode bit clear mask in I2C config register

i2c_cfg_hsen_mask
    high-speed mode bit field mask in I2C config register

i2c_mcode_mask
    MCODE field mask for I2C config register

.. _`omap_vc_common.description`:

Description
-----------

XXX One of cmd_on_mask and cmd_on_shift are not needed
XXX VALID should probably be a shift, not a mask

.. _`omap_vc_channel`:

struct omap_vc_channel
======================

.. c:type:: struct omap_vc_channel

    VC per-instance data

.. _`omap_vc_channel.definition`:

Definition
----------

.. code-block:: c

    struct omap_vc_channel {
        u16 i2c_slave_addr;
        u16 volt_reg_addr;
        u16 cmd_reg_addr;
        u8 cfg_channel;
        bool i2c_high_speed;
        const struct omap_vc_common *common;
        u32 smps_sa_mask;
        u32 smps_volra_mask;
        u32 smps_cmdra_mask;
        u8 cmdval_reg;
        u8 smps_sa_reg;
        u8 smps_volra_reg;
        u8 smps_cmdra_reg;
        u8 cfg_channel_reg;
        u8 cfg_channel_sa_shift;
        u8 flags;
    }

.. _`omap_vc_channel.members`:

Members
-------

i2c_slave_addr
    I2C slave address of PMIC for this VC channel

volt_reg_addr
    voltage configuration register address

cmd_reg_addr
    command configuration register address

cfg_channel
    current value of VC channel configuration register

i2c_high_speed
    whether or not to use I2C high-speed mode

common
    pointer to VC common data for this platform

smps_sa_mask
    i2c slave address bitmask in the PRM_VC_SMPS_SA register

smps_volra_mask
    VOLRA\* bitmask in the PRM_VC_VOL_RA register

smps_cmdra_mask
    CMDRA\* bitmask in the PRM_VC_CMD_RA register

cmdval_reg
    register for on/ret/off voltage level values for this channel

smps_sa_reg
    Offset of PRM_VC_SMPS_SA reg from PRM start

smps_volra_reg
    Offset of PRM_VC_SMPS_VOL_RA reg from PRM start

smps_cmdra_reg
    Offset of PRM_VC_SMPS_CMD_RA reg from PRM start

cfg_channel_reg
    VC channel configuration register

cfg_channel_sa_shift
    bit shift for slave address cfg_channel register

flags
    VC channel-specific flags (optional)

.. This file was automatic generated / don't edit.

