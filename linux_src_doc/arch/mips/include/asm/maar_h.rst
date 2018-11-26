.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/maar.h

.. _`platform_maar_init`:

platform_maar_init
==================

.. c:function:: unsigned platform_maar_init(unsigned num_pairs)

    perform platform-level MAAR configuration

    :param num_pairs:
        The number of MAAR pairs present in the system.
    :type num_pairs: unsigned

.. _`platform_maar_init.description`:

Description
-----------

Platforms should implement this function such that it configures as many
MAAR pairs as required, from 0 up to the maximum of num_pairs-1, and returns
the number that were used. Any further MAARs will be configured to be
invalid. The default implementation of this function will simply indicate
that it has configured 0 MAAR pairs.

.. _`platform_maar_init.return`:

Return
------

The number of MAAR pairs configured.

.. _`write_maar_pair`:

write_maar_pair
===============

.. c:function:: void write_maar_pair(unsigned idx, phys_addr_t lower, phys_addr_t upper, unsigned attrs)

    write to a pair of MAARs

    :param idx:
        The index of the pair (ie. use MAARs idx\*2 & (idx\*2)+1).
    :type idx: unsigned

    :param lower:
        The lowest address that the MAAR pair will affect. Must be
        aligned to a 2^16 byte boundary.
    :type lower: phys_addr_t

    :param upper:
        The highest address that the MAAR pair will affect. Must be
        aligned to one byte before a 2^16 byte boundary.
    :type upper: phys_addr_t

    :param attrs:
        The accessibility attributes to program, eg. MIPS_MAAR_S. The
        MIPS_MAAR_VL attribute will automatically be set.
    :type attrs: unsigned

.. _`write_maar_pair.description`:

Description
-----------

Program the pair of MAAR registers specified by idx to apply the attributes
specified by attrs to the range of addresses from lower to higher.

.. _`maar_init`:

maar_init
=========

.. c:function:: void maar_init( void)

    initialise MAARs

    :param void:
        no arguments
    :type void: 

.. _`maar_init.description`:

Description
-----------

Performs initialisation of MAARs for the current CPU, making use of the
platforms implementation of platform_maar_init where necessary and
duplicating the setup it provides on secondary CPUs.

.. _`maar_config`:

struct maar_config
==================

.. c:type:: struct maar_config

    MAAR configuration data

.. _`maar_config.definition`:

Definition
----------

.. code-block:: c

    struct maar_config {
        phys_addr_t lower;
        phys_addr_t upper;
        unsigned attrs;
    }

.. _`maar_config.members`:

Members
-------

lower
    The lowest address that the MAAR pair will affect. Must be
    aligned to a 2^16 byte boundary.

upper
    The highest address that the MAAR pair will affect. Must be
    aligned to one byte before a 2^16 byte boundary.

attrs
    The accessibility attributes to program, eg. MIPS_MAAR_S. The
    MIPS_MAAR_VL attribute will automatically be set.

.. _`maar_config.description`:

Description
-----------

Describes the configuration of a pair of Memory Accessibility Attribute
Registers - applying attributes from attrs to the range of physical
addresses from lower to upper inclusive.

.. _`maar_config`:

maar_config
===========

.. c:function:: unsigned maar_config(const struct maar_config *cfg, unsigned num_cfg, unsigned num_pairs)

    configure MAARs according to provided data

    :param cfg:
        Pointer to an array of struct maar_config.
    :type cfg: const struct maar_config \*

    :param num_cfg:
        The number of structs in the cfg array.
    :type num_cfg: unsigned

    :param num_pairs:
        The number of MAAR pairs present in the system.
    :type num_pairs: unsigned

.. _`maar_config.description`:

Description
-----------

Configures as many MAARs as are present and specified in the cfg
array with the values taken from the cfg array.

.. _`maar_config.return`:

Return
------

The number of MAAR pairs configured.

.. This file was automatic generated / don't edit.

