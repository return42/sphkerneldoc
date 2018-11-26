.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/fsl/qe/gpio.c

.. _`qe_pin_request`:

qe_pin_request
==============

.. c:function:: struct qe_pin *qe_pin_request(struct device_node *np, int index)

    Request a QE pin

    :param np:
        device node to get a pin from
    :type np: struct device_node \*

    :param index:
        index of a pin in the device tree
    :type index: int

.. _`qe_pin_request.context`:

Context
-------

non-atomic

.. _`qe_pin_request.description`:

Description
-----------

This function return qe_pin so that you could use it with the rest of
the QE Pin Multiplexing API.

.. _`qe_pin_free`:

qe_pin_free
===========

.. c:function:: void qe_pin_free(struct qe_pin *qe_pin)

    Free a pin

    :param qe_pin:
        pointer to the qe_pin structure
    :type qe_pin: struct qe_pin \*

.. _`qe_pin_free.context`:

Context
-------

any

.. _`qe_pin_free.description`:

Description
-----------

This function frees the qe_pin structure and makes a pin available
for further \ :c:func:`qe_pin_request`\  calls.

.. _`qe_pin_set_dedicated`:

qe_pin_set_dedicated
====================

.. c:function:: void qe_pin_set_dedicated(struct qe_pin *qe_pin)

    Revert a pin to a dedicated peripheral function mode

    :param qe_pin:
        pointer to the qe_pin structure
    :type qe_pin: struct qe_pin \*

.. _`qe_pin_set_dedicated.context`:

Context
-------

any

.. _`qe_pin_set_dedicated.description`:

Description
-----------

This function resets a pin to a dedicated peripheral function that
has been set up by the firmware.

.. _`qe_pin_set_gpio`:

qe_pin_set_gpio
===============

.. c:function:: void qe_pin_set_gpio(struct qe_pin *qe_pin)

    Set a pin to the GPIO mode

    :param qe_pin:
        pointer to the qe_pin structure
    :type qe_pin: struct qe_pin \*

.. _`qe_pin_set_gpio.context`:

Context
-------

any

.. _`qe_pin_set_gpio.description`:

Description
-----------

This function sets a pin to the GPIO mode.

.. This file was automatic generated / don't edit.

