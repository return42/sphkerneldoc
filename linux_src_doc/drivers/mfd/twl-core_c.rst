.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/twl-core.c

.. _`twl_get_regmap`:

twl_get_regmap
==============

.. c:function:: struct regmap *twl_get_regmap(u8 mod_no)

    Get the regmap associated with the given module

    :param mod_no:
        module number
    :type mod_no: u8

.. _`twl_get_regmap.description`:

Description
-----------

Returns the regmap pointer or NULL in case of failure.

.. _`twl_i2c_write`:

twl_i2c_write
=============

.. c:function:: int twl_i2c_write(u8 mod_no, u8 *value, u8 reg, unsigned num_bytes)

    Writes a n bit register in TWL4030/TWL5030/TWL60X0

    :param mod_no:
        module number
    :type mod_no: u8

    :param value:
        an array of num_bytes+1 containing data to write
    :type value: u8 \*

    :param reg:
        register address (just offset will do)
    :type reg: u8

    :param num_bytes:
        number of bytes to transfer
    :type num_bytes: unsigned

.. _`twl_i2c_write.description`:

Description
-----------

Returns 0 on success or else a negative error code.

.. _`twl_i2c_read`:

twl_i2c_read
============

.. c:function:: int twl_i2c_read(u8 mod_no, u8 *value, u8 reg, unsigned num_bytes)

    Reads a n bit register in TWL4030/TWL5030/TWL60X0

    :param mod_no:
        module number
    :type mod_no: u8

    :param value:
        an array of num_bytes containing data to be read
    :type value: u8 \*

    :param reg:
        register address (just offset will do)
    :type reg: u8

    :param num_bytes:
        number of bytes to transfer
    :type num_bytes: unsigned

.. _`twl_i2c_read.description`:

Description
-----------

Returns 0 on success or else a negative error code.

.. _`twl_set_regcache_bypass`:

twl_set_regcache_bypass
=======================

.. c:function:: int twl_set_regcache_bypass(u8 mod_no, bool enable)

    Configure the regcache bypass for the regmap associated with the module

    :param mod_no:
        module number
    :type mod_no: u8

    :param enable:
        Regcache bypass state
    :type enable: bool

.. _`twl_set_regcache_bypass.description`:

Description
-----------

Returns 0 else failure.

.. _`twl_read_idcode_register`:

twl_read_idcode_register
========================

.. c:function:: int twl_read_idcode_register( void)

    API to read the IDCODE register.

    :param void:
        no arguments
    :type void: 

.. _`twl_read_idcode_register.description`:

Description
-----------

Unlocks the IDCODE register and read the 32 bit value.

.. _`twl_get_type`:

twl_get_type
============

.. c:function:: int twl_get_type( void)

    API to get TWL Si type.

    :param void:
        no arguments
    :type void: 

.. _`twl_get_type.description`:

Description
-----------

Api to get the TWL Si type from IDCODE value.

.. _`twl_get_version`:

twl_get_version
===============

.. c:function:: int twl_get_version( void)

    API to get TWL Si version.

    :param void:
        no arguments
    :type void: 

.. _`twl_get_version.description`:

Description
-----------

Api to get the TWL Si version from IDCODE value.

.. _`twl_get_hfclk_rate`:

twl_get_hfclk_rate
==================

.. c:function:: int twl_get_hfclk_rate( void)

    API to get TWL external HFCLK clock rate.

    :param void:
        no arguments
    :type void: 

.. _`twl_get_hfclk_rate.description`:

Description
-----------

Api to get the TWL HFCLK rate based on BOOT_CFG register.

.. This file was automatic generated / don't edit.

