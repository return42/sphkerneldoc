.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/intel/pinctrl-merrifield.c

.. _`mrfld_family`:

struct mrfld_family
===================

.. c:type:: struct mrfld_family

    Intel pin family description

.. _`mrfld_family.definition`:

Definition
----------

.. code-block:: c

    struct mrfld_family {
        unsigned int barno;
        unsigned int pin_base;
        size_t npins;
        bool protected;
        void __iomem *regs;
    }

.. _`mrfld_family.members`:

Members
-------

barno
    MMIO BAR number where registers for this family reside

pin_base
    Starting pin of pins in this family

npins
    Number of pins in this family

protected
    True if family is protected by access

regs
    family specific common registers

.. _`mrfld_pinctrl`:

struct mrfld_pinctrl
====================

.. c:type:: struct mrfld_pinctrl

    Intel Merrifield pinctrl private structure

.. _`mrfld_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct mrfld_pinctrl {
        struct device *dev;
        raw_spinlock_t lock;
        struct pinctrl_desc pctldesc;
        struct pinctrl_dev *pctldev;
        const struct mrfld_family *families;
        size_t nfamilies;
        const struct intel_function *functions;
        size_t nfunctions;
        const struct intel_pingroup *groups;
        size_t ngroups;
        const struct pinctrl_pin_desc *pins;
        size_t npins;
    }

.. _`mrfld_pinctrl.members`:

Members
-------

dev
    Pointer to the device structure

lock
    Lock to serialize register access

pctldesc
    Pin controller description

pctldev
    Pointer to the pin controller device

families
    Array of families this pinctrl handles

nfamilies
    Number of families in the array

functions
    Array of functions

nfunctions
    Number of functions in the array

groups
    Array of pin groups

ngroups
    Number of groups in the array

pins
    Array of pins this pinctrl controls

npins
    Number of pins in the array

.. This file was automatic generated / don't edit.

