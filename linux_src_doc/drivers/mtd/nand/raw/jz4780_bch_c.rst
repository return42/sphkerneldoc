.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/jz4780_bch.c

.. _`jz4780_bch_calculate`:

jz4780_bch_calculate
====================

.. c:function:: int jz4780_bch_calculate(struct jz4780_bch *bch, struct jz4780_bch_params *params, const u8 *buf, u8 *ecc_code)

    calculate ECC for a data buffer

    :param bch:
        BCH device.
    :type bch: struct jz4780_bch \*

    :param params:
        BCH parameters.
    :type params: struct jz4780_bch_params \*

    :param buf:
        input buffer with raw data.
    :type buf: const u8 \*

    :param ecc_code:
        output buffer with ECC.
    :type ecc_code: u8 \*

.. _`jz4780_bch_calculate.return`:

Return
------

0 on success, -ETIMEDOUT if timed out while waiting for BCH
controller.

.. _`jz4780_bch_correct`:

jz4780_bch_correct
==================

.. c:function:: int jz4780_bch_correct(struct jz4780_bch *bch, struct jz4780_bch_params *params, u8 *buf, u8 *ecc_code)

    detect and correct bit errors

    :param bch:
        BCH device.
    :type bch: struct jz4780_bch \*

    :param params:
        BCH parameters.
    :type params: struct jz4780_bch_params \*

    :param buf:
        raw data read from the chip.
    :type buf: u8 \*

    :param ecc_code:
        ECC read from the chip.
    :type ecc_code: u8 \*

.. _`jz4780_bch_correct.description`:

Description
-----------

Given the raw data and the ECC read from the NAND device, detects and
corrects errors in the data.

.. _`jz4780_bch_correct.return`:

Return
------

the number of bit errors corrected, -EBADMSG if there are too many
errors to correct or -ETIMEDOUT if we timed out waiting for the controller.

.. _`jz4780_bch_get`:

jz4780_bch_get
==============

.. c:function:: struct jz4780_bch *jz4780_bch_get(struct device_node *np)

    get the BCH controller device

    :param np:
        BCH device tree node.
    :type np: struct device_node \*

.. _`jz4780_bch_get.description`:

Description
-----------

Gets the BCH controller device from the specified device tree node. The
device must be released with \ :c:func:`jz4780_bch_release`\  when it is no longer being
used.

.. _`jz4780_bch_get.return`:

Return
------

a pointer to jz4780_bch, errors are encoded into the pointer.
PTR_ERR(-EPROBE_DEFER) if the device hasn't been initialised yet.

.. _`of_jz4780_bch_get`:

of_jz4780_bch_get
=================

.. c:function:: struct jz4780_bch *of_jz4780_bch_get(struct device_node *of_node)

    get the BCH controller from a DT node

    :param of_node:
        the node that contains a bch-controller property.
    :type of_node: struct device_node \*

.. _`of_jz4780_bch_get.description`:

Description
-----------

Get the bch-controller property from the given device tree
node and pass it to jz4780_bch_get to do the work.

.. _`of_jz4780_bch_get.return`:

Return
------

a pointer to jz4780_bch, errors are encoded into the pointer.
PTR_ERR(-EPROBE_DEFER) if the device hasn't been initialised yet.

.. _`jz4780_bch_release`:

jz4780_bch_release
==================

.. c:function:: void jz4780_bch_release(struct jz4780_bch *bch)

    release the BCH controller device

    :param bch:
        BCH device.
    :type bch: struct jz4780_bch \*

.. This file was automatic generated / don't edit.

