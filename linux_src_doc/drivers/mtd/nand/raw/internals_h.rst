.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/internals.h

.. _`nand_manufacturer_ops`:

struct nand_manufacturer_ops
============================

.. c:type:: struct nand_manufacturer_ops

    NAND Manufacturer operations

.. _`nand_manufacturer_ops.definition`:

Definition
----------

.. code-block:: c

    struct nand_manufacturer_ops {
        void (*detect)(struct nand_chip *chip);
        int (*init)(struct nand_chip *chip);
        void (*cleanup)(struct nand_chip *chip);
        void (*fixup_onfi_param_page)(struct nand_chip *chip, struct nand_onfi_params *p);
    }

.. _`nand_manufacturer_ops.members`:

Members
-------

detect
    detect the NAND memory organization and capabilities

init
    initialize all vendor specific fields (like the ->read_retry()
    implementation) if any.

cleanup
    the ->init() function may have allocated resources, ->cleanup()
    is here to let vendor specific code release those resources.

fixup_onfi_param_page
    apply vendor specific fixups to the ONFI parameter
    page. This is called after the checksum is verified.

.. _`nand_manufacturer`:

struct nand_manufacturer
========================

.. c:type:: struct nand_manufacturer

    NAND Flash Manufacturer structure

.. _`nand_manufacturer.definition`:

Definition
----------

.. code-block:: c

    struct nand_manufacturer {
        int id;
        char *name;
        const struct nand_manufacturer_ops *ops;
    }

.. _`nand_manufacturer.members`:

Members
-------

id
    manufacturer ID code of device.

name
    Manufacturer name

ops
    manufacturer operations

.. This file was automatic generated / don't edit.

