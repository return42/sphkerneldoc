.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/intel/pinctrl-intel.h

.. _`intel_pingroup`:

struct intel_pingroup
=====================

.. c:type:: struct intel_pingroup

    Description about group of pins

.. _`intel_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct intel_pingroup {
        const char *name;
        const unsigned *pins;
        size_t npins;
        unsigned short mode;
        const unsigned *modes;
    }

.. _`intel_pingroup.members`:

Members
-------

name
    Name of the groups

pins
    All pins in this group

npins
    Number of pins in this groups

mode
    Native mode in which the group is muxed out \ ``pins``\ . Used if \ ``modes``\ 
    is \ ``NULL``\ .

modes
    If not \ ``NULL``\  this will hold mode for each pin in \ ``pins``\ 

.. _`intel_function`:

struct intel_function
=====================

.. c:type:: struct intel_function

    Description about a function

.. _`intel_function.definition`:

Definition
----------

.. code-block:: c

    struct intel_function {
        const char *name;
        const char * const *groups;
        size_t ngroups;
    }

.. _`intel_function.members`:

Members
-------

name
    Name of the function

groups
    An array of groups for this function

ngroups
    Number of groups in \ ``groups``\ 

.. _`intel_padgroup`:

struct intel_padgroup
=====================

.. c:type:: struct intel_padgroup

    Hardware pad group information

.. _`intel_padgroup.definition`:

Definition
----------

.. code-block:: c

    struct intel_padgroup {
        unsigned reg_num;
        unsigned base;
        unsigned size;
        unsigned padown_num;
    }

.. _`intel_padgroup.members`:

Members
-------

reg_num
    GPI_IS register number

base
    Starting pin of this group

size
    Size of this group (maximum is 32).

padown_num
    PAD_OWN register number (assigned by the core driver)

.. _`intel_padgroup.description`:

Description
-----------

If pad groups of a community are not the same size, use this structure
to specify them.

.. _`intel_community`:

struct intel_community
======================

.. c:type:: struct intel_community

    Intel pin community description

.. _`intel_community.definition`:

Definition
----------

.. code-block:: c

    struct intel_community {
        unsigned barno;
        unsigned padown_offset;
        unsigned padcfglock_offset;
        unsigned hostown_offset;
        unsigned is_offset;
        unsigned ie_offset;
        unsigned pin_base;
        unsigned gpp_size;
        unsigned gpp_num_padown_regs;
        size_t npins;
        unsigned features;
        const struct intel_padgroup *gpps;
        size_t ngpps;
        void __iomem *regs;
        void __iomem *pad_regs;
    }

.. _`intel_community.members`:

Members
-------

barno
    MMIO BAR number where registers for this community reside

padown_offset
    Register offset of PAD_OWN register from \ ``regs``\ . If \ ``0``\ 
    then there is no support for owner.

padcfglock_offset
    Register offset of PADCFGLOCK from \ ``regs``\ . If \ ``0``\  then
    locking is not supported.

hostown_offset
    Register offset of HOSTSW_OWN from \ ``regs``\ . If \ ``0``\  then it
    is assumed that the host owns the pin (rather than
    ACPI).

is_offset
    Register offset of GPI_IS from \ ``regs``\ . If \ ``0``\  then uses the
    default (%0x100).

ie_offset
    Register offset of GPI_IE from \ ``regs``\ .

pin_base
    Starting pin of pins in this community

gpp_size
    Maximum number of pads in each group, such as PADCFGLOCK,
    HOSTSW_OWN,  GPI_IS, GPI_IE, etc. Used when \ ``gpps``\  is \ ``NULL``\ .

gpp_num_padown_regs
    Number of pad registers each pad group consumes at
    minimum. Use \ ``0``\  if the number of registers can be
    determined by the size of the group.

npins
    Number of pins in this community

features
    Additional features supported by the hardware

gpps
    Pad groups if the controller has variable size pad groups

ngpps
    Number of pad groups in this community

regs
    Community specific common registers (reserved for core driver)

pad_regs
    Community specific pad registers (reserved for core driver)

.. _`intel_community.description`:

Description
-----------

Most Intel GPIO host controllers this driver supports each pad group is
of equal size (except the last one). In that case the driver can just
fill in \ ``gpp_size``\  field and let the core driver to handle the rest. If
the controller has pad groups of variable size the client driver can
pass custom \ ``gpps``\  and \ ``ngpps``\  instead.

.. _`pin_group`:

PIN_GROUP
=========

.. c:function::  PIN_GROUP( n,  p,  m)

    Declare a pin group

    :param  n:
        Name of the group

    :param  p:
        An array of pins this group consists

    :param  m:
        Mode which the pins are put when this group is active. Can be either
        a single integer or an array of integers in which case mode is per
        pin.

.. _`intel_pinctrl_soc_data`:

struct intel_pinctrl_soc_data
=============================

.. c:type:: struct intel_pinctrl_soc_data

    Intel pin controller per-SoC configuration

.. _`intel_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct intel_pinctrl_soc_data {
        const char *uid;
        const struct pinctrl_pin_desc *pins;
        size_t npins;
        const struct intel_pingroup *groups;
        size_t ngroups;
        const struct intel_function *functions;
        size_t nfunctions;
        const struct intel_community *communities;
        size_t ncommunities;
    }

.. _`intel_pinctrl_soc_data.members`:

Members
-------

uid
    ACPI \_UID for the probe driver use if needed

pins
    Array if pins this pinctrl controls

npins
    Number of pins in the array

groups
    Array of pin groups

ngroups
    Number of groups in the array

functions
    Array of functions

nfunctions
    Number of functions in the array

communities
    Array of communities this pinctrl handles

ncommunities
    Number of communities in the array

.. _`intel_pinctrl_soc_data.description`:

Description
-----------

The \ ``communities``\  is used as a template by the core driver. It will make
copy of all communities and fill in rest of the information.

.. This file was automatic generated / don't edit.

