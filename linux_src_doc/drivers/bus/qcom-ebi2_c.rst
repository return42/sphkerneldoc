.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/qcom-ebi2.c

.. _`cs_data`:

struct cs_data
==============

.. c:type:: struct cs_data

    struct with info on a chipselect setting

.. _`cs_data.definition`:

Definition
----------

.. code-block:: c

    struct cs_data {
        u32 enable_mask;
        u16 slow_cfg;
        u16 fast_cfg;
    }

.. _`cs_data.members`:

Members
-------

enable_mask
    mask to enable the chipselect in the EBI2 config

slow_cfg
    *undescribed*

fast_cfg
    *undescribed*

.. _`ebi2_xmem_prop`:

struct ebi2_xmem_prop
=====================

.. c:type:: struct ebi2_xmem_prop

    describes an XMEM config property

.. _`ebi2_xmem_prop.definition`:

Definition
----------

.. code-block:: c

    struct ebi2_xmem_prop {
        const char *prop;
        u32 max;
        bool slowreg;
        u16 shift;
    }

.. _`ebi2_xmem_prop.members`:

Members
-------

prop
    the device tree binding name

max
    maximum value for the property

slowreg
    true if this property is in the SLOW CS config register
    else it is assumed to be in the FAST config register

shift
    the bit field start in the SLOW or FAST register for this
    property

.. This file was automatic generated / don't edit.

