.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regmap.h

.. _`regmap_init`:

regmap_init
===========

.. c:function::  regmap_init( dev,  bus,  bus_context,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  bus:
        Bus-specific callbacks to use with device

    :param  bus_context:
        Data passed to bus-specific callbacks

    :param  config:
        Configuration for register map

.. _`regmap_init.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.  This function should generally not be called
directly, it should be called by bus-specific init functions.

.. _`regmap_init_i2c`:

regmap_init_i2c
===============

.. c:function::  regmap_init_i2c( i2c,  config)

    Initialise register map

    :param  i2c:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_i2c.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spi`:

regmap_init_spi
===============

.. c:function::  regmap_init_spi( dev,  config)

    Initialise register map

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`regmap_init_spi.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spmi_base`:

regmap_init_spmi_base
=====================

.. c:function::  regmap_init_spmi_base( dev,  config)

    Create regmap for the Base register space

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`regmap_init_spmi_base.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spmi_ext`:

regmap_init_spmi_ext
====================

.. c:function::  regmap_init_spmi_ext( dev,  config)

    Create regmap for Ext register space

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`regmap_init_spmi_ext.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_mmio_clk`:

regmap_init_mmio_clk
====================

.. c:function::  regmap_init_mmio_clk( dev,  clk_id,  regs,  config)

    Initialise register map with register clock

    :param  dev:
        Device that will be interacted with

    :param  clk_id:
        register clock consumer ID

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`regmap_init_mmio_clk.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_mmio`:

regmap_init_mmio
================

.. c:function::  regmap_init_mmio( dev,  regs,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`regmap_init_mmio.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_ac97`:

regmap_init_ac97
================

.. c:function::  regmap_init_ac97( ac97,  config)

    Initialise AC'97 register map

    :param  ac97:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_ac97.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`devm_regmap_init`:

devm_regmap_init
================

.. c:function::  devm_regmap_init( dev,  bus,  bus_context,  config)

    Initialise managed register map

    :param  dev:
        Device that will be interacted with

    :param  bus:
        Bus-specific callbacks to use with device

    :param  bus_context:
        Data passed to bus-specific callbacks

    :param  config:
        Configuration for register map

.. _`devm_regmap_init.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  This function should generally not be called
directly, it should be called by bus-specific init functions.  The
map will be automatically freed by the device management code.

.. _`devm_regmap_init_i2c`:

devm_regmap_init_i2c
====================

.. c:function::  devm_regmap_init_i2c( i2c,  config)

    Initialise managed register map

    :param  i2c:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_i2c.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_spi`:

devm_regmap_init_spi
====================

.. c:function::  devm_regmap_init_spi( dev,  config)

    Initialise register map

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spi.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The map will be automatically freed by the
device management code.

.. _`devm_regmap_init_spmi_base`:

devm_regmap_init_spmi_base
==========================

.. c:function::  devm_regmap_init_spmi_base( dev,  config)

    Create managed regmap for Base register space

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spmi_base.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_spmi_ext`:

devm_regmap_init_spmi_ext
=========================

.. c:function::  devm_regmap_init_spmi_ext( dev,  config)

    Create managed regmap for Ext register space

    :param  dev:
        *undescribed*

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spmi_ext.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_mmio_clk`:

devm_regmap_init_mmio_clk
=========================

.. c:function::  devm_regmap_init_mmio_clk( dev,  clk_id,  regs,  config)

    Initialise managed register map with clock

    :param  dev:
        Device that will be interacted with

    :param  clk_id:
        register clock consumer ID

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_mmio_clk.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_mmio`:

devm_regmap_init_mmio
=====================

.. c:function::  devm_regmap_init_mmio( dev,  regs,  config)

    Initialise managed register map

    :param  dev:
        Device that will be interacted with

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_mmio.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_ac97`:

devm_regmap_init_ac97
=====================

.. c:function::  devm_regmap_init_ac97( ac97,  config)

    Initialise AC'97 register map

    :param  ac97:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_ac97.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. This file was automatic generated / don't edit.
