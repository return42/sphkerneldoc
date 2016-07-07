.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/keypad.h

.. _`samsung_keypad_set_platdata`:

samsung_keypad_set_platdata
===========================

.. c:function:: void samsung_keypad_set_platdata(struct samsung_keypad_platdata *pd)

    Set platform data for Samsung Keypad device.

    :param struct samsung_keypad_platdata \*pd:
        Platform data to register to device.

.. _`samsung_keypad_set_platdata.description`:

Description
-----------

Register the given platform data for use with Samsung Keypad device.
The call will copy the platform data, so the board definitions can
make the structure itself \__initdata.

.. This file was automatic generated / don't edit.

