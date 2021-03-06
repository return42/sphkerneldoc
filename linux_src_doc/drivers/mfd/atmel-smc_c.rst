.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/atmel-smc.c

.. _`atmel_smc_cs_conf_init`:

atmel_smc_cs_conf_init
======================

.. c:function:: void atmel_smc_cs_conf_init(struct atmel_smc_cs_conf *conf)

    initialize a SMC CS conf

    :param conf:
        the SMC CS conf to initialize
    :type conf: struct atmel_smc_cs_conf \*

.. _`atmel_smc_cs_conf_init.description`:

Description
-----------

Set all fields to 0 so that one can start defining a new config.

.. _`atmel_smc_cs_encode_ncycles`:

atmel_smc_cs_encode_ncycles
===========================

.. c:function:: int atmel_smc_cs_encode_ncycles(unsigned int ncycles, unsigned int msbpos, unsigned int msbwidth, unsigned int msbfactor, unsigned int *encodedval)

    encode a number of MCK clk cycles in the format expected by the SMC engine

    :param ncycles:
        number of MCK clk cycles
    :type ncycles: unsigned int

    :param msbpos:
        position of the MSB part of the timing field
    :type msbpos: unsigned int

    :param msbwidth:
        width of the MSB part of the timing field
    :type msbwidth: unsigned int

    :param msbfactor:
        factor applied to the MSB
    :type msbfactor: unsigned int

    :param encodedval:
        param used to store the encoding result
    :type encodedval: unsigned int \*

.. _`atmel_smc_cs_encode_ncycles.description`:

Description
-----------

This function encodes the \ ``ncycles``\  value as described in the datasheet
(section "SMC Setup/Pulse/Cycle/Timings Register"). This is a generic
helper which called with different parameter depending on the encoding
scheme.

If the \ ``ncycles``\  value is too big to be encoded, -ERANGE is returned and
the encodedval is contains the maximum val. Otherwise, 0 is returned.

.. _`atmel_smc_cs_conf_set_timing`:

atmel_smc_cs_conf_set_timing
============================

.. c:function:: int atmel_smc_cs_conf_set_timing(struct atmel_smc_cs_conf *conf, unsigned int shift, unsigned int ncycles)

    set the SMC CS conf Txx parameter to a specific value

    :param conf:
        SMC CS conf descriptor
    :type conf: struct atmel_smc_cs_conf \*

    :param shift:
        the position of the Txx field in the TIMINGS register
    :type shift: unsigned int

    :param ncycles:
        value (expressed in MCK clk cycles) to assign to this Txx
        parameter
    :type ncycles: unsigned int

.. _`atmel_smc_cs_conf_set_timing.description`:

Description
-----------

This function encodes the \ ``ncycles``\  value as described in the datasheet
(section "SMC Timings Register"), and then stores the result in the
\ ``conf->timings``\  field at \ ``shift``\  position.

Returns -EINVAL if shift is invalid, -ERANGE if ncycles does not fit in
the field, and 0 otherwise.

.. _`atmel_smc_cs_conf_set_setup`:

atmel_smc_cs_conf_set_setup
===========================

.. c:function:: int atmel_smc_cs_conf_set_setup(struct atmel_smc_cs_conf *conf, unsigned int shift, unsigned int ncycles)

    set the SMC CS conf xx_SETUP parameter to a specific value

    :param conf:
        SMC CS conf descriptor
    :type conf: struct atmel_smc_cs_conf \*

    :param shift:
        the position of the xx_SETUP field in the SETUP register
    :type shift: unsigned int

    :param ncycles:
        value (expressed in MCK clk cycles) to assign to this xx_SETUP
        parameter
    :type ncycles: unsigned int

.. _`atmel_smc_cs_conf_set_setup.description`:

Description
-----------

This function encodes the \ ``ncycles``\  value as described in the datasheet
(section "SMC Setup Register"), and then stores the result in the
\ ``conf->setup``\  field at \ ``shift``\  position.

Returns -EINVAL if \ ``shift``\  is invalid, -ERANGE if \ ``ncycles``\  does not fit in
the field, and 0 otherwise.

.. _`atmel_smc_cs_conf_set_pulse`:

atmel_smc_cs_conf_set_pulse
===========================

.. c:function:: int atmel_smc_cs_conf_set_pulse(struct atmel_smc_cs_conf *conf, unsigned int shift, unsigned int ncycles)

    set the SMC CS conf xx_PULSE parameter to a specific value

    :param conf:
        SMC CS conf descriptor
    :type conf: struct atmel_smc_cs_conf \*

    :param shift:
        the position of the xx_PULSE field in the PULSE register
    :type shift: unsigned int

    :param ncycles:
        value (expressed in MCK clk cycles) to assign to this xx_PULSE
        parameter
    :type ncycles: unsigned int

.. _`atmel_smc_cs_conf_set_pulse.description`:

Description
-----------

This function encodes the \ ``ncycles``\  value as described in the datasheet
(section "SMC Pulse Register"), and then stores the result in the
\ ``conf->setup``\  field at \ ``shift``\  position.

Returns -EINVAL if \ ``shift``\  is invalid, -ERANGE if \ ``ncycles``\  does not fit in
the field, and 0 otherwise.

.. _`atmel_smc_cs_conf_set_cycle`:

atmel_smc_cs_conf_set_cycle
===========================

.. c:function:: int atmel_smc_cs_conf_set_cycle(struct atmel_smc_cs_conf *conf, unsigned int shift, unsigned int ncycles)

    set the SMC CS conf xx_CYCLE parameter to a specific value

    :param conf:
        SMC CS conf descriptor
    :type conf: struct atmel_smc_cs_conf \*

    :param shift:
        the position of the xx_CYCLE field in the CYCLE register
    :type shift: unsigned int

    :param ncycles:
        value (expressed in MCK clk cycles) to assign to this xx_CYCLE
        parameter
    :type ncycles: unsigned int

.. _`atmel_smc_cs_conf_set_cycle.description`:

Description
-----------

This function encodes the \ ``ncycles``\  value as described in the datasheet
(section "SMC Cycle Register"), and then stores the result in the
\ ``conf->setup``\  field at \ ``shift``\  position.

Returns -EINVAL if \ ``shift``\  is invalid, -ERANGE if \ ``ncycles``\  does not fit in
the field, and 0 otherwise.

.. _`atmel_smc_cs_conf_apply`:

atmel_smc_cs_conf_apply
=======================

.. c:function:: void atmel_smc_cs_conf_apply(struct regmap *regmap, int cs, const struct atmel_smc_cs_conf *conf)

    apply an SMC CS conf

    :param regmap:
        the SMC regmap
    :type regmap: struct regmap \*

    :param cs:
        the CS id
        \ ``conf``\  the SMC CS conf to apply
    :type cs: int

    :param conf:
        *undescribed*
    :type conf: const struct atmel_smc_cs_conf \*

.. _`atmel_smc_cs_conf_apply.description`:

Description
-----------

Applies an SMC CS configuration.
Only valid on at91sam9/avr32 SoCs.

.. _`atmel_hsmc_cs_conf_apply`:

atmel_hsmc_cs_conf_apply
========================

.. c:function:: void atmel_hsmc_cs_conf_apply(struct regmap *regmap, const struct atmel_hsmc_reg_layout *layout, int cs, const struct atmel_smc_cs_conf *conf)

    apply an SMC CS conf

    :param regmap:
        the HSMC regmap
    :type regmap: struct regmap \*

    :param layout:
        the layout of registers
        \ ``conf``\  the SMC CS conf to apply
    :type layout: const struct atmel_hsmc_reg_layout \*

    :param cs:
        the CS id
    :type cs: int

    :param conf:
        *undescribed*
    :type conf: const struct atmel_smc_cs_conf \*

.. _`atmel_hsmc_cs_conf_apply.description`:

Description
-----------

Applies an SMC CS configuration.
Only valid on post-sama5 SoCs.

.. _`atmel_smc_cs_conf_get`:

atmel_smc_cs_conf_get
=====================

.. c:function:: void atmel_smc_cs_conf_get(struct regmap *regmap, int cs, struct atmel_smc_cs_conf *conf)

    retrieve the current SMC CS conf

    :param regmap:
        the SMC regmap
    :type regmap: struct regmap \*

    :param cs:
        the CS id
    :type cs: int

    :param conf:
        the SMC CS conf object to store the current conf
    :type conf: struct atmel_smc_cs_conf \*

.. _`atmel_smc_cs_conf_get.description`:

Description
-----------

Retrieve the SMC CS configuration.
Only valid on at91sam9/avr32 SoCs.

.. _`atmel_hsmc_cs_conf_get`:

atmel_hsmc_cs_conf_get
======================

.. c:function:: void atmel_hsmc_cs_conf_get(struct regmap *regmap, const struct atmel_hsmc_reg_layout *layout, int cs, struct atmel_smc_cs_conf *conf)

    retrieve the current SMC CS conf

    :param regmap:
        the HSMC regmap
    :type regmap: struct regmap \*

    :param layout:
        the layout of registers
    :type layout: const struct atmel_hsmc_reg_layout \*

    :param cs:
        the CS id
    :type cs: int

    :param conf:
        the SMC CS conf object to store the current conf
    :type conf: struct atmel_smc_cs_conf \*

.. _`atmel_hsmc_cs_conf_get.description`:

Description
-----------

Retrieve the SMC CS configuration.
Only valid on post-sama5 SoCs.

.. _`atmel_hsmc_get_reg_layout`:

atmel_hsmc_get_reg_layout
=========================

.. c:function:: const struct atmel_hsmc_reg_layout *atmel_hsmc_get_reg_layout(struct device_node *np)

    retrieve the layout of HSMC registers

    :param np:
        the HSMC regmap
    :type np: struct device_node \*

.. _`atmel_hsmc_get_reg_layout.description`:

Description
-----------

Retrieve the layout of HSMC registers.

Returns NULL in case of SMC, a struct atmel_hsmc_reg_layout pointer
in HSMC case, otherwise ERR_PTR(-EINVAL).

.. This file was automatic generated / don't edit.

