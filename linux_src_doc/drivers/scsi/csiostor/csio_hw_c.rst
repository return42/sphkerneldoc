.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_hw.c

.. _`csio_hw_start`:

csio_hw_start
=============

.. c:function:: int csio_hw_start(struct csio_hw *hw)

    Kicks off the HW State machine

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. _`csio_hw_start.description`:

Description
-----------

It is assumed that the initialization is a synchronous operation.
So when we return afer posting the event, the HW SM should be in
the ready state, if there were no errors during init.

.. _`csio_hw_reset`:

csio_hw_reset
=============

.. c:function:: int csio_hw_reset(struct csio_hw *hw)

    Reset the hardware

    :param struct csio_hw \*hw:
        HW module.

.. _`csio_hw_reset.description`:

Description
-----------

Caller should hold lock across this function.

.. _`csio_hw_init`:

csio_hw_init
============

.. c:function:: int csio_hw_init(struct csio_hw *hw)

    Initialize HW module.

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. _`csio_hw_init.description`:

Description
-----------

Initialize the members of the HW module.

.. _`csio_hw_exit`:

csio_hw_exit
============

.. c:function:: void csio_hw_exit(struct csio_hw *hw)

    Un-initialize HW module.

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. This file was automatic generated / don't edit.

